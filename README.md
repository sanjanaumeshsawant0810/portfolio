# Sanjana Sawant Portfolio

Streamlit portfolio site for data science, data engineering, and applied AI roles.

## Structure

- `app.py` boots the app and routes between pages.
- `pages/` contains focused page modules for Home, About, Projects, Resume, and Contact.
- `components/` contains shared UI pieces such as the navigation, footer, and site-wide styling.
- `data/` stores the shared profile content and project records so details stay consistent across pages.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Launch checklist

- The Resume page embeds `assets/resume/Sanjana_Sawant_Data_Science_Resume.pdf` and exposes it as a download.
- Replace any placeholder project links with repo or demo URLs.
- Add project screenshots if you want visual thumbnails on the Projects page.
- Confirm the latest GPA, publication ranking, and internship dates before deployment.
- Initialize a git repository, push to GitHub, and deploy to a Streamlit-friendly host such as Streamlit Community Cloud.
