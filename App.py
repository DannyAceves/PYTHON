from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello World!'

@app.route('/add conctact')
def add_contact():
    return 'Agregar contacto'

@app.route('/edit contact')
def edit_contact():
    return 'editar contacto2'

@app.route('/delete contact')
def delete_contact():
    return 'borrar contacto'

if __name__ == '_main_':
    app.run(port = 3000, debug = True)
