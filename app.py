# Importamos flask
from flask import Flask, render_template
import dolar
# Generamos nuestra instancia de flask en app
app = Flask(__name__)

# Generamos primer ruta con app.route()


@app.route("/")
def index():
    return render_template('index.html', pc=dolar.decimeDolarCompra(), pv=dolar.decimeDolarVenta())
# la ruta siempre responde con la funcion


# validar que estemos en este modulo
if __name__ == "__main__":
    app.run(debug=True, port=3000)
