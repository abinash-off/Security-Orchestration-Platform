# Security Orchestration Platform

A safe SOAR learning project with simulated defensive playbooks. The current implementation deliberately avoids real endpoint isolation, deletion, credential changes or other destructive actions.

## Run
```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000.