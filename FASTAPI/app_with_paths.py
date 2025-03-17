from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item_id(item_id: int):
    return {"item_id":item_id}

@app.get("/names/{name}")
async def display_name( name: str):
    return {"The name of Person is": name}

