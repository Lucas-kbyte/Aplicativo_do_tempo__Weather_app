# 🌤️ Web Weather App (Checkpoint 5)

O Web Weather App é uma aplicação web dinâmica desenvolvida como projeto de conclusão do Bloco 3 da Formação Python & Django. O sistema integra uma interface web moderna a dados climáticos em tempo real consumidos diretamente da API global do OpenWeatherMap.

O projeto consolida conceitos fundamentais de desenvolvimento Full-Stack, como o consumo de APIs REST, manipulação de rotas dinâmicas, tratamento de exceções e renderização reativa no front-end.

Documentação da API acesse: https://openweathermap.org/api/one-call-4?collection=one_call_api

---

## 🚀 Funcionalidades

* **Busca Global em Tempo Real:** Permite pesquisar as condições climáticas de qualquer cidade do mundo.
* **Renderização Dinâmica:** Exibe o nome da cidade, país, descrição do clima, temperatura atual (em Celsius), umidade e velocidade do vento (convertida para km/h).
* **Tratamento de Erros:** Exibe alertas amigáveis caso a cidade não seja encontrada ou ocorra uma falha de conexão com o serviço de clima.
* **Interface Responsiva:** Design moderno no modo escuro adaptável para dispositivos móveis e desktops.

---

## 🛠️ Tecnologias Utilizadas

### **Back-end**
* **Python** (Linguagem base)
* **Flask** (Microframework para gerenciamento de rotas e servidor web)
* **Requests** (Biblioteca HTTP para consumo da API externa)

### **Front-end**
* **HTML5**
* **Bootstrap 5** (Estilização responsiva via CDN)
* **FontAwesome 6** (Ícones da interface)
* **Jinja2** (Motor de templates para lógica e exibição dinâmica de dados)

---

## 📁 Estrutura do Projeto

A arquitetura segue o padrão de mercado para aplicações Flask:
```
/weather_app
├── venv/          # Ambiente virtual Python
├── app.py         # Servidor Flask e lógica do back-end
└── templates/     # Pasta padrão de visuais do Flask
    └── index.html # Tela do aplicativo e lógica Jinja2
```
---

## 🔧 Como Executar o Projeto

### 1. Clonar o Repositório e Configurar o Ambiente
# Clone o repositório
git clone https://github.com/seu-usuario/web-weather-app.git
cd web-weather-app

# Crie e ative o ambiente virtual (venv)
```
python -m venv venv
```
```
source venv/bin/activate  # No Linux/macOS
```
ou 
```
venv\Scripts\activate # No Windows
```

### 2. Instalar as Dependências
```
pip install flask requests
```
ou caso tenha o arquivo requirements.txt
```
pip install -r requirements.txt
```

### 3. Configurar a Chave da API
1. Acesse o site oficial do OpenWeatherMap e crie uma conta gratuita.
2. Copie a sua chave gerada em My API Keys.
3. Abra o arquivo app.py e insira sua chave na variável correspondente:
```
   API_KEY = "SUA_API_KEY_AQUI"
```
### 4. Iniciar o Servidor
```
python app.py
```
Acesse http://127.0.0.1:5000/ no seu navegador para testar a aplicação.

---

## 🏆 Desafios Implementados (Modo Avançado)

Para turbinar o portfólio, foram adicionadas melhorias além da estrutura básica:
* [ ] **Desafio 1:** Interface dinâmica alterando cores e fundos com base nas condições do clima (Chuva, Céu Limpo, Nuvens).
* [ ] **Desafio 2:** Exibição do horário do nascer e pôr do sol formatados através do timestamp Unix da API.
* [ ] **Desafio 3:** Inclusão da sensação térmica na tela principal (feels_like).
* [ ] **Desafio 4:** Histórico de buscas persistente salvando as últimas 3 cidades pesquisadas em um arquivo JSON.

---
