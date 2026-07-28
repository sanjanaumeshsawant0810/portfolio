import streamlit as st


def render_navbar(page_names: list[str]) -> str:
    if "current_page" not in st.session_state or st.session_state.current_page not in page_names:
        st.session_state.current_page = page_names[0]

    selected_page = st.radio(
        "Navigation",
        page_names,
        key="current_page",
        horizontal=True,
        label_visibility="collapsed",
    )

    return selected_page
