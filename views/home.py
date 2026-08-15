import base64
import html
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from data.profile import PROFILE


ROOT_DIR = Path(__file__).resolve().parents[1]
BASE_PORTRAIT_PATH = ROOT_DIR / "assets/hero/base-portrait.png"
CHROME_PORTRAIT_PATH = ROOT_DIR / "assets/hero/chrome-portrait.png"


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
    hero_subtitle = "I take messy data and turn it into something people can actually use."
    hero_summary = (
        "I am not that interested in data for its own sake. I care about whether the work helps someone decide what to do next. "
        "Most of my work lives in the overlap between analytics, product thinking, and implementation. That includes KPI reporting, "
        "SQL and ETL pipelines, ranking and recommendation systems, and models that have to make sense to someone who is never going to read a notebook."
    )
    hero_kpis = [
        {"value": "307K+", "label": "borrower records in my loan default project"},
        {"value": "78%", "label": "trust reached in AI restaurant recommendation testing (started at 17%)"},
        {"value": "3.6/4.0", "label": "GPA, Rutgers M.S. in Data Science"},
        {"value": "Top 12%", "label": "paper placement at ICICIT 2024"},
    ]
    hero_card_html = f"""
        <div class="hero-card hero-intro-card">
            <div class="eyebrow">Data portfolio</div>
            <h1 class="hero-title">{PROFILE['name']}</h1>
            <p class="hero-subtitle">{hero_subtitle}</p>
            <p>{hero_summary}</p>
            <div class="chip-row">
                <span class="chip">Data science</span>
                <span class="chip">Analytics engineering</span>
                <span class="chip">SQL &amp; PostgreSQL</span>
                <span class="chip">Cloud dashboards</span>
            </div>
            <div class="kpi-grid">
                {''.join(f"<div class='kpi'><strong>{item['value']}</strong>{item['label']}</div>" for item in hero_kpis)}
            </div>
        </div>
    """

    st.markdown(hero_card_html, unsafe_allow_html=True)
    st.markdown("<div class='hero-stack-gap'></div>", unsafe_allow_html=True)

    _render_interactive_hero()

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    home_panels = [
        (
            "What I do",
            "I do my best work when the data is messy, the workflow needs cleanup, and someone actually needs a useful answer at the end of it.",
        ),
        (
            "Where I fit best",
            "I fit best in data science, analytics, analytics engineering, AI, and fintech-adjacent roles where the data is real and someone downstream has to make a decision with it.",
        ),
        (
            "Why this site exists",
            "I am not trying to put every class project I have touched on one page. This is the work I would actually want a hiring team to judge me on.",
        ),
    ]

    strengths = [
        "I learn fast, but I would rather the work hold up than sound impressive in a standup.",
        "I am a good teammate when the team is serious about getting things done well.",
        "If a workflow is broken or unclear, I'm the person who wants to go trace it down and fix it, not just patch around it.",
        "I do my best work when I can combine analysis, systems thinking, and clear explanation instead of being boxed into one lane.",
    ]
    bullets = "".join(f"<li>{item}</li>" for item in strengths)
    st.markdown(
        f"""
        <div class="section-shell">
                <div class="section-heading">
                    <div class="section-label">Overview</div>
                    <h2 class="section-title">A clearer map of what belongs on this portfolio</h2>
                    <p>This homepage should explain the shape of my work quickly: where I fit, what kind of problems I solve, and why the projects on this site belong together.</p>
                </div>
            <div class="section-grid">
                {''.join(
                    f"<div class='content-card compact-card'><div class='section-label'>{title}</div><p>{body}</p></div>"
                    for title, body in home_panels
                )}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="section-grid section-grid-wide">
            <div class="content-card compact-card section-stack">
                <div class="section-heading-block">
                    <div class="section-label">Core signal</div>
                    <h3>My strongest lane is analytics that knows it is building toward a product.</h3>
                    <p>I like figuring out where the friction is, building the logic under it, and turning that into something someone else can actually use.</p>
                </div>
                <div class="metric-strip">
                    <div class="metric-box"><strong>Analytics</strong> KPI reporting, trend-finding, retention and drop-off analysis</div>
                    <div class="metric-box"><strong>Data</strong> SQL, validation workflows, schema work, ETL, transformations</div>
                    <div class="metric-box"><strong>Delivery</strong> APIs, dashboards, ranking systems, and explanations a normal human can follow</div>
                </div>
            </div>
            <div class="content-card compact-card section-stack">
                <div class="section-heading-block">
                    <div class="section-label">How I work</div>
                    <h3>What I'm like on a team</h3>
                    <p>I do best on teams that care about clean logic, useful outputs, and fixing the real bottleneck instead of talking around it.</p>
                </div>
                <ul>{bullets}</ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    homepage_experience = [
        {
            "dates": "Spring 2026 | Product launched May 2026",
            "role": "Data Science Intern",
            "company": "Helius Health AI",
            "summary": (
                "Built the analytics backbone for an AI-enabled healthcare workforce platform, the kind of "
                "infrastructure that sits quietly underneath and makes everything else answerable."
            ),
            "bullets": [
                "Built KPI pipelines and reporting APIs in Python/FastAPI over Supabase/Postgres, tracking onboarding, assessment completion, engagement, retention, and where users were dropping off.",
                "Broke down completion behavior by user segment (students, grads, licensed and unlicensed users) to find where the flow was failing and for whom.",
                "Took a denormalized Excel-based dataset and rebuilt it as clean, validated Supabase/Postgres tables: schema mapping, UUID reconciliation, JSONB handling, the unglamorous stuff that makes everything downstream trustworthy.",
                "Turned all of that into recurring, sponsor-facing reports that didn't need me to interpret them.",
            ],
        },
        {
            "dates": "Spring 2026",
            "role": "AI Agent Developer Intern",
            "company": "NeuralSeek",
            "summary": (
                "Built an AI restaurant recommendation system and then spent a good chunk of time on the harder question: would anyone actually trust what it recommended?"
            ),
            "bullets": [
                "Built the recommendation workflow around retrieval and ranking, not just \"what's a good restaurant\" but \"what's a good restaurant for this person, right now.\"",
                "Ran user research to figure out what was actually killing trust in AI-generated suggestions, then rebuilt around that.",
                "Took willingness to trust the recommendations from 17% to 78%.",
                "Presented findings to stakeholders, where \"the model works\" was not a good enough answer.",
            ],
        },
    ]
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-label">Selected experience</div>
            <h2 class="section-title">The two roles that best explain how I work now</h2>
            <p>These are the strongest signals for the kind of data and AI work I want next. One is heavier on analytics infrastructure and reporting. The other is heavier on product logic and user trust.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    experience_columns = st.columns(2, gap="large")
    for column, role in zip(experience_columns, homepage_experience):
        with column:
            bullets = "".join(f"<li>{bullet}</li>" for bullet in role["bullets"])
            st.markdown(
                f"""
                <div class="content-card compact-card">
                    <div class="section-label">{role['dates']}</div>
                    <h3>{role['role']}</h3>
                    <p><strong>{role['company']}</strong></p>
                    <p>{role['summary']}</p>
                    <ul>{bullets}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
