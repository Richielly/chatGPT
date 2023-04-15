from api_key import API_KEY
import requests
import json

#link para acesso aos modelos da API
link_1 = 'https://api.openai.com/v1/models'

# url que dá acesso a interação com o chat de conversa
link_2 = 'https://api.openai.com/v1/chat/completions'



#Chamada do tipo get para listar os modelos existentes
def modelos_gpt():
    # Header com a chave API que precisa ser gerada na OpenIA e tipo de conteudo da requisição
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    requisicao_1 = requests.get(link_1, headers=headers)
    print(requisicao_1) #status da chamada
    print(requisicao_1.text) #Lista de modelos

#modelos que podem ser utilizados que foram encontrados na função acima
id_modelo = 'gpt-3.5-turbo'
id_modelo_2 ='gpt-3.5-turbo-0301'
id_modelo_4 = 'gpt-4'


def talk(question):

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    #Corpo da mensagem com informações minimas obrigaórias para uma interação simples
    body_mensagem = { "model": f"{id_modelo}",
                  "messages": [{"role": "user", "content": f"{question}"}]
                }

    #Transformação da mensagem para formato Json para envio da solicitação
    body_mensagem = json.dumps(body_mensagem)

    #criação da requisição agora do tipo poste para receber o retorno com a resposta da IA
    requisicao_2 = requests.post(link_2, headers=headers, data=body_mensagem)

    resposta = requisicao_2.json()
    #Se a chamada não tiver status [200] ele retorna a mensagem que ocasionou o erro.
    if not requisicao_2.ok:
        resposta = resposta["error"]
        resposta = resposta['message'] + '\n' + resposta['type']
    else:
        print(requisicao_2.text)
        resposta = resposta['choices'][0]['message']['content']

    return resposta
