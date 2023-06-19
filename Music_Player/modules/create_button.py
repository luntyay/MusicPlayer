import customtkinter as ctk 
import modules.screen_app as m_app
import modules.create_image as c_img
import modules.find_path as f_p
import modules.music as c_music
import modules.music as music
import pyglet

# import os
# from PIL import Image, ImageTk
# image = ImageTk.PhotoImage(file="image.png")
# image = None

def create_button(master, text, command, width, height, image, corner_radius = 5):
    button = ctk.CTkButton(master = master,
                           width = width,
                           height = height,
                        #    border_width = border_width,
                           corner_radius = corner_radius,
                        #    border_color = border_color,
                           text = text,
                           fg_color= "gray17",
                           image = image,
                           hover_color = "gray12",
                           command= command
                        #    img = img
    )
    return button
# FRAME 3

button_play = create_button(
    master= m_app.main_app.FRAME3,
    image = c_img.image_button_play,
    width = 166,
    height= 60,
    text = None,
    command= music.music_play
    )
button_play.place(x= 11, y= 11)


button_r = create_button(
    master = m_app.main_app.FRAME3,
    image= c_img.image_button_r,
    width = 60,
    height= 60,
    text = None,   
    command = music.prev_song
)
button_r.place(x= 11, y = 82)

button_l = create_button(
    master = m_app.main_app.FRAME3,
    image= c_img.image_button_l,
    width = 60,
    height= 60,
    text = None,   
    command = music.next_song
)
button_l.place(x= 117, y = 82)

button_pause = create_button(
    master = m_app.main_app.FRAME3,
    image= c_img.image_button_pause,
    width = 166,
    height= 60,
    text = None,
    command = music.music_pause)
button_pause.place(x = 11, y = 153)

button_stop = create_button(
    master = m_app.main_app.FRAME3,
    image= c_img.image_button_stop,
    width = 166,
    height= 60,
    text = None,
    command = music.music_stop)
button_stop.place(x = 11, y = 224)


#  FRAME4

# def open_file():
#     ctk.filedialog.askopenfile()

# def open_file():
#     global file, list_music, content
#     file = ctk.filedialog.askopenfile(mode ='r', filetypes =[('Файл "MP3"', '*.mp3')])
#     # file = ctk.filedialog.asksaveasfile(mode='r', filetypes =[('Open a .mp3 file', '*.mp3')])
#     if file is not None:
#         content = file.name
#         print(content)
#         list_music.append(content)
#         print(list_music)

        # list_music[ content]
        # print(list_music)
    # ctk.filedialog.SaveAs(master= f_p.find_path_file("music//"))
    # ctk.filedialog.SaveAs(master= list_music)

# def print(list_music):
#     # global list_music
#     print(list_music)

button_add = create_button(
    master= m_app.main_app.FRAME4,
    image= c_img.image_button_add,
    width = 50,
    height = 47,
    text = None,
    command= music.open_file
    )
button_add.place(x= 16, y= 11)

button_delete = create_button(
    master= m_app.main_app.FRAME4,
    image= c_img.image_button_delete,
    width = 50,
    height = 47,
    text = None,
    command = music.music_delete)
button_delete.place(x= 103, y= 11)

button_mix = create_button(
    master= m_app.main_app.FRAME4,
    image= c_img.image_button_mix,
    width = 50,
    height = 47,
    text = None,
    command = music.music_mix)
button_mix.place(x= 190, y= 11)

button_sound_p = create_button(
    master= m_app.main_app.FRAME4,
    image= c_img.image_button_sound_p,
    width = 50,
    height = 47,
    text = None,
    command = music.music_volume_p)
    
button_sound_p.place(x= 277, y= 11)

button_sound_m = create_button(
    master= m_app.main_app.FRAME4,
    image= c_img.image_button_sound_m,
    width = 50,
    height = 47,
    text = None,
    command = music.music_volume_m)
button_sound_m.place(x= 364, y= 11)

# FRAME 1 

# music_1 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = c_music.list_music,
#     fg_color = None,
#     command = None)
# music_1.place(x= 25, y= 50)

# music_2 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = "Music_2",
#     fg_color = None,
#     command = None)
# music_2.place(x= 25, y= 111)

# music_3 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = "Music_3",
#     fg_color = None,
#     command = None)
# music_3.place(x= 25, y= 172)

# music_4 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = "Music_4",
#     fg_color = None,
#     command = None)
# music_4.place(x= 25, y= 233)

# music_5 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = "Music_5",
#     fg_color = None,
#     command = None)
# music_5.place(x= 25, y= 294)

# music_6 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = "Music_6",
#     fg_color = None,
#     command = None)
# music_6.place(x= 25, y= 355)

# music_7 = create_button(
#     master= m_app.main_app.FRAME,
#     image= c_img.image_button_music_1,
#     width = 150,
#     height = 50,
#     text = "Music_7",
#     fg_color = None,
#     command = None)
# music_6.place(x= 25, y= 416)
