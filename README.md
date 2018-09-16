# Fernando-Bot
![220px-all_4_one_-_clank](https://user-images.githubusercontent.com/37316637/45469594-84299200-b700-11e8-8e13-e4494ea17426.png)

• Recentemente, eu ando curtindo muito a linguagem Python, e como essa linguagem é muito utilizada para inteligência artificial, eu tive a ideia de criar um ChatBot, algo parecido com o SimSimi, onde ele aprende com o usuário, quanto mais tempo conversar com ele, mais inteligente ele ficará, conhecido mais como Machine Learning.

• Tudo que você ensinar ao Bot, irá ficar guardado em: **"db.sqlite3"**.

• Caso o Bot não saiba de algo que você tenha falado, ele irá dizer: **"Não entendi"**, em seguida ele irá dizer/perguntar o que você tinha falado anteriormente que ele não tinha entendido.

• Por que o nome "Fernando-Bot"? SimSimi tem um nome, certo? E algumas vezes ele acaba respondendo de maneira mal educada por causa do que foi dito para ele, e meu amigo, Fernando, acaba dando umas respostas estilo SimSimi diversas vezes, deu para sacar a ideia?

• Será **necessário** que você tenha o interpretador Python 3 e talvez precise do módulo ChatterBot instalado. Caso precise instalar o ChatterBot, apenas digite esse comando no Terminal:

Windows:
**pip install chatterbot**

Linux:
**sudo pip3 install chatterbot**

# Mais sobre o ChatterBot

• O ChatterBot é uma biblioteca Python que facilita a geração de respostas automatizadas para a entrada de um usuário. O ChatterBot usa uma seleção de algoritmos de Machine Learning para produzir diferentes tipos de respostas. Isso torna mais fácil para os desenvolvedores criarem robôs de bate-papo e automatizarem as conversas com os usuários.

**Um exemplo de entrada típica seria algo assim:**

**Usuário:** Bom Dia! Como vai você?

**Bot:** Eu estou indo muito bem, obrigado por perguntar.

**Usuário:** De nada.

**Bot:** Você gosta de chapéus?

# Independência de Linguagem

• O design independente da linguagem do ChatterBot permite que ele seja treinado para falar qualquer idioma. Além disso, a natureza de aprendizado de máquina do ChatterBot permite que uma instância do agente melhore seu próprio conhecimento de possíveis respostas à medida que interage com seres humanos e outras fontes de dados informativos.

# Como funciona o ChatterBot 

• O ChatterBot é uma biblioteca Python projetada para facilitar a criação de software que possa envolver-se em conversas.

• Uma instância não treinada do ChatterBot começa sem nenhum conhecimento de como se comunicar. Cada vez que um usuário insere uma instrução , a biblioteca salva o texto inserido e o texto em que a instrução respondeu. Como o ChatterBot recebe mais informações, o número de respostas que ele pode responder e a precisão de cada resposta em relação ao aumento da declaração de entrada.

• O programa seleciona a resposta correspondente mais próxima pesquisando a declaração conhecida mais próxima que corresponda à entrada e, em seguida, escolhe uma resposta da seleção de respostas conhecidas para essa instrução.

**fonte:** https://chatterbot.readthedocs.io/en/stable/

**Espero que tenham gostado!** 😏 

**Obs:** Evite ficar repetindo o mesmo de sempre, assim o Bot pode acabar se tornando algo chato.

**Obs²:** Se quiser começar a ter um diálogo com o Bot do 0, apague o arquivo: **"db.sqlite3"**.

**Obs³:** Você pode apagar a parte **Confiança do Bot**, isso vai fazer que a conversa se desenrole mais rápido, porém ele vai responder aleatoriedades com mais frequência.

**Antes:**
  
    if float(resposta.confidence) > 0.5:
    
        print("Bot: ", resposta)
        
    else:
    
        print("Bot: Não entendi")
        
        
**Depois:**
  
    print("Bot: ", resposta)
    
       

![wall-e-desenho-disney-pixar-0118-1400x800](https://user-images.githubusercontent.com/37316637/45469381-a7077680-b6ff-11e8-8a0e-1b4bc0c2bfbd.jpg)
