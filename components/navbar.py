import streamlit as st


def render_navbar(page_names: list[str]) -> str:
    if "current_page" not in st.session_state or st.session_state.current_page not in page_names:
        st.session_state.current_page = page_names[0]

    nav_columns = st.columns(len(page_names), gap="small")

    for column, page_name in zip(nav_columns, page_names):
        button_type = "primary" if st.session_state.current_page == page_name else "secondary"
        if column.button(page_name, key=f"nav_{page_name.lower()}", type=button_type, use_container_width=True):
            st.session_state.current_page = page_name

    return st.session_state.current_page
