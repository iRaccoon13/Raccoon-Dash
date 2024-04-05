import flask
from flask import request, render_template, Flask
import feedparser
import requests
import os


app = Flask(__name__)

@app.get("/")
def index():
	return render_template('index.html')

@app.get("/news/")
def fetch_news():
	url = "https://news.google.com/rss"
	feed = feedparser.parse(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content)
	return render_template('news.html', feed=feed)


@app.get("/cal/")
def fetch_cal():
  return requests.get(os.environ["cal"], headers={'User-Agent': 'Mozilla/5.0'}).content

@app.get("/weather/")
def fetch_weather():
  return requests.get("https://api.wo-cloud.com/content/widget/?geoObjectKey=2917915&language=en&region=US&timeFormat=HH:mm&windUnit=mph&systemOfMeasurement=imperial&temperatureUnit=fahrenheit", headers={'User-Agent': 'Mozilla/5.0'}).content

if __name__ == '__main__':
  app.run()