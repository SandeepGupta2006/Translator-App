from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES
import asyncio

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", languages=LANGUAGES, default_src=None, default_dest='hi')


@app.route("/translate", methods=['GET', 'POST'])
def translate_method():
    data = request.get_json()
    src = data['src']
    dest = data['dest']
    input_text = data['inputText']

    async def translate():
        return await Translator().translate(input_text, src=src, dest=dest)

    translated = asyncio.run(translate())

    return jsonify({"text": translated.text, "pronunciation": translated.pronunciation})


if __name__ == "__main__":
    app.run(debug=True)
