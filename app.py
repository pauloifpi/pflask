from flask import Flask, render_template, request
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO
from dao.matricula_dao import MatriculaDAO


app = Flask(__name__)


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


@app.route('/professor')
def listar_professor():
   dao = ProfessorDAO()
   lista = dao.listar()
   return render_template('professor/listar.html', lista=lista)

@app.route('/turma')
def listar_turma():
   dao = TurmaDAO()
   lista = dao.listar()
   return render_template('turma/listar.html', lista=lista)

@app.route('/curso')
def listar_curso():
   dao = CursoDAO()
   lista = dao.listar()
   return render_template('curso/listar.html', lista=lista)

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

if __name__ == '__main__':
    app.run(debug=True)
