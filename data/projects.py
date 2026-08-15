PROJECTS = [
    {
        "title": "InstaDine",
        "dates": "Spring 2026",
        "tag": "Agentic AI product",
        "problem": (
            "Most restaurant tools feel shallow. They throw generic results at users instead of asking better questions, "
            "grounding answers in live place data, or checking whether a place actually fits what someone wants to eat."
        ),
        "built": (
            "I built a runnable restaurant recommendation product with Flask, Google Places, Gemini-style agent workflows, "
            "saved chats, account support, live maps, and dish verification from menus, PDFs, and images when I could get them."
        ),
        "tools": ["Flask", "SQLite", "Google Places API", "Gemini", "OCR", "HTML/CSS/JS"],
        "result": (
            "This became a real end-to-end product instead of a one-shot demo: multi-turn recommendation flows, grounded retrieval, "
            "live map results, and recommendations I could actually explain."
        ),
        "hover": (
            "I structured the product around intent parsing, clarification, retrieval, and response generation because real user requests are messy, "
            "and I wanted the system to handle that instead of collapsing into keyword search."
        ),
        "image_path": "assets/instadine.png",
        "link_url": "https://github.com/sanjanaumeshsawant0810/restaurant-recommendation-agent",
        "link_label": "View repository",
    },
    {
        "title": "Quantifying the Environmental Cost of AI",
        "dates": "September 2025 to December 2025",
        "tag": "ML evaluation",
        "problem": (
            "People talk about model performance all day, but they usually stop at accuracy and ignore the energy and carbon cost of getting there."
        ),
        "built": (
            "I built an evaluation study around SQuAD 2.0 to compare DistilBERT, BERT-base, and GPT-2 across model architecture, "
            "dataset size, and training strategy, including full fine-tuning, LoRA, and few-shot approaches."
        ),
        "tools": ["Python", "Transformers", "CodeCarbon", "SQuAD 2.0", "LoRA", "NLP Evaluation"],
        "result": (
            "I made the performance versus emissions tradeoff visible by comparing model quality against carbon cost across architectures and training choices."
        ),
        "hover": (
            "I cared about this one because responsible AI should mean something measurable, not just something that sounds good in a presentation."
        ),
        "link_url": "https://github.com/shrutielangovan/CarbonEmissionsinFine-TuningLanguageModelS",
        "link_label": "View repository",
    },
    {
        "title": "Effect of Technology Use on Mental Health",
        "dates": "January 2025 to March 2025",
        "tag": "Analytics research",
        "problem": (
            "The signal was there, but it was buried across separate national datasets, messy codebooks, and inconsistent year-to-year structures."
        ),
        "built": (
            "I built an analysis workflow around the NTIA Internet Use Survey and NSDUH to merge technology-use and mental-health data, "
            "then explore how the patterns changed across stress, anxiety, depression, and related indicators."
        ),
        "tools": ["R", "Survey Data", "EDA", "Data Integration", "Statistical Analysis"],
        "result": (
            "I turned scattered survey files into a reproducible cross-dataset workflow that could actually support an interpretable analysis."
        ),
        "hover": (
            "Most of the hard part was not the final chart. It was the cleaning, standardization, and variable tracing needed to make the analysis trustworthy."
        ),
        "link_url": "https://github.com/mallick20/tech-health-impact",
        "link_label": "View repository",
    },
    {
        "title": "Bankruptcy Prediction ML Pipeline",
        "dates": "2025",
        "tag": "Predictive modeling",
        "problem": (
            "I did not want this to be another notebook that trains a model once and then says nothing useful. I wanted a repeatable risk workflow."
        ),
        "built": (
            "I built a machine-learning pipeline for bankruptcy prediction with code, assets, and app structure organized around a reproducible classification workflow."
        ),
        "tools": ["Python", "Machine Learning", "Classification", "HTML/CSS/JS"],
        "result": (
            "I packaged it as a reusable bankruptcy workflow so modeling, evaluation, and business-facing explanation could live in one place."
        ),
        "hover": (
            "I treated this as a productized prediction workflow, not just a single model run, because that is closer to how the work would matter in real use."
        ),
        "link_url": "https://github.com/sanjanaumeshsawant0810/bankruptcy-lab",
        "link_label": "View repository",
    },
    {
        "title": "Loan Default Prediction",
        "dates": "2026",
        "tag": "Fintech analytics",
        "problem": (
            "Credit-risk work is not just about getting a score. It is about making the tradeoff between missed risk and unnecessary rejections visible."
        ),
        "built": (
            "I built an end-to-end Home Credit default-risk pipeline around 307K+ application records using reusable preprocessing, "
            "logistic regression and XGBoost baselines, calibration-aware evaluation, and threshold analysis."
        ),
        "tools": ["Python", "pandas", "scikit-learn", "XGBoost", "Imbalanced Classification", "Threshold Analysis"],
        "result": (
            "I turned an imbalanced lending problem into a business-facing evaluation workflow that compares ranking quality, precision-recall tradeoffs, and decision-threshold behavior."
        ),
        "hover": (
            "I framed this around lending decisions, not leaderboard metrics, because a model is only useful if the threshold behavior makes sense."
        ),
    },
    {
        "title": "Deep Exponential Families Replication",
        "dates": "2026",
        "tag": "ML research",
        "problem": (
            "Probabilistic models often get discussed in the abstract, so I wanted to understand one by rebuilding it and seeing where the assumptions break."
        ),
        "built": (
            "I replicated the Deep Exponential Families paper using mean-field variational inference instead of black-box variational inference, "
            "with a Poisson-Gamma document-model setup and layer-wise perplexity analysis."
        ),
        "tools": ["Python", "Variational Inference", "Probabilistic Modeling", "Document Modeling", "Research Replication"],
        "result": (
            "I turned a theory-heavy paper into a runnable replication and made the implementation gaps explicit instead of pretending it was a perfect match."
        ),
        "hover": (
            "The point here was disciplined replication and interpretation, not pretending every research reimplementation is exact."
        ),
    },
    {
        "title": "Growth Mindset Causal Project",
        "dates": "2025",
        "tag": "Causal inference",
        "problem": (
            "Education interventions are easy to oversell, so I wanted the analysis to be careful about uncertainty instead of more dramatic than the evidence supported."
        ),
        "built": (
            "I analyzed a growth-mindset intervention using bootstrap validation, interpretable outcome analysis, and student-versus-school factor comparisons."
        ),
        "tools": ["Python", "Causal Inference", "Bootstrap Validation", "Statistics", "Outcome Analysis"],
        "result": (
            "I estimated a 41.2 percent improvement in average outcomes and backed it with 1,000-plus bootstrap samples and a 95 percent confidence interval."
        ),
        "hover": (
            "I kept this one grounded by highlighting uncertainty and showing that individual expectations mattered more than broad school-level factors."
        ),
    },
]
