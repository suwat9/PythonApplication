from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/result", methods=["GET", "POST"])
def home():
    result = request.form
    return render_template("result.html",result=result)

if __name__ == "__main__":
    app.run()