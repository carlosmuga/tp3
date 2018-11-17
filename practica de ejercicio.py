import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()

fe=open("file1.txt","r")
fx=open("file2","w")
line=fe.readline()

while line:
	answer = simpledialog.askstring("Input",line,
                                parent=application_window)
								
	fx.write(answer + "\n")
	line=fe.readline()
	
fe.close()
fx.close()

'''ff=open("file2","r")
fg=open("file3","w")
line=fe.readline()


while line:
answer = simpledialog.askstring("Input", "¿sabes programar?",
                                parent=application_window)

	if answer is not None:
    	print("Eso parece")
	else:
    	print("Normal, estas empezando")

    	fg.write(answer + "\n")
    	line=ff.readline()

ff.close()
fg.close()
'''


