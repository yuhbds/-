from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()
rooms = {}

class JoinRoomRequest(BaseModel):
    room_id: str

@app.get("/")
def index():
    return {"message": "Room API is running"}

@app.post("/create-room")
def create_room():
    room_id = str(uuid.uuid4())[:8]
    rooms[room_id] = {"members": []}
    return {"room_id": room_id}

@app.post("/join-room")
def join_room(request: JoinRoomRequest):
    room_id = request.room_id
    if room_id in rooms:
        return {"message": f"Joined room {room_id}"}
    else:
        raise HTTPException(status_code=404, detail="Room not found")