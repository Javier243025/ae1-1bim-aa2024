from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class LocalComida(Base):
    __tablename__ = 'locales_comida'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    tipo_cocina = Column(String)

class CentroDeportivo(Base):
    __tablename__ = 'centros_deportivos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    tipo_deporte = Column(String)

# Crear la base de datos y las tablas
engine = create_engine('sqlite:///database_relacional.db')
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Agregar información a la base de datos
nuevo_local = LocalComida(nombre="La Buena Mesa", direccion="Calle Falsa 123", tipo_cocina="Italiana")
nuevo_centro = CentroDeportivo(nombre="Gimnasio Fit", direccion="Avenida Siempre Viva 742", tipo_deporte="Crossfit")

session.add(nuevo_local)
session.add(nuevo_centro)
session.commit()

# Consultar la base de datos
locales = session.query(LocalComida).all()
centros = session.query(CentroDeportivo).all()

print("Locales de Comida:")
for local in locales:
    print(f"Nombre: {local.nombre}, Dirección: {local.direccion}, Tipo de Cocina: {local.tipo_cocina}")

print("\nCentros Deportivos:")
for centro in centros:
    print(f"Nombre: {centro.nombre}, Dirección: {centro.direccion}, Tipo de Deporte: {centro.tipo_deporte}")

session.close()
