from models import Aluno, db

class AlunoController:
    @staticmethod
    def listar():
        return Aluno.query.all()
    
    @staticmethod
    def criar(data):
        novo = Aluno(nome=data['nome'])