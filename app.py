from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO
from dao.matricula_dao import MatriculaDAO


app = Flask(__name__)
app.secret_key = 'uma_chave_muito_secreta_e_unica'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/aluno')
def listar_aluno():
   dao = AlunoDAO()
   lista = dao.listar()
   return render_template('aluno/listar.html', lista=lista)

@app.route('/aluno/form')
def form():
   return render_template('aluno/form.html', aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])
@app.route('/aluno/salvar/<int:id>', methods=['POST'])    
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade) 


    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")


    return redirect('/aluno')

@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)  

@app.route('/aluno/remover/<int:id>')
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/aluno')


@app.route('/professor')
def listar_professor():
   dao = ProfessorDAO()
   lista = dao.listar()
   return render_template('professor/listar.html', lista=lista)

@app.route('/professor/form')
def form_professor():
   return render_template('professor/form.html', professor=None)

@app.route('/professor/salvar/', methods=['POST'])
@app.route('/professor/salvar/<int:id>', methods=['POST'])
def salvar_professor(id=None):
    id = request.form.get('id') or None    
    nome = request.form['nome']
    disciplina = request.form['disciplina']

    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina)

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')

@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = ProfessorDAO()
    professor = dao.buscar_por_id(id)
    return render_template('professor/form.html', professor=professor)  

@app.route('/professor/remover/<int:id>')
def remover_professor(id):
    dao = ProfessorDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/professor')



@app.route('/turma')
def listar_turma():
   dao = TurmaDAO()
   lista = dao.listar()
   return render_template('turma/listar.html', lista=lista)

@app.route('/turma/form')
def form_turma():
   return render_template('turma/form.html', turma=None)

@app.route('/turma/salvar/', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def turma_salvar():
    dao = TurmaDAO()
    id = request.form.get('id')
    semestre = request.form.get('semestre')
    curso = request.form.get('curso')
    professor = request.form.get('professor')

    dao.salvar(id, semestre, curso, professor)

    return redirect('/turma')

@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)
    return render_template('turma/form.html', turma=turma)  
@app.route('/turma/remover/<int:id>')

def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')

@app.route('/curso')
def listar_curso():
   dao = CursoDAO()
   lista = dao.listar()
   return render_template('curso/listar.html', lista=lista)

@app.route('/curso/form')
def form_curso():
   return render_template('curso/form.html', curso=None)

@app.route('/curso/salvar/', methods=['POST'])
@app.route('/curso/salvar/<int:id>', methods=['POST'])
def curso_salvar():
    dao = CursoDAO()
    id = request.form.get('id')
    nome = request.form.get('nome_curso')
    duracao = request.form.get('duracao')

    dao.salvar(id, nome, duracao)

    return redirect('/curso')

@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    dao = CursoDAO()
    curso = dao.buscar_por_id(id)
    return render_template('curso/form.html', curso=curso)  
@app.route('/curso/remover/<int:id>')

def remover_curso(id):
    dao = CursoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/curso')

@app.route('/matricula')
def listar_matricula():
   dao = MatriculaDAO()
   lista = dao.listar()
   return render_template('matricula/listar.html', lista=lista)

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
   print(nome)
   return render_template('saudacao/saudacao.html',valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
   nome = request.args.get('nome')
   return render_template('saudacao/saudacao.html',valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['user']
    senha = request.form['password']
    dados = f'Usuário: {usuario}, Senha: {senha}'
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio1')
def cadastro():
    return render_template('cadastro.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form.get('nome')
    data_nasc = request.form.get('data_nasc')
    cpf = request.form.get('cpf')
    mae = request.form.get('mae')
    return render_template('resultado.html', nome=nome, data_nasc=data_nasc, cpf=cpf, mae=mae)

if __name__ == '__main__':
    app.run(debug=True)
