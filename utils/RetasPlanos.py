from utils.bibliotecaswm import vetorcadeia_para_vetornumerico, produto_escalar, produto_vetorial

def equacao_reta(texto):
    p1, p2 = texto.split()
    P = vetorcadeia_para_vetornumerico(p1)
    Q = vetorcadeia_para_vetornumerico(p2)

    v = [Q[i] - P[i] for i in range(len(P))]

    if len(P) == 2:
        a = -v[1]
        b = v[0]
        c = a * P[0] + b * P[1]
        geral = f"{a}x + {b}y = {c}"
        return {
            "vetorial": f"(x,y) = ({P[0]}, {P[1]}) + t({v[0]}, {v[1]})",
            "parametricas": [f"x = {P[0]} + {v[0]} t", f"y = {P[1]} + {v[1]} t"],
            "geral": geral,
            "latex": {
                "geral": geral.replace(" ", ""),
                "parametricas": [
                    f"x = {P[0]} + {v[0]}t",
                    f"y = {P[1]} + {v[1]}t"
                ]
            }
        }
    else:
        return {"erro": "Reta em R3 ainda não implementada."}

def equacao_plano(texto):
    p1, p2, p3 = texto.split()
    P = vetorcadeia_para_vetornumerico(p1)
    Q = vetorcadeia_para_vetornumerico(p2)
    R = vetorcadeia_para_vetornumerico(p3)

    v1 = [Q[i] - P[i] for i in range(3)]
    v2 = [R[i] - P[i] for i in range(3)]
    n = produto_vetorial(v1, v2)

    a, b, c = n
    d = a*P[0] + b*P[1] + c*P[2]

    equacao = f"{a}x + {b}y + {c}z = {d}"

    return {
        "vetores_contidos": [v1, v2],
        "vetor_normal": n,
        "equacao": equacao,
        "latex": equacao.replace(" ", "")
    }
