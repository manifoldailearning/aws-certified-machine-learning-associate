from flask import Flask, render_template
import os


app = Flask(__name__)

# list of cat images
url_link = "https://dz8fbjd9gwp2s.cloudfront.net/courses/63ab29b2e4b0e45b5c7246d4/63ab29b2e4b0e45b5c7246d4_scaled_cover.jpg"


@app.route("/")
def index():
    return render_template("index.html", url=url_link)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
