class Usuario:
  def __init__(self, nombre, contraseña):
    self.nombre = nombre
    self.contraseña = contraseña


usuario1 = Usuario("Ainhoa", "1234")
print(usuario1)
print(usuario1.nombre)
print(usuario1.contraseña)