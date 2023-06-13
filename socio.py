from dataclasses import dataclass
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, MappedAsDataclass


class Base (MappedAsDataclass, DeclarativeBase):
    pass

@dataclass
class Socio(Base, order=True):
    __tablename__= "clientes"

    id: Mapped[int]= mapped_column(init= False, primary_key= True)
    dni: Mapped[str]
    nombre: Mapped [str]
    apellido: Mapped [str]


    @classmethod
    def crear_socio(cls):
        while True:
            try:
                dni = input('Ingrese el DNI del socio: ')
                nombre= input('Ingrese el nombre del socio: ')
                apellido= input('Ingrese el apellido del socio: ')

                socio = cls (dni, nombre, apellido)
                return socio
            
            except Exception as e:
                print ("Error: ", e)


    def guardar_socio (self, engine):
        with Session(engine) as session:
            session.add(self)
            session.commit()
            print ("*** Socio agregado a base de datos ***\n")


    @classmethod
    def mostrar_socios(cls, engine, dni):
       
        with Session(engine) as session:
            try:
                consulta= select(Socio).where(Socio.dni== dni)
                socio= session.scalars(consulta).first()
                print (f''' *** Datos del socio ***
                    - Nombre: {socio.nombre}
                    - Apellido: {socio.apellido}
                    - DNI: {socio.dni}''')            
            except Exception as e:
                print ("** Error: No se encuentra el socio con el DNI ingresado **\n")

