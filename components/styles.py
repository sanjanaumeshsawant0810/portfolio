import streamlit as st


def apply_global_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #f7f4ee;
            --surface: #ffffff;
            --surface-soft: #f0ebe2;
            --text: #27231f;
            --muted: #6f6860;
            --quiet: #91887d;
            --line: #ded6cb;
            --line-strong: #c8bfb3;
            --accent: #315f72;
            --accent-soft: #e2edf1;
            --accent-warm: #9b6249;
            --ease-out: cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        html,
        body,
        [class*="css"] {
            font-family: "Avenir Next", "Segoe UI", "Helvetica Neue", sans-serif;
            color: var(--text);
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        .stApp {
            background: var(--bg);
        }

        ::selection {
            background: rgba(49, 95, 114, 0.18);
            color: var(--text);
        }

        section[data-testid="stSidebar"],
        div[data-testid="stSidebarNav"],
        div[data-testid="collapsedControl"],
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stStatusWidget"],
        [data-testid="stDecoration"],
        .stAppHeader,
        header {
            display: none !important;
            height: 0 !important;
        }

        .block-container {
            max-width: 1080px;
            padding-top: 1.2rem;
            padding-bottom: 3.5rem;
        }

        .page-gap {
            height: 1rem;
        }

        .home-hero-gap {
            height: 1.7rem;
        }

        .hero-stack-gap {
            height: 0.75rem;
        }

        h1,
        h2,
        h3,
        h4 {
            color: var(--text);
            font-family: "Avenir Next", "Segoe UI", "Helvetica Neue", sans-serif;
            font-weight: 650;
            letter-spacing: 0;
            line-height: 1.08;
        }

        h1 {
            font-size: 2.8rem;
            margin-bottom: 0.8rem;
        }

        h2 {
            font-size: 2rem;
        }

        h3 {
            font-size: 1.35rem;
        }

        h4 {
            font-size: 1.05rem;
        }

        p,
        li,
        label,
        span {
            color: var(--text);
        }

        p,
        li {
            line-height: 1.65;
        }

        div[data-testid="stHorizontalBlock"] {
            margin-bottom: 1.2rem;
        }

        div[data-testid="stButton"] > button,
        div[data-testid="stDownloadButton"] button {
            min-height: 2.55rem;
            border-radius: 8px !important;
            border: 1px solid var(--line) !important;
            background: var(--surface) !important;
            color: var(--muted) !important;
            font-weight: 600 !important;
            letter-spacing: 0 !important;
            box-shadow: none !important;
            transition: background 160ms var(--ease-out), border-color 160ms var(--ease-out), color 160ms var(--ease-out);
        }

        div[data-testid="stButton"] > button:hover,
        div[data-testid="stDownloadButton"] button:hover {
            border-color: var(--accent) !important;
            color: var(--accent) !important;
            background: var(--accent-soft) !important;
        }

        div[data-testid="stButton"] > button[kind="primary"] {
            background: var(--accent) !important;
            border-color: var(--accent) !important;
            color: #ffffff !important;
        }

        div[data-testid="stButton"] > button[kind="primary"]:hover {
            background: #274f60 !important;
            color: #ffffff !important;
        }

        .hero-card,
        .content-card,
        .contact-card,
        .project-card,
        .timeline-card {
            background: transparent;
            border: 0;
            border-radius: 0;
            box-shadow: none;
            padding: 0;
            position: relative;
        }

        .content-card,
        .contact-card,
        .timeline-card {
            min-height: 100%;
        }

        .compact-card {
            padding: 0;
        }

        .simple-hero {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(220px, 0.42fr);
            gap: 3.5rem;
            align-items: end;
        }

        .hero-copy {
            display: flex;
            flex-direction: column;
            max-width: 43rem;
        }

        .hero-title {
            font-size: 3rem;
            margin: 0;
        }

        .hero-subtitle {
            color: var(--muted);
            font-size: 1.1rem;
            line-height: 1.6;
            max-width: 41rem;
            margin: 1rem 0 0;
        }

        .hero-summary {
            color: var(--muted);
            max-width: 46rem;
            margin-top: 0.9rem;
        }

        .hero-photo {
            margin: 0;
            overflow: hidden;
            background: var(--surface-soft);
        }

        .hero-photo img {
            display: block;
            width: 100%;
            height: 340px;
            object-fit: cover;
            object-position: center top;
        }

        .text-link-row {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1.7rem;
        }

        .text-link-row a,
        .project-link-row a {
            color: var(--accent);
            font-weight: 650;
            text-decoration: none;
            border-bottom: 1px solid var(--accent);
            padding-bottom: 0.15rem;
        }

        .text-link-row a:hover,
        .project-link-row a:hover {
            color: var(--accent-warm);
            border-color: var(--accent-warm);
        }

        .eyebrow,
        .section-label {
            color: var(--accent-warm);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 0.65rem;
        }

        .section-title {
            margin: 0;
        }

        .section-intro-card p,
        .section-heading-block p {
            margin-bottom: 0;
        }

        .section-heading-block {
            margin-bottom: 0.8rem;
        }

        .content-card p,
        .timeline-card p,
        .contact-card p,
        .project-card p {
            color: var(--muted);
            line-height: 1.65;
        }

        .content-card h3,
        .timeline-card h3 {
            margin-top: 0;
            margin-bottom: 0.65rem;
        }

        .content-card h4,
        .timeline-card h4 {
            margin-top: 0.85rem;
            margin-bottom: 0.35rem;
        }

        .content-card ul,
        .timeline-card ul {
            margin: 0.35rem 0 0;
            padding-left: 1.1rem;
        }

        .content-card li,
        .timeline-card li {
            margin-bottom: 0.45rem;
            color: var(--muted);
        }

        .chip-row,
        .tool-chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .chip,
        .tool-chip {
            display: inline-flex;
            align-items: center;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--surface-soft);
            color: var(--muted);
            padding: 0.42rem 0.62rem;
            font-size: 0.86rem;
            font-weight: 500;
        }

        .kpi-grid,
        .metric-strip,
        .section-grid,
        .section-grid-wide,
        .detail-grid,
        .contact-link-grid,
        .quiet-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
        }

        .kpi,
        .metric-box,
        .detail-box,
        .project-block,
        .contact-link-card {
            background: transparent;
            border: 0;
            border-radius: 0;
            padding: 0;
        }

        .kpi strong,
        .metric-box strong,
        .detail-box strong,
        .project-block strong,
        .contact-link-card strong {
            display: block;
            color: var(--text);
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }

        .kpi {
            color: var(--muted);
        }

        .kpi strong {
            color: var(--accent);
            font-size: 1.35rem;
        }

        .section-shell,
        .section-stack {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .section-heading {
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
        }

        .section-heading p,
        .section-heading-block p {
            color: var(--muted);
            max-width: 46rem;
        }

        .project-card {
            border-top: 1px solid var(--line);
            padding: 1.6rem 0;
        }

        .project-image {
            display: block;
            width: 100%;
            height: 210px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 1rem;
            border: 1px solid var(--line);
        }

        .project-card-inner {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .project-meta {
            display: flex;
            justify-content: space-between;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
        }

        .project-date,
        .project-tag,
        .detail-box span,
        .contact-link-card span {
            color: var(--quiet);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .project-tag {
            color: var(--accent);
        }

        .project-lead h3 {
            margin: 0;
        }

        .project-summary {
            color: var(--muted);
            margin: 0;
        }

        .project-structure {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
            gap: 0.75rem;
        }

        .project-block p {
            margin: 0;
            color: var(--muted);
        }

        .project-footer {
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
        }

        .project-link-row a,
        .resume-download-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: fit-content;
            min-height: 2.55rem;
            padding: 0.65rem 0.9rem;
            border-radius: 0;
            border: 0;
            border-bottom: 1px solid var(--accent);
            background: transparent;
            color: var(--accent);
            font-weight: 650;
            text-decoration: none;
            transition: color 160ms var(--ease-out), border-color 160ms var(--ease-out);
        }

        .project-link-row a:hover,
        .resume-download-link:hover {
            background: transparent;
            border-color: var(--accent-warm);
            color: var(--accent-warm);
        }

        .contact-link-grid {
            margin-top: 1rem;
        }

        .contact-link-card {
            display: block;
            text-decoration: none;
            min-width: 0;
            border-bottom: 1px solid var(--line);
            padding: 0.8rem 0;
            transition: color 160ms var(--ease-out);
        }

        .contact-link-card:hover {
            border-color: var(--accent);
        }

        .contact-link-card span {
            display: block;
            margin-bottom: 0.3rem;
        }

        .contact-link-card strong {
            overflow-wrap: anywhere;
            word-break: break-word;
        }

        .experience-entry + .experience-entry {
            margin-top: 1.1rem;
            padding-top: 1.1rem;
            border-top: 1px solid var(--line);
        }

        .work-list {
            border-top: 1px solid var(--line);
            margin-top: 1.2rem;
        }

        .work-row {
            display: grid;
            grid-template-columns: 3rem minmax(0, 1fr) minmax(150px, 0.35fr);
            gap: 1.25rem;
            align-items: start;
            padding: 1.25rem 0;
            border-bottom: 1px solid var(--line);
        }

        .work-index,
        .work-type {
            color: var(--quiet);
            font-size: 0.78rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        .work-copy h3 {
            margin: 0 0 0.35rem;
        }

        .work-copy p,
        .work-type {
            color: var(--muted);
            margin: 0;
        }

        .about-strip {
            display: grid;
            grid-template-columns: minmax(0, 0.8fr) minmax(0, 1fr);
            gap: 3rem;
            padding: 1.5rem 0;
            border-top: 1px solid var(--line);
            border-bottom: 1px solid var(--line);
        }

        .about-strip h2 {
            margin: 0;
            max-width: 22rem;
        }

        .about-strip p {
            color: var(--muted);
            margin: 0;
        }

        .site-footer {
            text-align: center;
            color: var(--quiet);
            font-size: 0.9rem;
            padding-bottom: 1rem;
            margin-top: 1.5rem;
        }

        .site-footer p {
            color: var(--quiet);
            margin: 0.25rem 0;
        }

        hr {
            border: none;
            border-top: 1px solid var(--line);
            margin: 2rem 0 1.5rem;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-top: 0.9rem;
            }

            h1 {
                font-size: 2.25rem;
            }

            h2 {
                font-size: 1.65rem;
            }

            .simple-hero {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }

            .hero-title {
                font-size: 2.45rem;
            }

            .hero-photo img {
                height: 300px;
            }

            .project-image {
                height: 185px;
            }

            .work-row,
            .about-strip {
                grid-template-columns: 1fr;
                gap: 0.5rem;
            }

            .work-index {
                margin-bottom: 0.15rem;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                animation: none !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
