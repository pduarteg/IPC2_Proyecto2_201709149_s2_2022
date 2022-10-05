class Escritorio:

	state = False
	next = None

	# sim values
	total_a_time = 0
	med_time = 0
	min_a_time = None
	max_a_time = None
	a_client = None
	total_clients_a = 0
	
	def __init__(self, id, identification, manager):
		self.id = id
		self.identification = identification
		self.manager = manager

	def set_state(self, value):
		self.state = value

	def reset_sim_values(self):
		self.med_time = 0
		self.min_a_time = 0
		self.max_a_time = 0
		self.a_client = None

	def print_desk_state(self):
		print("     ID: " + self.id)
		print("       Identificación: " + self.identification)
		print("       Encargado: " + self.manager)
		if self.a_client != None:
			print("       Cliente en atención: " + self.a_client.name)
		if self.total_clients_a > 0:
			print("       Tiempo promedio de atención: " + str(self.med_time))
			print("       Tiempo máximo de atención: " + str(self.max_a_time))
			print("       Tiempo mínimo de atención: " + str(self.min_a_time))
			print("       Cantidad de clientes atendidos: " + str(self.total_clients_a))
		else:
			print("       Este escritorio aún no ha atendido clientes.")