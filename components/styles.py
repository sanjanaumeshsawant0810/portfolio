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
            --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
            --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
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
            padding-top: 0.8rem;
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
            top: 0.2rem;
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
            gap: 0;
            min-height: 2.65rem;
            padding: 0.42rem 0.95rem;
            border-radius: 999px;
            background: transparent;
            transition: transform 140ms ease, background 180ms ease, box-shadow 180ms ease;
        }

        div[data-testid="stRadio"] input[type="radio"] {
            position: absolute !important;
            opacity: 0 !important;
            pointer-events: none !important;
            width: 0 !important;
            height: 0 !important;
            margin: 0 !important;
        }

        div[data-testid="stRadio"] input[type="radio"] + div,
        div[data-testid="stRadio"] [data-baseweb="radio"],
        div[data-testid="stRadio"] [role="radio"] {
            display: none !important;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label > div:first-child {
            display: none;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] label > div {
            margin: 0 !important;
            padding: 0 !important;
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

        .hero-card,
        .content-card,
        .contact-card,
        .project-card,
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
        .project-card::before,
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
        .project-card p {
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
            transition: opacity 160ms var(--ease-out), transform 160ms var(--ease-out);
        }

        @media (hover: hover) and (pointer: fine) {
            .link-row a:hover {
                opacity: 0.82;
                transform: translateY(-1px);
            }
        }

        .link-row a:active {
            transform: scale(0.985);
        }

        .project-card {
            position: relative;
            min-height: 100%;
            overflow: hidden;
            transition: transform 220ms var(--ease-out), border-color 220ms var(--ease-out), box-shadow 220ms var(--ease-out), background 220ms var(--ease-out);
            background:
                linear-gradient(180deg, rgba(24, 33, 25, 0.84), rgba(12, 17, 13, 0.88));
        }

        .project-image {
            position: relative;
            width: 100%;
            height: 220px;
            object-fit: cover;
            opacity: 0.72;
            border-radius: 20px;
            margin-bottom: 1rem;
            display: block;
        }

        @media (hover: hover) and (pointer: fine) {
            .project-card:hover {
                transform: translateY(-4px);
                border-color: rgba(255, 255, 255, 0.14);
                box-shadow: var(--shadow-strong);
            }
        }

        .project-card:active {
            transform: scale(0.99);
        }

        .project-card-inner {
            position: relative;
            z-index: 1;
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

        .project-date {
            color: var(--muted);
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .project-tag {
            display: inline-flex;
            align-items: center;
            padding: 0.34rem 0.7rem;
            border-radius: 999px;
            background: rgba(219, 231, 194, 0.1);
            color: #edf2df;
            border: 1px solid rgba(219, 231, 194, 0.16);
            font-size: 0.78rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .project-lead {
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
        }

        .project-lead h3 {
            margin: 0;
        }

        .project-summary {
            color: #edf0e8;
            margin: 0;
            font-size: 1rem;
            line-height: 1.7;
        }

        .project-structure {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 0.85rem;
        }

        .project-block {
            background: rgba(255, 255, 255, 0.035);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 18px;
            padding: 0.95rem 1rem;
        }

        .project-block strong {
            display: block;
            color: #f5f6f1;
            margin-bottom: 0.4rem;
            font-size: 0.88rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .project-block p {
            margin: 0;
            color: var(--muted);
            line-height: 1.65;
        }

        .project-footer {
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
        }

        .tool-chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .tool-chip {
            display: inline-flex;
            align-items: center;
            padding: 0.42rem 0.68rem;
            border-radius: 999px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: rgba(255, 255, 255, 0.04);
            color: #edf0e8;
            font-size: 0.84rem;
        }

        .project-link-row a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: fit-content;
            min-height: 2.75rem;
            padding: 0.72rem 1rem;
            border-radius: 14px;
            border: 1px solid rgba(219, 231, 194, 0.18);
            background: linear-gradient(135deg, rgba(219, 231, 194, 0.12), rgba(226, 186, 120, 0.12));
            color: #f0f2e9;
            font-weight: 600;
            text-decoration: none;
            transition: transform 160ms var(--ease-out), box-shadow 180ms var(--ease-out), opacity 180ms var(--ease-out);
        }

        @media (hover: hover) and (pointer: fine) {
            .project-link-row a:hover {
                transform: translateY(-1px);
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
            }
        }

        .project-link-row a:active {
            transform: scale(0.985);
        }

        .contact-link-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 0.85rem;
            margin-top: 1rem;
        }

        .contact-link-card {
            display: block;
            padding: 1rem;
            border-radius: 18px;
            text-decoration: none;
            background: rgba(255, 255, 255, 0.035);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: transform 160ms var(--ease-out), border-color 180ms var(--ease-out), box-shadow 180ms var(--ease-out);
            min-width: 0;
        }

        .contact-link-card span {
            display: block;
            color: var(--accent-warm);
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.35rem;
        }

        .contact-link-card strong {
            color: #f5f6f1;
            font-size: 0.98rem;
            line-height: 1.5;
            overflow-wrap: anywhere;
            word-break: break-word;
        }

        @media (hover: hover) and (pointer: fine) {
            .contact-link-card:hover {
                transform: translateY(-2px);
                border-color: rgba(255, 255, 255, 0.14);
                box-shadow: 0 18px 40px rgba(0, 0, 0, 0.18);
            }
        }

        .metric-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 1rem;
            margin-top: 1.1rem;
        }

        .section-stack {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .section-shell {
            display: flex;
            flex-direction: column;
            gap: 1.15rem;
        }

        .section-heading {
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
        }

        .section-heading p,
        .section-heading-block p {
            max-width: 46rem;
        }

        .section-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
        }

        .section-grid-wide {
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        }

        .detail-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 0.75rem;
        }

        .detail-box {
            background: rgba(255, 255, 255, 0.035);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 0.95rem 1rem;
        }

        .detail-box span {
            display: block;
            color: var(--muted);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.3rem;
        }

        .detail-box strong {
            color: #f5f6f1;
            font-size: 0.98rem;
            line-height: 1.45;
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
            .project-card,
            .timeline-card {
                padding: 1.15rem;
                border-radius: 24px;
            }

            .project-image {
                height: 190px;
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
            .project-card,
            .timeline-card,
            .kpi,
            .metric-box {
                backdrop-filter: none;
            }

            .project-card:hover,
            .project-card:active,
            div[data-testid="stRadio"] div[role="radiogroup"] label:hover,
            div[data-testid="stRadio"] div[role="radiogroup"] label:active,
            .resume-download-link:active,
            .contact-link-card:hover,
            .contact-link-card:active,
            .project-link-row a:hover,
            .project-link-row a:active {
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
