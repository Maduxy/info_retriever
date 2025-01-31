# info_retriever
1. # Project Overview
 A simple FastAPI-based public API that returns an email, the current UTC datetime, and a GitHub link.

2. # How to Run Locally
git clone https://github.com/Maduxy/info_retriever
cd info_retriever
pip install -r requirements.txt
uvicorn main:app --reload

3. # API Endpoint
GET /profile → Returns:
    
{  "email": "onyejiakamadu@gmail.com",
  "current_datetime": "2025-01-31T01:45:36.457198+00:00",
  "github_url": "https://github.com/Maduxy/info_retriever"
}

4. # Live API
Base URL: https://your-api-url.com

5. # [Python Developers]
(https://hng.tech/hire/python-developers)