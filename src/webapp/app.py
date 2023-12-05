from flask import Flask, render_template, request

from src.main import run_algorithm

app = Flask(__name__)


# Home page
@app.route("/", methods=["GET"])
def home():
    # Render the home page for GET requests
    return render_template("home.html")  # home.html is the page with the input form


# Results page
@app.route("/result", methods=["POST"])
def result():
    source = request.form['source']
    destination = request.form['destination']

    # If the user entered the same city for both source and destination
    if source == destination:
        return render_template("home.html", error_message="Source and destination cities cannot be the same.")

    # Check if both source and destination inputs are given
    if source and destination:
        result, max_capacity = run_algorithm(source, destination)

        # In case source, destination, or both are missing, render the home page with an error message
        if not result:
            # Handle error messages
            if max_capacity == 'source and destination':
                error_message = f'Please enter valid source and destination cities. "{source}" and "{destination}" are not valid city names.'
            elif max_capacity == "source":
                error_message = f'Please enter a valid source city. "{source}" is not a valid city name.'
            elif max_capacity == "destination":
                error_message = f'Please enter a valid destination city. "{destination}" is not a valid city name.'

            # Redirect back to the home page with the error message
            return render_template("home.html", error_message=error_message)

        # Sort by capacity in decreasing order
        result = sorted(result, key=lambda x: x["maximum capacity"], reverse=True)

        # Render the results page with the display results
        return render_template("results.html", display_results=result, source_city=source.title(),
                               destination_city=destination.title(), max_capacity=max_capacity)

    # In case source or destination is missing, render the home page again with an error message
    return render_template("home.html", error_message="Please enter both source and destination.")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
