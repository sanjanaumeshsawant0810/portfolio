import streamlit as st


def apply_global_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #0d120d;
            --bg-soft: #161d16;
            --panel: rgba(17, 24, 18, 0.84);
            --panel-strong: rgba(23, 31, 24, 0.94);
            --text: #edf1e7;
            --muted: #a8b09a;
            --line: rgba(154, 177, 129, 0.18);
            --accent: #b8c98c;
            --accent-soft: rgba(184, 201, 140, 0.12);
            --accent-warm: #d6a75a;
            --shadow: 0 18px 44px rgba(2, 8, 23, 0.34);
        }

        html, body, [class*="css"]  {
            font-family: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
            color: var(--text);
        }

        .stApp {
            background:
                linear-gradient(rgba(184, 201, 140, 0.045) 1px, transparent 1px),
                linear-gradient(90deg, rgba(184, 201, 140, 0.045) 1px, transparent 1px),
                radial-gradient(circle at top right, rgba(184, 201, 140, 0.16), transparent 24%),
                radial-gradient(circle at 18% 18%, rgba(214, 167, 90, 0.1), transparent 20%),
                linear-gradient(180deg, #0b100b 0%, #121812 52%, #0d120d 100%);
            background-size: 34px 34px, 34px 34px, auto, auto, auto;
        }

        section[data-testid="stSidebar"],
        div[data-testid="stSidebarNav"],
        div[data-testid="collapsedControl"] {
            display: none !important;
        }

        h1, h2, h3, h4 {
            font-family: "Space Grotesk", "IBM Plex Sans", sans-serif;
            color: #f0f2e9;
            letter-spacing: -0.02em;
        }

        p, li, label, span, div {
            color: var(--text);
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        .page-gap {
            height: 1.35rem;
        }

        .home-hero-gap {
            height: 2.4rem;
        }

        .hero-stack-gap {
            height: 1.1rem;
        }

        div[data-testid="stRadio"] {
            background:
                linear-gradient(135deg, rgba(18, 27, 19, 0.94), rgba(13, 18, 13, 0.92));
            border: 1px solid var(--line);
            border-radius: 999px;
            box-shadow: var(--shadow);
            padding: 0.55rem 0.9rem;
            margin-bottom: 1.75rem;
            backdrop-filter: blur(10px);
            width: fit-content;
            max-width: 100%;
            margin-left: auto;
            margin-right: auto;
        }

        div[data-testid="stRadio"] > div {
            margin: 0;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.45rem;
            flex-wrap: wrap;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.7rem;
            padding: 0.45rem 1rem;
            border-radius: 999px;
            background: transparent;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] p {
            color: var(--muted);
            font-weight: 700;
            font-size: 1rem;
            transition: background 0.18s ease, color 0.18s ease, transform 0.18s ease;
            margin: 0;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
            background: rgba(184, 201, 140, 0.08);
            transform: translateY(-1px);
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label:hover p {
            color: #f0f2e9;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label[data-selected="true"] {
            background: rgba(184, 201, 140, 0.14);
            box-shadow: inset 0 0 0 1px rgba(184, 201, 140, 0.14);
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label[data-selected="true"] p {
            color: #ffffff;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label[data-selected="true"]::after {
            content: "";
            width: 0.45rem;
            height: 0.45rem;
            border-radius: 50%;
            background: #d6a75a;
            margin-left: 0.55rem;
            box-shadow: 0 0 10px rgba(214, 167, 90, 0.45);
        }

        .hero-card,
        .content-card,
        .contact-card,
        .hover-project-card,
        .timeline-card {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 24px;
            box-shadow: var(--shadow);
            padding: 1.5rem;
            backdrop-filter: blur(10px);
        }

        .content-card,
        .contact-card,
        .timeline-card {
            min-height: 100%;
        }

        .stack-card {
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
            height: 100%;
        }

        .compact-card {
            padding: 1.35rem;
        }

        .hero-card {
            padding: 2.1rem;
            background:
                radial-gradient(circle at top right, rgba(184, 201, 140, 0.1), transparent 26%),
                linear-gradient(135deg, rgba(16, 24, 17, 0.94), rgba(20, 29, 21, 0.94));
            position: relative;
            overflow: hidden;
        }

        .hero-card::after {
            content: "";
            position: absolute;
            inset: auto -10% -35% 35%;
            height: 220px;
            background: radial-gradient(circle, rgba(214, 167, 90, 0.14), transparent 64%);
            pointer-events: none;
        }

        .eyebrow {
            color: var(--accent);
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }

        .hero-title {
            font-size: clamp(2.3rem, 4vw, 4.3rem);
            line-height: 1.02;
            margin: 0;
        }

        .hero-subtitle {
            font-size: 1.08rem;
            color: var(--muted);
            max-width: 46rem;
            margin-top: 1rem;
        }

        .chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 1rem;
        }

        .chip {
            display: inline-block;
            background: var(--accent-soft);
            color: var(--accent);
            border: 1px solid rgba(184, 201, 140, 0.2);
            border-radius: 999px;
            padding: 0.45rem 0.8rem;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 1rem;
            margin-top: 1.35rem;
        }

        .kpi {
            background: rgba(18, 25, 18, 0.9);
            border: 1px solid var(--line);
            border-radius: 18px;
            padding: 1rem;
        }

        .kpi strong {
            display: block;
            color: var(--accent);
            font-size: 1.35rem;
        }

        .section-label {
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 0.35rem;
        }

        .section-title {
            margin: 0;
        }

        .section-intro-card p,
        .section-heading-block p {
            margin-bottom: 0;
        }

        .section-heading-block {
            margin-bottom: 0.9rem;
        }

        .content-card p, .timeline-card p, .contact-card p, .hover-project-card p {
            color: var(--text);
            line-height: 1.65;
        }

        .content-card h3,
        .timeline-card h3 {
            margin-top: 0;
            margin-bottom: 0.8rem;
        }

        .content-card h4,
        .timeline-card h4 {
            margin-top: 0.9rem;
            margin-bottom: 0.35rem;
            color: #f0f2e9;
        }

        .content-card ul, .timeline-card ul {
            margin: 0.35rem 0 0;
            padding-left: 1.1rem;
        }

        .content-card li, .timeline-card li {
            margin-bottom: 0.35rem;
        }

        .link-row a {
            color: var(--accent);
            font-weight: 700;
            text-decoration: none;
            margin-right: 1rem;
        }

        .link-row a:hover {
            color: #ffffff;
        }

        .hover-project-card {
            position: relative;
            min-height: 265px;
            overflow: hidden;
            transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
            background:
                linear-gradient(180deg, rgba(22, 31, 23, 0.96), rgba(12, 17, 13, 0.95));
        }

        .project-image {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.28;
            pointer-events: none;
        }

        .hover-project-card:hover {
            transform: translateY(-4px);
            border-color: rgba(184, 201, 140, 0.34);
            box-shadow: 0 22px 44px rgba(2, 8, 23, 0.42);
        }

        .hover-summary {
            position: relative;
            z-index: 1;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: opacity 0.22s ease, transform 0.22s ease;
        }

        .hover-topline {
            color: var(--muted);
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.45rem;
        }

        .hover-preview {
            color: var(--muted);
            margin-top: 0.8rem;
        }

        .hover-details {
            position: absolute;
            inset: 0;
            z-index: 1;
            padding: 1.35rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            background: linear-gradient(180deg, rgba(10, 14, 10, 0.08), rgba(10, 14, 10, 0.98) 24%);
            opacity: 0;
            transform: translateY(14px);
            transition: opacity 0.24s ease, transform 0.24s ease;
        }

        .hover-project-card:hover .hover-summary {
            opacity: 0;
            transform: scale(0.985);
        }

        .hover-project-card:hover .hover-details {
            opacity: 1;
            transform: translateY(0);
        }

        .hover-details p {
            margin: 0.35rem 0;
            font-size: 0.94rem;
        }

        .metric-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 1rem;
            margin-top: 1.1rem;
        }

        .metric-box {
            background: rgba(17, 24, 18, 0.7);
            border: 1px solid var(--line);
            border-radius: 18px;
            padding: 1rem;
        }

        .metric-box strong {
            display: block;
            color: var(--accent-warm);
            font-size: 1.25rem;
            margin-bottom: 0.2rem;
        }

        .experience-entry + .experience-entry {
            margin-top: 1.2rem;
            padding-top: 1.2rem;
            border-top: 1px solid var(--line);
        }

        .resume-download-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            box-sizing: border-box;
            border-radius: 14px;
            border: 1px solid rgba(184, 201, 140, 0.25);
            background: linear-gradient(135deg, rgba(184, 201, 140, 0.18), rgba(214, 167, 90, 0.14));
            color: #f0f2e9;
            font-weight: 700;
            min-height: 3rem;
            padding: 0.9rem 1rem;
            text-decoration: none;
        }

        .site-footer {
            text-align: center;
            color: var(--muted);
            font-size: 0.9rem;
            padding-bottom: 1rem;
            margin-top: 2rem;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-top: 1rem;
            }

            .page-gap {
                height: 1rem;
            }

            .home-hero-gap {
                height: 1.5rem;
            }

            .hero-stack-gap {
                height: 0.85rem;
            }

            .hero-card,
            .content-card,
            .contact-card,
            .hover-project-card,
            .timeline-card {
                padding: 1.15rem;
                border-radius: 20px;
            }

            .hover-details {
                position: static;
                padding: 0.9rem 0 0;
                opacity: 1;
                transform: none;
                background: transparent;
            }

            .hover-summary {
                opacity: 1 !important;
                transform: none !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
