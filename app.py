from flask import Flask, render_template
import urllib.request, json, requests

app = Flask(__name__)

@app.route("/index")
def get_activity():
    response_API = requests.get('http://www.boredapi.com/api/activity/')
    data = response_API.text
    dict = json.loads(data)

    return render_template ("index.html", activity=dict["activity"])

if __name__ == '__main__':
    app.run(debug=True)
