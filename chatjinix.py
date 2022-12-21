from chatterbot import ListTrainer

from chatterbot import ChatBot

AMGbot = ChatBot("Dinix")

conversa1 = ['oi','olá','tudo bem?', 'tudo bem e você?', 'estou òtimo']
conversa2 = ['bom dia dinix','bom dia mestre bom dia gg','como vão?', 'vamos bem']

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