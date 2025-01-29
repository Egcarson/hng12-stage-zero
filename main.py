from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone

app = FastAPI()

# Allow all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

#response
stage_0_db = {
    "email": "esehgodprevail@gmail.com",
    "current_datetime": f"{current_date}",
    "github_url": "https://github.com/Egcarson/hng12-stage-zero"
}

#root
@app.get('/')
async def root():
    return {"message": "Welcome to HNG Internship Stage 0"}

@app.get("/stage-zero", status_code=status.HTTP_200_OK)
async def get_stage_zero_info():
    return stage_0_db