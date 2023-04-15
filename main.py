from bottle import get, post, route, run, debug, template, request, static_file, error
import call as cl
import datetime as dt

@post('/')
def response():
    # API_KEY = cl.modelos_gpt(request.forms.get("API_KEY"))
    # print(API_KEY)
    pergunta = ''
    if (request.forms.get("pergunta") != ''):
        pergunta = request.forms.get("pergunta")
        resposta = cl.talk(request.forms.get("pergunta"))
    else: resposta = 'Me faça uma pergunta...'
    hora = dt.datetime.now()
    hora = hora.strftime('%A %d %B %Y %I:%M')

    print(resposta)

    return template('template/index2', resposta=resposta, pergunta=pergunta, hora=hora)

@route('/')
def index():
    pergunta = request.forms.get("pergunta")
    resposta = request.forms.get("pergunta")
    hora = dt.datetime.now()
    hora = hora.strftime('%A %d %B %Y %I:%M')
    return template('template/index2', resposta=resposta, pergunta=pergunta, hora=hora)

run(port=2424, reloader=True)

# pyinstaller --name export_unifica_frotas --onefile --noconsole main.py