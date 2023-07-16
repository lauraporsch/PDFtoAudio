from tkinter import *

TEAL = "#569DAA"
DARKTEAL = "#577D86"
LIGHTMINT = "#B9EDDD"
FONT = "Arial"


class Window(Tk):
    """creates class Window based on super class Tk, creates widgets for UI"""
    def __init__(self):
        super().__init__()
        self.title("Text to Speech Converter")
        self.config(bg=TEAL)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(4, weight=1)

        self.explanation = Label()
        self.explanation.config(text="Upload a PDF file and automatically convert it to MP3\n\nDepending on the file "
                                "size this might take a moment.", font=(FONT, 15, "bold"), fg=DARKTEAL,
                                bg=LIGHTMINT, pady=50, padx=90)
        self.explanation.grid(column=1, row=1, columnspan=3, pady=(50, 50))

        self.name_label = Label()
        self.name_label.config(text="Save Audio File as", font=(FONT, 15), bg=TEAL, fg=LIGHTMINT,
                               padx=20)
        self.name_label.grid(column=1, row=3)

        self.name_file = Entry(width=20, font=(FONT, 15))
        self.name_file.insert(0, "Name file here")
        self.name_file.grid(column=2, row=3)

        self.upload_button = Button(self, text="UPLOAD", highlightthickness=0, height=2, width=10, bg=LIGHTMINT,
                                    fg=DARKTEAL, font=(FONT, 10, "bold"))
        self.upload_button.grid(column=3, row=3, padx=(20, 0))
