import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def designate_save_point():
    pwd = os.getcwd()
    save_path = filedialog.askdirectory(parent=root, initialdir=pwd, title='Please select a savepoint directory.')
    return save_path


def rename(output_file):
    os.rename(output_file, output_file.replace('.mp4', '.mp3'))
    return output_file