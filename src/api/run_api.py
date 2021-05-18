import os
import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from utils.log_setup import setup_custom_logger
from utils.kafka_conf import produce_data

topic_name = os.getenv("TOPIC_NAME")
logger = setup_custom_logger("root")
logger.debug("api running!")
app = FastAPI()


class produce_data_serial(BaseModel):
    user_id: str = None
    cur_time: str = None


@app.get("/")
def base():
    return {"Hello to": "Face Verify APP!", "GO to": "/docs"}


@app.post("/produce/pen_test")
async def produce_data_api(data: produce_data_serial):
    try:
        produce_data(topic_name, data.dict())
        response = {"status": 200, "info": "ok"}

    except Exception as e:
        logger.error("error: " + str(e))
        response = {
            "status": 400,
            "info": "failed",
        }

    return JSONResponse(content=response, status_code=response["status"])
