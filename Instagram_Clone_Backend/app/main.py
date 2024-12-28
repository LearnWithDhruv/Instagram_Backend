from fastapi import FastAPI
from app.routes import auth_routes, user_routes, post_routes
from app.db.database import test_connection

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(post_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Instagram Clone API!"}

@app.on_event("startup")
async def startup_event():
    await test_connection()
