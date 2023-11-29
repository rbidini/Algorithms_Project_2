from flask import Flask, render_template, request
from src.main import run_algorithm

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    display_results = []

    if request.method == 'POST':
        source = request.form.get('source')
        destination = request.form.get('destination')

        result, max_capacity = run_algorithm(source, destination)
        result = sorted(result, key=lambda x: x["maximum capacity"], reverse=True)

        for report in result:
            if report.get('layover'):
                display_results.append(
                    f'{report["source city"]} -> {report["layover"]} (operated by {report["layover airline"]}: {report["layover model"]}) Flight capacity: {report["layover capacity"]}<br>'
                    f'{report["layover"]} -> {report["destination city"]} (operated by {report["destination airline"]}: {report["destination model"]}) Flight capacity: {report["destination capacity"]}<br>'
                    f'Maximum capacity: {report["maximum capacity"]}<br>')
            else:
                display_results.append(
                    f'{report["source city"]} -> {report["destination city"]} (operated by {report["destination airline"]}: {report["destination model"]}) Flight capacity: {report["maximum capacity"]}<br>')

        display_results.append(f'Total capacity: {max_capacity}')

    return render_template("home.html", display_results=display_results)


if __name__ == "__main__":
    app.run(debug=True)
