from fastapi import FastAPI
from enum import Enum


#creatiing subclass ModelName which is inheriting from str and Enum
class ModelName(str,Enum):
    alxnet = "alxnet"
    resnet = 'resnet'
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alxnet:
        return {"Model_name":model_name, "message":"Deep Learning basic TLA"}
    elif model_name is ModelName.resnet:
        return {"Model_name":model_name, "message":"Deep Learning Best TLA"}
    else:
        return {"Model_name":model_name, "message":"Have some residuals"}
    
#passing path using fast-api: it is a good practice to specify at top the type of variable file-path is
@app.get("/files/{file_path:path}")
def read_file_path(file_path:str):
    return {"file_path":file_path}
