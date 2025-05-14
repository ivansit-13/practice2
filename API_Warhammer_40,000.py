from flask import Flask, jsonify
import os
app = Flask(__name__)

# Ваши цитаты и изображения
quotes = [
    "За Империум!",
    "Время крошить врагов!",
    "Тех, кто с Империумом — с нами!",
    "Бей врага до последней капли крови.",
    "Никогда не сдавайся!"
]

images = [
    "https://i.pinimg.com/736x/66/00/42/6600425268f7f7bb5c269bdc78e1a1f4.jpg",
    "https://i.pinimg.com/736x/5c/52/8b/5c528ba1f67b082ddcd9eec4451e2205.jpg",
    "https://i.pinimg.com/736x/e6/9a/5e/e69a5e48ea77c6767a73396af63cdd46.jpg"
]

@app.route('/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes)

@app.route('/images', methods=['GET'])
def get_images():
    return jsonify(images)

@app.route('/quote', methods=['GET'])
def get_random_quote():
    import random
    return jsonify({"quote": random.choice(quotes)})

@app.route('/image', methods=['GET'])
def get_random_image():
    import random
    return jsonify({"image": random.choice(images)})

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)