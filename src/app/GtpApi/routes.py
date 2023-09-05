from flask import Flask
from get_response import get_gtp_response
app = Flask(__name__)

@app.route('/get-response/<user-messasge>')
def get_response(user_message: str) -> str:
    return get_gtp_response(user_message)

if __name__ == '__main__':
    app.run(port=8888)