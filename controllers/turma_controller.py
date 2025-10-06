from models import Turma
from config import db

class TurmaController:
    @staticmethod
    def listar_turmas():
        return Turma.query.all()
    
    def consultar_turma(turma_id):
        return Turma.query.filter_by(id=turma_id).first()
    
    @staticmethod
    def criar(data):
        novo = Turma(descricao=data['descricao'], professor_id=data.get('professor_id'), ativo=data.get('ativo'))
        db.session.add(novo)
        db.session.commit()
        return novo
    
    @staticmethod
    def atualizar(turma_id, data):
        turma = Turma.query.get_or_404(turma_id)
        turma.descricao = data.get('descricao', turma.descricao)
        turma.professor_id = data.get('professor_id', turma.professor_id)
        turma.ativo = data.get('ativo', turma.ativo)
        db.session.commit()
        return turma
    
    @staticmethod
    def deletar(turma_id):
        turma = Turma.query.get_or_404(turma_id)
        db.session.delete(turma)
        db.session.commit()
        return {}