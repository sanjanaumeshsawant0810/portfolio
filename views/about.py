import streamlit as st

from data.profile import PROFILE


def render_about_page() -> None:
    st.markdown(
        """
        <div class="content-card">
            <div class="section-label">Experience</div>
            <h1>How I got here, what I learned, and what kind of work I want more of</h1>
            <p>I did not come into this with a perfectly linear data science story. I came in through engineering, systems, debugging, and figuring things out. Over time, the pattern became clear. I like data work that leads to a real decision, a cleaner workflow, or a better product experience.</p>
            <p>This page is here so the projects do not feel random. I want the work to read like it came from one person with a clear direction.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='home-hero-gap'></div>", unsafe_allow_html=True)

    leadership_html = []
    for item in PROFILE["leadership"]:
        leadership_html.append(f"<h4>{item['title']}</h4><p>{item['details']}</p>")

    certification_html = ["<ul>"]
    for item in PROFILE["certifications"]:
        certification_html.append(f"<li>{item}</li>")
    certification_html.append("</ul>")

    experience_html = []
    for role in PROFILE["experience"]:
        bullets = "".join(f"<li>{bullet}</li>" for bullet in role["bullets"])
        experience_html.append(
            f"<div class='experience-entry'>"
            f"<div class='section-label'>{role['dates']}</div>"
            f"<h4>{role['role']} | {role['company']}</h4>"
            f"<ul>{bullets}</ul>"
            f"</div>"
        )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="section-shell">
            <div class="section-heading">
                <div class="section-label">Timeline</div>
                <h2 class="section-title">The work history that connects the portfolio</h2>
                <p>The common thread is not one job title. It is tracing a messy system, cleaning up the logic under it, and turning the output into something another person can use.</p>
            </div>
            <div class="content-card compact-card">
                <h3>Internship and work experience</h3>
                {''.join(experience_html)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    education_html = []
    for item in PROFILE["education"]:
        education_html.append(
            f"<div class='experience-entry'>"
            f"<div class='section-label'>{item['dates']}</div>"
            f"<h4>{item['degree']} | {item['school']}</h4>"
            f"<p><strong>GPA:</strong> {item['gpa']}</p>"
            f"<p>{item['notes']}</p>"
            f"</div>"
        )

    st.markdown(
        f"""
        <div class="section-grid section-grid-wide">
            <div class="content-card compact-card">
                <h3>Education</h3>
                {''.join(education_html)}
            </div>
            <div class="content-card compact-card">
                <h3>Leadership and recognition</h3>
                {''.join(leadership_html)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='page-gap'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="section-grid section-grid-wide">
            <div class="content-card compact-card">
                <h3>What I want next</h3>
                <ul>
                    <li>Roles where analytics, SQL, experimentation, and product thinking all matter at the same time.</li>
                    <li>Teams that care about trustworthy reporting, clean data flow, and useful outputs instead of analysis that just sits in a notebook.</li>
                    <li>Work where I can keep growing across data science, analytics engineering, AI products, and fintech-style decision systems.</li>
                </ul>
            </div>
            <div class="content-card compact-card">
                <h3>Certifications</h3>
                {''.join(certification_html)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
