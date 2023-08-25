from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dato_guardado = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    global dato_guardado
    dato = request.form.get('dato')
    dato_guardado = dato
    return "Dato guardado: " + dato

@app.route('/obtener_dato', methods=['GET'])
def obtener_dato():
    global dato_guardado
    return jsonify({'dato': dato_guardado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

