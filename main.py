
# import pygame
# from pynput import mouse
# from pynput import keyboard
# from pynput.keyboard import Listener as KeyboardListener
# from pynput.mouse import Listener as MouseListener
# from infi.systray import SysTrayIcon
import os
from tkinter import *
from tkinter import filedialog as tkFileDialog
from PIL import ImageTk, Image
from pydub import AudioSegment
from playsound import playsound

# import time

# pygame.mixer.init()

# file_to_kick        =       "kick1.wav"
# file_to_clap        =       "clap1.wav"
# file_to_hit         =       "hit1.wav"
# file_to_snare       =       "snare1.wav"

# kick_sound          =       pygame.mixer.Sound(file_to_kick)
# clap_sound          =       pygame.mixer.Sound(file_to_clap)
# hit_sound           =       pygame.mixer.Sound(file_to_hit)
# snare_sound         =       pygame.mixer.Sound(file_to_snare)

click_list = []

# def exit_action(icon):
#     with open("squeaks_gen.txt", "w") as output:
#         for row in click_list:
#             s = "".join(map(str, row))
#             output.write(s + '\n')

#     print("[+] Music sheet recorded")
#     os._exit(1)

def open_mouse_one():
    global mouse_one
    mouse_one = tkFileDialog.askopenfilename(initialdir=os.getcwd(), title="Select for left mouse button", filetypes=(("mp3 files", "*.mp3"), ("wav Files", "*.wav*")))
    if not mouse_one:
        # mouse_one = file_to_kick
        return
    
    with open("lmb", "w") as lmb:
        lmb.write(mouse_one)

def open_mouse_three():
    global mouse_three
    mouse_three = tkFileDialog.askopenfilename(initialdir=os.getcwd(), title="Select for right mouse button", filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav*")))
    if not mouse_three:
        # mouse_three = file_to_clap
        return

    with open("rmb", "w") as rmb:
        rmb.write(mouse_three)

def open_mouse_four():
    global mouse_four
    mouse_four = tkFileDialog.askopenfilename(initialdir=os.getcwd(), title="Select for side mouse button 1", filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav*")))
    if not mouse_four:
        # mouse_four = file_to_hit
        return
    
    with open("smb1", "w") as smb_one:
        smb_one.write(mouse_four)

def open_mouse_five():
    global mouse_five
    mouse_five = tkFileDialog.askopenfilename(initialdir=os.getcwd(), title="Select for side mouse button 2", filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav*")))
    if not mouse_five:
        # mouse_five = file_to_snare
        return
    
    with open("smb2", "w") as smb_two:
        smb_two.write(mouse_five)

def save_directory():
    if click_list == []:
        output.insert(END, "[-] Your squeaklist is currently empty\n")
        output.insert(END, "[-] Please create a new beat before saving once again\n")
        output.yview(END)
        return
    else:
        #save_path.delete(0, END)
        opened = tkFileDialog.askdirectory()
        if not opened:
            return
        
        save_path.delete(0, END)
        save_path.insert(END, opened)

        with open(opened + "\\squeaks_gen.txt", "w") as audio_output:
            for row in click_list:
                s = "".join(map(str, row))
                audio_output.write(s + '\n')

        output.insert(END, "[+] Music sheet recorded\n")
        output.insert(END, "[+] Generating music file\n")
        output.yview(END)

        with open(opened + '\\squeaks_gen.txt', 'r') as file:
            lines = []

            for line in file:
                line = line.strip()
                lines.append(line)

        wavs = lines

        combined_wav = AudioSegment.empty()
        for wav in wavs:                                                            
            order = AudioSegment.from_wav(wav)                                                          
            combined_wav += order 

        combined_wav.export(opened + "\\merged_sound.mp3", format="mp3", bitrate="192k")
        output.insert(END, "[+] Generated music file saved as merged_sound.mp3\n")
        output.yview(END)

        click_list.clear()
        output.insert(END, "[+] After being saved your squeaklist is now cleared\n")
        output.yview(END)

muted = False

def mute_music():
    global muted
    if muted == True:  # Unmute the music
        output.insert(END, "[+] Audio playback is unmuted\n")
        output.yview(END)
        volumeBtn.configure(image=volumePhoto)
        muted = False
    else:  # mute the music
        output.insert(END, "[+] Audio playback is muted\n")
        output.yview(END)
        volumeBtn.configure(image=mutePhoto)
        muted = True

def firstToKick(event):
    # length = kick_sound.get_length()
    # kick_sound.play()
    # playsound(file_to_kick, block = False)
    try:
        if os.path.exists('lmb') and os.path.getsize('lmb') > 0:
            mouse_one = open('lmb', 'r')
            mouse_one = mouse_one.read()
        if muted == False:
            playsound(mouse_one, block = False)
            click_list.append(mouse_one)
        else:
            click_list.append(mouse_one)
    except:
        output.insert(END, "[-] Please assign a music file to the Left Mouse Button\n")
        output.yview(END)
        return

    canvas.itemconfigure('event', text='{0}'.format(os.path.basename(click_list[-1]).split('/')[-1]))
    xpos = (canvas.winfo_width() / 2)
    ypos = (canvas.winfo_height() / 2)

    canvas.coords(mytext, xpos, ypos)
    canvas.itemconfigure('event', font=('helvetica 30 normal'))
    
    output.insert(END, str(os.path.basename(mouse_one).split('/')[-1]) + "\n")
    output.yview(END)
    # time.sleep(length)

def firstToClap(event):
    # clap_sound.play()
    # playsound(file_to_clap, block = False)
    try:
        if os.path.exists('rmb') and os.path.getsize('rmb') > 0:
            mouse_three = open('rmb', 'r')
            mouse_three = mouse_three.read()
        if muted == False:
            playsound(mouse_three, block = False)
            click_list.append(mouse_three)
        else:
            click_list.append(mouse_three)
    except:
        output.insert(END, "[-] Please assign a music file to the Right Mouse Button\n")
        output.yview(END)
        return

    canvas.itemconfigure('event', text='{0}'.format(os.path.basename(click_list[-1]).split('/')[-1]))
    xpos = (canvas.winfo_width() / 2)
    ypos = (canvas.winfo_height() / 2)

    canvas.coords(mytext, xpos, ypos)
    canvas.itemconfigure('event', font=('helvetica 30 normal'))
    
    output.insert(END, str(os.path.basename(mouse_three).split('/')[-1]) + "\n")
    output.yview(END)

def firstToHit(event):
    # hit_sound.play()
    # playsound(file_to_hit, block = False)
    try:
        if os.path.exists('smb1') and os.path.getsize('smb1') > 0:
            mouse_four = open('smb1', 'r')
            mouse_four = mouse_four.read()
        if muted == False:
            playsound(mouse_four, block = False)
            click_list.append(mouse_four)
        else:
            click_list.append(mouse_four)
    except:
        output.insert(END, "[-] Please assign a music file to the Side Mouse Button 1\n")
        output.yview(END)
        return
    # click_list.append(file_to_hit)

    canvas.itemconfigure('event', text='{0}'.format(os.path.basename(click_list[-1]).split('/')[-1]))
    xpos = (canvas.winfo_width() / 2)
    ypos = (canvas.winfo_height() / 2)

    canvas.coords(mytext, xpos, ypos)
    canvas.itemconfigure('event', font=('helvetica 30 normal'))

    output.insert(END, str(os.path.basename(mouse_four).split('/')[-1]) + "\n")
    output.yview(END)

def firstToSnare(event):
    # snare_sound.play()
    # playsound(file_to_snare, block = False)
    # click_list.append(file_to_snare)

    try:
        if os.path.exists('smb2') and os.path.getsize('smb2') > 0:
            mouse_five = open('smb2', 'r')
            mouse_five = mouse_five.read()
        if muted == False:
            playsound(mouse_five, block = False)
            click_list.append(mouse_five)
        else:
            click_list.append(mouse_five)
    except:
        output.insert(END, "[-] Please assign a music file to the Side Mouse Button 2\n")
        output.yview(END)
        return

    canvas.itemconfigure('event', text='{0}'.format(os.path.basename(click_list[-1]).split('/')[-1]))
    xpos = (canvas.winfo_width() / 2)
    ypos = (canvas.winfo_height() / 2)

    canvas.coords(mytext, xpos, ypos)
    canvas.itemconfigure('event', font=('helvetica 30 normal'))

    output.insert(END, str(os.path.basename(mouse_five).split('/')[-1]) + "\n")
    output.yview(END)


root = Tk()
root.title("Squeak Music Alchemy")
root.iconbitmap("squeakicon.ico")
root.option_readfile("optionDB")

frame = Frame(root)
button = Button(frame, text="Left Mouse Button", command=open_mouse_one)
button.pack(side=LEFT, padx=10)
button = Button(frame, text="Right Mouse Button", command=open_mouse_three)
button.pack(side=LEFT, padx=10)
button = Button(frame, text="Side Mouse Button 1", command=open_mouse_four)
button.pack(side=LEFT, padx=10)
button = Button(frame, text="Side Mouse Button 2", command=open_mouse_five)
button.pack(side=LEFT, padx=10)
frame.pack(fill=X)

frame = Frame(root)
save_path = Entry(frame)
save_path.pack(side=LEFT, fill=X, expand=True, padx=10)
save_path.insert(END, os.getcwd())
button = Button(frame, text="Choose Save Folder", command=save_directory)
button.pack(side=LEFT)

mutePhoto = ImageTk.PhotoImage(Image.open('mute.png'))
volumePhoto = ImageTk.PhotoImage(Image.open('volume.png'))
volumeBtn = Button(frame, image=volumePhoto, command=mute_music)
volumeBtn.pack(side=LEFT)

frame.pack(fill=X)

frame = Frame(root)
canvas = Canvas(frame, bg="bisque", width=500, height=300)
canvas.bind("<Button-1>", firstToKick)
canvas.bind("<Button-3>", firstToClap)
canvas.bind("<Button-4>", firstToHit)
canvas.bind("<Button-5>", firstToSnare)
canvas.pack(fill='both', expand = True, padx=10, pady=10)

background = ImageTk.PhotoImage(Image.open('ocean.jpg'))
canvas.create_image(0, 0, image=background, anchor=NW)

mytext = canvas.create_text(275, 150, fill='black', anchor="c", tags=['event'])

frame.pack(fill='both', expand = True)

frame = Frame(root)
scrollbar2 = Scrollbar(frame)
scrollbar2.pack(side=RIGHT, fill=Y)
output = Text(frame)
output.pack(fill=BOTH, expand=True)
output.insert(END, "Status of squeak music playback, or squeakback\n")
output.insert(END, "Your current squeaklist will appear below as you create\n")
output.yview(END)
output.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=output.yview)
frame.pack(fill=BOTH, expand=True)

root.mainloop()


# def on_click(x, y, button, pressed):
#     if pressed and button == mouse.Button.left:
#         firstToKick()
#         click_list.append(file_to_kick)

#     if pressed and button == mouse.Button.right:
#         firstToClap()
#         click_list.append(file_to_clap)
    
#     if pressed and button == mouse.Button.x1:
#         firstToHit()
#         click_list.append(file_to_hit)

#     if pressed and button == mouse.Button.x2:
#         firstToSnare()
#         click_list.append(file_to_snare)

# def on_press(key):
#     # print(str(key))

#     if key == keyboard.Key.esc:     
#         print("[+] The program Squeak has ended after pressing the Esc key")
#         exit_action(icon)

#     if key == keyboard.Key.f8:
#         mouse_listener.stop()
#         print("[+] The Mouse Listener has stopped after pressing the f8 key")

#     # if key == keyboard.Key.f1:
#     #     with MouseListener(on_click=on_click) as mouse_listener_reload:
#     #         with KeyboardListener(on_press=on_press) as keyboard_listener:
#     #             mouse_listener_reload.join()
#     #             keyboard_listener.join()
                
# if __name__ == '__main__':
#     menu_options = "" #(("Exit Squeak", None, lambda : exit_action(icon)),)
#     icon = SysTrayIcon("squeakicon.ico", "Squeak 1.0.0", menu_options, on_quit=exit_action)

#     with MouseListener(on_click=on_click) as mouse_listener:
#         with KeyboardListener(on_press=on_press) as keyboard_listener:
#             icon.start()
#             mouse_listener.join()
#             keyboard_listener.join()
            