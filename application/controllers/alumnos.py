importar  web   # pip instalar web.py
importar  csv   # analizador CSV
importar  json   # analizador json

'' '
    Controlador Alumnos que es invocado cuando el usuario ingresa a la 
    URL: http: // localhost: 8080 / alumnos? Action = get & token = 1234
'' '


 Alumnos de clase :

    app_version  =  "0.02"   # versión de la aplicación web
    file  =  'static / csv / alumnos.csv'   # define el archivo donde se almacenan los datos

    def  __init__ ( self ):   # Método inicial o constructor de la clase
        pase   # Simplemente continua con la ejecución

    def  GET ( auto ):
        prueba :
            datos  =  web . input ()   # recibe los datos por la url
            if  data [ 'token' ] ==  "1234" :   # validar el token que se recibe por url
                if  data [ 'action' ] ==  'get' :   # evaluar la acción a realizar
                    resultado  =  auto . actionGet ( self . app_version , self . file )   # llama al metodo actionGet (), y almacena el resultado
                    vuelve  json . vuelcos ( resultado )   # Parsea el diccionario resultado a formato json
                más :
                    resultado  = {}   # crear diccionario vacio
                    resultado [ 'app_version' ] =  self . app_version   # version de la webapp
                    result [ 'status' ] =  "Comando no encontrado"
                    vuelve  json . vuelcos ( resultado )   # Parsea el diccionario resultado a formato json
            más :
                resultado  = {}   # crear diccionario vacio
                resultado [ 'app_version' ] =  self . app_version   # version de la webapp
                result [ 'status' ] =  "Token inválido"
                vuelve  json . vuelcos ( resultado )   # Parsea el diccionario resultado a formato json
        excepto  Excepción  como  e :
            print ( "Error" )
            resultado  = {}   # crear diccionario vacio
            resultado [ 'app_version' ] =  self . app_version   # version de la webapp
            result [ 'status' ] =  "Faltan valores, sintaxis: alumnos? action = get & token = XXXX"
            vuelve  json . vuelcos ( resultado )   # Parsea el diccionario resultado a formato json

    @ método estático
    def  actionGet ( aplicación_versión , archivo ):
        prueba :
            resultado  = {}   # crear diccionario vacio
            result [ 'app_version' ] =  app_version   # version de la webapp
            result [ 'status' ] =  "200 ok"   # mensaje de status
            
            con  open ( file , 'r' ) como  csvfile :   # abre el archivo en modo lectura
                lector  =  csv . DictReader ( csvfile )   # toma la 1er fila para los nombres
                alumnos  = []   # matriz para todos los alumnos
                para  fila  en  lector :   # grabar el archivo CSV fila por fila
                    fila  = {}   # Genera un diccionario por cada registro en el csv
                    fila [ 'matricula' ] =  fila [ 'matricula' ]   # obtiene la matricula y la agrega al diccionario
                    fila [ 'nombre' ] =  fila [ 'nombre' ]   # opcióne el nombre y lo agrega al diccionario
                    fila [ 'primer_a Apellidos' ] =  fila [ 'primer_un apellido' ]   # optiene el primer_un apellido
                    fila [ 'segundo_a Apellidos' ] =  fila [ 'segundo_a Apellidos' ]   # optiene el segundo apellido
                    fila [ 'carrera' ] =  fila [ 'carrera' ]   # obtiene la carrera
                    alumnos . append ( fila )   # agrega el diccionario generador al array alumnos
                resultado [ 'alumnos' ] =  alumnos   # agrega el conjunto alumnos al diccionario resultado
             resultado   devuelto # Regresa el diccionario generador
        excepto  Excepción  como  e :
            resultado  = {}   # crear diccionario vacio
            print ( "Error {}" . format ( e . args ()))
            result [ 'app_version' ] =  app_version   # version de la webapp
            result [ 'status' ] =  "Error"   # mensaje de status
             resultado   devuelto # Regresa el diccionario generador

