import json
with open('message-data.json', 'r') as f:
    msg = json.loads(f.read().strip())
# print(msg)
# with open('message-data.json', 'w') as f:
