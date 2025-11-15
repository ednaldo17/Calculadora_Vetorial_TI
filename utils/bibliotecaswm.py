from math import sqrt

def vetorcadeia_para_vetornumerico(cadeia):
    cadeia = cadeia.replace(" ", "").strip()
    cadeia = cadeia.replace("(", "").replace(")", "")
    partes = cadeia.split(",")
    vetor = []
    for p in partes:
        if "/" in p:
            num, den = p.split("/")
            vetor.append(float(num) / float(den))
        else:
            vetor.append(float(p))
    return vetor

def separar_cadeias_vetores(texto):
    texto = texto.replace("),", ") ")
    partes = texto.split()
    return partes

def atribuir_vetores(texto):
    partes = separar_cadeias_vetores(texto)
    if len(partes) != 2:
        raise ValueError("É necessário fornecer 2 vetores.")
    return partes[0], partes[1]

def somar_vetores(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def subtrair_vetores(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def produto_escalar(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

def produto_vetorial(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def norma_vetor(v):
    return sqrt(sum(i*i for i in v))

def vetor_unitario(v):
    n = norma_vetor(v)
    return [i/n for i in v]

def projecao_vetor(v, u):
    fator = produto_escalar(v, u) / produto_escalar(u, u)
    return [fator * i for i in u]

def componente_vetorial(v, u):
    return produto_escalar(v, u) / norma_vetor(u)

def ortogonalizacao_gram_schmidt(vetores):
    base = []
    for v in vetores:
        w = v[:]
        for b in base:
            fator = produto_escalar(w, b) / produto_escalar(b, b)
            w = [w[i] - fator * b[i] for i in range(len(w))]
        if any(abs(x) > 1e-9 for x in w):
            base.append(w)
    return base
