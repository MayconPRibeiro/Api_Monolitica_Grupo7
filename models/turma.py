from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Turma(Base):
    __tablename__ = 'turmas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(100))
    professor_id = Column(Integer, ForeignKey('professores.id'))
    ativo = Column(Boolean)

    professor = relationship("Professor", back_populates="turmas")
    alunos = relationship("Aluno", back_populates="turma", cascade="all, delete-orphan")