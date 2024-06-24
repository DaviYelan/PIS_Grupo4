import os
import json
from models.server import Server

DATA_DIR = "data"
FILENAME = "servers.json"
FILE_PATH = os.path.join(DATA_DIR, FILENAME)

def save_to_json(servers, filename=FILE_PATH):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    data = [server.to_dict() for server in servers]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_from_json(filename=FILE_PATH):
    if not os.path.exists(filename):
        return [Server(1, "Server 1"), Server(2, "Server 2"), Server(3, "Server 3")]

    with open(filename, "r") as f:
        data = json.load(f)
        return [Server.from_dict(server_data) for server_data in data]
