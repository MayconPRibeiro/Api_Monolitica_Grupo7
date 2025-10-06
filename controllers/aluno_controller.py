from models import Aluno
from config import db

class AlunoController:
    @staticmethod
    def listar():
        return Aluno.query.all()
    
    @staticmethod
    def criar(data):
        novo = Aluno(nome=data['nome'], idade=data['idade'])
        db.session.add(novo)
        db.session.commit()
        return novo
    
    @staticmethod
    def atualizar(aluno_id, data):
        aluno = Aluno.query.get_or_404(aluno_id)
        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        db.session.commit()
        return aluno
    
    @staticmethod
    def deletar(aluno_id):
        aluno = Aluno.query.get_or_404(aluno_id)
        db.session.delete(aluno)
        db.session.commit()
        return {}
    
        
    

        
