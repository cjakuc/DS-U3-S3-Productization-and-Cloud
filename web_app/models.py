# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Tweet(db.Model):
    tweet_id = db.Column(db.Integer, primary_key=True)
    tweet_content = db.Column(db.String(128))
    # user_id = db.Column(db.Integer, ForeignKey("User.user_id"))

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_handle = db.Column(db.String(128))

def parse_records(database_records):
    """
    Parses database records into a clean json-like structure
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records