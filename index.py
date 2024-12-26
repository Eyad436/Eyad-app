from flask import Flask, request

app = Flask(__name__)

# الإجابات الصحيحة
correct_answers = {
    "q1": "ب",
    "q2": "ب",
    "q3": "أ",
    "q4": "أ",
    "q5": "أ",
    "q6": "ب",
    "q7": "ج",
    "q8": "ب",
    "q9": "د",
    "q10": "أ",
}

# صفحة الأسئلة
quiz_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz</title>
</head>
<body>
    <h1>Quiz</h1>
    <form method="POST">
        <label>1. ما الأداة التي تُستخدم لقبول النصوص المدخلة من المستخدم؟</label><br>
        <input type="radio" name="q1" value="أ"> أ) Label<br>
        <input type="radio" name="q1" value="ب"> ب) TextBox<br>
        <input type="radio" name="q1" value="ج"> ج) CheckBox<br>
        <input type="radio" name="q1" value="د"> د) Button<br><br>
        
        <label>2. أي خاصية في TextBox تُحدد عدد الأحرف المسموح بإدخالها؟</label><br>
        <input type="radio" name="q2" value="أ"> أ) Text<br>
        <input type="radio" name="q2" value="ب"> ب) MaxLength<br>
        <input type="radio" name="q2" value="ج"> ج) MultiLine<br>
        <input type="radio" name="q2" value="د"> د) Password<br><br>

        <!-- أضف باقي الأسئلة هنا -->

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# صفحة النتيجة
result_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
</head>
<body>
    <h1>Result</h1>
    <p>You answered {score} out of {total} correctly.</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = request.form
        score = 0
        total = len(correct_answers)
        
        for key, correct in correct_answers.items():
            if user_answers.get(key) == correct:
                score += 1
        
        return result_page.format(score=score, total=total)
    
    return quiz_page

if __name__ == "__main__":
    app.run(debug=True)
