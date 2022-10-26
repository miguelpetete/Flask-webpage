from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/studies")
def studies():
    return render_template('index.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/technologies")
def technologies():
    return render_template('technologies.html')

if __name__ == "__main__":
    app.run()