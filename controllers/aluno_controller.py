from models import Aluno, db

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
        
    

        
