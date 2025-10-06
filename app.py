from flask import Flask, request, render_template
import caesar_cipher as cipher  # tera original code import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    text = request.form["text"]
    shift = int(request.form["shift"])
    action = request.form["action"]

    if action == "encrypt":
        result = cipher.encrypt(text, shift)
    else:
        result = cipher.decrypt(text, shift)

    return render_template("index.html", text=text, shift=shift, action=action, result=result)

if __name__ == "__main__":
    app.run(debug=True)
