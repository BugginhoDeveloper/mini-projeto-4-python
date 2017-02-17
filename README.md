# MINI PROJETO 4

A ideia desse desafio é estimular o estudo de novas tecnologias e acabar ou pelo menos diminuir o preconceito que muitos têm com a linguagem **Python**.

----------

Linguagem Python
--------

**Python** ([https://www.python.org/][1]) Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a implementação CPython.

A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.

Python é utilizada em diversos projetos como:

- **Globo.com** (Um dos maiores portais de notícias e entretenimento da web brasileira);
- **Netflix** (Maior provedora de filmes e séries de televisão via streaming do mundo);
- **Youtube** (Apesar de não ser inteiramente construído em Python o Google utiliza Python em diversos projetos inclusive na ferramenta de busca do Youtube);
- **Gimp** (Poderoso editor de imagens muito conhecido no ambiente LINUX);
- **Blender** (Software de modelagem 3D muito poderoso e utilizado até mesmo por grandes produtoras de cinema);
- **Sublime Text** (Um dos mais populares editores de texto para programadores);

Confira também o [Manual da linguagem][2]

----------

Desafio
--------

Crie um aplicativo console que simule o funcionamento básico de um caixa eletrônico. 

O aplicativo deverá:

- Solicitar do usuário sua agência, conta, e senha para que o mesmo possa utilizar o aplicativo;
- Solicitar do usuário qual operação o mesmo quer realizar:
  - Consultar o seu saldo
  - Emitir um extrado (histórico das transações, em tela)
  - Depositar um valor na própria conta
  - Depositar um valor em outra conta
  - Sacar um determinado valor (No máximo 1000 reais por operação, desde que não ultrapasse o seu saldo. Apenas cédulas de 20, 50 e 100 reais estarão disponíveis)
  - Tranferir um valor de sua conta para outra conta (Desde que não ultrapasse o seu saldo)

> **Observações:**

> - Persistir os dados em um banco sqlite
> - Durante o saque, quando o usuário informar o valor a ser sacado, informe-o as opções de cédulas disponíveis para que ele escolha o que melhor atende a sua necessidade. Exemplo, se o usuário sacar 120 reais o sistemas deverá dar a ele as seguintes opções:
  - 1) 1 cédula de 100 e 1 cédula de 20;
  - 2) 2 cédulas de 50 e 1 cédula de 20;
  - 3) 6 cédulas de 20
> - Não existe prazo limite para conclusão, a ideia é que você tenha uma experiência diferente.
> - Você poderá tirar suas dúvidas no [Slack do Desafio][3]
> - Ao finalizar o seu projeto, publique-o no Github e envie o link para bugginhodeveloper@gmail.com

----------

Quem já enviou?
--------

Confira abaixo uma lista com todos os amiguinhos que já concluíram o desafio:

- Hugo Peres (https://github.com/hugueds/mini-projeto-4-python)
- Jorgel Luiz (https://github.com/theFullStacker/Sistema-Bancario-python)
- Marcell Guilherme (https://github.com/Mazuh/BugginhoDeveloper-Mini-Projects/tree/master/project_4_python)

[1]: https://www.python.org/
[2]: https://www.python.org/doc/
[3]: https://bugginhominiprojetos.slack.com/
