from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "your_secret_key_here"
