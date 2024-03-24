from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos (inicialmente vazia)
produtos = []

# Contador para atribuir IDs únicos aos produtos
contador_id = 1

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    global contador_id
    
    nome = request.form['nome']
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    disponivel = request.form['disponivel'] == 'sim'
    
    # Adiciona o produto à lista de produtos com um ID único
    produtos.append({'id': contador_id, 'nome': nome, 'descricao': descricao, 'valor': valor, 'disponivel': disponivel})
    contador_id += 1
    
    return redirect(url_for('index'))

@app.route('/excluir_produto/<int:id>')
def excluir_produto(id):
    # Remove o produto da lista com base no ID fornecido
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            break
    return redirect(url_for('index'))

@app.route('/editar_produto/<int:id>')
def editar_produto(id):
    # Encontra o produto na lista com base no ID fornecido
    for produto in produtos:
        if produto['id'] == id:
            return render_template('editar_produto.html', produto=produto)
    return redirect(url_for('index'))

@app.route('/salvar_edicao/<int:id>', methods=['POST'])
def salvar_edicao(id):
    # Encontra o produto na lista com base no ID fornecido
    for produto in produtos:
        if produto['id'] == id:
            # Atualiza os dados do produto com os valores do formulário de edição
            produto['nome'] = request.form['nome']
            produto['descricao'] = request.form['descricao']
            produto['valor'] = float(request.form['valor'])
            produto['disponivel'] = request.form['disponivel'] == 'sim'
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
