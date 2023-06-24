from flask import Flask, render_template, request, jsonify
import natural

app = Flask(__name__)

@app.route('/')
def natural_web():
    return render_template('natural_web.html')

@app.route('/transform', methods=['POST'])
def transform():
    input_TA_text = request.json['inputText']
    output_TA_text = natural.translation(input_TA_text)
    return jsonify({"outputText": output_TA_text})

if __name__ == "__main__":
    app.run()

