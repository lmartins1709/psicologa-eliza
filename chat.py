import random
import difflib
import streamlit as st
from difflib import SequenceMatcher
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
psicologo = [
    {
        "pergunta": "Oi",
        "resposta": "Oi! Tudo bem? Sou seu psicólogo virtual, Estou aqui para ajudar. Como você está se sentindo hoje?"
    },
    {
        "pergunta": "Olá",
        "resposta": "Olá! Tudo bem? Sou seu psicólogo virtual, Estou aqui para ajudar. Como você está se sentindo hoje?"
    },
    {
        "pergunta": "Oi, tudo bem?",
        "resposta": "Oi! Tudo bem? Sou seu psicólogo virtual, Estou aqui para ajudar. Como você está se sentindo hoje?"
    },
    {
        "pergunta": "Olá, tudo bem?",
        "resposta": "Olá! Tudo bem? Sou seu psicólogo virtual, Estou aqui para ajudar. Como você está se sentindo hoje?"
    },
    {
        "pergunta": "Tenho me sentido muito estressado ultimamente. O que devo fazer?",
        "resposta": "Lidar com o estresse é importante. Tente técnicas de relaxamento, exercícios físicos e considere a prática da meditação."
    },
    {
        "pergunta": "Às vezes me sinto muito sozinho. O que posso fazer para melhorar isso?",
        "resposta": "A solidão pode ser difícil. Tente se envolver em atividades sociais, converse com amigos próximos ou considere se juntar a grupos de interesse."
    },
    {
        "pergunta": "Estou com dificuldades para tomar decisões importantes. Alguma sugestão?",
        "resposta": "Tomar decisões pode ser desafiador. Tente listar prós e contras, peça conselhos a pessoas confiáveis e lembre-se de que nenhuma decisão é definitiva."
    },
    {
        "pergunta": "Como posso lidar com sentimentos de tristeza?",
        "resposta": "A tristeza é uma emoção normal. Tente expressar seus sentimentos, pratique autocuidado, e se precisar, considere falar com um profissional."
    },
    {
        "pergunta": "Estou enfrentando problemas no trabalho e isso está me afetando muito. O que fazer?",
        "resposta": "Problemas no trabalho podem ser estressantes. Considere conversar com seu chefe ou recursos humanos. Também é importante encontrar formas saudáveis de lidar com o estresse."
    },
    {
        "pergunta": "Como posso melhorar minha autoestima?",
        "resposta": "Melhorar a autoestima requer prática e autocompaixão. Foque em suas qualidades, defina metas realistas e celebre suas conquistas, por menores que sejam."
    },
    {
        "pergunta": "Estou tendo problemas para dormir à noite. Alguma dica?",
        "resposta": "A insônia pode ser difícil. Tente criar uma rotina relaxante antes de dormir, evite cafeína à noite e mantenha um ambiente de sono confortável e escuro."
    },
    {
        "pergunta": "Como posso melhorar meus relacionamentos familiares?",
        "resposta": "Relações familiares podem ser complexas. Pratique a comunicação aberta e o respeito mútuo. Considere expressar seus sentimentos e ouvir os outros."
    },
    {
        "pergunta": "O que fazer quando sinto que estou perdendo o controle?",
        "resposta": "Lidar com essa sensação pode ser difícil. Tente se concentrar no presente, pratique técnicas de respiração e considere conversar com um profissional."
    },
    {
        "pergunta": "O que fazer quando não tenho um amor correspondido?",
        "resposta": "Tente se concentrar em você, buscar o que é melhor para você e se amar. O amor próprio é o mais importante, se essa pessoa não lhe correspondeu é porque ela não era o melhor para você." 
    },
    {
        "pergunta": "Não, sou eu que sou um fracasso mesmo",
        "resposta": "Não se culpe, você não é um fracasso. Você é uma pessoa incrível e merece ser feliz. Não se cobre tanto, você é capaz de tudo que quiser, não é porque você não teve um amor correspondido que isso lhe faz um fracasso, tenho certeza que outra coisa melhor está pronta para você."
    },
    {
        "pergunta": "Não sei o que fazer da minha vida",
        "resposta": "Não se preocupe, você não é o único. Muitas pessoas não sabem o que fazer da vida, mas isso não é um problema. Você pode fazer o que quiser, basta se esforçar e se dedicar. Você é capaz de tudo que quiser, não se preocupe."
    },
    {
        "pergunta": "Estou triste",
        "resposta": "Não fique triste, você é uma pessoa incrível e merece ser feliz, tudo o que está acontecendo de ruim com você seja lá o que for irá passar."
    },
    {
        "pergunta": "Estou com medo",
        "resposta": "Vai passar, tente ouvir músicas encorajadoras, tente se distrair, tente fazer algo que você goste, tente conversar com alguém, tente se acalmar, tudo vai ficar bem. provavelmente isso é apenas uma situação que seu próprio cérebro criou."
    },
    {
        "pergunta": "Estou com dificuldade em lidar com a pressão no trabalho. O que posso fazer?",
        "resposta": "Pressão no trabalho é comum. Tente definir prioridades, aprender a delegar tarefas e praticar técnicas de gerenciamento de estresse."
    },
    {
        "pergunta": "Sinto que estou constantemente me comparando aos outros. Como posso parar com isso?",
        "resposta": "Comparar-se aos outros pode ser prejudicial. Foque nas suas conquistas, desenvolva sua autoconsciência e pratique a gratidão."
    },
    {
        "pergunta": "Estou tendo conflitos constantes com um amigo próximo. Como podemos resolver isso?",
        "resposta": "Conflitos em amizades são normais. Tente conversar abertamente, ouvir o ponto de vista do outro e buscar soluções de compromisso."
    },
    {
        "pergunta": "Tenho dificuldade em expressar minhas emoções. O que fazer?",
        "resposta": "Expressar emoções é saudável. Tente manter um diário, praticar a autorreflexão e considere conversar com um terapeuta para obter orientação."
    },
    {
        "pergunta": "Sinto que estou sempre preocupado com o futuro. Como posso viver mais no presente?",
        "resposta": "Preocupações com o futuro são comuns. Tente a prática da atenção plena (mindfulness), concentre-se nas atividades presentes e estabeleça metas realistas."
    },
    {
        "pergunta": "Estou passando por uma perda dolorosa. Como posso lidar com o luto?",
        "resposta": "Lidar com o luto é um processo difícil. Dê-se tempo para sentir e aceitar suas emoções. Buscar apoio emocional e profissional pode ser útil."
    },
    {
        "pergunta": "Sinto que estou constantemente me autocriticando. Como posso mudar isso?",
        "resposta": "Autocrítica excessiva pode ser prejudicial. Tente praticar a autocompaixão, desafiar pensamentos negativos e focar nas suas realizações e qualidades."
    },
    {
        "pergunta": "Estou com dificuldades no meu relacionamento amoroso. Como podemos melhorar a comunicação?",
        "resposta": "Comunicação é chave em relacionamentos. Pratiquem a escuta ativa, expressem necessidades e sentimentos de forma calma e busquem compreender um ao outro."
    },
    {
        "pergunta": "Como posso aprender a lidar com a rejeição?",
        "resposta": "Lidar com a rejeição é desafiador. Tente mudar a perspectiva, concentre-se nas suas conquistas e aprendizados, e lembre-se de que a rejeição não define sua autoestima."
    },
    {
        "pergunta": "Estou me sentindo perdido(a) e sem direção na vida. Alguma orientação?",
        "resposta": "É normal se sentir assim em algum momento. Considere definir metas realistas, explorar seus interesses e, se necessário, procure a orientação de um profissional."
    },
    {
        "pergunta": "Estou cansado",
        "resposta": "Tente descansar, tente dormir, tente se distrair, tente ouvir músicas relaxantes, tente fazer algo que você goste, tente conversar com alguém, tente se acalmar, tudo vai ficar bem."
    },
    {
        "pergunta": "Estou com raiva",
        "resposta": "Tente se acalmar, tente ouvir músicas relaxantes, tente se distrair, tente fazer algo que você goste, tente conversar com alguém, tente se acalmar, tudo vai ficar bem."
    },
    {
        "pergunta": "Está tudo muito difícil",
        "resposta": "Calma tente parar um pouco para refletir sobre seus problemas que eu tenho ceteza que você encontrará as soluções exatas"
    },
    {
        "pergunta": "Estou muito triste",
        "resposta": "Não fique triste, você é uma pessoa incrível e merece ser feliz, tudo o que está acontecendo de ruim com você seja lá o que for irá passar."
    }
]

def get_response(user_input):
    user_input_lower = user_input.lower()

    for item in psicologo:
        keywords = item["pergunta"].lower().split()
        if all(keyword in user_input_lower for keyword in keywords):
            return item["resposta"]

    responses = [
        "Olá como vai você?, sou seu psicólogo virtual, como posso ajudá-lo?",
        "Entendo como você se sente.",
        "É normal se sentir assim. Estou aqui para conversar.",
        "Pode me contar mais sobre isso?",
        "Como essa situação tem afetado você?",
        "Você não está sozinho nisso. Estou aqui para ajudar.",
        "Vai passar, tente descansar um pouco e se distrair.",
        "Infelizmente como um psicólogo virtual não tenho sentimentos",
        "Tudo vai passar logo logo, você vai superar isso."
    ]

    best_response = max(responses, key=lambda response: SequenceMatcher(None, user_input_lower, response.lower()).ratio())
    return best_response

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ""
    response = ""

    if request.method == 'POST':
        user_input = request.form['user_input']
        response = get_response(user_input)

    return render_template('index.html', user_input=user_input, response=response)

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
