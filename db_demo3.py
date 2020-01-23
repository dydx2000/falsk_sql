#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app =Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    # content = db.Column(db.Text,nullable=False)

class Article(db.Model):
    __tablename__='article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id =db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref=db.backref('articles'))

db.create_all()

@app.route("/")
def index():
    #添加用户
    # user1 =User(username="zhiliao")
    # db.session.add(user1)
    # db.session.commit()



    # 添加文章
    # article = Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # 查询标题为aaa的文章 的作者
    # article = Article.query.filter(Article.title =='aaa').first()
    # author_id = article.author_id
    # user =User.query.filter(User.id ==author_id).first()
    # print(user.username)

    #zhiliao 这个用户写过的所有文章
    # article =Article(title='111',content='222',author_id=1)
    # db.session.add(article)
    #
    #
    # db.session.commit()


    user = User.query.filter(User.username =='zhiliao').first()
    result =user.articles
    for article in result:
        print('-'*20)
        print(article.title)

    return 'hello mysql!'

if __name__ == '__main__':
    app.run(debug=True)