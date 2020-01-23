#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app =Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__='article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)


db.create_all()

@app.route("/")
def hello_world():

    # #增加
    # article1= Article(title="aaa",content='bbbb')
    # db.session.add(article1)
    # #提交 事务
    # db.session.commit()

    # 查
    result = Article.query.filter(Article.title=='aaa').all()
    # result = Article.query.filter(Article.title=='aaa').first()
    # print(result.title)
    # print(result.content)
    # article1 = result[1]
    # print(article1.title)
    # print(article1.content)


    # 改
    # article1=Article.query.filter(Article.title=='new title').first()
    # article1.title='new title'
    # article1.content='da da shazhucai'
    # db.session.commit()

    # 删
    article1=Article.query.filter(Article.content=='bbbb').first()
    print(article1.title)
    db.session.delete(article1)

    db.session.commit()

    return 'hello mysql!'

if __name__ == '__main__':
    app.run(debug=True)