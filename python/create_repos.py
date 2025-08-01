import time, requests, os
from dotenv import load_dotenv

load_dotenv()  # завантажує .env

# ======== НАЛАШТУВАННЯ =========
GITEA_URL = "https://git.comsys.kpi.ua"
WEBHOOK_URL = "http://77.47.193.173:8080//generic-webhook-trigger/invoke?token=my-gitea-webhook-token"
TEACHER = "huk_dmytro"  # логін викладача
STUDENT_USERNAME = "huk_dmytro"
REPO_PREFIX = "course2025_"  # префікс до імені репозиторію
STUDENTS_FILE = "students.txt"

API_TOKEN = os.getenv("GITEA_TOKEN")
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"token {API_TOKEN}"
}
# ===============================

def read_students(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def create_repo(student_username):
    repo_name = f"{REPO_PREFIX}{student_username}"
    url = f"{GITEA_URL}/api/v1/user/repos"
    data = {
        "name": repo_name,
        "private": True,
        "auto_init": True,
        "description": f"Repo for {student_username}",
    }
    response = requests.post(url, json=data, headers=HEADERS)
    if response.status_code == 201:
        print(f"\n✅ Створено репозиторій: {repo_name}")
        return repo_name
    elif response.status_code == 409:
        print(f"⚠️ Репозиторій {repo_name} вже існує.")
        return None
    else:
        print(f"❌ Помилка створення: {response.status_code} {response.text}")
        return None

def add_collaborator(repo_name, collaborator):
    url = f"{GITEA_URL}/api/v1/repos/{TEACHER}/{repo_name}/collaborators/{collaborator}"
    data = {
        "permission": "write"  # можна "read", "write" або "admin"
    }
    response = requests.put(url, json=data, headers=HEADERS)
    if response.status_code in [201, 204]:
        print(f"✅ Додано {collaborator} як колаборатора до {repo_name}")
    else:
        print(f"⚠️ Помилка при додаванні колаборатора до {repo_name}: {response.text}")


def add_webhook(repo_name):
    hook_data = {
        "type": "gitea",
        "active": True,
        "config": {
            "url": WEBHOOK_URL,
            "content_type": "json"
        },
        "events": ["push"]
    }

    hook_url = f"{GITEA_URL}/api/v1/repos/{TEACHER}/{repo_name}/hooks"
    r = requests.post(hook_url, headers=HEADERS, json=hook_data)
    if r.status_code == 201:
        print(f"✅ Webhook додано.")
    else:
        print(f"⚠️ Не вдалося додати webhook: {r.status_code} {r.text}")


students = read_students(STUDENTS_FILE)
for student in students:
    repo_name = create_repo(student)
    if repo_name:
        add_collaborator(repo_name, STUDENT_USERNAME)
        add_webhook(repo_name)
    time.sleep(0.3) # Невелика пауза, щоб не перевантажити API

print("\n✅ Усі репозиторії оброблено.")
