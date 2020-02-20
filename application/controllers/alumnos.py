import web 
import json
import csv 

class Alumnos:
    def GET(self):
        try:
            datos = web.input() 
            if datos['action'] == 'get':
                if datos['token'] == "1234":
                    result2 = {}
                    result1 = []
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

                    result = self.actionGet(self.app_version, self.file)  # llama al metodo actionGet(), y almacena el resultado
                    return json.dumps(result)  # Parsea el diccionario result a formato json
                else:
                    result = {}  # crear diccionario vacio
                    result['app_version'] = self.app_version  # version de la webapp
                    result['status'] = "Command not found"
                    return json.dumps(result)  # Parsea el diccionario result a formato json
            else:
                result = {}  # crear diccionario vacio
                result['app_version'] = self.app_version  # version de la webapp
                result['status'] = "Invalid Token"
                return json.dumps(result)  # Parsea el diccionario result a formato json
        except Exception as e:
            print("Error")
            result = {}  # crear diccionario vacio
            result['app_version'] = self.app_version  # version de la webapp
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)  # Parsea el diccionario result a formato json
            
    def actionGet(app_version, file):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status
            
            with open(file, 'r') as csvfile:  # abre el archivo en modo lectura
                reader = csv.DictReader(csvfile)  # toma la 1er fila para los nombres
                alumnos = []  # array para almacenar todos los alumnos
                for row in reader:  # recorre el archivo CSV fila por fila
                    fila = {}  # Genera un diccionario por cada registro en el csv
                    fila['matricula'] = row['matricula']  # obtiene la matricula y la agrega al diccionario
                    fila['nombre'] = row['nombre']  # optione el nombre y lo agrega al diccionario
                    fila['primer_apellido'] = row['primer_apellido']  # optiene el primer_apellido
                    fila['segundo_apellido'] = row['segundo_apellido']  # optiene el segundo apellido
                    fila['carrera'] = row['carrera']  # obtiene la carrera
                    alumnos.append(fila)  # agrega el diccionario generado al array alumnos
                result['alumnos'] = alumnos  # agrega el array alumnos al diccionario result
            return result  # Regresa el diccionario generado
        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args()))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado