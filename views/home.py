import base64
from pathlib import Path

import streamlit as st

from data.profile import PROFILE


ROOT_DIR = Path(__file__).resolve().parents[1]
PORTRAIT_PATH = ROOT_DIR / "assets" / "hero" / "sanjana-portrait.png"


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


def render_home_page() -> None:
    portrait = _to_data_uri(PORTRAIT_PATH)
    portrait_html = (
        f'<figure class="hero-photo"><img src="{portrait}" alt="{PROFILE["name"]}"></figure>'
        if portrait
        else ""
    )
    selected_work = [
        (
            "01",
            "Helius Health AI",
            "Turned messy survey and Excel inputs into validated workflows and reporting for onboarding, completion, engagement, retention, and specialty matching.",
            "Data workflows + KPI reporting",
        ),
        (
            "02",
            "NeuralSeek / InstaDine",
            "Worked on a retrieval and ranking flow for restaurant recommendations, then built a fuller app with session state, maps, and grounded responses.",
            "Applied AI + product flow",
        ),
        (
            "03",
            "Loan Default Prediction",
            "Built a 307K+ record credit-risk workflow comparing logistic regression and XGBoost with calibration and threshold analysis.",
            "Modeling + evaluation",
        ),
    ]

    work_html = "".join(
        f"""
        <article class="work-row">
            <div class="work-index">{index}</div>
            <div class="work-copy">
                <h3>{title}</h3>
                <p>{body}</p>
            </div>
            <div class="work-type">{kind}</div>
        </article>
        """
        for index, title, body, kind in selected_work
    )

    st.markdown(
        f"""
        <section class="simple-hero">
            <div class="hero-copy">
                <div class="eyebrow">Data, AI, and analytics</div>
                <h1 class="hero-title">{PROFILE['name']}</h1>
                <p class="hero-subtitle">I work on data and AI systems that need to be understandable, useful, and maintained after the first demo.</p>
                <p class="hero-summary">My recent work has included cleaning healthcare workforce data, building sponsor-facing KPI reporting, testing an AI restaurant recommendation product, and evaluating credit-risk models.</p>
                <div class="text-link-row">
                    <a href="mailto:{PROFILE['email']}">Email me</a>
                    <a href="{PROFILE['linkedin']}" target="_blank">LinkedIn</a>
                    <a href="{PROFILE['github']}" target="_blank">GitHub</a>
                </div>
            </div>
            {portrait_html}
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <section class="section-shell selected-work">
            <div class="section-heading">
                <div class="section-label">Selected work</div>
                <h2 class="section-title">The work I can explain clearly.</h2>
                <p>Three examples of the problems, systems, and tradeoffs behind the portfolio.</p>
            </div>
            <div class="work-list">{work_html}</div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <section class="about-strip">
            <div>
                <div class="section-label">A little context</div>
                <h2>Useful work over impressive-looking work.</h2>
            </div>
            <p>I am most interested in roles where analysis meets implementation: analytics, data science, data engineering, and applied AI. I like the part where a vague problem becomes a workflow, a decision, or a product someone can actually use.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
