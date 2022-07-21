from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import Request
from typing import Union

from fastapi import FastAPI

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))

@app.get("/judgeme")
def read_root():
    return FileResponse("static/judgeme.html")

# @app.post("/judgeme")
# async def read_root(request: Request):
#     raw_input = await request.json()
#     print(raw_input)
#     return {"message": "Okay"}


@app.get("/trustpilot")
def read_root():
    return FileResponse("static/trustpilot.html")

@app.get("/yotpo")
def read_root():
    return FileResponse("static/yotpo.html")
