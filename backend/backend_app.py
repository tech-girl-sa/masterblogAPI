from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET', 'POST'])
def get_posts():
    if request.method == "POST":
        new_post = request.get_json()
        if "title" not in new_post or "content" not in new_post:
            return  jsonify({"error":"Invalid post data."}), 400
        else:
            new_post["id"] = max([post['id'] for post in POSTS]) + 1
            POSTS.append(new_post)
            return new_post, 201
    return jsonify(POSTS)


def fetch_post_by_id(id):
    posts = [post for post in POSTS if post['id']==id]
    if len(posts) > 0:
        return posts[0]


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete(id):
    post_to_delete = fetch_post_by_id(id)
    if post_to_delete:
        POSTS.remove(post_to_delete)
        return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200
    else:
        return jsonify({"error": "Post doesn't exist."}), 404


@app.route('/api/posts/<int:id>', methods=['PUT'])
def update(id):
    post_to_update = fetch_post_by_id(id)
    if post_to_update:
        post = request.get_json()
        if "title" in post :
            post_to_update['title'] = post['title']
        if "content" in post:
            post_to_update['content'] = post['content']
        return jsonify(post_to_update), 200
    else:
        return jsonify({"error": "Post doesn't exist."}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
