import cv2
import os
import re
import numpy as np
import crud, models, schemas
from fastapi import FastAPI, Depends, File, Response
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from datetime import datetime
from database import SessionLocal, engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent # /db
IMAGE_DIR = str(BASE_DIR/"image")

# 처음 실행 시 DB에 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def create_database():
    return {"Database" : "Created"}


# 입고처리 DB INPUT ls_cd ,ls_dt, barcode, ex_dt, ls_ct
@app.post("/stock/", response_model=schemas.CreateStock)
async def create_stock(stock : schemas.CreateStock, db:Session = Depends(get_db)):
    return crud.create_stock(db, stock)


# 재촬영 사진 저장
@app.post("/save_badpicture", response_class=HTMLResponse)
def save_badpicture(file:bytes = File()):
    # YYYY-MM-DD
    current_time = str(datetime.today().date())
    image_name = str(datetime.today())
    image_name = re.sub(r'[.|:]', '', image_name) # 파일명에 사용할 수 없는 문자열 제거
    # byte 이미지 cv2 이미지로 디코드
    decoded = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)
    # IMAGE_DIR 위치에 DIR이 없으면 image 폴더 생성
    if not os.path.isdir(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)
    # 날짜별 폴더 생성
    DATE_DIR = os.path.join(IMAGE_DIR, current_time)
    if not os.path.isdir(DATE_DIR):
        os.mkdir(DATE_DIR)
    # 날짜별 폴더 내 이미지 생성
    SAVE_DIR = os.path.join(DATE_DIR, image_name)
    print(f"{SAVE_DIR}.jpg")
    
    cv2.imwrite(f"{SAVE_DIR}.jpg", decoded)
    # return Response('Hello World')