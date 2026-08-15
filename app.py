from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        total_students = int(request.form["total_students"])
        students_ate = int(request.form["students_ate"])
        wasted_food = float(request.form["wasted_food"])

        remaining_meals = total_students - students_ate
        waste_percentage = (remaining_meals / total_students) * 100
        saving_score = round(100 - waste_percentage)

        if wasted_food > 10:
            message = "Food waste is high. Reduce tomorrow's food preparation."
        elif wasted_food > 5:
            message = "Food waste is moderate. Prepare slightly less food."
        else:
            message = "Food waste is low. Good job!"

        result = {
            "remaining_meals": remaining_meals,
            "waste_percentage": round(waste_percentage, 2),
            "saving_score": saving_score,
            "message": message
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)