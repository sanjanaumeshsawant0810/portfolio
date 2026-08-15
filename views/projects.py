import base64
from pathlib import Path

import streamlit as st

from data.projects import PROJECTS


def _image_to_data_uri(path_str: str) -> str:
    path = Path(path_str)
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(path.suffix.lower())
    if not path.exists() or mime_type is None:
        return path_str

    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def render_projects_page() -> None:
    st.markdown(
        """
        <div class="section-shell">
            <div class="content-card">
                <div class="section-label">Projects</div>
                <h1>The projects here are the ones I would actually want to talk about</h1>
                <p>I am not trying to make every project look the same. Some are more product-heavy, some are more analytics-heavy, and some are here because they show how I think when the problem is messy or technically hard.</p>
            </div>
            <div class="detail-grid">
                <div class="detail-box">
                    <span>What matters here</span>
                    <strong>Clear problem framing, what I built, and why the result matters.</strong>
                </div>
                <div class="detail-box">
                    <span>What I avoid</span>
                    <strong>Project cards that hide the useful part until someone hovers and has to guess where to look.</strong>
                </div>
                <div class="detail-box">
                    <span>How to read this page</span>
                    <strong>Each card starts with the context, then the build, then the business or research takeaway.</strong>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    for project in PROJECTS:
        image_html = ""
        if "image_path" in project:
            image_src = _image_to_data_uri(project["image_path"])
            image_html = f'<img class="project-image" src="{image_src}" alt="{project["title"]} screenshot">'

        link_html = ""
        if project.get("link_url") and project.get("link_label"):
            link_html = f'<div class="project-link-row"><a href="{project["link_url"]}" target="_blank">{project["link_label"]}</a></div>'

        card_html = (
            f'<div class="project-card">'
            f'<div class="project-card-inner">'
            f"{image_html}"
            f'<div class="project-meta">'
            f'<div class="project-date">{project["dates"]}</div>'
            f'<div class="project-tag">{project["tag"]}</div>'
            f"</div>"
            f'<div class="project-lead">'
            f'<h3>{project["title"]}</h3>'
            f'<p class="project-summary">{project["result"]}</p>'
            f"</div>"
            f'<div class="project-structure">'
            f'<div class="project-block"><strong>Problem</strong><p>{project["problem"]}</p></div>'
            f'<div class="project-block"><strong>What I built</strong><p>{project["built"]}</p></div>'
            f'<div class="project-block"><strong>Why it matters</strong><p>{project["hover"]}</p></div>'
            f"</div>"
            f'<div class="project-footer">'
            f'<div class="tool-chip-row">{"".join(f"<span class=\'tool-chip\'>{tool}</span>" for tool in project["tools"])}</div>'
            f"{link_html}"
            f"</div>"
            f"</div>"
        )

        st.markdown(
            card_html,
            unsafe_allow_html=True,
        )
        st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
