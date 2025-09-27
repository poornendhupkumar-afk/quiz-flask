import os
from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("questions.json") as f:
    questions = json.load(f)

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = 0
    if request.method == "POST":
        for i, q in enumerate(questions, 1):
            selected = request.form.get(f"q{i}")
            if selected and int(selected) == q["answer"]:
                score += 1
        return render_template("result.html", score=score, total=len(questions))
    return render_template("quiz.html", questions=questions, enumerate=enumerate)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
