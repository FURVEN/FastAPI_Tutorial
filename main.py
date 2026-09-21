from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 서버 실행
@app.get("/") # 엔드 포인트
def root_handler():
    return {"message": "Hello, FastAPI!"}

# 경로 사용
@app.get("/login") # 엔드 포인트
def login_handler():
    return {"message": "로그인 페이지에 오신 것을 환영합니다."}

# 경로 변수 사용
@app.get("/login/{user_id}") # 엔드 포인트
def read_user_handler(user_id: int):
    return {"user_id": user_id, "message": f"사용자 {user_id} 정보 조회"}

# 쿼리 파라미터 사용
@app.get("/items") # 엔드 포인트
def read_item_handler(max_price: int | None = None):
    return {"max_price": max_price}

# 아이템 모델 정의
class Item(BaseModel): # 요청 본문 검증을 위한 Item 모델 정의
    name: str
    price: int
    in_stock: bool = True

# 새 아이템 등록
@app.post("/Items") # POST 요청과 경로 매핑 설정
def create_item_handler(item: Item): # 요청 본문 데이터를 Item 객체로 변환
    return {"Message": f"아이템 '{item.name}'이(가) 추가되었습니다.", "item": item}

# 경로 변수, 쿼리 파라미터, 요청 본문 혼합 사용
@app.put("/items/{item_id}")
def update_item_handler(item_id: int, assignee: str, item: Item):
    return {
        "item_id": item_id,
        "assignee": assignee, # 담당자 또는 작업자
        "item": Item
    }