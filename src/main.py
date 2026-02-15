from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.mobile.routes import router as mobile_router
from src.api.categories.routes import router as category_router
from src.api.groups.routes import router as group_router
from src.api.products.routes import router as product_router

app = FastAPI(title="Kartax API", description="In development", version="1.0")

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:4200",
    "https://kartax-app-angular.vercel.app"
  ],
  allow_credentials=True,
  allow_methods=["GET", "POST", "PUT", "DELETE"],
  allow_headers=["*"],
)

@app.get("/")
async def root():
  return {
    "status": "Api Running",
    "swagger": "/docs",
  }

app.include_router(mobile_router, prefix="/api")
app.include_router(category_router, prefix="/api")
app.include_router(group_router, prefix="/api")
app.include_router(product_router, prefix="/api")
