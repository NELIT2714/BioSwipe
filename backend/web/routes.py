from fastapi import Request, UploadFile, File, Form
from fastapi.responses import JSONResponse

from web import app, mongo
from web.functions import get_file, save_file



@app.get("/api/get_themes/")
async def get_cards() -> JSONResponse:
    themes_cursor = mongo["themes"].find({})
    themes = await themes_cursor.to_list(length=None)
    for theme in themes:
        theme["_id"] = str(theme["_id"])
    return JSONResponse({"themes": themes})


@app.post("/api/add_theme/")
async def add_theme(name: str = Form(...), description: str = Form(...), picture: UploadFile = File(...)):
    picture_filename = await save_file(picture)
    await mongo["themes"].insert_one({
        "name": name,
        "description": description,
        "picture": picture_filename,
        "completed": 0,
        "views": 0
    })

    return {"message": "Theme added successfully"}
