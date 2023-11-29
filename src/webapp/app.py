from flask import Flask, render_template, request
from src.main import run_algorithm

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("welcome.html")  # Assuming you have a welcome.html for the input form

@app.route("/result", methods=["POST"])
def result():
    # Get source and destination from the form
    source = request.form['source']
    destination = request.form['destination']

    # Call the run_algorithm function with source and destination
    result = run_algorithm(source, destination)

    # Pass the result to the template
    return render_template("result.html", source=source, destination=destination, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")


