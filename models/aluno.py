from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idade = Column(Integer)
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    data_nascimento = Column(Date)
    nota_primeiro_semestre = Column(Float)
    nota_segundo_semestre = Column(Float)
    media_final = Column(Float)

    turma = relationship("Turma", back_populates="alunos")

    