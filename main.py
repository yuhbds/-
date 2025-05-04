from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

rooms = {}

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Room API is running"})

@app.route("/create-room", methods=["POST"])
def create_room():
    room_id = str(uuid.uuid4())[:8]  # 自动生成一个 8 位房间号
    rooms[room_id] = {"members": []}
    return jsonify({"room_id": room_id})

@app.route("/join-room", methods=["POST"])
def join_room():
    data = request.get_json()
    room_id = data.get("room_id")
    if room_id in rooms:
        return jsonify({"message": f"Joined room {room_id}"})
    else:
        return jsonify({"error": "Room not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
