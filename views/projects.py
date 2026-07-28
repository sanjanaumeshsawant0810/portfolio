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
        <div class="content-card">
            <div class="section-label">Projects</div>
            <h1>The projects here are the ones I would actually want to talk about</h1>
            <p>I am not trying to make every project look the same. Some of these are more product-heavy, some are more analytics-heavy, and some are here because they show how I think when the problem is messy, technical, or worth digging into.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    for project in PROJECTS:
        tools = " | ".join(project["tools"])
        image_html = ""
        if "image_path" in project:
            image_src = _image_to_data_uri(project["image_path"])
            image_html = f'<img class="project-image" src="{image_src}" alt="{project["title"]} screenshot">'

        link_html = ""
        if project.get("link_url") and project.get("link_label"):
            link_html = f'<p><a href="{project["link_url"]}" target="_blank">{project["link_label"]}</a></p>'

        card_html = (
            f'<div class="hover-project-card">'
            f"{image_html}"
            f'<div class="hover-summary">'
            f"<div>"
            f'<div class="hover-topline">{project["dates"]} | {project["tag"]}</div>'
            f'<h3>{project["title"]}</h3>'
            f"</div>"
            f'<p class="hover-preview">{project["result"]}</p>'
            f"</div>"
            f'<div class="hover-details">'
            f'<p><strong>Problem:</strong> {project["problem"]}</p>'
            f'<p><strong>What I built:</strong> {project["built"]}</p>'
            f'<p><strong>Tools used:</strong> {tools}</p>'
            f"{link_html}"
            f"</div>"
            f"</div>"
        )

        st.markdown(
            card_html,
            unsafe_allow_html=True,
        )
        st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
