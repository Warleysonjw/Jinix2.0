# -*- coding: utf-8 -*-
from chatterbot_corpus import ListTrainer

from chatterbot_corpus import ChatBot

AMGbot = ChatBot("Dinix")

conversa1 = ['oi','olá','tudo bem?', 'tudo bem e você?', 'estou òtimo']
conversa2 = ['bom dia diniz','bom dia mestre bom dia gg','como você esta?', 'estou bem muito obrigada']

treinar = ListTrainer(AMGbot)

treinar.train(conversa1)
treinar.train(conversa2)

while True:
    try:
        questao = input('Você: ')
        if questao == "sair":
            break
        resposta = AMGbot.get_responde(questao)
        print('Dinix: ', resposta)
    except (KeyboardInterrupt, SystemExit):
        print("Apertou Ctrl+C")
        break