import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    soma = 0
    for i in range(len(as_a)):
        soma += abs(as_a[i] - as_b[i])
    return soma/6

def calcula_assinatura(texto):
    sent = separa_sentencas(texto)
    carac = 0
    
    frase = []
    for i in range(len(sent)):
        f = separa_frases(sent[i])
        frase.append(f)
        carac += len(sent[i])

    pal = []
    n_fra = 0
    carac_f = 0
    for i in range(len(frase)):
        for j in range(len(frase[i])):
            p = separa_palavras(frase[i][j])
            pal.append(p)
            n_fra += 1
            carac_f += len(frase[i][j])
    aux = []
    for i in range(len(pal)):
        for j in range(len(pal[i])):
            aux.append(pal[i][j])
    pal = aux[:]

    soma_pal = 0
    for i in range(len(pal)):
        soma_pal += len(pal[i])
    tam = soma_pal/len(pal)  # Tamanho medio de palavras

    dif = n_palavras_diferentes(pal)
    token = dif/len(pal)  # Type-token

    unica = n_palavras_unicas(pal)
    hapax = unica/len(pal)  # Hapax Legomana

    tam_sent = carac/len(sent)  # Tamanho médio sentença

    comp = n_fra/len(sent)  # Complexidade

    tam_fra = carac_f/n_fra  # Tamanho médio frase

    return [tam, token, hapax, tam_sent, comp, tam_fra]

def avalia_textos(textos, ass_cp):
    assinaturas = []
    for i in range(len(textos)):
        assinaturas.append(calcula_assinatura(textos[i]))

    coef = []
    for i in assinaturas:
        coef.append(compara_assinatura(ass_cp, i))
        
    menor = coef[0]
    num = 0
    for i in range(len(coef)):
        if(coef[i] < menor):
            menor = coef[i]
            num = i
    return num+1

def main():
    assinatura = le_assinatura()
    texto = le_textos()
    autor = avalia_textos(texto, assinatura)
    print("O autor do texto", autor, "está infectado com COH-PIAH")
