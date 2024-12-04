from fastapi import APIRouter
from services.cve_service import load_data, filter_by_date, filter_newest, filter_known, search_by_keyword

router = APIRouter()

@router.get("/get/all")
def get_all():
    data = load_data()
    return filter_by_date(data)

@router.get("/get/new")
def get_new():
    data = load_data()
    return filter_newest(data)

@router.get("/get/known")
def get_known():
    data = load_data()
    return filter_known(data)

@router.get("/get")
def get_by_query(query: str):
    data = load_data()
    return search_by_keyword(data, query)
