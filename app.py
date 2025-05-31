from flask import Flask, render_template, render_template_string

import subprocess
import os

app = Flask(__name__)

def run_script(script_name):
    path = os.path.join('static', script_name)
    subprocess.Popen(['python', path])
    return f"{script_name} iniciado!"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run/snake')
def run_snake():
    try:
    # Caminho absoluto correto com barra invertida dupla
        caminho_jogo = r"C:\Users\dti\jogos\Jogos_retr-\static\Snake.py"

        # Executa o jogo com o Python
        subprocess.Popen(["python", caminho_jogo])

        # Página de sucesso
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Jogo Iniciado</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-black text-white flex flex-col items-center justify-center h-screen">
                <h1 class="text-2xl font-bold mb-6">Jogo jogo da cobrinha iniciado!</h1>
                <a href="/" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Voltar para o início
                </a>
            </body>
            </html>
        """)

    except Exception as e:
        return f"Erro ao iniciar o jogo: {e}"


@app.route('/run/tetris')
def run_tetris():
    try:
    # Caminho absoluto correto com barra invertida dupla
        caminho_jogo = r"C:\Users\dti\jogos\Jogos_retr-\static\tetris.py"

        # Executa o jogo com o Python
        subprocess.Popen(["python", caminho_jogo])

        # Página de sucesso
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Jogo Iniciado</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-black text-white flex flex-col items-center justify-center h-screen">
                <h1 class="text-2xl font-bold mb-6">Tetris iniciado!</h1>
                <a href="/" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Voltar para o início
                </a>
            </body>
            </html>
        """)

    except Exception as e:
        return f"Erro ao iniciar o jogo: {e}"
@app.route('/run/breaker')
def run_breaker():
    try:
    # Caminho absoluto correto com barra invertida dupla
        caminho_jogo = r"C:\Users\dti\jogos\Jogos_retr-\static\breaker.py"

        # Executa o jogo com o Python
        subprocess.Popen(["python", caminho_jogo])

        # Página de sucesso
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Jogo Iniciado</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-black text-white flex flex-col items-center justify-center h-screen">
                <h1 class="text-2xl font-bold mb-6">Jogo breaker iniciado!</h1>
                <a href="/" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Voltar para o início
                </a>
            </body>
            </html>
        """)

    except Exception as e:
        return f"Erro ao iniciar o jogo: {e}"

@app.route('/run/esquiva')
def run_esquiva():
    try:
    # Caminho absoluto correto com barra invertida dupla
        caminho_jogo = r"C:\Users\dti\jogos\Jogos_retr-\static\esquiva.py"

        # Executa o jogo com o Python
        subprocess.Popen(["python", caminho_jogo])

        # Página de sucesso
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Jogo Iniciado</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-black text-white flex flex-col items-center justify-center h-screen">
                <h1 class="text-2xl font-bold mb-6">Jogo mais dificil iniciado!</h1>
                <a href="/" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Voltar para o início
                </a>
            </body>
            </html>
        """)

    except Exception as e:
        return f"Erro ao iniciar o jogo: {e}"

@app.route('/run/velha')
def run_velha():
    try:
    # Caminho absoluto correto com barra invertida dupla
        caminho_jogo = r"C:\Users\dti\jogos\Jogos_retr-\static\velha.py"

        # Executa o jogo com o Python
        subprocess.Popen(["python", caminho_jogo])

        # Página de sucesso
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Jogo Iniciado</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-black text-white flex flex-col items-center justify-center h-screen">
                <h1 class="text-2xl font-bold mb-6">Jogo da velha iniciado!</h1>
                <a href="/" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Voltar para o início
                </a>
            </body>
            </html>
        """)

    except Exception as e:
        return f"Erro ao iniciar o jogo: {e}"

@app.route('/run/space')
def run_space():
    try:
    # Caminho absoluto correto com barra invertida dupla
        caminho_jogo = r"C:\Users\dti\jogos\Jogos_retr-\static\spaceinvaders.py"

        # Executa o jogo com o Python
        subprocess.Popen(["python", caminho_jogo])

        # Página de sucesso
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>Jogo Iniciado</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-black text-white flex flex-col items-center justify-center h-screen">
                <h1 class="text-2xl font-bold mb-6"> iniciado!</h1>
                <a href="/" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Voltar para o início
                </a>
            </body>
            </html>
        """)

    except Exception as e:
        return f"Erro ao iniciar o jogo: {e}"

if __name__ == '__main__':
    app.run(debug=True)
