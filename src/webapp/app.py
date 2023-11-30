from flask import Flask, render_template, request
from src.main import run_algorithm

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    # Render the home page for GET requests
    return render_template("home.html")  # home.html is the page with the input form


@app.route("/result", methods=["POST"])
def result():
    source = request.form['source']
    destination = request.form['destination']

    if source and destination:
        result, max_capacity = run_algorithm(source, destination)

        if not result:
            # Handle error messages
            if max_capacity == 'source and destination':
                error_message = f'"{source}" and "{destination}" are not valid city names. Please enter valid source and destination cities.'
            elif max_capacity == "source":
                error_message = f'"{source}" is not a valid city name. Please enter a valid source city.'
            elif max_capacity == "destination":
                error_message = f'"{destination}" is not a valid city name. Please enter a valid destination city.'

            # Redirect back to the home page with the error message
            return render_template("home.html", error_message=error_message)

        display_results = []
        result = sorted(result, key=lambda x: x["maximum capacity"], reverse=True)

        # for report in result:
        #     if report.get('layover'):
        #         display_results.append(
        #             f'{report["source city"]} -> {report["layover"]} (operated by {report["layover airline"]}: {report["layover model"]}) Flight capacity: {report["layover capacity"]}<br>'
        #             f'{report["layover"]} -> {report["destination city"]} (operated by {report["destination airline"]}: {report["destination model"]}) Flight capacity: {report["destination capacity"]}<br>'
        #             f'Maximum capacity: {report["maximum capacity"]}<br>')
        #     else:
        #         display_results.append(
        #             f'{report["source city"]} -> {report["destination city"]} (operated by {report["destination airline"]}: {report["destination model"]}) Flight capacity: {report["maximum capacity"]}<br>')
        #
        # display_results.append(f'Total capacity: {max_capacity}')

        # Render the results page with the display results
        return render_template("results.html", display_results=result, source_city=source.title(), destination_city=destination.title())

    # In case source or destination is missing, render the home page again with an error message
    return render_template("home.html", error_message="Please enter both source and destination.")


if __name__ == "__main__":
    app.run(debug=True)

