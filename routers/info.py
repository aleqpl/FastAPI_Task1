from fastapi import APIRouter

router = APIRouter()

@router.get("/info", summary="Інформація про додаток")
async def get_info():
    return {
        "app_name": "CVE Viewer",
        "version": "1.0.0",
        "author": "Олег Пліхтяк",
        "description": "Додаток для перегляду CVE"
    }
