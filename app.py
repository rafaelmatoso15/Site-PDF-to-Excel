from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

# CONFIGURAÇÃO: coloque aqui o seu número de WhatsApp no formato internacional
WHATSAPP_NUMBER = "5511952882273"  # ex: 55 + DDD + número

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        quantidade_pdfs = request.form.get("quantidade_pdfs")
        observacoes = request.form.get("observacoes", "")

        mensagem = (
            f"Olá! Gostaria de solicitar um orçamento para extração de informes de rendimentos.\n\n"
            f"Nome: {nome}\n"
            f"E-mail: {email}\n"
            f"Telefone/WhatsApp: {telefone}\n"
            f"Quantidade de PDFs: {quantidade_pdfs}\n"
            f"Observações: {observacoes}"
        )

        encoded_message = urllib.parse.quote(mensagem)
        wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"
        return redirect(wa_url)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
