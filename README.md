---
title: Radiology Summarisation API
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# Medical Text Summarisation — IT Career Switch Project 1

A fine-tuned FLAN-T5-base model that generates concise clinical impressions
from radiology medical findings text. Built as part of the IT Career Switch AI
Engineering project.

## Project Overview

This project fine-tunes Google's FLAN-T5-base model on the NLM Chest X-ray
dataset (NLMCXR) to summarise free-text radiology findings into short
clinical impressions.

## Repository Structure

- `Medical_Text_Summariser_Proj.ipynb` — end-to-end source code covering
  data preparation, cleaning, tokenisation, model fine-tuning, and evaluation
- `app.py` — FastAPI REST API deployment code
- `requirements.txt` — Python dependencies
- `Dockerfile` — container configuration for HuggingFace Spaces deployment

## Live API

**Endpoint:** POST /summarise

**URL:**https://graceogungbesan1809-debug-radiology-summarisation-api.hf.space/summarise

**Example request:**
```json
{"findings": "The lungs are clear. Heart size and mediastinal contours are normal."}
```

**Example response:**
```json
{"impression": "The lungs are clear and the heart size and mediastinal contours are normal."}
```

## Model Performance

- ROUGE-1 F1: 0.133
- BERTScore F1: 0.866

## How to Run

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `uvicorn app:app --host 0.0.0.0 --port 8000`
4. Or use the live API directly at:
   https://graceogungbesan1809-debug-radiology-summarisation-api.hf.space/summarise
