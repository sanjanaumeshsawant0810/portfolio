import streamlit as st


def apply_global_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --bg: #090d09;
            --bg-soft: #111811;
            --panel: rgba(18, 26, 20, 0.72);
            --panel-strong: rgba(22, 31, 24, 0.9);
            --panel-solid: #182019;
            --text: #f5f6f1;
            --muted: #afb7a6;
            --line: rgba(214, 223, 203, 0.1);
            --line-strong: rgba(214, 223, 203, 0.18);
            --accent: #dbe7c2;
            --accent-soft: rgba(219, 231, 194, 0.12);
            --accent-warm: #e2ba78;
            --highlight: rgba(255, 255, 255, 0.08);
            --shadow: 0 24px 60px rgba(0, 0, 0, 0.28);
            --shadow-strong: 0 30px 80px rgba(0, 0, 0, 0.36);
            --blur: blur(18px) saturate(150%);
        }

        html,
        body,
        [class*="css"] {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Avenir Next", "Segoe UI", sans-serif;
            color: var(--text);
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        .stApp {
            background:
                radial-gradient(circle at top right, rgba(226, 186, 120, 0.14), transparent 18%),
                radial-gradient(circle at 12% 16%, rgba(219, 231, 194, 0.14), transparent 22%),
                radial-gradient(circle at 50% -12%, rgba(255, 255, 255, 0.05), transparent 26%),
                linear-gradient(180deg, #0a0d0a 0%, #101510 42%, #0b100b 100%);
            background-attachment: fixed;
        }

        .stApp::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background:
                linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
            background-size: 40px 40px;
            mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.7), transparent 85%);
            opacity: 0.3;
        }

        ::selection {
            background: rgba(226, 186, 120, 0.3);
            color: #ffffff;
        }

        section[data-testid="stSidebar"],
        div[data-testid="stSidebarNav"],
        div[data-testid="collapsedControl"] {
            display: none !important;
        }

        h1, h2, h3, h4 {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Avenir Next", sans-serif;
            color: #f7f8f4;
            letter-spacing: -0.03em;
            font-weight: 600;
        }

        h1 {
            line-height: 0.98;
        }

        h2, h3, h4 {
            line-height: 1.08;
        }

        p, li, label, span {
            color: var(--text);
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3.5rem;
            max-width: 1120px;
        }

        .page-gap {
            height: 1.15rem;
        }

        .home-hero-gap {
            height: 2rem;
        }

        .hero-stack-gap {
            height: 0.9rem;
        }

        div[data-testid="stRadio"] {
            background:
                linear-gradient(180deg, rgba(24, 33, 25, 0.82), rgba(16, 22, 17, 0.74));
            border: 1px solid var(--line-strong);
            border-radius: 999px;
            box-shadow:
                0 1px 0 rgba(255, 255, 255, 0.06) inset,
                var(--shadow);
            padding: 0.45rem 0.7rem;
            margin-bottom: 1.5rem;
            backdrop-filter: var(--blur);
            width: fit-content;
            max-width: 100%;
            margin-left: auto;
            margin-right: auto;
            position: sticky;
            top: 0.9rem;
            z-index: 10;
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
            min-height: 2.65rem;
            padding: 0.42rem 0.95rem;
            border-radius: 999px;
            background: transparent;
            transition: transform 140ms ease, background 180ms ease, box-shadow 180ms ease;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label > div:first-child {
            display: none;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] p {
            color: var(--muted);
            font-weight: 600;
            font-size: 0.96rem;
            letter-spacing: -0.01em;
            transition: color 0.18s ease;
            margin: 0;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
            background: rgba(255, 255, 255, 0.05);
            transform: translateY(-1px);
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label:active {
            transform: scale(0.985);
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label:hover p {
            color: #f0f2e9;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label[data-selected="true"] {
            background: linear-gradient(180deg, rgba(223, 235, 203, 0.12), rgba(212, 225, 188, 0.08));
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.08),
                inset 0 0 0 1px rgba(223, 235, 203, 0.1);
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
            border-radius: 28px;
            box-shadow: var(--shadow);
            padding: 1.5rem;
            backdrop-filter: var(--blur);
            position: relative;
            overflow: hidden;
        }

        .content-card,
        .contact-card,
        .timeline-card {
            min-height: 100%;
        }

        .hero-card::before,
        .content-card::before,
        .contact-card::before,
        .hover-project-card::before,
        .timeline-card::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.06), transparent 22%);
            pointer-events: none;
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
                radial-gradient(circle at top right, rgba(226, 186, 120, 0.16), transparent 24%),
                radial-gradient(circle at 18% 0%, rgba(255, 255, 255, 0.08), transparent 28%),
                linear-gradient(135deg, rgba(20, 28, 21, 0.9), rgba(15, 21, 16, 0.84));
            box-shadow: var(--shadow-strong);
        }

        .hero-card::after {
            content: "";
            position: absolute;
            inset: auto -8% -34% 38%;
            height: 250px;
            background: radial-gradient(circle, rgba(226, 186, 120, 0.16), transparent 64%);
            pointer-events: none;
        }

        .eyebrow {
            color: #e9efd6;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 0.85rem;
        }

        .hero-title {
            font-size: clamp(2.7rem, 5vw, 4.8rem);
            line-height: 0.94;
            margin: 0;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            line-height: 1.45;
            color: #edf0e5;
            max-width: 42rem;
            margin: 1rem 0 0.35rem;
            letter-spacing: -0.01em;
        }

        .hero-card > p:last-of-type {
            color: var(--muted);
            max-width: 47rem;
            line-height: 1.7;
        }

        .chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
            margin-top: 1.15rem;
        }

        .chip {
            display: inline-block;
            background: rgba(255, 255, 255, 0.05);
            color: #edf2df;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 999px;
            padding: 0.48rem 0.82rem;
            font-size: 0.88rem;
            font-weight: 500;
            letter-spacing: -0.01em;
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 0.9rem;
            margin-top: 1.45rem;
        }

        .kpi {
            background: rgba(15, 21, 16, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 22px;
            padding: 1rem;
            backdrop-filter: blur(10px);
            color: #b7c0b3;
        }

        .kpi strong {
            display: block;
            color: #f5f6f1;
            font-size: 1.55rem;
            letter-spacing: -0.04em;
            margin-bottom: 0.25rem;
        }

        .section-label {
            color: var(--accent-warm);
            text-transform: uppercase;
            letter-spacing: 0.13em;
            font-size: 0.74rem;
            font-weight: 700;
            margin-bottom: 0.45rem;
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

        .content-card p,
        .timeline-card p,
        .contact-card p,
        .hover-project-card p {
            color: var(--muted);
            line-height: 1.7;
            letter-spacing: -0.01em;
        }

        .content-card h3,
        .timeline-card h3 {
            margin-top: 0;
            margin-bottom: 0.75rem;
            font-size: clamp(1.45rem, 2vw, 1.8rem);
        }

        .content-card h4,
        .timeline-card h4 {
            margin-top: 0.9rem;
            margin-bottom: 0.35rem;
            color: #f5f6f1;
        }

        .content-card ul,
        .timeline-card ul {
            margin: 0.35rem 0 0;
            padding-left: 1.1rem;
        }

        .content-card li,
        .timeline-card li {
            margin-bottom: 0.45rem;
            color: #d9ddd1;
            line-height: 1.65;
        }

        .link-row a {
            color: #edf2df;
            font-weight: 600;
            text-decoration: none;
            margin-right: 1rem;
            transition: opacity 160ms ease, transform 160ms ease;
        }

        .link-row a:hover {
            opacity: 0.82;
        }

        .link-row a:active {
            transform: scale(0.985);
        }

        .hover-project-card {
            position: relative;
            min-height: 265px;
            overflow: hidden;
            transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
            background:
                linear-gradient(180deg, rgba(24, 33, 25, 0.84), rgba(12, 17, 13, 0.88));
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
            border-color: rgba(255, 255, 255, 0.14);
            box-shadow: var(--shadow-strong);
        }

        .hover-project-card:active {
            transform: scale(0.99);
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
            color: #edf0e8;
        }

        .metric-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 1rem;
            margin-top: 1.1rem;
        }

        .metric-box {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 1rem;
            color: #c4cbc0;
            line-height: 1.6;
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
            border: 1px solid rgba(255, 255, 255, 0.12);
            background: linear-gradient(135deg, rgba(219, 231, 194, 0.18), rgba(226, 186, 120, 0.16));
            color: #f0f2e9;
            font-weight: 600;
            min-height: 3rem;
            padding: 0.9rem 1rem;
            text-decoration: none;
            transition: transform 140ms ease, box-shadow 180ms ease, opacity 180ms ease;
            box-shadow: 0 1px 0 rgba(255, 255, 255, 0.08) inset;
        }

        .resume-download-link:hover {
            box-shadow:
                0 1px 0 rgba(255, 255, 255, 0.08) inset,
                0 12px 30px rgba(0, 0, 0, 0.18);
        }

        .resume-download-link:active {
            transform: scale(0.985);
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

            div[data-testid="stRadio"] {
                top: 0.6rem;
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
                border-radius: 24px;
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

        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                animation: none !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }

            div[data-testid="stRadio"],
            .hero-card,
            .content-card,
            .contact-card,
            .hover-project-card,
            .timeline-card,
            .kpi,
            .metric-box {
                backdrop-filter: none;
            }

            .hover-project-card:hover,
            .hover-project-card:active,
            div[data-testid="stRadio"] div[role="radiogroup"] label:hover,
            div[data-testid="stRadio"] div[role="radiogroup"] label:active,
            .resume-download-link:active {
                transform: none;
            }
        }

        @media (prefers-contrast: more) {
            :root {
                --panel: rgba(24, 30, 24, 0.96);
                --line: rgba(255, 255, 255, 0.22);
                --line-strong: rgba(255, 255, 255, 0.28);
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
