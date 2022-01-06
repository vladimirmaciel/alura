from collections import Counter

# Testando uso de diversas coleções
texto1 = """
Se você iniciou há pouco tempo sua jornada no mundo do desenvolvimento, provavelmente em algum momento se deparou com os famosos testes de software, ou mesmo percebeu que dentre as exigências para vagas em muitas empresas estão presentes algumas tecnologias de testes. Existem diferentes tipos de testes e é isso que vamos discutir neste artigo!

Tornou-se padrão que empresas busquem testar seus produtos em diferentes etapas do desenvolvimento até a entrega ao usuário final, devido às vantagens que os testes nos trazem, possibilitando a identificação de erros e garantindo a confiabilidade no uso do software, que deve ser um produto com qualidade de funcionamento.

Então sabendo do quão importantes são os testes e de como as empresas hoje buscam utilizá-los em diversas etapas da criação do software, nos vem a pergunta: quais são os tipos de testes?


"""


texto2 = """ O Marketing Digital utiliza estratégias para que um produto ou serviço seja encontrado pelas pessoas através de canais digitais. Ou seja, são estratégias e ações realizadas na internet: em sites, e-mails ou mídias sociais.

Por que o Marketing Digital é importante? O mundo mudou e hoje a internet é o principal meio de comunicação, por isso, uma empresa que não está na internet e/ou não realiza ações de marketing dentro dela, não aparece e, consequentemente, não vende.

Por que devo estudar Marketing Digital?

A internet trouxe diversos novos desafios para profissionais de marketing, sendo eles: o Inbound Marketing, mídias sociais, marketing de conteúdo, anúncios online e muito mais. Por isso, é importante dominar esses assuntos para que você se destaque no mercado de trabalho e consiga criar ótimas estratégias e ações para alavancar os resultados de sua empresa.
"""


def analisa_frequencia_de_letras(texto):
    conta_letras1 = Counter(texto.lower())
    soma_todos_caracteres = sum(conta_letras1.values())
    # print(conta_letras1, soma_todos_caracteres, "Caracteres")
    x = [
        # List Comprehension
        (letra, frequencia / soma_todos_caracteres)
        for letra, frequencia in conta_letras1.items()
    ]

    proporcoes = Counter(dict(x))

    # print(proporcoes)
    # pega os 10 mais comuns
    mais_comuns = proporcoes.most_common(10)
    for caracter, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caracter, proporcao * 100))


analisa_frequencia_de_letras(texto2)
analisa_frequencia_de_letras(texto1)
