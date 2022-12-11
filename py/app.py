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

    def __repr__(self):
        return 'Post' + str(self.id)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Comment' + str(self.id)


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
        }
        all_posts.append(postObject)
    return json.dumps({"posts": all_posts})


@app.route('/posts/newPost', methods=["GET", "POST"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def new_post():
    post_title = request.get_json(force=True)['title']
    post_content = request.get_json(force=True)['content']
    post_status = request.get_json(force=True)['status']
    db.session.add(Post(title=post_title, content=post_content,
                   status=post_status))
    db.session.commit()
    return "h"


@app.route('/posts/delete/<int:id>', methods=["GET", "DELETE"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return 'h'


@app.route('/posts/editPost', methods=["GET", "PUT"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def edit_post():
    id = request.get_json(force=True)['id']
    post = Post.query.get(id)
    post.title = request.get_json(force=True)['title']
    post.content = request.get_json(force=True)['content']
    db.session.commit()
    return 'h'


@app.route('/posts/editlike/<int:id>', methods=["GET", "PUT"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def like_post(id):
    post = Post.query.get(id)
    post.status = not post.status
    db.session.commit()
    return 'h'


@app.route('/comments', methods=["GET"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def comments():
    comments = Comment.query.all()
    all_comments = []
    for comment in comments:
        commentObject = {
            'id': comment.__dict__['id'],
            'post_id': comment.__dict__['post_id'],
            'content': comment.__dict__['content']
        }
        all_comments.append(commentObject)
    return json.dumps({"comments": all_comments})


@app.route('/comments/newcomment', methods=["GET", "POST"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def new_comment():
    n_post_id = request.get_json(force=True)['post_id']
    n_content = request.get_json(force=True)['content']
    db.session.add(Comment(post_id=n_post_id, content=n_content))
    db.session.commit()
    return "h"


@app.route('/comments/delete/<int:id>', methods=["GET", "DELETE"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def delete_comment(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    return 'h'


if __name__ == "__main__":
    app.run(debug=True)
