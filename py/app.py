from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin, CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myData.db'
db = SQLAlchemy(app)
app.config['CORS_HEADERS'] = "content-type"
cors = CORS(app, resources={r"/foo": {"origins": "*"}})


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Post' + str(self.id)


with app.app_context():
    db.create_all()


@app.route('/posts', methods=["GET"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def posts():
    posts = Post.query.all()
    all_posts = []
    for post in posts:
        postObject = {
            'id': post.__dict__['id'],
            'title': post.__dict__['title'],
            'content': post.__dict__['content'],
            'status': post.__dict__['status'],
            'comment': post.__dict__['comment'],
        }
        all_posts.append(postObject)
    return json.dumps({"posts": all_posts})


@app.route('/posts/newPost', methods=["GET", "POST"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def newPost():
    post_title = request.get_json(force=True)['title']
    post_content = request.get_json(force=True)['content']
    post_status = request.get_json(force=True)['status']
    post_comment = request.get_json(force=True)['comment']
    db.session.add(Post(title=post_title, content=post_content,
                   status=post_status, comment=post_comment))
    db.session.commit()
    return "h"


if __name__ == "__main__":
    app.run(debug=True)
