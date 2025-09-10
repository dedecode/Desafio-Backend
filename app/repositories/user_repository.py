import json
import os

_users_data = []
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', '..', 'mock-users.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        _users_data = json.load(f)
except Exception as e:
    _users_data = []
    print(f"[ERROR] Loading mock data: {e}")

def get_all_users():
    return _users_data
