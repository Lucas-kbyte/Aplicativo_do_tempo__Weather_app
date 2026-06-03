from flask import Flask, render_template, request
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)
API_KEY = "b41b079a232ac65bd2551f1ab4dbfdbf"
HISTORY_FILE = "historico.json"

@app.template_filter('formatar_hora')
def formatar_hora(timestamp, timezone_offset):
    dt = datetime.utcfromtimestamp(timestamp + timezone_offset)
    return dt.strftime('%H:%M')

def carregar_historico():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_historico(cidade):
    historico = carregar_historico()
    if cidade in historico:
        historico.remove(cidade)
    historico.insert(0, cidade)
    historico = historico[:3]
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(historico, f, ensure_ascii=False)
    return historico

@app.route("/", methods=["GET", "POST"])
def index():
    clima = None
    erro = None
    historico = carregar_historico()
    
    if request.method == "POST":
        cidade_digitada = request.form.get("cidade", "").strip()
        
        if cidade_digitada:
            geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={cidade_digitada}&limit=1&appid={API_KEY}"
            try:
                geo_res = requests.get(geo_url)
                if geo_res.status_code == 200 and geo_res.json():
                    cidade_oficial = geo_res.json()[0]['name']
                else:
                    cidade_oficial = cidade_digitada
            except:
                cidade_oficial = cidade_digitada

            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_oficial}&appid={API_KEY}&units=metric&lang=pt_br"
            try:
                resposta = requests.get(url)
                if resposta.status_code == 200:
                    clima = resposta.json()
                    historico = salvar_historico(clima['name'])
                else:
                    erro = "Cidade não encontrada! Tente novamente."
            except requests.exceptions.RequestException:
                erro = "Não foi possível conectar ao servidor de clima."
                
    return render_template("index.html", clima=clima, erro=erro, historico=historico)

if __name__ == "__main__":
    app.run(debug=True)