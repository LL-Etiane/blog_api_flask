from flask import Blueprint, request, jsonify, make_response
from . import db
from .models import Posts
from sqlalchemy import exc

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/', methods=['GET'])
def all_posts():
    posts = Posts.query.order_by(-Posts.id)
    #create dict off posts
    columns = ['id', 'title', 'body']
    dict_posts = [{col: getattr(post, col) for col in columns} for post in posts]
    return jsonify(dict_posts)

#create post route
@posts.route('/create', methods=['POST'])
def create_post():
    rdata = request.get_json()
    #check to make sure that valid data is submited
    if not rdata or 'title' not in rdata.keys() or 'body' not in rdata.keys():
        return jsonify({"error": "Valid post body must be provided"}), 400
    try:
        #create post
        new_post = Posts(title=rdata['title'], body=rdata['body'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created successfully"})
    except exc.IntegrityError: #catches exception when creating a title that already exists
        return jsonify({"error": "Post title already exist"}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "There was an error creating post. please try again later"}), 400

#get single post route
@posts.route('/<int:id>')
def single_post(id):
    try:
        post = Posts.query.get(id)

        if not post:
            return jsonify({"error": "Post with provided id not found"}), 404
        return jsonify({
            "id": post.id,
            "title": post.title,
            "body": post.body
        })
    except Exception as e:
        print(e)
        return jsonify({"error": "There was a problem gettign post"}), 500