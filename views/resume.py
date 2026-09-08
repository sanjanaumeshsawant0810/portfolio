from pathlib import Path

import streamlit as st


RESUME_PATH = Path(__file__).resolve().parents[1] / "assets" / "resume" / "Sanjana_Sawant_Data_Science_Resume.pdf"
PREVIEW_PATH = RESUME_PATH.with_name("Sanjana_Sawant_Data_Science_Resume_Preview-1.png")


def render_resume_page() -> None:
    if not RESUME_PATH.exists():
        st.error("The resume PDF is missing from assets/resume.")
        return

    st.markdown(
        """
        <style>
            div[data-testid="stDownloadButton"] button {
                background: #315f72 !important;
                border: 1px solid #315f72 !important;
                color: #ffffff !important;
            }

            div[data-testid="stDownloadButton"] button:hover {
                background: #274f60 !important;
                border-color: #274f60 !important;
                color: #ffffff !important;
            }

            div[data-testid="stDownloadButton"] button p {
                color: inherit !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="content-card compact-card">
            <div class="section-label">Resume</div>
            <h1>Resume download and preview</h1>
            <p>This page keeps the document in the same structure as the rest of the site: quick access to the file first, then an embedded preview for a faster scan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)

    with st.container(border=False):
        st.download_button(
            "Download resume",
            data=RESUME_PATH.read_bytes(),
            file_name=RESUME_PATH.name,
            mime="application/pdf",
            use_container_width=True,
        )
    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    if not PREVIEW_PATH.exists():
        st.error("The resume preview is missing from assets/resume.")
        return

    with st.container(border=True):
        st.image(str(PREVIEW_PATH), use_column_width=True)
