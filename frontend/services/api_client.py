import requests

API_URL = "http://127.0.0.1:8000"


def analyze_prompt(prompt):

    response = requests.post(
        f"{API_URL}/analyze_prompt",
        json={"prompt": prompt}
    )

    return response.json()


def chat_prompt(prompt):

    response = requests.post(
        f"{API_URL}/chat",
        json={"prompt": prompt}
    )

    return response.json()


def get_logs():

    response = requests.get(f"{API_URL}/logs")

    return response.json()


def delete_log(log_id):

    requests.delete(f"{API_URL}/logs/{log_id}")


def get_stats():

    response = requests.get(f"{API_URL}/stats")

    return response.json()


# -------- ADMIN REVIEW FUNCTIONS --------

def get_admin_reviews():

    response = requests.get(f"{API_URL}/admin/reviews")

    return response.json()


def approve_prompt(prompt_id):

    requests.post(f"{API_URL}/admin/approve/{prompt_id}")


def reject_prompt(prompt_id):

    requests.post(f"{API_URL}/admin/reject/{prompt_id}")