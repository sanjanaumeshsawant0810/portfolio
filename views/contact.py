import streamlit as st

from data.profile import PROFILE


PHONE = "+1 (848) 565-1174"


def render_contact_page() -> None:
    st.markdown(
        """
        <div class="contact-card">
            <div class="section-label">Connect</div>
            <p>I am mainly targeting data science, analytics, AI, and fintech-oriented roles, but I am always open to good conversations around useful data, product, and practical technical work.</p>
            <div class="link-row">
                <a href="mailto:{email}">Email</a>
                <a href="tel:+18485651174">Phone</a>
                <a href="{linkedin}" target="_blank">LinkedIn</a>
                <a href="{github}" target="_blank">GitHub</a>
            </div>
        </div>
        """.format(
            email=PROFILE["email"],
            linkedin=PROFILE["linkedin"],
            github=PROFILE["github"],
        ),
        unsafe_allow_html=True,
    )
