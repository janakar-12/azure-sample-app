from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    version = os.getenv("APP_VERSION", "dev")
    return {
        "app": "sampleapp",
        "version": version,
        "message": "Hello from azure-sample-app"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
