from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])
        operation = request.form["operation"]
        if operation == "encrypt":
            result = caesar_cipher(text, shift, encrypt=True)
        elif operation == "decrypt":
            result = caesar_cipher(text, shift, encrypt=False)
        else:
            result = "Invalid operation"
        return render_template("index.html", result=result, text=text, shift=shift)
    return render_template("index.html", result="", text="", shift=0)

if __name__ == "__main__":
    app.run(debug=True)
