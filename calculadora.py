from flask import Flask, request, jsonify, render_template
from parser_logic import parser, evaluate_tree

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json()
    expression = data.get("expression")
    try:
        tree = parser.parse(expression)
        result = evaluate_tree(tree)
        return jsonify({"result": result, "tree": tree})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)