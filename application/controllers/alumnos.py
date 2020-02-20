import web 
import app
import json
import csv 

class Alumnos:
    def GET(self):
        try:
            datos = web.input() 
            if datos['action'] == 'get' and datos['token'] == "1234":
                result1 = []
                result2 = {}
                with open('static/csv/datos.csv','r') as csvfile:
                    reader = csv.DictReader(csvfile) #Toma la primer fila para los nombres
                    for row in reader:
                        result1.append(row)
                        result2['status'] = "200 Ok"
                        result2['alumnos'] = result1
                return json.dumps(result2)
            else:
                result = [] #CREAR VALORES 
                result.append("No te conozco")
                return result
        except Exception as error:
            result = [] #Crear 
            result.append("Faltan valores {}".format(error.args)) 
            return result

