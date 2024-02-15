from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usuario'
app.config['MYSQL_PASSWORD'] = 'contraseña'
app.config['MYSQL_DB'] = 'basededatos'

mysql = MySQL(app)

@app.route('/cosa2', methods=['POST'])
def agregar():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tabla (campo) VALUES (%s)", (request.form['valor'],))
    mysql.connection.commit()
    cur.close()
    return 'Agregado con éxito'

@app.route('/leer')
def leer():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tabla")
    datos = cur.fetchall()
    cur.close()
    return str(datos)

@app.route('/actualizar', methods=['PUT'])
def actualizar():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE tabla SET campo = %s WHERE id = %s", (request.form['valor'], request.form['id']))
    mysql.connection.commit()
    cur.close()
    return 'Actualizado con éxito'

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tabla WHERE id = %s", (request.form['id'],))
    mysql.connection.commit()
    cur.close()
    return 'Eliminado con éxito'

if __name__ == '__main__':
    app.run(debug=True)
