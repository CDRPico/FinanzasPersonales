import pandas as pd
import numpy as np

class ReadDataClient:
	total_income = None 
	total_expenses = None
	total_finexp = None
	total_saves = None
	surplus = []
	perc_expenses = []
	perc_finexp = []
	perc_saves = []

	def __init__(self):
		self.gen_data = pd.read_excel('Tabla campos simulador.xlsx')

	# Functions to summarize the input
	def sum_incomes(self):
		self.total_income = self.gen_data[self.gen_data["Categoria"]=="Ingreso"]
		self.total_income = self.total_income.groupby("Categoria").sum()
		self.total_income = self.total_income.to_numpy()

	def sum_expenditures(self):
		self.total_expenses = self.gen_data[self.gen_data["Categoria"]=="Gasto"]
		self.total_expenses = self.total_expenses.groupby("Categoria").sum()
		self.total_expenses = self.total_expenses.to_numpy()

	def sum_financialexp(self):
		self.total_finexp = self.gen_data[self.gen_data["Categoria"]=="Gastos Financieros"]
		self.total_finexp = self.total_finexp.groupby("Categoria").sum()
		self.total_finexp = self.total_finexp.to_numpy()

	def sum_savings(self):
		self.total_saves = self.gen_data[self.gen_data["Categoria"]=="Ahorro"]
		self.total_saves = self.total_saves.groupby["Categoria"].sum()
		self.total_saves = self.total_saves.to_numpy()

	def compute_first_stats(self):
		self.sum_incomes()
		self.sum_expenditures()
		self.sum_financialexp()
		self.sum_savings()
		# compute surplus money at the end of each month
		self.surplus = self.total_income - self.total_expenses - self.total_finexp - self.total_saves
		# compute percentages
		self.perc_expenses = self.total_expenses / self.total_income
		self.perc_finexp = self.total_finexp / self.total_income
		self.perc_saves = self.total_saves / self.total_income

	# Function to determine if the client has some surplus money
	# TODO: extend for many months
	def surplus_money(self):
		if (self.surplus[0] > 0):
			print("Tienes un sobrante de " + str(self.sum_financialexp[0]) + \
			". Te aconsejamos explorar alternativas de ahorro e inversión.\n ¡Veamos las opciones!")
		

	# Function to compute stats
	#We will start only considering the first month
	# TODO: explore to extend analysis to the whole year or months entered
	def client_message(self):
		pass
		

a = ReadDataClient()
a.sum_incomes()
a.sum_expenditures()
a.sum_financialexp()
a.compute_first_stats()
a.surplus_money()
