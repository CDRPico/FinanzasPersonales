import pandas as pd
import numpy as np

class ReadDataClient:
	total_income = None 
	total_expenses = None
	total_finexp = None
	total_saves = None
	surplus = None
	perc_expenses = None
	perc_finexp = None
	perc_saves = None

	def __init__(self):
		self.gen_data = pd.read_excel('Tabla campos simulador.xlsx')

	# Functions to summarize the input
	def sum_incomes(self):
		self.total_income = self.gen_data[self.gen_data["Categoria"]=="Ingreso"]
		self.total_income = self.total_income.groupby("Categoria").sum()
		self.total_income = self.total_income.loc["Ingreso",:].to_numpy()

	def sum_expenditures(self):
		self.total_expenses = self.gen_data[self.gen_data["Categoria"]=="Gastos Fijos"]
		self.total_expenses = self.total_expenses.groupby("Categoria").sum()
		self.total_expenses = self.total_expenses.loc["Gastos Fijos",:].to_numpy()

	def sum_financialexp(self):
		self.total_finexp = self.gen_data[self.gen_data["Categoria"]=="Gastos Financieros"]
		self.total_finexp = self.total_finexp.groupby("Categoria").sum()
		self.total_finexp = self.total_finexp.loc["Gastos Financieros",:].to_numpy()

	def sum_savings(self):
		self.total_saves = self.gen_data[self.gen_data["Categoria"]=="Ahorro"]
		self.total_saves = self.total_saves.groupby("Categoria").sum()
		self.total_saves = self.total_saves.loc["Ahorro",:].to_numpy()

	def compute_first_stats(self):
		self.sum_incomes()
		self.sum_expenditures()
		self.sum_financialexp()
		self.sum_savings()
		# compute surplus money at the end of each month
		self.surplus = self.total_income - self.total_expenses - self.total_finexp - self.total_saves
		# compute percentages
		self.perc_expenses = self.comp_percentage(self.total_expenses)
		self.perc_finexp = self.comp_percentage(self.total_finexp)
		self.perc_saves = self.comp_percentage(self.total_saves)

	# Function to compute percentages
	def comp_percentage(self, data):
		perc = np.array([])
		for i in range(len(self.total_income)):
			if (self.total_income[i] < 0.0001):
				perc = np.append(perc, 0.0)
			else:
				perc = np.append(perc, data[i]/self.total_income[i])
		return perc

	# Function to determine if the client has some surplus money
	# TODO: extend for many months
	def surplus_money(self):
		if (self.surplus[0] > 0):
			print("Tienes un sobrante de " + str(self.surplus[0]) + \
			". Te aconsejamos explorar alternativas de ahorro e inversión.\n ¡Veamos las opciones!\n")
		

	# Function to compute stats
	#We will start only considering the first month
	# TODO: explore to extend analysis to the whole year or months entered
	def client_message(self):
		if (self.perc_finexp[0]<=0.4):
			print("¡FELICITACIONES! Tienes un buen manejo de tus finanzas personales\n")
			if (self.perc_expenses[0]<=0.4):
				print("Tus gastos fijos se encuentran controlados, esto te permite mayor capacidad de ahorro e inversión en el futuro\n")
				if (self.perc_saves[0]>=0.2):
					print("Tienes una excelente capacidad de ahorro e inversión\n")
			elif (self.perc_expenses[0]<=0.5):
				print("Debemos analizar tus gastos para identificar oportunidades de optimización que te permitan mejorar tu capacidad de ahorro\n")
				if (self.perc_saves[0]>=0.1):
					print("¡Muy bien! El habito de ahorro te permitirá alcanzar tus objetivos. Recuerda que existen productos de ahorro con rentabilidad en COP y USD, beneficio tributario y protección para el futuro\n")
			else:
				print("¡Cuidado! Aunque tus finanzas son saludables, tienes gastos hormiga que ponen en peligro tu futuro ante eventuales crisis\n")
		elif (self.perc_expenses[0] + self.perc_finexp[0] > 1):
			print("¡ALERTA! Tus finanzas personales requieren atención inmediata\n")
			if (self.perc_finexp[0]>=0.6):
				print("Tu endeudamiento actual requiere análisis y optimización inmediata, los ajustes en este item te permitirá liberar flujo de caja para ajustar tu situación financiera\n")
			print("Debemos analizar tus gastos para identificar oportunidades de optimización que te permitan mejorar tu capacidad de ahorro\n")
		else:
			print("¡ATENCIÓN! El comportamiento actual de tu flujo de caja pone en 
			riesgo el manejo de tus finanzas personales\n")
			if (self.perc_expenses[0] + self.perc_finexp[0]>=0.9):
				print("Tu endeudamiento actual requiere revisión y ajustes, la optimización en este rubro te permitirá mejorar tu flujo de caja\n")
				print("Debemos analizar tus gastos para identificar oportunidades de optimización que te permitan mejorar tu capacidad de ahorro\n")
			else:
				print("Tus niveles de gasto muestra un desbalance importante, debemos analizar las oportunidades de reducir el gasto financiero ya que genera fuga de dinero debido a los intereses de dichos productos\n")
		if (self.perc_saves[0]<0.0001):
			print("¡Peligro! El ahorro es fundamental para afrontar momentos de crisis y capitalizar tus objetivos\n")
		

a = ReadDataClient()
a.sum_incomes()
a.sum_expenditures()
a.sum_financialexp()
a.compute_first_stats()
a.surplus_money()
