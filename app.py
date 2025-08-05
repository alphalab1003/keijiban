import os
from flask import Flask, render_template, request, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)
posts_file = 'posts.json'  # 投稿データを保存するファイル名

# ファイルから投稿を読み込む関数
def load_posts():
    if os.path.exists(posts_file):
        with open(posts_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# ファイルに投稿を書き込む関数
def save_posts(posts):
    with open(posts_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

# 投稿一覧を読み込む
posts = load_posts()

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
    name = request.form['name']
    message = request.form['message']
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    posts.append({'name': name, 'message': message, 'timestamp': timestamp})
    save_posts(posts)  # ファイルに保存
    return redirect('/')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    if 0 <= post_id < len(posts):
        posts.pop(post_id)
        save_posts(posts)  # ファイルに保存
    return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Renderが割り当てるポートを取得（なければ5000）
    app.run(host="0.0.0.0", port=port, debug=True)