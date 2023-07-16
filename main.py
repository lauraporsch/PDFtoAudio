from PyPDF2 import PdfReader
import pyttsx3
from UI import Window
import tkinter.filedialog
import tkinter.messagebox


def convert_file():
    """opens tkinter filedialog to choose file from computer, extracts text from pdf, opens messagebox if pdf should
    be saved as mp3 file, opens tkinter filedialog to choose path, converts pdf to mp3 and saves file with the chosen
    name to the chosen directory, creates messagebox with info, when done"""
    file = tkinter.filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')])
    reader = PdfReader(file)
    name = window.name_file.get()
    text = ""

    for page_number in range(0, len(reader.pages)-1):
        page = reader.pages[page_number]
        text += page.extract_text()

    user_answer = tkinter.messagebox.askquestion(title='Save file?', message=f'Save {name} as mp3 file?')

    if user_answer == "yes":
        file_path = tkinter.filedialog.asksaveasfilename(initialfile=name)
        if file_path == "":
            pass
        else:
            engine = pyttsx3.init()
            engine.save_to_file(text, f'{file_path}.mp3')
            engine.runAndWait()

            tkinter.messagebox.showinfo(title="Done", message="Your file has been saved")
    else:
        pass


window = Window()
window.upload_button.config(command=convert_file)


window.mainloop()