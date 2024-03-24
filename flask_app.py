from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

lat = {'Ch': 'Ч', 'ch': 'ч', 'Sh': 'Ш', 'sh': 'ш', '\'': 'ъ', 'Yu': 'Ю', 'yu': 'ю', 'Ya': 'Я', 'ya': 'я', 'Oʻ': 'Ў', 'oʻ': 'ў', 'Q': 'Қ', 'q': 'қ', 'Gʻ': 'Ғ', 'gʻ': 'ғ', 'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в', 'G': 'Г', 'g': 'г', 'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е', 'Yo': 'Ё', 'yo': 'ё', 'J': 'Ж', 'j': 'ж', 'Z': 'З', 'z': 'з', 'I': 'И', 'i': 'и', 'Y': 'Й', 'y': 'й', 'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н', 'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у', 'F': 'Ф', 'f': 'ф', 'X': 'Х', 'x': 'х', 'H': 'Ҳ', 'h': 'ҳ'}

cyr = {'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Yo', 'ё': 'yo', 'Ж': 'J', 'ж': 'j', 'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'Y', 'й': 'y', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'X', 'х': 'x', 'Ц': 'S', 'ц': 's', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Ъ': '\'', 'ъ': '\'', 'Э': 'E', 'э': 'e', 'Ю': 'Yu', 'ю': 'yu', 'Я': 'Ya', 'я': 'ya', 'Ў': 'Oʻ', 'ў': 'oʻ', 'Қ': 'Q', 'қ': 'q', 'Ғ': 'Gʻ', 'ғ': 'gʻ', 'Ҳ': 'H', 'ҳ': 'h'}


def alphachanger(context, pattern):
    patterns = {"latin": cyr, "cyrillic": lat}
    if patterns.get(pattern):
        for before, after in patterns[pattern].items():
            context = context.replace(before, after)
        return context
    else:
        return False

@app.route('/')
def index():
    return 'AlphaChanger'

@app.route("/translate", methods=["POST"])
def changealph():
    data = request.get_json()

    context = data.get("context", None)
    pattern = data.get("pattern", None)

    if context == "":
        return jsonify({"result": context}), 200

    if not (context and pattern):
        return jsonify({ 'error': 'Invalid input.' }), 400

    result = {
        "result": alphachanger(context, pattern),
    }
    if not result["result"]:
        return jsonify({ 'error': 'Invalid pattern.' }), 400
    return jsonify(result), 200

if __name__ == '__main__':
   app.run(debug=False)