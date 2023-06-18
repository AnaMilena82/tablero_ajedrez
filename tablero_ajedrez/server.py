from flask import Flask, render_template, url_for  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def index():
    return render_template("tablero.html")

@app.route('/<int:y>')
def tableroy(y):
    return render_template("tablero.html",y=y)

@app.route('/<int:x>/<int:y>')
def tableroxy(x,y):
    return render_template("tablero.html",x=x,y=y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def tableroxycolor(x,y,color1,color2):
    return render_template("tablero.html",x=x,y=y,color1=color1,color2=color2)



@app.route('/<path:path>') #Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
def error(path):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

    






if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

