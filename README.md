\---

title: Radiology Summarisation API

emoji: 🏥

colorFrom: blue

colorTo: green

sdk: docker

app\_file: app.py

pinned: false

\---



\# Radiology Report Summarisation API



A fine-tuned FLAN-T5-base model that generates concise clinical impressions from radiology findings.



\## API Usage



\*\*Endpoint:\*\* POST /summarise



\*\*Input:\*\*

```json

{"findings": "The lungs are clear. Heart size and mediastinal contours are normal."}

```



\*\*Output:\*\*

```json

{"impression": "No acute cardiopulmonary abnormality."}

```

