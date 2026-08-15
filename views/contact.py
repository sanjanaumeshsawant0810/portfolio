import streamlit as st

from data.profile import PROFILE


PHONE = "+1 (848) 565-1174"


def render_contact_page() -> None:
    st.markdown(
        """
        <div class="contact-card">
            <div class="section-label">Connect</div>
            <h1>Reach me through the channel that makes the most sense</h1>
            <p>I am mainly targeting data science, analytics, AI, and fintech-oriented roles, but I am always open to a good conversation about useful data work, product thinking, and practical technical problems.</p>
            <div class="contact-link-grid">
                <a class="contact-link-card" href="mailto:{email}">
                    <span>Email</span>
                    <strong>{email}</strong>
                </a>
                <a class="contact-link-card" href="tel:+18485651174">
                    <span>Phone</span>
                    <strong>{phone}</strong>
                </a>
                <a class="contact-link-card" href="{linkedin}" target="_blank">
                    <span>LinkedIn</span>
                    <strong>View profile</strong>
                </a>
                <a class="contact-link-card" href="{github}" target="_blank">
                    <span>GitHub</span>
                    <strong>See repositories</strong>
                </a>
            </div>
        </div>
        """.format(
            email=PROFILE["email"],
            phone=PHONE,
            linkedin=PROFILE["linkedin"],
            github=PROFILE["github"],
        ),
        unsafe_allow_html=True,
    )
