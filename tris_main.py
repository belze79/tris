from tkinter import Tk, Label

from session import session
from view_py import set_window
from controller_py import music_loop

print('print di log prima dell\'avvio dell\'interfaccia')

session.root_config.root = Tk()
session.root_config.root.title('Tic Tac Toe')
session.root_config.root.geometry(f'{session.root_config.width}x{session.root_config.height}+{1300 - session.root_config.width}+80')
session.root_config.root.configure(bg=session.root_config.bg)

session.root_config.root.grid_columnconfigure((0, 2), weight=1)
session.root_config.root.grid_rowconfigure((0, 2, 4, 6, 8, 10), weight=1)


set_window()

music_loop()

print('print di log dopo il set dell\'interfaccia')

session.root_config.root.mainloop()

print('print di log alla chiusura dell\'app')