from tkinter import *
from tkinter import ttk

class App(Tk):
	def __init__(self):
		super().__init__()
		self.title('Moonkin DPS Simulator')
		
		# Init the main content frame 
		self.content = ttk.Frame(self, padding="3 3 12 12")
		self.content.grid(column=0, row=0, sticky=(N, W, E, S))

		# Setup character stat variables for entry widgets
		self.stats = {
			'Intellect'   			: StringVar(name='int', 			 value=115),
			'Spellpower'  			: StringVar(name='sp',         value=0),
			'Spell Hit Rating'  : StringVar(name='spell_hit',  value=0),
			'Spell Crit Rating'	: StringVar(name='spell_crit', value=0),
			'Spell Haste' 			: StringVar(name='haste', 		 value=0)
		}
		
		# Build stat input widgets & labels
		self.create_widgets()

	def create_widgets(self):
		# Create a row w/ an entry and label for each player stat
		for idx, (stat_name, tkVar) in enumerate(self.stats.items()):
			entry = ttk.Entry(self.content, width=7, textvariable=tkVar)
			label = ttk.Label(self.content, text=stat_name)

			entry.grid(column=0, row=idx)
			label.grid(column=1, row=idx)

		# Row 5 / Calculate Button
		submit_button = ttk.Button(self.content, command=self.calculate, text='Calculate DPS')
		submit_button.grid(row=5, columnspan=2)

		# Add padding to all widgets
		for child in self.content.winfo_children(): 
				child.grid_configure(padx=5, pady=5)


	def calculate(self, *args):
		try:
			for stat, value in self.stats.items():
				print(f'{stat}: {value.get()}')
		except ValueError:
			pass


if __name__ == '__main__':
	app = App()
	app.mainloop()