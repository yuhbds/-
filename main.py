import uuid
from flask import Flask, jsonify

app = Flask(__name__)

rooms = {}

@app.route("/create-room", methods=["POST"])
def create_room():
    room_id = str(uuid.uuid4())[:8]
    rooms[room_id] = []  # 创建房间并将其存入 rooms 字典
    return jsonify({"room_id": room_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
