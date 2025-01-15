from flask import Flask, render_template_string

app = Flask(__name__)

# HTML-шаблон с кнопкой и всплывающим сообщением
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>БУ!</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }
        button {
            font-size: 24px;
            padding: 20px 40px;
            background-color: #ff4747;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        button:hover {
            transform: scale(1.1);
        }
        button:active {
            background-color: #e63e3e;
        }
    </style>
</head>
<body>
    <button onclick="showMessage()">БУ!</button>

    <script>
        function showMessage() {
            alert("испугался? Не бойся, я друг, я тебя не обижу. Иди сюда, иди ко мне, сядь рядом со мной, посмотри мне в глаза. Ты видишь меня? Я тоже тебя вижу. Давай смотреть друг на друга до тех пор, пока наши глаза не устанут. Ты не хочешь? Почему? Что-то не так?");
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)