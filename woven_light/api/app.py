from flask import Flask, request
import os

from lines import schedule_lines
from tasks import get_tasks

app = Flask(__name__)
port = int(os.environ.get("PORT", 5555))


@app.get("/health")
def health_check() -> str:
    return "OK"


@app.route("/tasks", methods=["GET", "POST"])
@app.route("/tasks/<id>", methods=["GET"])
def tasks(id: str | None = None):
    if request.method == "POST":
        return schedule_lines(request)
    else:
        return get_tasks(id)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
