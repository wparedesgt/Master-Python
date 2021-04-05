import clases

persona = clases.Persona()

persona.setNombre("William")
persona.setApellidos("Paredes")
persona.setAltura("173cm")
persona.setEdad("48 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("----------------------------------")

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)


print("----------------------------------")

tecnico = clases.TecnioRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre())




