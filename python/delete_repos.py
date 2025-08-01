import requests
from dotenv import load_dotenv
import os

load_dotenv()  # завантаження змінних оточення з файлу .env

# ======== НАЛАШТУВАННЯ =========
GITEA_URL = "https://git.comsys.kpi.ua"
API_TOKEN = os.getenv("GITEA_TOKEN")
OWNER = "huk_dmytro"  # логін викладача або назва організації
REPO_PREFIX = "course2025_"  # префікс до імені репозиторію
STUDENTS_FILE = "students.txt"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"token {API_TOKEN}"
}
# ===============================

def read_students(file_path):
    """Зчитує список студентів з файлу."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def delete_repo(student_username):
    """Видаляє репозиторій для конкретного студента."""
    repo_name = f"{REPO_PREFIX}{student_username}"
    url = f"{GITEA_URL}/api/v1/repos/{OWNER}/{repo_name}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"✅ Успішно видалено репозиторій: {repo_name}")
    else:
        print(f"⚠️ Помилка видалення репозиторію {repo_name}: {response.status_code} {response.text}")


students = read_students(STUDENTS_FILE)
for student in students:
    delete_repo(student)
