import customtkinter
import modules.create_frame as m_frame
import modules.music as c_music


class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.resizable(False, False)
        self.title("Music")

        # self.FRAME1 = m_frame.My_Frame(text= "список треків", 
        #                                text_color= None, 
        #                                master = self, 
        #                                width= 233, 
        #                                height= 367, 
        #                                border_width= None, 
        #                                fg_color= None)        
        

      
        # self.FRAME2 = m_frame.My_Frame(text= "назва треку що грає", 
        self.FRAME2 = m_frame.My_Frame(text= "", 
                                       text_color= "orange", 
                                       master = self, 
                                       width= 188, 
                                       height= 59, 
                                       border_width= None, 
                                       fg_color= None)
        
        self.FRAME3 = m_frame.My_Frame(text= "", 
                                       text_color= None, 
                                       master = self, 
                                       width= 188, 
                                       height= 297, 
                                       border_width= None, 
                                       fg_color= None)

        self.FRAME4 = m_frame.My_Frame(text= "", 
                                       text_color= None, 
                                       master = self, 
                                       width= 432, 
                                       height= 69, 
                                       border_width= None, 
                                       fg_color= None)
        
        self.FRAME = customtkinter.CTkScrollableFrame(master= self, width=199, height= 310, label_text="список треків")
        
        # self.FRAME1.place(x=11, y=11)
        # self.FRAME1.grid(row=0, column=0, padx=11, pady=11, sticky=customtkinter.NW)
        self.FRAME2.place(x=255, y=11)
        self.FRAME3.place(x=255, y=81)
        self.FRAME4.place(x=11, y=387)
        # self.FRAME.grid(row=0, column=0, padx=11, pady=11, sticky=customtkinter.NW)
        self.FRAME.place(x=11, y=11)
        self.FRAME._scrollbar.grid(padx=5)
        # self.FRAME2.grid_columnconfigure(0, weight=1)
        # self.FRAME3.grid_columnconfigure(0, weight=1)
        # self.FRAME4.grid_columnconfigure(0, weight=1)
        # self.FRAME.grid_columnconfigure(0, weight=1)

        # self.FRAME.grid(padx=1, pady = 40)      
        # self.FRAME._scrollbar.grid(padx=1)

        self.SONG_OF_NAME_LBL = customtkinter.StringVar()
        self.SONG_NAME_LBL = customtkinter.CTkLabel(self.FRAME2, textvariable= self.SONG_OF_NAME_LBL, width=35).place(x= 5,y= 5)
        self.SONG_OF_NAME_LBL.set('Назва пісні:')
        
        self.SONG_NAME = customtkinter.StringVar()
        self.SONGLABEl = customtkinter.CTkLabel(self.FRAME2, textvariable= self.SONG_NAME, width=35).place(x= 5, y= 30)
        
        
        

main_app = App(454, 469)
