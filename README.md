# Distributed System Fault Diagnosis

A Django-based experimental system for diagnosing distributed-system faults with machine-learning models.

## Overview

The project combines data preparation, model training/inference, and a web interface for exploring diagnosis results. Exact features and model behavior depend on the datasets and code in this repository.

## Quick start

~~~bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python manage.py runserver
~~~

Configure dataset locations and model artifacts locally. Do not commit private logs, credentials, or production traces.

## Evaluation

Document the dataset split, label definitions, model version, random seed, and per-class metrics for each experiment. A high aggregate score alone is not sufficient evidence for reliable diagnosis.

## Status

Research/educational software. Diagnosis results require operational and domain validation before being used to respond to real incidents.