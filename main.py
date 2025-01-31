from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Adding CORS Handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/profile")
def my_info():
    return {"email": "onyejiakamadu@gmail.com",
            "current_datetime":datetime.now(pytz.utc).isoformat() ,
            "github_url": "to be determined"}

