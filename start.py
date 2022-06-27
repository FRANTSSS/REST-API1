import uvicorn
from fastapi import FastAPI

from bootstrap import bootstrap
from routes import route

app = FastAPI()
app.include_router(route)


# To get started, launch Redis or Postgres services on your server
# Edit the .env file to select storage
# Use the words "Redis" or "Postgres" to select a repository
if __name__ == "__main__":
    uvicorn.run("start:app",
                host="0.0.0.0",
                port=8000)
