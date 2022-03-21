class Asiento:
	def __init__(self, color, precio, registro):
		self.color = color
		self.precio = precio
		self.registro = registro
	
	def cambiarColor(self, ncolor):
		if (ncolor in ["rojo", "verde", "amarillo", "negro", "blanco"]):
			self.color = ncolor

class Auto:
	cantidadCreados = 0
	def __init__(self, modelo, precio, asientos, marca, motor, registro):
		self.modelo = modelo
		self.precio = precio
		self.asientos = asientos
		self.marca = marca
		self.motor = motor
		self.registro = registro
	
	def cantidadAsientos(self):
		count = 0
		for asiento in self.asientos:
			if asiento.__class__.__name__ == "Asiento":
				count += 1
		return count
	
	def verificarIntegridad(self):
		asientoOriginal = True
		for asiento in self.asientos:
			if asiento.__class__.__name__ == "Asiento" and asiento.registro != self.registro:
				asientoOriginal = False
				break
		
		motorOriginal = self.registro == self.motor.registro
		if asientoOriginal and motorOriginal:
			return "Auto original"
		else:
			return "Las piezas no son originales"

class Motor:
	def __init__(self, numeroCilindros, tipo, registro):
		self.numeroCilindros = numeroCilindros
		self.tipo = tipo
		self.registro = registro
	
	def cambiarRegistro(self, nregistro):
		self.registro = nregistro
	
	def asignarTipo(self, ntipo):
		if ntipo in ["electrico", "gasolina"]:
			self.tipo = ntipo