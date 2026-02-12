from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.oauth import auth


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def root():
    return {"Hello": "This is Relationship Family Project"} 

app.include_router(auth.router)