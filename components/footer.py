import streamlit as st


def render_footer() -> None:
    st.markdown("---")
    st.markdown(
        """
        <div class="site-footer">
            <p>Built to present experience, projects, and application materials in one focused portfolio system.</p>
            <p>&copy; 2026 Sanjana Sawant</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
