from flask import Flask, render_template
from random import randrange


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dado')
def dado():
    num = randrange(1,7)
    return render_template('dado.html',
                           numero_dado = num)


@app.route('/fecha')
def fecha():
  mes = randrange(1,13)
  dia = diasAleatorios(mes)
  año = randrange(1970,2101)

  fecha = f'{dia}/{mes}/{año}'
  return render_template('fecha.html',
                         fecha_html=fecha)


@app.route('/color')
def color():
  color = ''
  for i in range(3):
    numero_hexa = randrange(0,256)
    color += str(numero_hexa)
    if i != 2:
      color += ','

  color_html = f'rgb({color})'
  return render_template('color.html',
                        color_hexa = color_html)
  

    
@app.route('/dado/<n>')
def mostrarNumeros(n):
  try:  
    n= int(n)
    if n<=0 or n>10:
      return "El valor ingresado debe ser mayor a 0 y menor a 11"
    num = ""
    for i in range(n):
      num += f'{str(randrange(1,7))}  '
      
    return render_template("mostrar_numeros.html",
                          numeros=num)
  except ValueError:
    return "El valor ingresado en la direccion debe ser un numero entero"


def diasAleatorios(unMes):
  if unMes in [1,3,5,7,8,10,12]:
      dia = randrange(1,32)
  elif unMes in [4,6,9,11]:
      dia = randrange(1,31)
  else:
      dia = randrange(0,29)

  return dia
    
    
@app.route('/fecha/<y>')
def mostrarFechaPorY(y):
  try:
    y = int(y)
    if y<=0:
      return "El valor ingresado debe ser mayor a 0"
      
    mes = randrange(1,13)
    dia = diasAleatorios(mes)
    año = y
  
    fecha = f'{dia}/{mes}/{año}'
    return render_template('fecha.html',
                           fecha_html=fecha)

  except ValueError:
    return "El valor ingresado en la direccion debe ser un numero entero"


@app.route('/fecha/<y>/<m>')
def mostrarFechaPorYM(y,m):
  try:
    y = int(y)
    m=int(m)
    if y<=0 or (m<1 or m>12):
      return "El valor ingresado no es valido para una fecha"
      
    mes = m
    dia = diasAleatorios(m)
    año = y
  
    fecha = f'{dia}/{mes}/{año}'
    return render_template('fecha.html',
                           fecha_html=fecha)

  except ValueError:
    return "El valor ingresado en la direccion debe ser un numero entero"


app.run(host='0.0.0.0', port=81)
