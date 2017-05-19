import feedparser
from flask import Flask

app=Flask(__name__)
CNN_FEED = "http://rss.cnn.com/rss/edition.rss"
@app.route("/")
def get_news():
    feed = feedparser.parse(CNN_FEED)
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> CNN Headline </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))
if __name__ == "__main__":
    app.run(port=5000, debug=False)