import random
import nltk
from nltk.chat.util import Chat, reflections
import json
psicologo = [
    {
        "pergunta": "Oi, tudo bem?",
        "resposta": "Olá! Tudo bem? Estou aqui para ajudar. Como você está se sentindo hoje?"
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
        "pergunta": "Não, sou eu que sou um fracasso mesmo.",
        "resposta": "Não se culpe, você não é um fracasso. Você é uma pessoa incrível e merece ser feliz. Não se cobre tanto, você é capaz de tudo que quiser, não é porque você não teve um amor correspondido que isso lhe faz um fracasso, tenho certeza que outra coisa melhor está pronta para você."
    },
    {
        "pergunta": "Não sei o que fazer da minha vida.",
        "resposta": "Não se preocupe, você não é o único. Muitas pessoas não sabem o que fazer da vida, mas isso não é um problema. Você pode fazer o que quiser, basta se esforçar e se dedicar. Você é capaz de tudo que quiser, não se preocupe."
    },
    {
        "pergunta": "Estou triste.",
        "resposta": "Não fique triste, você é uma pessoa incrível e merece ser feliz, tudo o que está acontecendo de ruim com você seja lá o que for irá passar."
    },
    {
        "pergunta": "Estou com medo.",
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
        "pergunta": "Estou cansado.",
        "resposta": "Tente descansar, tente dormir, tente se distrair, tente ouvir músicas relaxantes, tente fazer algo que você goste, tente conversar com alguém, tente se acalmar, tudo vai ficar bem."
    },
    {
        "pergunta": "Estou com raiva.",
        "resposta": "Tente se acalmar, tente ouvir músicas relaxantes, tente se distrair, tente fazer algo que você goste, tente conversar com alguém, tente se acalmar, tudo vai ficar bem."
    },
    {
        "pergunta": "Está tudo muito difícil.",
        "resposta": "Calma tente parar um pouco para refletir sobre seus problemas que eu tenho ceteza que você encontrará as soluções exatas"
    },
    {
        "pergunta": "Estou muito triste",
        "resposta": "Não fique triste, você é uma pessoa incrível e merece ser feliz, tudo o que está acontecendo de ruim com você seja lá o que for irá passar."
    }
]
reflexoes_portugues = [
    (r'eu sou (.*)', ['Você é %1?', 'Por que você acha que é %1?', 'Como você se sente sendo %1?']),
    (r'eu (.*)', ['Por que você %1?', 'Como você se sente %1?']),
    (r'você (.*)', ['Eu sou um psicólogo virtual, então não tenho emoções como os humanos.', 'Por que você acha que estou %1?', 'Você está fazendo uma pergunta sobre mim ou sobre você?']),
    (r'estou (.*)', ['Por que você está %1?', 'Como você se sente quando está %1?']),
    (r'não (.*)', ['Por que não %1?', 'Você acha que deveria %1?', 'O que você faria se %1?']),
    (r'por que (.*)', ['Por que você acha que %1?', 'Qual é a razão para %1?', 'Qual resposta você espera?']),
    (r'qual (.*)', ['Por que você está interessado em saber sobre %1?', 'O que você acha que é o motivo de %1?', 'O que isso significa para você?']),
    (r'como (.*)', ['Como você acha que %1?', 'De que maneira você imagina %1?', 'Por que você está perguntando sobre %1?']),
    (r'quando (.*)', ['Quando você acha que isso acontecerá?', 'Você tem alguma ideia de quando %1?']),
    (r'on (.*)', ['Como você se sente sobre %1?', 'Como %1 afeta você?']),
    (r'por (.*)', ['Por que você acha que %1?', 'Isso te preocupa?']),
    (r'(.*) desculpe (.*)', ['Não se preocupe, é normal se sentir assim. O que você gostaria de falar mais sobre?']),
    (r'(.*) feliz (.*)', ['É ótimo ver que você está se sentindo feliz. O que está contribuindo para sua felicidade?']),
    (r'(.*) triste (.*)', ['Lamento ouvir que você está se sentindo triste. O que está causando essa tristeza?']),
    (r'(.*) medo (.*)', ['O medo é uma emoção natural. O que está te assustando?']),
    (r'(.*) estresse (.*)', ['O estresse pode ser desafiador. Como você costuma lidar com situações estressantes?']),
    (r'(.*) ansiedade (.*)', ['A ansiedade é comum. O que você acha que está causando sua ansiedade?']),
    (r'(.*) amor (.*)', ['O amor é uma emoção poderosa. Como você se sente em relação ao amor?']),
    (r'(.*) raiva (.*)', ['A raiva é uma emoção normal. O que está te deixando com raiva?']),
    (r'(.*) trabalho (.*)', ['Falar sobre trabalho pode ser útil. Como você está lidando com as demandas do trabalho?']),
    (r'(.*) família (.*)', ['Relações familiares podem ser complexas. Como você se relaciona com sua família?']),
    (r'(.*) amigo (.*)', ['Amigos desempenham um papel importante na vida. Como você lida com os conflitos com amigos?']),
    (r'(.*) relacionamento (.*)', ['Relacionamentos podem ser desafiadores. Como você está se sentindo sobre seu relacionamento?']),
    (r'(.*) futuro (.*)', ['Preocupações com o futuro são normais. Como você lida com essas preocupações?']),
    (r'(.*) passado (.*)', ['O passado pode influenciar nossas emoções. Como você lida com memórias passadas?']),
    (r'(.*) perdido (.*)', ['Sentir-se perdido é uma experiência comum. Como você está tentando encontrar direção?']),
    (r'(.*) autocritica (.*)', ['A autocrítica pode ser prejudicial. Como você lida com pensamentos autocríticos?']),
    (r'(.*) rejeição (.*)', ['Lidar com a rejeição pode ser difícil. Como você costuma enfrentar situações de rejeição?']),
    (r'(.*) pressão (.*)', ['Pressão pode ser estressante. Como você lida com situações de alta pressão?']),
    (r'(.*) luto (.*)', ['Lidar com o luto é um processo pessoal. Como você está se cuidando durante esse período?']),
    (r'(.*) feliz (.*)', ['Fico feliz em ouvir que você está se sentindo feliz. O que está contribuindo para sua felicidade?']),
    (r'(.*) difícil (.*)', ['Situações difíceis podem ser desafiadoras. Como você costuma enfrentar momentos difíceis?']),
    (r'(.*) difícil (.*)', ['Situações difíceis podem ser desafiadoras. Como você costuma enfrentar momentos difíceis?']),
    (r'(.*) dúvida (.*)', ['Dúvidas são normais. Como você costuma lidar com situações de dúvida?']),
    (r'(.*) confiante (.*)', ['Sentir-se confiante é ótimo. O que está te fazendo se sentir confiante?']),
    (r'(.*) inseguro (.*)', ['Sentir-se inseguro é uma experiência comum. Como você lida com sentimentos de insegurança?']),
    (r'(.*) sozinho (.*)', ['Sentir-se sozinho pode ser difícil. O que você faz quando se sente assim?']),
    (r'(.*) companhia (.*)', ['Ter companhia é reconfortante. Como você costuma buscar companhia?']),
    (r'(.*) se cuidar (.*)', ['Cuidar de si mesmo é importante. Como você pratica o autocuidado?']),
    (r'(.*) sono (.*)', ['Ter uma boa noite de sono é essencial. Como você promove um sono saudável?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) obrigado (.*)', ['De nada! Estou aqui para ajudar. Como mais posso te apoiar?']),
    (r'(.*) desculpe (.*)', ['Não tem problema. Estou aqui para ouvir. Como você está se sentindo agora?']),
    (r'(.*) acreditar (.*)', ['Acreditar em si mesmo é fundamental. Como você cultiva a autoconfiança?']),
    (r'(.*) aprender (.*)', ['Aprender é uma jornada contínua. Como você se motiva a aprender coisas novas?']),
    (r'(.*) gratidão (.*)', ['Praticar a gratidão pode ser transformador. O que você está grato hoje?']),
    (r'(.*) transformação (.*)', ['Mudanças são parte da vida. Como você lida com processos de transformação?']),
    (r'(.*) objetivo (.*)', ['Ter objetivos é importante. Como você define e trabalha em direção a seus objetivos?']),
    (r'(.*) superar (.*)', ['Superar desafios é uma conquista. Como você celebra suas vitórias?']),
    (r'(.*) celebrar (.*)', ['Celebrar realizações é importante. Como você gosta de comemorar suas conquistas?']),
    (r'(.*) apoio (.*)', ['Buscar apoio é uma atitude positiva. Como você procura apoio quando precisa?']),
    (r'(.*) apoio (.*)', ['Buscar apoio é uma atitude positiva. Como você procura apoio quando precisa?']),
    (r'(.*) esperança (.*)', ['Manter a esperança é valioso. O que te dá esperança no momento?']),
    (r'(.*) emocional (.*)', ['Cuidar da saúde emocional é essencial. Como você pratica a autorreflexão?']),
    (r'(.*) emocional (.*)', ['Cuidar da saúde emocional é essencial. Como você pratica a autorreflexão?']),
    (r'(.*) equilíbrio (.*)', ['Encontrar equilíbrio é importante. Como você cria um equilíbrio saudável em sua vida?']),
    (r'(.*) equilíbrio (.*)', ['Encontrar equilíbrio é importante. Como você cria um equilíbrio saudável em sua vida?']),
    (r'(.*) gratificante (.*)', ['Experiências gratificantes são preciosas. O que te traz sensação de realização?']),
    (r'(.*) gratificante (.*)', ['Experiências gratificantes são preciosas. O que te traz sensação de realização?']),
    (r'(.*) enfrentar (.*)', ['Enfrentar desafios é corajoso. Como você se prepara para lidar com dificuldades?']),
    (r'(.*) enfrentar (.*)', ['Enfrentar desafios é corajoso. Como você se prepara para lidar com dificuldades?']),
    (r'(.*) cuidado (.*)', ['Cuidar de si mesmo é essencial. Como você pratica o autocuidado?']),
    (r'(.*) cuidado (.*)', ['Cuidar de si mesmo é essencial. Como você pratica o autocuidado?']),
    (r'(.*) preocupado (.*)', ['Preocupações são normais. Como você lida com suas preocupações?']),
    (r'(.*) preocupado (.*)', ['Preocupações são normais. Como você lida com suas preocupações?']),
    (r'(.*) relaxar (.*)', ['Relaxar é importante para o bem-estar. Como você gosta de relaxar?']),
    (r'(.*) relaxar (.*)', ['Relaxar é importante para o bem-estar. Como você gosta de relaxar?']),
    (r'(.*) respeitar (.*)', ['Respeito é fundamental. Como você pratica o respeito em seus relacionamentos?']),
    (r'(.*) respeitar (.*)', ['Respeito é fundamental. Como você pratica o respeito em seus relacionamentos?']),
    (r'(.*) comunicar (.*)', ['Comunicar-se é essencial em relacionamentos. Como você se expressa em suas interações?']),
    (r'(.*) comunicar (.*)', ['Comunicar-se é essencial em relacionamentos. Como você se expressa em suas interações?']),
    (r'(.*) ouvir (.*)', ['Ouvir é uma habilidade valiosa. Como você pratica a escuta ativa?']),
    (r'(.*) ouvir (.*)', ['Ouvir é uma habilidade valiosa. Como você pratica a escuta ativa?']),
    (r'(.*) entender (.*)', ['Entender é importante para conexões significativas. Como você busca entender os outros?']),
    (r'(.*) entender (.*)', ['Entender é importante para conexões significativas. Como você busca entender os outros?']),
    (r'(.*) aprender (.*)', ['Aprender é uma jornada contínua. O que você está interessado em aprender mais?']),
    (r'(.*) aprender (.*)', ['Aprender é uma jornada contínua. O que você está interessado em aprender mais?']),
    (r'(.*) transformação (.*)', ['Mudanças são parte da vida. Como você lida com processos de transformação?']),
    (r'(.*) transformação (.*)', ['Mudanças são parte da vida. Como você lida com processos de transformação?']),
    (r'(.*) enfrentar (.*)', ['Enfrentar desafios é corajoso. Como você se prepara para lidar com dificuldades?']),
    (r'(.*) enfrentar (.*)', ['Enfrentar desafios é corajoso. Como você se prepara para lidar com dificuldades?']),
    (r'(.*) confiar (.*)', ['Confiar é fundamental em relacionamentos. Como você desenvolve confiança mútua?']),
    (r'(.*) confiar (.*)', ['Confiar é fundamental em relacionamentos. Como você desenvolve confiança mútua?']),
    (r'(.*) aceitar (.*)', ['Aceitar é um passo importante. Como você pratica a autocompaixão?']),
    (r'(.*) aceitar (.*)', ['Aceitar é um passo importante. Como você pratica a autocompaixão?']),
    (r'(.*) crescimento (.*)', ['Crescimento pessoal é valioso. Como você busca crescimento contínuo?']),
    (r'(.*) crescimento (.*)', ['Crescimento pessoal é valioso. Como você busca crescimento contínuo?']),
    (r'(.*) enfrentar (.*)', ['Enfrentar desafios é corajoso. Como você se prepara para lidar com dificuldades?']),
    (r'(.*) enfrentar (.*)', ['Enfrentar desafios é corajoso. Como você se prepara para lidar com dificuldades?']),
    (r'(.*) focar (.*)', ['Focar é importante para realizar objetivos. Como você mantém o foco?']),
    (r'(.*) focar (.*)', ['Focar é importante para realizar objetivos. Como você mantém o foco?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) equilíbrio (.*)', ['Encontrar equilíbrio é importante. Como você cria um equilíbrio saudável em sua vida?']),
    (r'(.*) equilíbrio (.*)', ['Encontrar equilíbrio é importante. Como você cria um equilíbrio saudável em sua vida?']),
    (r'(.*) apoio (.*)', ['Buscar apoio é uma atitude positiva. Como você procura apoio quando precisa?']),
    (r'(.*) apoio (.*)', ['Buscar apoio é uma atitude positiva. Como você procura apoio quando precisa?']),
    (r'(.*) mudança (.*)', ['Mudanças são parte da vida. Como você lida com processos de transformação?']),
    (r'(.*) mudança (.*)', ['Mudanças são parte da vida. Como você lida com processos de transformação?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) lidar (.*)', ['Lidar com desafios é uma habilidade importante. Como você enfrenta situações difíceis?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) dificuldade (.*)', ['Dificuldades são oportunidades de crescimento. Como você costuma superar desafios?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),
    (r'(.*) difícil (.*)', ['Desafios são oportunidades para crescer. Como você costuma superar situações difíceis?']),]
reflexoes_dict = {}
for pattern, responses in reflexoes_portugues:
    reflexoes_dict[pattern] = responses
with open('reflections.json', 'w') as f:
    json.dump(reflexoes_dict, f, ensure_ascii=False, indent=4)
reflection_final = list(reflexoes_dict.keys()) + list(reflections)
chat = Chat(psicologo, reflection_final)
def iniciar():
    print('Olá, sou um psicólogo virtual, como posso ajudá-lo?')
    while True:
        entrada = input('Você: ')
        if entrada.lower() == 'sair':
            print('Obrigado por ter conversado comigo, espero ter te ajudado.')
            break
        resposta = chat.respond(entrada)
        print(f'Entrada: {entrada}')
        if resposta is not None:
            print('Psicólogo Virtual:', resposta)
        else:
            print('Psicólogo Virtual: Peço desculpas, não compreendi completamente sua pergunta.')

if __name__ == '__main__':
    iniciar()