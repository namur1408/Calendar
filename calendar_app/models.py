from db_config import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(500), nullable=True)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'
