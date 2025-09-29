from models import Professor, db

class ProfessorController:
    @staticmethod
    def listar():
        return Professor.query.all()

    @staticmethod
    def criar(data):
        novo = Professor(nome=data['nome'], idade=data.get('idade'), materia=data.get('materia'), observacoes=data.get('observacoes'))
        db.session.add(novo)
        db.session.commit()
        return novo

    @staticmethod
    def atualizar(professor_id, data):
        professor = Professor.query.get_or_404(professor_id)
        professor.nome = data.get('nome', professor.nome)
        professor.idade = data.get('idade', professor.idadei)
        professor.materia = data.get('materia', professor.materia)
        professor.observacoes = data.get('observacoes', professor.observacoes)
        db.session.commit()
        return professor

    @staticmethod
    def deletar(professor_id):
        professor = Professor.query.get_or_404(professor_id)
        db.session.delete(professor)
        db.session.commit()
        return {}
