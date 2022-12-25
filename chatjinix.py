# -*- coding: utf-8 -*-
from chatterbot_corpus import ListTrainer

from chatterbot_corpus import ChatBot

Jixbot = ChatBot("Dinix")

conversa1 = ['oi','olá','tudo bem?', 'tudo bem e você?', 'estou òtimo']

treinar = ListTrainer(Jixbot)

treinar.train(conversa1)

while True:
    try:
        questao = input('Você: ')
        if questao == "sair":
            break
        resposta = Jixbot.get_response(questao)
        print('Dinix: ', resposta)
    except (KeyboardInterrupt, SystemExit):
        print("Apertou Ctrl+C")
        break