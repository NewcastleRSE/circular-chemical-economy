from importlib import import_module
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    industry = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

# class Entry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, nullable=False)
#     created = db.Column(db.DateTime, default=datetime.utcnow)
#     olefin_mass = db.Column(db.Float, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     imported = db.Column(db.Float, nullable=False)
#     exported = db.Column(db.Float, nullable=False)
#     acquired = db.Column(db.Float, nullable=False)
#     manufactured = db.Column(db.Float, nullable=False)
#     transferred = db.Column(db.Float, nullable=False)
#     disposed = db.Column(db.Float, nullable=False)
#     recycled = db.Column(db.Float, nullable=False)

#     def __repr__(self):
#         return '<Entry %r>' % self.id

with app.app_context():
    db.create_all()

    db.session.add(User(username="example", password="password", company="Unilever", industry="Pharmaceutical"))
    #db.session.add(Entry(user_id=1, olefin_mass=70, year=2022, imported=10, exported=10, acquired=10, manufactured=10, transferred=10, disposed=10, recycled=10))
    db.session.commit()

    users = db.session.execute(db.select(User)).scalars()

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
