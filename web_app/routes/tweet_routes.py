# web_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, render_template, request, redirect

from web_app.models import db, Tweet, User, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():
    print("REQUESTED THE TWEETS IN JSON FORMAT")
    #tweet = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"},
    #] # todo: get from the database
    tweet_records = Tweet.query.all()
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def tweets():
    print("VISITED THE TWEETS PAGE")
    #books = [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"},
    #] # todo: get from the database
    tweet_records = Tweet.query.all()
    return render_template("tweets.html", tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    #return jsonify({
    #    "message": "BOOK CREATED OK (TODO)",
    #    "book": dict(request.form)
    #})
    new_tweet = Tweet(tweet_id=request.form["tweet_id"], tweet_content=request.form["tweet_content"])
    print(new_tweet)
    db.session.add(new_tweet)
    db.session.commit()
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect("/tweets")