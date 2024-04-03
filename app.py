import flask
from flask import request, render_template, Flask
import feedparser
import requests


app = Flask(__name__)

@app.get("/")
def index():
	return render_template('index.html')

@app.get("/news/")
def fetch_news():
	url = "https://news.google.com/rss"
	feed = feedparser.parse(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content)
	return render_template('news.html', feed=feed)


proxydata = {}

@app.route("/proxy/<name>", methods=["POST", "GET", "DELETE"])
def proxy(name):
	global proxydata
	if request.method == "POST":
		proxydata[name] = requests.get(request.form.get("url"), headers={'User-Agent': 'Mozilla/5.0'}.content)
		return proxydata[name], 200
	elif request.method == "GET":
		try:
			return proxydata[name], 200
		except KeyError:
			return "NOT FOUND", 404
	elif request.method == "DELETE":
		try:
			del proxydata
		except KeyError:
			return "NOT FOUND", 404
		else: 
			return "SUCCESS", 200