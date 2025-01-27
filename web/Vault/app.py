from flask import Flask, render_template, make_response, request
import jwt

SECRET="rafa2986"

def generateAccessToken():
    payload_data = {
        "user": "guest",
    }
    return jwt.encode(payload=payload_data, key=SECRET)

with open('/flag.txt', 'r') as f:
    FLAG = f.read()

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    access_token=generateAccessToken()
    if request.method == "POST":
        user_input = request.form["access_token"]
        try:
            user_input = jwt.decode(user_input, key=SECRET, algorithms=["HS256"])["user"]
        except:
            user_input = "INVALID ACCESS TOKEN!"
        if user_input == "admin":
            return render_template('index.html', access_token=access_token, user_input=user_input, flag=FLAG, tokenMatches=True)
        return render_template('index.html', access_token=access_token, user_input=user_input, tokenMatches=False)
    return render_template('index.html', access_token=access_token)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
