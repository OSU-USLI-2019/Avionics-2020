import tkinter as tk
import time
import threading
import serial
import time, threading
from tkinter import *
from tkinter import messagebox
testme = ""


class GUI():
    def __init__(self, master=None):
        master.geometry("200x200")
        master.title("My GUI Title")
        l= Label(master, text=testme, font=("Courier New", 16)).place(x=20, y=20)
        a = Label(master, text="STUFF")
        btn = Button(master, command = initProcesses, text="RUN" )
        btn.pack()
        a.pack()
        #initProcesses()

        #self.update_label()



def initProcesses():
    serialDataProcess = threading.Thread(target=getSerialData)
    serialDataProcess.start()
    # Process.join()


def getSerialData():

    while 1:
        arduino = serial.Serial('COM9', 9600, timeout=1)
        while 1:
            data = arduino.readline().decode('utf-8').strip()
            # splitter = data.split()
            # print("TEST", splitter[0])
            if data:
                # print(data)
                testme = data
                print(testme)

def init():
    mainWindow = Tk()
    GUI(mainWindow)
    mainWindow.mainloop()
    # When the GUI is closed we set finish to "True"
    finish = True

init()