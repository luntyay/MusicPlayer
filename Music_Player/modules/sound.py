import customtkinter as ctk

class MessageFrame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, bg_color, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, bg_color= bg_color, **kwargs)
        self.SOUND = text
        self.FONT = ctk.CTkFont(family= "Arial", size= 20, weight= "bold")
        # self.SOUNDNAME = soundname

    def place_sound(self):
        self.MESSAGE = ctk.CTkLabel(self, text= self.SOUND)
        self.MESSAGE.place(x = 5, y = 10)
        # self.NAME = ctk.CTkLabel(master= self, text= self.SOUNDNAME, font= self.FONT)
        # self.NAME.place(x = 5, y = 2)
