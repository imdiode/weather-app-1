from flask import Flask, render_template
from threading import Thread
import json

app = Flask('')


@app.route('/')
def home():
  return render_template("/public/index.html")

@app.route('/data')
def jsonrtn():
  with open('./templates/public/data.json', 'r') as f:
      data = json.load(f)
      return data


def run():
  app.run(host='127.0.0.1', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
