from flask import Flask, request

app = Flask(__name__)

@app.route('/tasks/<id>', methods=['GET', 'POST'])
def tasks(id: str):
    if request.method == 'POST':
        return get_lines()
    else:
        return get_task(id)

