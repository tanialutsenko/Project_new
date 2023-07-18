from fastapi import FastAPI

from typing import List
from pydantic import BaseModel, Field

from base_data import create_tables, session

create_tables()

users_base = session()

print(users_base)
app = FastAPI(title="Test App")

@app.get("/users/{gender}")

def get_users(gender: str,limit:int, offset:int):
    return [user for user in users_base[offset:][:limit] if user.get('gender') == gender]

@app.get("/users")

def get_users():
    return users_base

class Users(BaseModel):
    id: int
    name: str
    gender: str

@app.post("/users")
def get_users(users: List[Users]):
    users_base.extend(users)
    new_user = users[0]
    print(new_user)
    return {'status': 200, 'data': users_base}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
