from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", message="Hello Flask")


if __name__ == "__main__":
    # Enable debug for development convenience
    app.run(debug=True)

