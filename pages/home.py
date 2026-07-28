import base64
import html
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from data.profile import PROFILE


BASE_PORTRAIT_PATH = Path("/Users/sanjanasawant/Downloads/wide portrait 1.png")
CHROME_PORTRAIT_PATH = Path("/Users/sanjanasawant/Downloads/wide portrait 2.png")


def _to_data_uri(path: Path) -> str | None:
    if not path.exists():
        return None

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(path.suffix.lower())
    if mime_type is None:
        return None

    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def _render_interactive_hero() -> bool:
    base_image = _to_data_uri(BASE_PORTRAIT_PATH)
    chrome_image = _to_data_uri(CHROME_PORTRAIT_PATH)
    if not base_image or not chrome_image:
        return False

    profile_name = html.escape(PROFILE["name"])
    component_html = f"""
    <div class="portrait-shell">
      <section class="portrait-stage">
        <div class="canvas-frame">
          <canvas id="reveal-canvas" aria-label="{profile_name} interactive portrait"></canvas>
          <div class="canvas-glow"></div>
        </div>
      </section>
    </div>

    <style>
      :root {{
        color-scheme: dark;
      }}

      html, body {{
        margin: 0;
        background:
          radial-gradient(circle at top right, rgba(184, 201, 140, 0.14), transparent 26%),
          radial-gradient(circle at 15% 20%, rgba(214, 167, 90, 0.12), transparent 18%),
          linear-gradient(180deg, #0b100b 0%, #090c09 100%);
        font-family: "Space Grotesk", "Avenir Next", "Segoe UI", sans-serif;
        color: #edf1e7;
      }}

      .portrait-shell {{
        padding: 24px;
        box-sizing: border-box;
      }}

      .portrait-stage {{
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(184, 201, 140, 0.12);
        border-radius: 28px;
        background: rgba(15, 21, 15, 0.72);
        box-shadow: 0 28px 60px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
      }}

      .portrait-stage {{
        padding: 18px;
      }}

      .canvas-frame {{
        position: relative;
        width: 100%;
        min-height: 520px;
        border-radius: 24px;
        overflow: hidden;
        background:
          radial-gradient(circle at center, rgba(54, 60, 41, 0.14) 0%, rgba(28, 33, 22, 0.34) 58%, rgba(13, 18, 13, 0.92) 100%),
          linear-gradient(180deg, rgba(17, 22, 14, 0.72), rgba(13, 18, 13, 0.96));
        box-shadow: inset 0 0 0 1px rgba(184, 201, 140, 0.08);
      }}

      #reveal-canvas {{
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        display: block;
      }}

      .canvas-glow {{
        position: absolute;
        inset: 0;
        background:
          radial-gradient(circle at center, rgba(10, 14, 10, 0) 54%, rgba(10, 14, 10, 0.14) 68%, rgba(10, 14, 10, 0.48) 100%),
          linear-gradient(180deg, rgba(10, 14, 10, 0.04), rgba(10, 14, 10, 0.5));
        pointer-events: none;
      }}

      @media (max-width: 920px) {{
        .portrait-shell {{
          padding: 16px;
        }}

        .canvas-frame {{
          min-height: 420px;
        }}
      }}
    </style>

    <script>
      const baseSrc = {json.dumps(base_image)};
      const chromeSrc = {json.dumps(chrome_image)};
      const canvas = document.getElementById("reveal-canvas");
      const frame = canvas.parentElement;
      const ctx = canvas.getContext("2d");
      const layerCanvas = document.createElement("canvas");
      const layerCtx = layerCanvas.getContext("2d");
      const baseImage = new Image();
      const chromeImage = new Image();
      const trail = [];
      const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      const config = {{
        radius: 220,
        tail: 16,
        decay: reducedMotion ? 0.9 : 0.84,
        chroma: reducedMotion ? 0 : 3.5,
        zoomOut: 0.58,
        offsetY: -6,
      }};
      let pointerActive = false;
      let renderHandle = null;

      function resizeCanvas() {{
        const width = frame.clientWidth;
        const height = frame.clientHeight;
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        canvas.width = Math.round(width * dpr);
        canvas.height = Math.round(height * dpr);
        layerCanvas.width = canvas.width;
        layerCanvas.height = canvas.height;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        layerCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
      }}

      function coverMetrics(image) {{
        const width = frame.clientWidth;
        const height = frame.clientHeight;
        const scale = Math.max(width / image.width, height / image.height) * config.zoomOut;
        const drawWidth = image.width * scale;
        const drawHeight = image.height * scale;
        const offsetX = (width - drawWidth) / 2;
        const offsetY = (height - drawHeight) / 2 + config.offsetY;
        return {{ width, height, drawWidth, drawHeight, offsetX, offsetY }};
      }}

      function drawCover(targetCtx, image, shiftX = 0, shiftY = 0) {{
        const metrics = coverMetrics(image);
        targetCtx.drawImage(
          image,
          metrics.offsetX + shiftX,
          metrics.offsetY + shiftY,
          metrics.drawWidth,
          metrics.drawHeight
        );
      }}

      function addPoint(clientX, clientY, strength = 1) {{
        const rect = frame.getBoundingClientRect();
        trail.unshift({{
          x: clientX - rect.left,
          y: clientY - rect.top,
          strength,
          life: 1,
        }});
        if (trail.length > 36) {{
          trail.length = 36;
        }}
      }}

      function seedReducedMotionReveal() {{
        if (!reducedMotion || trail.length) {{
          return;
        }}

        const rect = frame.getBoundingClientRect();
        addPoint(rect.width * 0.52 + rect.left, rect.height * 0.34 + rect.top, 1);
        addPoint(rect.width * 0.48 + rect.left, rect.height * 0.52 + rect.top, 0.9);
      }}

      function drawRevealTrail() {{
        layerCtx.save();
        layerCtx.globalCompositeOperation = "destination-out";
        layerCtx.lineCap = "round";
        layerCtx.lineJoin = "round";

        for (let index = 0; index < trail.length; index += 1) {{
          const point = trail[index];
          const radius = config.radius * (0.3 + point.life * 0.7) * point.strength;
          const gradient = layerCtx.createRadialGradient(point.x, point.y, radius * 0.18, point.x, point.y, radius);
          gradient.addColorStop(0, "rgba(0, 0, 0, 1)");
          gradient.addColorStop(0.72, "rgba(0, 0, 0, 0.72)");
          gradient.addColorStop(1, "rgba(0, 0, 0, 0)");
          layerCtx.fillStyle = gradient;
          layerCtx.beginPath();
          layerCtx.arc(point.x, point.y, radius, 0, Math.PI * 2);
          layerCtx.fill();

          const nextPoint = trail[index + 1];
          if (nextPoint) {{
            layerCtx.strokeStyle = "rgba(0, 0, 0, 0.94)";
            layerCtx.lineWidth = radius * 1.35;
            layerCtx.beginPath();
            layerCtx.moveTo(point.x, point.y);
            layerCtx.lineTo(nextPoint.x, nextPoint.y);
            layerCtx.stroke();
          }}

          point.life *= config.decay;
        }}

        layerCtx.restore();
        while (trail.length && trail[trail.length - 1].life < 0.03) {{
          trail.pop();
        }}
      }}

      function renderScene() {{
        if (!baseImage.complete || !chromeImage.complete) {{
          renderHandle = window.requestAnimationFrame(renderScene);
          return;
        }}

        const width = frame.clientWidth;
        const height = frame.clientHeight;
        ctx.clearRect(0, 0, width, height);
        layerCtx.clearRect(0, 0, width, height);

        drawCover(ctx, baseImage);
        layerCtx.save();
        drawCover(layerCtx, chromeImage);

        const overlay = layerCtx.createLinearGradient(0, 0, width, height);
        overlay.addColorStop(0, "rgba(184, 201, 140, 0.12)");
        overlay.addColorStop(0.42, "rgba(214, 167, 90, 0.08)");
        overlay.addColorStop(1, "rgba(16, 21, 15, 0.28)");
        layerCtx.fillStyle = overlay;
        layerCtx.fillRect(0, 0, width, height);
        layerCtx.restore();

        drawRevealTrail();

        if (config.chroma > 0) {{
          ctx.save();
          ctx.globalAlpha = 0.08;
          ctx.filter = "hue-rotate(40deg) saturate(1.15)";
          ctx.drawImage(layerCanvas, -config.chroma, 0, width, height);
          ctx.filter = "hue-rotate(-8deg) saturate(1.25)";
          ctx.drawImage(layerCanvas, config.chroma, 0, width, height);
          ctx.restore();
        }}

        ctx.drawImage(layerCanvas, 0, 0, width, height);

        const vignette = ctx.createLinearGradient(0, 0, 0, height);
        vignette.addColorStop(0, "rgba(9, 12, 9, 0)");
        vignette.addColorStop(1, "rgba(9, 12, 9, 0.42)");
        ctx.fillStyle = vignette;
        ctx.fillRect(0, 0, width, height);

        renderHandle = window.requestAnimationFrame(renderScene);
      }}

      function startIfReady() {{
        resizeCanvas();
        seedReducedMotionReveal();
        if (renderHandle === null) {{
          renderScene();
        }}
      }}

      frame.addEventListener("pointerenter", () => {{
        pointerActive = true;
      }});

      frame.addEventListener("pointerleave", () => {{
        pointerActive = false;
      }});

      frame.addEventListener("pointermove", (event) => {{
        if (!pointerActive && event.pointerType === "mouse") {{
          return;
        }}
        addPoint(event.clientX, event.clientY);
      }});

      frame.addEventListener("pointerdown", (event) => {{
        pointerActive = true;
        addPoint(event.clientX, event.clientY, 1.15);
      }});

      frame.addEventListener("pointerup", () => {{
        pointerActive = false;
      }});

      const observer = new ResizeObserver(() => {{
        resizeCanvas();
        seedReducedMotionReveal();
      }});
      observer.observe(frame);

      baseImage.addEventListener("load", startIfReady);
      chromeImage.addEventListener("load", startIfReady);
      baseImage.src = baseSrc;
      chromeImage.src = chromeSrc;
    </script>
    """
    components.html(component_html, height=620)
    return True


def render_home_page() -> None:
    st.markdown(
        """
        <div class="content-card section-intro-card">
            <div class="section-label">Overview</div>
            <h2 class="section-title">This is the version of my work that actually sounds like me</h2>
            <p>I did not want this site to read like generic portfolio copy. I wanted it to show how I think, what I build, where I have done real work, and why I care about certain problems more than others.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)

    hero_card_html = f"""
        <div class="hero-card hero-intro-card">
            <div class="eyebrow">Data portfolio</div>
            <h1 class="hero-title">{PROFILE['name']}</h1>
            <p class="hero-subtitle">{PROFILE['headline']}</p>
            <p>{PROFILE['summary']}</p>
            <div class="chip-row">
                <span class="chip">Data science</span>
                <span class="chip">Analytics engineering</span>
                <span class="chip">SQL and PostgreSQL</span>
                <span class="chip">Cloud dashboards</span>
            </div>
            <div class="kpi-grid">
                {''.join(f"<div class='kpi'><strong>{item['value']}</strong>{item['label']}</div>" for item in PROFILE['highlights'])}
            </div>
        </div>
    """

    st.markdown(hero_card_html, unsafe_allow_html=True)
    st.markdown("<div class='hero-stack-gap'></div>", unsafe_allow_html=True)

    if not _render_interactive_hero():
        st.info(
            "The interactive portrait reveal is waiting for the two source images at "
            f"`{BASE_PORTRAIT_PATH}` and `{CHROME_PORTRAIT_PATH}`."
        )

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    highlight_columns = st.columns(3, gap="large")
    home_panels = [
        (
            "What I do",
            "I usually work best when the data is messy, the workflow is a little broken, and someone needs a result they can actually use.",
        ),
        (
            "Where I fit best",
            "Data scientist, data analyst, analytics engineering, AI, and fintech-adjacent roles where product thinking matters too.",
        ),
        (
            "Why this site exists",
            "Not to dump every class project online, but to show the work I would actually want a hiring team to judge me on.",
        ),
    ]

    for column, (title, body) in zip(highlight_columns, home_panels):
        with column:
            st.markdown(
                f"""
                <div class="content-card">
                    <div class="section-label">{title}</div>
                    <p>{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="content-card compact-card">
            <div class="section-label">Core signal</div>
            <h3>My strongest lane is analytics with product awareness, not analytics in a vacuum.</h3>
            <p>I like work where I have to trace the data, figure out where the friction is, build the logic, and turn it into something another person can use without needing me in the room to explain it.</p>
            <div class="metric-strip">
                <div class="metric-box"><strong>Analytics</strong> KPI reporting, trend finding, retention and drop-off analysis</div>
                <div class="metric-box"><strong>Data</strong> SQL, validation workflows, schema inspection, ETL, transformations</div>
                <div class="metric-box"><strong>Delivery</strong> APIs, dashboards, ranking systems, and explanations that make sense to normal people</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)

    bullets = "".join(f"<li>{item}</li>" for item in PROFILE["strengths"])
    st.markdown(
        f"""
        <div class="content-card compact-card">
            <div class="section-label">How I work</div>
            <h3>What I am like on a team</h3>
            <ul>{bullets}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    homepage_experience_highlights = {
        "Data Science Intern": [
            "Built a verified raw-survey-to-Supabase staging workflow and an end-to-end KPI reporting process.",
            "Analyzed onboarding, engagement, retention, drop-off, and specialty-matching data for sponsor-facing reporting.",
        ],
        "AI Agent Developer Intern": [
            "Built a restaurant recommendation workflow around retrieval, ranking logic, and user trust.",
            "Validated the product with users and improved trust in AI recommendations from 17 percent to 78 percent.",
        ],
    }
    relevant_experience = PROFILE["experience"][:2]
    experience_columns = st.columns(2, gap="large")
    for column, role in zip(experience_columns, relevant_experience):
        with column:
            homepage_bullets = homepage_experience_highlights.get(role["role"], role["bullets"][:2])
            bullets = "".join(f"<li>{bullet}</li>" for bullet in homepage_bullets)
            st.markdown(
                f"""
                <div class="content-card compact-card">
                    <div class="section-label">{role['dates']}</div>
                    <h3>{role['role']}</h3>
                    <p><strong>{role['company']}</strong></p>
                    <ul>{bullets}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
