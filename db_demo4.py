#encoding:utf-8
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)



@app.route("/")
def hello_demo4():
    return 'Hello Demo4'


if __name__ == '__main__':
    app.run(debug=True)