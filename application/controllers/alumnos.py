import web 
import json
import csv 

class Alumnos:
    file = 'static/csv/alumnos.csv'

    def __init__(self):
        pass 

    def GET(self):
        try:
            data = web.input() 
            if data['action'] == 'get':
                if data['token'] == "1234":
                    result = self.actionGet(self.file) 
                    return json.dumps(result)
                else:
                    result = {} 
                    result['status'] = "Command not found"
                    return json.dumps(result) 
            else:
                result = {} 
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            print("Error" + str(e.args()))
            result = {}
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result) 

    @staticmethod
    def actionGet(file):
        try:
            result = {}  
            result['status'] = "200 ok"
            
            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile)  
                alumnos = []  
                for row in reader:
                    fila = {}  
                    fila['matricula'] = row['matricula']  
                    fila['nombre'] = row['nombre']  
                    fila['primer_apellido'] = row['primer_apellido'] 
                    fila['segundo_apellido'] = row['segundo_apellido'] 
                    fila['carrera'] = row['carrera'] 
                    alumnos.append(fila) 
                result['alumnos'] = alumnos
            return result
        except Exception as e:
            result = {} 
            print("Error {}".format(e.args))
            result['status'] = "Error " 
            return result 


#METODO PARA HHACER LA BUSQUEDA
    def actionSearch(self):
            try:
                data = web.input() 
                if data['action'] == 'search':
                    if data['matricula'] == "001":
                        result = self.actionSearch(self.file) 
                        return json.dumps(result)
                    else:
                        result = {} 
                        result['status'] = "Command not found"
                        return json.dumps(result) 
                else:
                    result = {} 
                    result['status'] = "Invalid Token"
                    return json.dumps(result)
            except Exception as e:
                print("Error" + str(e.args()))
                result = {}
                result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
                return json.dumps(result) 

        @staticmethod
        def actionSearch(file):
            try:
                result = {}  
                result['status'] = "200 ok"
                
                with open(file, 'r') as csvfile:  
                    reader = csv.DictReader(csvfile)  
                    alumnos = []  
                    for row in reader:
                        fila = {}  
                        fila['matricula'] = row['matricula']  #revisar porque esta ,al
                        fila['nombre'] = row['nombre']  
                        fila['primer_apellido'] = row['primer_apellido'] 
                        fila['segundo_apellido'] = row['segundo_apellido'] 
                        fila['carrera'] = row['carrera'] 
                        alumnos.append(fila) 
                    result['alumnos'] = alumnos
                return result
            except Exception as e:
                result = {} 
                print("Error {}".format(e.args))
                result['status'] = "Error " 
                return result 

        #hackear con un index, agregar 