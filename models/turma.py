from app import db
from sqlalchemy import ForeignKey

class Turma(db.Model):
    __tablename__ = "turma"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=True)
    professor_id = db.Column(db.Integer, ForeignKey('professores.id'))
    ativo = db.Column(db.Boolean, nullable=False, default=True)

    professor = db.relationship(
        "Professor", 
        back_populates="turmas"
    )

    def __repr__(self):
        return f"<Turma {self.descricao}>"