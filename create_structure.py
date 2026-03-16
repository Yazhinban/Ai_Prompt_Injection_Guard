import os

base = r"c:\ai_prompt_guard"

files = [
    "backend/main.py",
    "backend/security_engine.py",
    "backend/decision_engine.py",
    "backend/api/chat_api.py",
    "backend/api/prompt_api.py",
    "backend/api/logs_api.py",
    "backend/api/stats_api.py",
    "backend/services/llm_service.py",
    "backend/services/logging_service.py",
    "frontend/app.py",
    "frontend/pages/chat.py",
    "frontend/pages/dashboard.py",
    "frontend/pages/attack_logs.py",
    "frontend/pages/model_analytics.py",
    "frontend/components/prompt_box.py",
    "frontend/components/response_box.py",
    "frontend/components/risk_indicator.py",
    "frontend/components/threat_card.py",
    "frontend/services/api_client.py",
    "frontend/styles/theme.py",
    "models/train_model.py",
    "models/prompt_classifier.py",
    "models/embeddings_detector.py",
    "dataset/prompts.csv",
    "database/db.py",
    "database/logs.db",
    "utils/helpers.py",
    "requirements.txt",
    "README.md"
]

for file in files:
    path = os.path.join(base, file)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        pass

print("Structure created")