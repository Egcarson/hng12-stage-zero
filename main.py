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


#root
@app.get('/')
async def root():
    return {"message": "Welcome to HNG Internship Stage 0"}

@app.get("/stage-zero", status_code=status.HTTP_200_OK)
async def get_stage_zero_info():
    current_date = datetime.now(timezone.utc).isoformat(timespec='seconds').replace("+00:00", "Z")
    
    stage_0_db = {
        "email": "esehgodprevail@gmail.com",
        "current_datetime": current_date,
        "github_url": "https://github.com/Egcarson/hng12-stage-zero"
    }
    
    return stage_0_db