# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#Criando o Bot
bot = ChatBot('Fernando-Bot')

conversaIntroducao = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'tudo bem com você?', 'sim e você?', 'eu estou bem']
conversaFilmes = ['qual é seu filme favorito?', 'meu filme favorito é os vingadores']

#Método de Treinamento
bot.set_trainer(ListTrainer)
bot.train(conversaIntroducao)
bot.train(conversaFilmes)

while True:
    quest = input("Você: ")
    resposta = bot.get_response(quest)

    # Confiança do Bot
    if float(resposta.confidence) > 0.5:
        print("Bot: ", resposta)
    else:
        print("Bot: Não entendi")
