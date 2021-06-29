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
		self.intellect   = StringVar()
		self.spellpower  = StringVar()
		self.spell_hit	 = StringVar()
		self.spell_crit	 = StringVar()
		self.spell_haste = StringVar()

		# Build stat input widgets & labels
		self.create_widgets()

	def create_widgets(self):
		# Row 1
		int_input = ttk.Entry(self.content, width=7, textvariable=self.intellect)
		int_label = ttk.Label(self.content, text="Intellect")

		int_input.grid(column=0, row=0, sticky=(W, E))
		int_label.grid(column=1, row=0, sticky=(W, E))

		# Row 2
		hit_input = ttk.Entry(self.content, width=7, textvariable=self.spell_hit)
		hit_label = ttk.Label(self.content, text="Spell Hit Rating")

		hit_input.grid(column=0, row=1, sticky=(W, E))
		hit_label.grid(column=1, row=1, sticky=(W, E))

		# Row 3
		crit_input = ttk.Entry(self.content, width=7, textvariable=self.spell_crit)
		crit_label = ttk.Label(self.content, text="Spell Crit Rating")

		crit_input.grid(column=0, row=2, sticky=(W, E))
		crit_label.grid(column=1, row=2, sticky=(W, E))

		# Row 4
		sp_input = ttk.Entry(self.content, width=7, textvariable=self.spellpower)
		sp_label = ttk.Label(self.content, text="Spellpower")

		sp_input.grid(column=0, row=2, sticky=(W, E))
		sp_label.grid(column=1, row=2, sticky=(W, E))

		# Row 5
		haste_input = ttk.Entry(self.content, width=7, textvariable=self.spell_haste)
		haste_label = ttk.Label(self.content, text="Haste")

		haste_input.grid(column=0, row=3, sticky=(W, E))
		haste_label.grid(column=1, row=3, sticky=(W, E))

		# Row 5 / Calculate Button
		submit_button = ttk.Button(self.content, command=self.calculate, text='Calculate DPS')
		submit_button.grid(row=4, columnspan=2)

		# Add padding to all widgets
		for child in self.content.winfo_children(): 
				child.grid_configure(padx=5, pady=5)


	def calculate(*args):
		try:
			print('Calculating!')	
		except ValueError:
			pass


if __name__ == '__main__':
	app = App()
	app.mainloop()