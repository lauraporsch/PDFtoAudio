from tkinter import *

TEAL = "#569DAA"
MINT = "#87CBB9"
DARKTEAL = "#577D86"
LIGHTMINT = "#B9EDDD"


class Window(Tk):
    """creates class Window based on super class Tk, creates widgets for UI"""
    def __init__(self):
        super().__init__()
        self.title("Text to Speech Converter")
        self.config(bg=DARKTEAL)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        self.explanation = Label()
        self.explanation.config(text="Upload a PDF file and automatically convert it to MP3\n\nDepending on the file "
                                "size this might take a moment.", font=("Georgia", 10, "bold"), fg=DARKTEAL,
                                bg=LIGHTMINT, pady=50, padx=20)
        self.explanation.grid(column=1, row=0)

        self.empty_space = Label()
        self.empty_space.config(text="", bg=DARKTEAL)
        self.empty_space.grid(column=1, row=1, columnspan=5)

        self.name_label = Label()
        self.name_label.config(text="Save Audio File as", font=("Georgia", 10, "bold"), bg=DARKTEAL, fg=LIGHTMINT,
                               padx=20)
        self.name_label.grid(column=0, row=2)

        self.name_file = Entry(width=20, font=("Georgia", 14))
        self.name_file.grid(column=1, row=2)

        self.empty_space = Label()
        self.empty_space.config(text="", bg=DARKTEAL)
        self.empty_space.grid(column=1, row=3, columnspan=5)

        self.upload_button = Button(self, text="UPLOAD", highlightthickness=0, height=2, width=10, bg=TEAL,
                                    fg=MINT, font=("Georgia", 10, "bold"))
        self.upload_button.grid(column=1, row=4, columnspan=2)
