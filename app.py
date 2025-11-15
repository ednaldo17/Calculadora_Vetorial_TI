from flask import Flask, jsonify, render_template, request
from utils.bibliotecaswm import (
    somar_vetores, subtrair_vetores, produto_escalar, produto_vetorial, vetor_unitario, projecao_vetor,
    componente_vetorial, norma_vetor, ortogonalizacao_gram_schmidt,
    vetorcadeia_para_vetornumerico, atribuir_vetores, separar_cadeias_vetores
)
from utils.RetasPlanos import equacao_reta, equacao_plano

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        data = request.get_json()
        operacao = data.get("operacao")
        entrada = data.get("entrada", "").strip()

        if not entrada:
            return jsonify({"erro": "Entrada vazia"}), 400

        vetor1, vetor2 = None, None

        # Operações que precisam de dois vetores
        if operacao in ["somar", "subtracao", "produto_escalar", "produto_vetorial", "projecao", "componente"]:
            vetor1, vetor2 = atribuir_vetores(entrada)
            v1 = vetorcadeia_para_vetornumerico(vetor1)
            v2 = vetorcadeia_para_vetornumerico(vetor2)

        # Operações com um vetor
        elif operacao in ["norma", "unitario"]:
            vetor1 = entrada
            v1 = vetorcadeia_para_vetornumerico(vetor1)

        # Retas e planos
        elif operacao == "reta":
            return jsonify({"resultado": equacao_reta(entrada)})

        elif operacao == "plano":
            return jsonify({"resultado": equacao_plano(entrada)})

        # Gram-Schmidt
        elif operacao == "gram_schmidt":
            vetores = separar_cadeias_vetores(entrada)
            vetores_convertidos = [vetorcadeia_para_vetornumerico(v) for v in vetores]
            return jsonify({"resultado": ortogonalizacao_gram_schmidt(vetores_convertidos)})

        else:
            return jsonify({"erro": "Operação inválida"}), 400

        # Tabela de operações
        operações = {
            "somar": lambda: somar_vetores(v1, v2),
            "subtracao": lambda: subtrair_vetores(v1, v2),
            "produto_escalar": lambda: produto_escalar(v1, v2),
            "produto_vetorial": lambda: produto_vetorial(v1, v2),
            "unitario": lambda: vetor_unitario(v1),
            "norma": lambda: norma_vetor(v1),
            "projecao": lambda: projecao_vetor(v1, v2),
            "componente": lambda: componente_vetorial(v1, v2)
        }

        resultado = operações[operacao]()
        return jsonify({"resultado": resultado})

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 400


if __name__ == "__main__":
    app.run(debug=True)
