from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = Path(__file__).parent / "assets" / "resume" / "Sanjana_Sawant_Data_Science_Resume.pdf"


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Name",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=21,
        textColor=colors.HexColor("#111B21"),
        alignment=TA_CENTER,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.4,
        leading=10,
        textColor=colors.HexColor("#3D454B"),
        alignment=TA_CENTER,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="Section",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.2,
        leading=11,
        textColor=colors.HexColor("#173349"),
        spaceBefore=6,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name="Entry",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=10.4,
        textColor=colors.HexColor("#111B21"),
        spaceBefore=2,
        spaceAfter=1,
    ))
    styles.add(ParagraphStyle(
        name="SubEntry",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8,
        leading=9.2,
        textColor=colors.HexColor("#4A4A4A"),
        spaceAfter=1,
    ))
    styles.add(ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.25,
        leading=9.65,
        textColor=colors.HexColor("#22272B"),
        spaceAfter=1,
    ))
    styles.add(ParagraphStyle(
        name="Summary",
        parent=styles["Body"],
        fontSize=8.5,
        leading=10.1,
        spaceAfter=1,
    ))
    styles.add(ParagraphStyle(
        name="Footer",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.4,
        leading=8.5,
        textColor=colors.HexColor("#68747B"),
        alignment=TA_CENTER,
    ))
    return styles


def p(text, style):
    return Paragraph(text, style)


def entry_header(left, right, styles):
    table = Table([[p(left, styles["Entry"]), p(right, styles["Entry"])],], colWidths=[5.75 * inch, 1.0 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return table


def bullet(text, styles):
    return p(f"&bull;&nbsp; {text}", styles["Body"])


def section(story, title, styles):
    story.extend([p(title, styles["Section"]), HRFlowable(width="100%", thickness=0.55, color=colors.HexColor("#CAD1D4"), spaceAfter=3)])


def add_experience(story, styles):
    section(story, "EXPERIENCE", styles)
    story.append(entry_header("Helius Health AI | Data Science Intern | Remote", "Spring 2026", styles))
    for text in [
        "Enabled production loading of validated healthcare workforce data by building and testing local ETL/ELT workflows that staged raw survey files into Supabase/PostgreSQL and were reviewed by the CTO before handoff.",
        "Gave sponsors visibility into onboarding, assessment completion, engagement, retention, conversion, drop-off, and specialty matching by querying Supabase/PostgreSQL through API access and turning outputs into KPI analyses.",
        "Made one-run monitoring of user and workforce activity possible by building an end-to-end KPI reporting workflow with graphical outputs for sponsor-facing engagement and onboarding metrics.",
        "Advanced a nursing specialty-matching decision-support model toward review by developing an initial predictive workflow that estimates which department may best fit each nursing student.",
    ]:
        story.append(bullet(text, styles))
    story.append(entry_header("NeuralSeek | AI Agent Developer Intern | Remote", "Spring 2026", styles))
    for text in [
        "Developed an AI-powered restaurant recommendation workflow using retrieval-based reasoning and recommendation-ranking logic.",
        "Analyzed user feedback and recommendation behavior to identify factors influencing trust, relevance, and decision quality in AI-assisted discovery.",
        "Validated the product with users and increased willingness to trust AI-generated recommendations from 17% to 78%, then extended the work into InstaDine.",
    ]:
        story.append(bullet(text, styles))
    story.append(entry_header("Superpack Packaging Machines Pvt. Ltd. | PLC Programming Engineering Intern", "Oct 2023 - Jul 2024", styles))
    story.append(p("Hyderabad, India", styles["SubEntry"]))
    story.append(bullet("Improved industrial filling-machine control logic for fluids with different viscosity levels through testing and engineering iteration, increasing machine efficiency by 4% to 8%.", styles))


def add_projects(story, styles):
    section(story, "SELECTED DATA SCIENCE PROJECTS", styles)
    projects = [
        ("InstaDine | Full-Stack AI Restaurant Recommendation Platform", "Spring 2026", [
            "Built a full-stack AI product using Flask, PostgreSQL, Docker, Google Places API, and Vertex AI/Gemini to deliver personalized, live-data-grounded recommendations.",
            "Designed conversational retrieval, ranking, filtering, session, and persistence workflows combining user preferences, travel constraints, ratings, and availability.",
        ]),
        ("Loan Default Prediction | Credit Risk Modeling", "Summer 2026", [
            "Built an end-to-end credit-risk modeling project to predict loan default from 307K+ borrower records using Python, pandas, scikit-learn, and XGBoost.",
            "Compared logistic regression and XGBoost with ROC-AUC, PR-AUC, precision/recall, calibration, and threshold optimization to connect model performance to lending tradeoffs.",
        ]),
        ("Bankruptcy Prediction Pipeline and Explainer App", "Summer 2026", [
            "Built reusable preprocessing and modeling pipelines for scaling, encoding, missing-value imputation, interpretable classification, artifact persistence, and rare-event evaluation.",
            "Framed the workflow through a business-friendly frontend explaining why naive accuracy is misleading for imbalanced financial-risk prediction.",
        ]),
        ("Quantifying the Environmental Cost of AI", "Fall 2025", [
            "Compared transformer fine-tuning tradeoffs across DistilBERT, BERT-family models, and GPT-style baselines using F1 performance and carbon-emissions cost.",
            "Analyzed full fine-tuning, LoRA, and efficient training setups, finding roughly 78% lower emissions with limited performance loss.",
        ]),
        ("Effect of Technology Use on Mental Health", "Spring 2025", [
            "Processed NTIA and NSDUH survey data across multiple years, standardized inconsistent historical formats, and built R/Databricks transformation workflows.",
            "Identified demographic trends while clearly separating correlation from causation in the final analysis.",
        ]),
    ]
    for title, date, bullets in projects:
        story.append(entry_header(title, date, styles))
        for text in bullets:
            story.append(bullet(text, styles))


def add_header(story, styles):
    story.extend([
        p("SANJANA UMESH SAWANT", styles["Name"]),
        p("New Brunswick, NJ | sanjanaumesh.sawant@rutgers.edu | LinkedIn: Sanjana Umesh Sawant | GitHub: sanjanaumeshsawant0810", styles["Contact"]),
        HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#AEB8BC"), spaceAfter=2),
    ])


def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.4)
    canvas.setFillColor(colors.HexColor("#68747B"))
    canvas.drawCentredString(letter[0] / 2, 0.32 * inch, f"Sanjana Sawant | Data Science Resume | {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=letter,
        rightMargin=0.62 * inch,
        leftMargin=0.62 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.5 * inch,
        title="Sanjana Umesh Sawant - Data Science Resume",
        author="Sanjana Umesh Sawant",
    )
    story = []
    add_header(story, styles)
    section(story, "SUMMARY", styles)
    story.append(p("Data science graduate building practical data and AI products across analytics, KPI reporting, ETL, applied modeling, ranking systems, and product-facing experimentation. Strongest at turning messy data into usable insight and translating technical work into clear business value. Targeting data analyst, data scientist, AI, analytics engineering, and fintech-oriented roles.", styles["Summary"]))
    section(story, "EDUCATION", styles)
    story.append(entry_header("Rutgers University | M.S. in Data Science, High Honor", "May 2026", styles))
    story.append(p("GPA: 3.6/4.0 | Coursework: Machine Learning, Regression and Time Series, DBMS, Deep Learning, LLMs, Agentic AI", styles["SubEntry"]))
    story.append(entry_header("SRM Institute of Science and Technology | B.Tech. in Electronics and Computer Engineering", "Jun 2024", styles))
    story.append(p("GPA: 9.01/10", styles["SubEntry"]))
    add_experience(story, styles)
    story.append(Spacer(1, 5))
    add_projects(story, styles)
    section(story, "TECHNICAL SKILLS", styles)
    story.append(p("Python, R, SQL, pandas, scikit-learn, XGBoost, PyTorch, TensorFlow, PySpark, Flask, FastAPI, Streamlit, PostgreSQL, Supabase, SQLite, Databricks, BigQuery, Power BI, Docker, Git, REST APIs, OpenAI API, LLM evaluation, prompt engineering, LoRA fine-tuning, data pipelines, ETL, KPI analytics, experimentation, model evaluation, credit-risk modeling", styles["Body"]))
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    return OUTPUT_PATH


if __name__ == "__main__":
    print(build_pdf())
