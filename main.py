from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

rooms = {}

class JoinRequest(BaseModel):
    room_id: str

@app.post("/create-room")
def create_room():
    room_id = str(uuid.uuid4())[:8]
    rooms[room_id] = []
    return {"room_id": room_id}

@app.post("/join-room")
def join_room(data: JoinRequest):
    room_id = data.room_id
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    if len(rooms[room_id]) >= 5:
        raise HTTPException(status_code=403, detail="Room is full")
    rooms[room_id].append("user")  # 实际项目中你可以用 IP 或 session 标识用户
    return {"message": f"Joined room {room_id}", "members": len(rooms[room_id])}

@app.get("/")
def root():
    return {"message": "Room API is running"}
