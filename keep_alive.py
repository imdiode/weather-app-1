from flask import Flask, render_template
from threading import Thread
import json

# Flask server

app = Flask('')

# Getting index.html view on the startpage
@app.route('/')
def home():
  return render_template("/public/index.html")

# Fetch API data
@app.route('/data')
def jsonrtn():
  with open('./templates/public/data.json', 'r') as f:
      data = json.load(f)
      return data

# Start server
def run():
  app.run(host='127.0.0.1', port=8080)

# Thread for keeping it running
def keep_alive():
  t = Thread(target=run)
  t.start()
