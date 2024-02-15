from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login')
def inicio():
  return render_template('login.html')


@app.route('/index')
def acercade():

 return render_template('index.html')

@app.route('/agregaruser')
def aduser():
  return render_template('admin_user.html')

@app.route('/Inventario')
def iventory():
  return render_template()

@app.route


def iventory():
  return render_template()


if __name__ == '__main__':
    app.run(debug=True)