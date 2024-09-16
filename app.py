from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            # Validar que las notas estén en el rango de 10 a 70 y la asistencia de 0 a 100
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
                return render_template('ejercicio1.html', error=error, promedio="", estado="")
            if not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
                return render_template('ejercicio1.html', error=error, promedio="", estado="")

            promedio = round((nota1 + nota2 + nota3) / 3, 1)
            estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"

            return render_template('ejercicio1.html', promedio=promedio, estado=estado, error="")
        except ValueError:
            error = "Por favor, ingrese valores numéricos válidos."
            return render_template('ejercicio1.html', error=error, promedio="", estado="")
    return render_template('ejercicio1.html', promedio="", estado="", error="")



@app.route('/ejercicio2',methods=["GET","POST"])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        caracteres = len(nombre_largo)


        return render_template('ejercicio2.html', nombre_largo=nombre_largo, caracteres=caracteres)
    return render_template('ejercicio2.html', nombre_largo="", caracteres="")

if __name__ == '__main__':
    app.run(debug=True)
