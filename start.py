import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from routes import route
from bootstrap import bootstrap

app = FastAPI()
app.include_router(route)


# To get started, launch Redis or Postgres services on your server
# Edit the .env file to select storage
# Use the words "Redis" or "Postgres" to select a repository
if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    bootstrap()
    uvicorn.run("setup:app",
                host="0.0.0.0",
                port=8000)
