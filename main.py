from fastapi import FastAPI
from routers import cve, info

app = FastAPI(
    title="CVE Viewer",
    description="FastAPI додаток для роботи з CVE",
    version="1.0.0",
    contact={"name": "Олег Пліхтяк"}
)

app.include_router(info.router)
app.include_router(cve.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
