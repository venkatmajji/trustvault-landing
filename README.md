
# TrustVault Investor Agent

## Description

Modern landing page and Investor Agent interactive Q&A built in Streamlit.

- Home page → overview + CTA
- Investor Agent → RAG + pitch deck + compliance friendly answers
- All built with LangChain + Streamlit + OpenAI

## How to run

```
pip install -r requirements.txt
streamlit run Home.py
```

Make sure to place `TrustVault_Investor_One_Pager.pdf` into `assets` folder.

Add your `OPENAI_API_KEY` to secrets or environment variables.

## Pages

- Home (Landing page)
- Investor Agent (via pages/Investor_Pitch_Agent.py)
