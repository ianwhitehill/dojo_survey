from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    return render_template("result.html", result = request.form)

if __name__ == "__main__":
    app.run(debug=True)
