# services/cve_service.py

from datetime import datetime, timedelta
import json
from pathlib import Path

CISA_FILE = Path(__file__).parent.parent / "data" / "cisa.json"

def load_data():
    """
    Завантажує дані з JSON-файлу та повертає список вразливостей.
    """
    try:
        with open(CISA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("vulnerabilities", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Помилка завантаження даних: {e}")
        return []

def parse_date(date_string):
    """
    Парсує дату з різними форматами.
    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError as e:
            print(f"Невдале перетворення дати: {date_string}. Помилка: {e}")
            return None

def filter_by_date(vulnerabilities, days: int = 5, max_items: int = 40):
    """
    Фільтрує вразливості, додані за останні `days` днів.
    """
    recent_date = datetime.utcnow() - timedelta(days=days)
    filtered = [
        v for v in vulnerabilities
        if (date := parse_date(v.get("dateAdded"))) and date >= recent_date
    ]
    return filtered[:max_items]

def filter_newest(vulnerabilities, max_items: int = 10):
    """
    Повертає `max_items` найновіших вразливостей.
    """
    return sorted(
        vulnerabilities,
        key=lambda x: parse_date(x.get("dateAdded")),
        reverse=True
    )[:max_items]

def filter_known(vulnerabilities, max_items: int = 10):
    """
    Повертає `max_items` вразливостей, пов'язаних з відомими кампаніями викупу.
    """
    return [
        v for v in vulnerabilities
        if v.get("knownRansomwareCampaignUse") == "Known"
    ][:max_items]

def search_by_keyword(vulnerabilities, keyword: str):
    """
    Пошук вразливостей за ключовим словом у короткому описі.
    """
    return [
        v for v in vulnerabilities
        if keyword.lower() in v.get("shortDescription", "").lower()
    ]
