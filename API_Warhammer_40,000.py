from flask import Flask, jsonify
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
    "https://i.pinimg.com/736x/e6/9a/5e/e69a5e48ea77c6767a73396af63cdd46.jpg",
    "https://i.pinimg.com/736x/e8/fb/de/e8fbde6b454251d719a6aff9c71c7646.jpg",
    "https://i.pinimg.com/originals/b4/39/2e/b4392ed00577cb8c94a3178d6008be72.gif",
    "https://i.pinimg.com/736x/37/c4/ee/37c4eef61bb27e06181afe5922769549.jpg",
    "https://i.pinimg.com/736x/42/0e/bb/420ebb91e5c51bf5cfb57a199d87f495.jpg"
]

@app.route('/quote', methods=['GET'])
def get_random_quote():
    import random
    return jsonify({"quote": random.choice(quotes)})

@app.route('/image', methods=['GET'])
def get_random_image():
    import random
    return jsonify({"image": random.choice(images)})


app.run(debug=True)