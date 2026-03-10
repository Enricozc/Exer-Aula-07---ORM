from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, Float,  Boolean

from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idade = Column(Integer)
    curso = Column(String(100))

    
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', curso='{self.curso}')"


