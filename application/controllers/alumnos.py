import web 
import json
import csv 
'''
http://localhost:8080/alumnos?action=get&token=1234
http://localhost:8080/alumnos?action=search&token=1234&matricula=17161511
http://localhost:8080/alumnos?action=put&token=1234&matricula=17161513&nombre=Jose&primer_apellido=Vasquez&segundo_apellido=Vargas&carrera=TI
http://localhost:8080/alumnos?action=delete&token=1234&matricula=17161611
http://localhost:8080/alumnos?action=update&token=1234&matricula=17161513&nombre=Jose&primer_apellido=Vasquez&segundo_apellido=Vargas&carrera=TI
'''

class Alumnos:
    app_version = "0.02"
    file = 'static/csv/alumnos.csv'

    def __init__(self):
        pass 

    def GET(self):
        try:
            data = web.input() 
            if data['token'] == "1234":
                if data['action'] == 'get':
                    result = self.actionGet(self.app_version,self.file) 
                    return json.dumps(result)
                elif data['action'] == 'search':
                    matricula = data['matricula']
                    result = self.actionSearch(self.app_version,self.file,matricula) 
                    return json.dumps(result)
                elif data['action'] == 'put':
                    matricula = int(data['matricula'])
                    nombre = str(data['nombre'])
                    primer_apellido = str(data['primer_apellido'])
                    segundo_apellido = str(data['segundo_apellido'])
                    carrera = str(data['carrera'])
                    alumnos1=[]
                    alumnos1.append(matricula)
                    alumnos1.append(nombre)
                    alumnos1.append(primer_apellido)
                    alumnos1.append(segundo_apellido)
                    alumnos1.append(carrera)
                    result1 = self.actionPut(self.app_version,self.file,alumnos1)
                    return json.dumps(result1)
                elif data['action'] == 'delete':
                    matricula = data['matricula']
                    result1 = self.actionDelete(self.app_version,self.file,matricula)
                    return json.dumps(result1)
                elif data['action'] == 'update':
                    matricula = data['matricula']
                    result1 = self.actionDelete(self.app_version,self.file,matricula)
                    return json.dumps(result1)
                else:
                    result = {} 
                    result['app_version'] = self.app_version 
                    result['status'] = "Command not found"
                    return json.dumps(result) 
            else:
                result = {} 
                result['app_version'] = self.app_version 
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            print("Error" + str(e.args(e)))
            result = {}
            result['app_version'] = self.app_version 
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result) 

    @staticmethod
    def actionGet(app_version,file):
        try:
            result = {}  
            result['app_version'] = app_version 
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
            result['app_version'] = app_version
            result['status'] = "Error " 
            return result 


#METODO PARA HACER LA BUSQUEDA
    @staticmethod
    def actionSearch(app_version,file,matricula):
        try:
            result = {}  
            result['app_version'] = app_version 
            result['status'] = "200 ok"
                
            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile)  
                alumnos = []  
                for row in reader:  
                    if (row['matricula'] == matricula):
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
            result['app_version'] = app_version 
            print("Error {}".format(e.args))
            result['status'] = "Error " 
            return result 

#PONER DATOS EN UN NUEVO REGISTRO
    @staticmethod
    def actionPut(app_version, file, alumnos1):
        try:
            result = {}  
            result['app_version'] = app_version 
            result['status'] = "200 ok"

            with open(file, 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(alumnos1)
                
            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile)  
                alumnoss1 = []  
                for row in reader: 
                    fila1 = {}   
                    fila1['matricula'] = row['matricula']  
                    fila1['nombre'] = row['nombre']  
                    fila1['primer_apellido'] = row['primer_apellido'] 
                    fila1['segundo_apellido'] = row['segundo_apellido'] 
                    fila1['carrera'] = row['carrera'] 
                    alumnoss1.append(fila1) 
                result['alumnoss1'] = alumnoss1
            return result
        except Exception as e:
            result = {} 
            result['app_version'] = app_version 
            print("Error {}".format(e.args))
            result['status'] = "Error " 
            return result 
    
    @staticmethod
    def actionDelete(app_version, file, matricula):
        try:
            result = {}  
            result['app_version'] = app_version 
            result['status'] = "200 Ok"

            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile) 
                alumnos = []  
                for row in reader:  
                    if (row['matricula'] != matricula):
                        alumnos.append(row)
                        result['alumnos'] = row
            tam = (len(alumnos))
            with open(file, 'w', newline='') as csvfile:  
                writer = csv.writer(csvfile) 
                alumnos1 = []  
                alumnos1.append("matricula")
                alumnos1.append("nombre")
                alumnos1.append("primer_apellido")
                alumnos1.append("segundo_apellido")
                alumnos1.append("carrera")
                writer.writerow(alumnos1)
                data=[]
                for x in range (0,tam):
                    data.append(alumnos[x]['matricula'])
                    data.append(alumnos[x]['nombre'])
                    data.append(alumnos[x]['primer_apellido'])
                    data.append(alumnos[x]['segundo_apellido'])
                    data.append(alumnos[x]['carrera'])
                    writer.writerow(data)
                    data=[]

            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile) 
                for row in reader:
                    alumnos.append(row)
                    result['alumnos'] = alumnos
            return result
        except Exception as e:
            result = {} 
            print("Error {}".format(e.args))
            result['status'] = "Error " 
            return result 
    
    @staticmethod
    def actionUpdate(app_version, file, matricula):
        try:
            result = {}  
            result['app_version'] = app_version 
            result['status'] = "200 Ok"
            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile)  
                alumnos = []  
                for row in reader:  
                    if (row['matricula'] == matricula):
                        fila = {}  
                        fila['matricula'] = row['matricula']  
                        fila['nombre'] = row['nombre']  
                        fila['primer_apellido'] = row['primer_apellido'] 
                        fila['segundo_apellido'] = row['segundo_apellido'] 
                        fila['carrera'] = row['carrera'] 
                        alumnos.append(fila) 
                    result['alumnos'] = alumnoss
            tam = (len(alumnos))
            with open(file, 'w', newline='') as csvfile:  
                writer = csv.writer(csvfile) 
                alumnos1 = []  
                alumnos1.append("matricula")
                alumnos1.append("nombre")
                alumnos1.append("primer_apellido")
                alumnos1.append("segundo_apellido")
                alumnos1.append("carrera")
                writer.writerow(alumnos1)
                data=[]
                for x in range (0,tam):
                    data.append(alumnos[x]['matricula'])
                    data.append(alumnos[x]['nombre'])
                    data.append(alumnos[x]['primer_apellido'])
                    data.append(alumnos[x]['segundo_apellido'])
                    data.append(alumnos[x]['carrera'])
                    writer.writerow(data)
                    data=[]

            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile) 
                for row in reader:
                    alumnos.append(row)
                    result['alumnos'] = alumnos
            return result
            with open(file, 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(alumnos1)
                
            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile)  
                alumnoss1 = []  
                for row in reader: 
                    fila1 = {}   
                    fila1['matricula'] = row['matricula']  
                    fila1['nombre'] = row['nombre']  
                    fila1['primer_apellido'] = row['primer_apellido'] 
                    fila1['segundo_apellido'] = row['segundo_apellido'] 
                    fila1['carrera'] = row['carrera'] 
                    alumnoss1.append(fila1) 
                result['alumnoss1'] = alumnoss1
            return result
        except Exception as e:
            result = {} 
            print("Error {}".format(e.args))
            result['status'] = "Error " 
            return result 
    
