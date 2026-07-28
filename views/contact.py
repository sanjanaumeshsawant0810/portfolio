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

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="content-card stack-card">
            <div>
                <h3>Best way to reach me</h3>
                <p>The fastest way to reach me is through email.</p>
                <p><strong>Email:</strong> <a href="mailto:{PROFILE['email']}">{PROFILE['email']}</a></p>
                <p><strong>Phone:</strong> <a href="tel:+18485651174">{PHONE}</a></p>
                <p><strong>Location:</strong> {PROFILE['location']}</p>
                <p><strong>LinkedIn:</strong> <a href="{PROFILE['linkedin']}" target="_blank">{PROFILE['linkedin']}</a></p>
                <p><strong>GitHub:</strong> <a href="{PROFILE['github']}" target="_blank">{PROFILE['github']}</a></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
