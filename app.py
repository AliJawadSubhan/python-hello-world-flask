from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

datetime.now()
print(datetime.now)

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# database = SQLAlchemy(app)

# @app.route('/')
# def index():
#     data = {"status" : "Flask successfuly works :3"}
#     return render_template("index.html", data=data)


# if __name__ == '__main__':
#     app.run(debug=True)


# class Todo(database.Model):
#     id = database.Column(database.String(200))