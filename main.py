from fastapi import FastAPI
from routes.all_routes import combined_router

app = FastAPI(
    title="Practice Tickets API",
    description="A simple FastAPI application with combined routers",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

@app.get("/")
async def root():
    return {"message": "Hello to the App"}

app.include_router(combined_router) 