async def get_file(filename):
    from web import mongo

    files = await mongo["files_metadata"].find({}, {"filename": 1, "_id": 0}).to_list(length=None)
    filenames = []
    for file in files:
        filenames.append(str(file))
    if str(filename) in filenames:
        return False
    return True


async def save_file(file):
    from web import mongo
    from uuid import uuid4

    file_extension = file.filename.split(".")[-1]
    unique_filename = str(f"{uuid4()}.{file_extension}").replace("-", "")

    result = await get_file(unique_filename)
    if result:
        file_content = await file.read()
        with open(f"resources/{unique_filename}", "wb") as file:
            file.write(file_content)

        await mongo["files_metadata"].insert_one({"filename": unique_filename})
    else:
        return await save_file(file)

    return str(unique_filename)
