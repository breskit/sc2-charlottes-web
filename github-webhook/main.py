import git
from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)
webhook = Webhook(app)

@app.route("/")
def hello_world():
    return "Hello world"

@webhook.hook()
def on_push(data):
    g = git.cmd.Git("/code")
    g.pull()
    return("done")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")