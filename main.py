from backend import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from AutoHotPy import AutoHotPy
import pyperclip as pc
import threading
from ui import *
from game_address import *

# The following function is called when you press ESC.
#autohotpy is the instance that controlls the library, you should do everything through it.
def exitAutoHotKey(autohotpy,event):
    """
    exit the program when you press ESC
    """
    autohotpy.stop() #makes the program finish successfully. Thisis the right way to stop it

 
# THIS IS WERE THE PROGRAM STARTS EXECUTING!!!!!!!!
if __name__=="__main__":
    auto = AutoHotPy()  #Initialize the library
    auto.registerExit(auto.ESC, exitAutoHotKey)   # Registering an end key is mandatory to be able to stop the program gracefully
    scripts = threading.Thread(target=auto.start, args=(), daemon=True)
    scripts.start()
    app = App(auto)
    app.mainloop()