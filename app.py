import streamlit as st

from components.footer import render_footer
from components.navbar import render_navbar
from components.styles import apply_global_styles
from data.profile import PROFILE
from pages.about import render_about_page
from pages.contact import render_contact_page
from pages.home import render_home_page
from pages.projects import render_projects_page
from pages.resume import render_resume_page


st.set_page_config(
    page_title=f"{PROFILE['name']} | Portfolio",
    page_icon="Data-Professionals.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_global_styles()

PAGES = {
    "Overview": render_home_page,
    "Experience": render_about_page,
    "Projects": render_projects_page,
    "Resume": render_resume_page,
    "Connect": render_contact_page,
}

selected_page = render_navbar(list(PAGES))
PAGES[selected_page]()
render_footer()
