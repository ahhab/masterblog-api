from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)

@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    title = data.get('title')
    content = data.get('content')

    missing_fields = []
    if not title:
        missing_fields.append('title')
    if not content:
        missing_fields.append('content')

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    new_id = max(p['id'] for p in POSTS) + 1 if POSTS else 1
    new_post = {
        "id": new_id,
        "title": title,
        "content": content
    }
    POSTS.append(new_post)
    return jsonify(new_post), 201


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = next((p for p in POSTS if p['id'] == id), None)
    if post:
        POSTS.remove(post)
        return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200
    return jsonify({"message": "Post not found"}), 404


@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = next((p for p in POSTS if p['id'] == id), None)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    title = data.get('title')
    content = data.get('content')

    if title:
        post['title'] = title
    if content:
        post['content'] = content

    return jsonify(post)


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_query = request.args.get('title')
    content_query = request.args.get('content')

    results = POSTS

    if title_query:
        results = [p for p in results if title_query.lower() in p['title'].lower()]

    if content_query:
        results = [p for p in results if content_query.lower() in p['content'].lower()]

    return jsonify(results)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
