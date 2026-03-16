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


engine = create_engine("sqlite:///escola.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

aluno1 = Aluno("João", 21, "Desenvolvimento")
aluno2 = Aluno("Maria", 19, "Design")
aluno3 = Aluno("Carlos", 25, "Desenvolvimento")
aluno4 = Aluno("Ana", 22, "Dados")
aluno5 = Aluno("Lucas", 18, "Desenvolvimento")

session.add_all([aluno1, aluno2, aluno3, aluno4, aluno5])
session.commit()



print("\nTodos os alunos:")
alunos = session.query(Aluno).all()

for aluno in alunos:
    print(aluno)


aluno = session.query(Aluno).filter_by(id=1).first()

aluno.curso = "Back-end com Gabriel"
session.commit()

print("\nAluno atualizado:")
print(aluno)

aluno_remover = session.query(Aluno).filter_by(nome="Lucas").first()

session.delete(aluno_remover)
session.commit()


print("\nAlunos com idade maior que 20:")

for aluno in session.query(Aluno).filter(Aluno.idade > 20):
    print(aluno)


print("\nAlunos do curso Desenvolvimento:")

for aluno in session.query(Aluno).filter_by(curso="Desenvolvimento"):
    print(aluno)