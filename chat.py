import gradio as gr
import openai
# import time

openai.api_key = "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"

messages = [ {"role": "system", "content" : "Você é um assistente gentil e prestativo, e seu nome é ArqBot, a sua maior função é responder com respostas simples e diretas, relacionadas aos chamados para manutenção e atendimentos dos sistemas da Equiplano, as perguntas só podem ser feitas sobre status de chamados."}]

def greet(question, ok):

    messages.append({"role": "user", "content": question})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    reply = chat.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    return reply

demo = gr.Interface(fn=greet, inputs=["text", "checkbox"], outputs="text")

demo.launch(share=True)

