from sqlalchemy import create_engine

# importa tipos de dados e estruturas de colunos
from sqlalchemy import Column, Integer, String, Float,  Boolean

# importa a classe base usada para criar os modelos ORMS
from sqlalchemy.orm import declarative_base

#importa a ferramena para criar sessões no banco
from sqlalchemy.orm import sessionmaker
