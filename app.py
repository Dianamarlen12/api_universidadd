import web #pip install web.py
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')


urls = ( #Parentesis tuplas
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals()) #Configurar aplicacion, glo: variables en sesiones

#render = web.template.render('templates')


if __name__ == "__main__":
    web.config.debug = True
    app.run() #Ejecucion del servidor 

