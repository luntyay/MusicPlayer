import customtkinter
from PIL import Image
import modules.find_path as f_p

image_button_play = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_PLAY.png")), size= (150, 50))
image_button_l = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_l.png")), size= (50, 50))
image_button_r = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_r.png")), size= (50, 50))
image_button_pause = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_PAUSE.png")), size= (150, 50))
image_button_stop = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_STOP.png")), size= (150, 50))
image_button_add = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_ADD.png")), size= (45, 42))
image_button_delete = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_Delete.png")), size= (45, 42))
image_button_mix = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_MIX.png")), size= (45, 42))
image_button_sound_p = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_SOUND +.png")), size= (45, 42))
image_button_sound_m = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_SOUND -.png")), size= (45, 42))
image_button_music_1 = customtkinter.CTkImage(light_image = Image.open(f_p.find_path_file("images\\Button_ADD.png")), size= (45, 42))

# list_image= [image_button_play,
#              image_button_l,
#              image_button_r,
#              image_button_pause,
#              image_button_stop,
#              image_button_add,
#              image_button_delete,
#              image_button_mix,
#              image_button_sound_p,
#              image_button_sound_m,
#              image_button_music_1]

# i = 0
# for i in range(len(list_image)):
#     list_image[i].itemconfig()

# if "image" in kwargs:
#             if isinstance(self._image, CTkImage):
#                 self._image.remove_configure_callback(self._update_image)
#             self._image = self._check_image_type(kwargs.pop("image"))
#             if isinstance(self._image, CTkImage):
#                 self._image.add_configure_callback(self._update_image)
#             self._update_image()

