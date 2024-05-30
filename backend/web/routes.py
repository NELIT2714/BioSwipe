from bson import ObjectId
from fastapi import Request, UploadFile, File, Form
from fastapi.responses import JSONResponse

from web import app, mongo
from web.functions import get_file, save_file


@app.get("/api/get_themes/")
async def get_themes() -> JSONResponse:
    themes = await mongo["themes"].find({}).to_list(length=None)
    for theme in themes:
        theme["_id"] = str(theme["_id"])
    return JSONResponse({"themes": themes})


@app.get("/api/get_cards/{theme_id}")
async def get_cards(theme_id: str) -> JSONResponse:
    print(theme_id)
    theme = await mongo["themes"].find_one({"_id": ObjectId(theme_id)})
    cards = theme.get("cards", [])
    print(cards)
    return JSONResponse({"cards": cards})


@app.post("/api/add_theme/")
async def add_theme(name: str = Form(...), description: str = Form(...), picture: UploadFile = File(...)):
    picture_filename = await save_file(picture)
    await mongo["themes"].insert_one({
        "name": name,
        "description": description,
        "picture": picture_filename,
        "cards": [],
        "completed": 0,
        "views": 0
    })
    return JSONResponse({"status": True})


@app.post("/api/add_question/")
async def add_question(theme_id: str = Form(...), question: str = Form(...), answer: str = Form(...)):
    theme = await mongo["themes"].find_one({"_id": ObjectId(theme_id)})
    await mongo["themes"].update_one(
        {"_id": theme.get("_id")},
        {"$addToSet": {"cards": {
            "question": str(question),
            "answer": str(answer)
        }}}
    )
    return JSONResponse({"status": True})
