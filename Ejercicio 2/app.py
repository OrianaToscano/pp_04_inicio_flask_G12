from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():  
  return render_template('index.html')
 
@app.route('/ayuda')
def ayuda():  
  return render_template('ayuda.html')

@app.route('/listado')
def listadoPerCapita():
  conn = sqlite3.connect('co_emissions.db')

  consulta = conn.execute('''SELECT Country, Value, Year
                           FROM emissions
                           WHERE Series LIKE 'pcap'
                           ORDER BY Year DESC, Value DESC
                           LIMIT 10;''')

  paises = []
  for i in consulta:
    paises.append(i)

  conn.close()
  
  return render_template('listados.html', 
                          datosPaises=paises,
                          subtitulo='Ordenados por valores PerCapita',
                          categoria='perCapita')


  
@app.route('/listado/top')
def listadoTotal():
  conn = sqlite3.connect('co_emissions.db')

  consulta = conn.execute('''SELECT Country, Value, Year
                           FROM emissions
                           WHERE Series LIKE 'total'
                           ORDER BY Year DESC, Value DESC
                           LIMIT 10;''')

  paises = []
  for i in consulta:
    paises.append(i)

  conn.close()
  return render_template('listados.html', 
                          datosPaises=paises,
                          subtitulo='Ordenados por valores totales',
                          categoria='totales')


@app.route('/listado/<pais>')
def listadoPorPais(pais):
  conn = sqlite3.connect('co_emissions.db')

  consulta = conn.execute(f'''SELECT Series, Value, Year
                           FROM emissions
                           WHERE Country LIKE "{pais}"
                           ORDER BY Year DESC
                           LIMIT 2;''').fetchall()
  conn.close()
  
  if len(consulta)>0:
    datos = []
    for i in consulta:
      datos.append(i)
    
    return render_template('listadoPorPais.html', 
                            datos=datos,
                            pais = pais,
                            subtitulo = 'Emiciones de CO del país segun valores')
  else:
    return 'El pais ingresado no es valido'




    
app.run(host='0.0.0.0', port=81)