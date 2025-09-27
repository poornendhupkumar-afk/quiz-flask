from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load questions from JSON
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
        return f"<h1>Your Score: {score}/{len(questions)}</h1><br><a href='/'>Try Again</a>"
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
