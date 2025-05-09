from flask import Flask
from avatars import randAvatar


app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    return randAvatar()

if __name__ == "__main__":
    app.run("127.0.0.1", 8080)

