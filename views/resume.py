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
                background: #161d16 !important;
                border: 1px solid rgba(184, 201, 140, 0.42) !important;
                color: #edf1e7 !important;
            }

            div[data-testid="stDownloadButton"] button:hover {
                background: #1d281d !important;
                border-color: #b8c98c !important;
                color: #f0f2e9 !important;
            }

            div[data-testid="stDownloadButton"] button p {
                color: inherit !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
