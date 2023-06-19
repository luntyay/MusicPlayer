import pygame
import customtkinter as ctk
import modules.screen_app as m_app
import modules.sound as sound
import random

pygame.init()
pygame.mixer.init()

list_of_song_frames = []
listofsongs = []
names = []
message_y = 0
el = 0
all_list_m = []
i_2 = 0.5
pygame.mixer.music.set_volume(i_2)
index = 0
SONG_END = pygame.USEREVENT + 1
event = False


pygame.mixer.music.set_volume(1.0)

def updatelabel():
    global index
    m_app.main_app.SONG_NAME.set(names[index])



def open_file():
    # работает 
    global file
    file = ctk.filedialog.askopenfile(mode ='r', filetypes =[('Файл "MP3"', '*.mp3'), ('Файл "MP4"', "*.mp4")])
    dowload_file()


def dowload_file():
    # работает 
    global listofsongs, names, file, content
    if file is not None:
        content = file.name

        names.append(f"{content.split('/')[-1]}")
        listofsongs.append(content)

        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.queue(content, loops= -1)
        pygame.mixer.music.set_endevent(SONG_END)
        m_app.main_app.SONG_NAME.set(names[0])

        add_song_frame()


def add_song_frame():
    global song_frame, listofsongs, names, file, content, event, message_y
    song_frame = sound.MessageFrame(text= content.split("/")[-1],
                                    master= m_app.main_app.FRAME, 
                                    width= 200, 
                                    height= 50,
                                    border_width= 2,
                                    bg_color= None)
    # song_frame.place_sound()
    # song_frame.grid(row = message_y, pady = 10)

    # button = ctk.CTkButton(master = song_frame,
    #                 width = 30,
    #                 height = 30,
    #                 corner_radius = 5,
    #                 text= None,
    #                 fg_color= "gray",
    #                 hover_color = "gray12",
    #                 command= music_delete )
    
                    # command= None )
    # button.place(x= 11, y= 11)
    # message_y += 1


    list_of_song_frames.append(song_frame)

    if event == False:
        song_frame.place_sound()
        song_frame.grid(row = message_y, pady = 10)
        message_y += 1
        print(event)

    else:
        song_frame.grid_remove()
        event = False
        print(111)
    
    # button.place(x= 11, y= 11)



def music_play():
    # работает, но осталось ещё сделать подсветку для работающей музыки
    if pygame.mixer.music.get_busy() == True:
        pass
    elif pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_endevent(SONG_END)
        # list_of_song_frames[index].bg_color = "red"
        updatelabel()
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
            # list_of_song_frames[index].bg_color = "red"
            updatelabel()
    



def music_pause():
    # работает
    if pygame.mixer.music.get_busy() == True:
        pygame.mixer.music.pause()
    elif pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()



def music_stop():
    # работает
    pygame.mixer.music.stop()
    pygame.mixer.music.set_endevent(SONG_END)
    m_app.main_app.SONG_NAME.set("")

       


def music_delete():
    # работает
    global event, index
    event = True
    print(event)

    pygame.mixer.music.unload()

    list_of_song_frames[index].grid_remove()
    
    del list_of_song_frames[index]
    del listofsongs[index]
    del names[index]
    m_app.main_app.SONG_NAME.set("")
    # if names[index] == song_frame.SOUND:
    
    # add_song_frame()
    if len(listofsongs) >= 1:
        prev_song()
        # add_song_frame()
        music_pause()
    # elif len(listofsongs) == 0:
    #     index = index - 1

    event = False
    updatelabel()



def music_volume_p():
    # работает
    global i_2
    i = 0.1
    if i_2 < 1.0:
        pygame.mixer.music.set_volume(i_2 + i)
        i_2 = i_2 + i
        print(i_2)
    else:
        pygame.mixer.music.set_volume(1.0)
    return i, i_2

def music_volume_m():
    # работает
    global i_2
    i = 0.1
    if not i_2 <= 0.0:
        pygame.mixer.music.set_volume(i_2 - i)
        i_2 = i_2 - i
        print(i_2)
    else:
        pygame.mixer.music.set_volume(0.0)
    return i, i_2



def next_song():
    # работает
    global index
    try:
        index +=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()
    except:
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()



def prev_song():
    # работает
    global index
    try:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()
    except:
        index = -1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()



def music_mix():
    # работает
    global random_music, listofsongs

    i = len(listofsongs) - 1

    random_music = random.randint(0, i)

    pygame.mixer.music.load(listofsongs[random_music])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(SONG_END)
    m_app.main_app.SONG_NAME.set(names[random_music])














