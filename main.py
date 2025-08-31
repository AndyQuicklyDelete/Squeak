import os
from tkinter import *
from tkinter import filedialog as tkFileDialog
from tkinter import font
from tkinter import ttk
from PIL import ImageTk, Image
from pydub import AudioSegment
# from playsound import playsound
import winsound
import pyaudiowpatch as pyaudio
import time
import wave
from threading import *


click_list = []

FILEOPENOPTIONS = dict(defaultextension='.wav',
                  filetypes=[('Wav files','*.wav')]) #('All files','*.*'), 

def open_mouse_one():
    global mouse_one
    mouse_one = tkFileDialog.askopenfilename(title="Select for left mouse button", **FILEOPENOPTIONS)
    if not mouse_one:
        return
    
    with open("lmb", "w") as lmb:
        lmb.write(mouse_one)

def open_mouse_three():
    global mouse_three
    mouse_three = tkFileDialog.askopenfilename(title="Select for right mouse button", **FILEOPENOPTIONS)
    if not mouse_three:
        return

    with open("rmb", "w") as rmb:
        rmb.write(mouse_three)

def open_mouse_four():
    global mouse_four
    mouse_four = tkFileDialog.askopenfilename(title="Select for side mouse button 1", **FILEOPENOPTIONS)
    if not mouse_four:
        return
    
    with open("smb1", "w") as smb_one:
        smb_one.write(mouse_four)

def open_mouse_five():
    global mouse_five
    mouse_five = tkFileDialog.askopenfilename(title="Select for side mouse button 2", **FILEOPENOPTIONS)
    if not mouse_five:
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
        winsound.PlaySound(None, winsound.SND_PURGE)
        output.insert(END, "[+] Audio playback is muted\n")
        output.yview(END)
        volumeBtn.configure(image=mutePhoto)
        muted = True

def firstToKick(event):
    try:
        if os.path.exists('lmb') and os.path.getsize('lmb') > 0:
            mouse_one = open('lmb', 'r')
            mouse_one = mouse_one.read()
        if muted == False:
            winsound.PlaySound(mouse_one, winsound.SND_ASYNC)
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

def firstToClap(event):
    try:
        if os.path.exists('rmb') and os.path.getsize('rmb') > 0:
            mouse_three = open('rmb', 'r')
            mouse_three = mouse_three.read()
        if muted == False:
            winsound.PlaySound(mouse_three, winsound.SND_ASYNC)
            # playsound(mouse_three, block = False)
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
    try:
        if os.path.exists('smb1') and os.path.getsize('smb1') > 0:
            mouse_four = open('smb1', 'r')
            mouse_four = mouse_four.read()
        if muted == False:
            winsound.PlaySound(mouse_four, winsound.SND_ASYNC)
            # playsound(mouse_four, block = False)
            click_list.append(mouse_four)
        else:
            click_list.append(mouse_four)
    except:
        output.insert(END, "[-] Please assign a music file to the Side Mouse Button 1\n")
        output.yview(END)
        return

    canvas.itemconfigure('event', text='{0}'.format(os.path.basename(click_list[-1]).split('/')[-1]))
    xpos = (canvas.winfo_width() / 2)
    ypos = (canvas.winfo_height() / 2)

    canvas.coords(mytext, xpos, ypos)
    canvas.itemconfigure('event', font=('helvetica 30 normal'))

    output.insert(END, str(os.path.basename(mouse_four).split('/')[-1]) + "\n")
    output.yview(END)

def firstToSnare(event):
    try:
        if os.path.exists('smb2') and os.path.getsize('smb2') > 0:
            mouse_five = open('smb2', 'r')
            mouse_five = mouse_five.read()
        if muted == False:
            winsound.PlaySound(mouse_five, winsound.SND_ASYNC)
            # playsound(mouse_five, block = False)
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

def record_threaded(event):
    mythread = Thread(target=record_from_speaker, args=(event,))
    mythread.start()

def record_from_speaker(event):
    value = n.get().strip()
    if value == "--- No record option selected ---":
        return
    else:
        DURATION = float(value)

        output.insert(END, "[+] Your recording time will begin in 5 seconds\n")
        output.yview(END)

        seconds = 0
        for i in range(0, 5):
            seconds += 1
            time.sleep(1)
            output.insert(END, "[+] \t\t%s\n" % seconds)
            output.yview(END)
            
        CHUNK_SIZE = 512

        folder = save_path.get()
        # os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        filename = "loopback_record.wav"

        desktop = folder + "\\" + filename

        with pyaudio.PyAudio() as p:
            try:
                # Get default WASAPI info
                wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
            except OSError:
                output.insert(END, "[-] Looks like WASAPI is not available on the system. Exiting...\n")
                output.yview(END)
                exit()

            # Get default WASAPI speakers
            default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])

            if not default_speakers["isLoopbackDevice"]:
                for loopback in p.get_loopback_device_info_generator():
                    """
                    Try to find loopback device with same name(and [Loopback suffix]).
                    Unfortunately, this is the most adequate way at the moment.
                    """
                    if default_speakers["name"] in loopback["name"]:
                        default_speakers = loopback
                        break
                else:
                    output.insert(END, "[-] Default loopback output device not found. Exiting...\n")
                    output.yview(END)
                    exit()
                    
            output.insert(END, "[+] Recording from: (%s) %s\n\n" % (default_speakers['index'], default_speakers['name']))
            output.yview(END)

            wave_file = wave.open(desktop, 'wb')
            wave_file.setnchannels(default_speakers["maxInputChannels"])
            wave_file.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
            wave_file.setframerate(int(default_speakers["defaultSampleRate"]))

            def callback(in_data, frame_count, time_info, status):
                wave_file.writeframes(in_data)
                return (in_data, pyaudio.paContinue)

            with p.open(format=pyaudio.paInt16, channels=default_speakers["maxInputChannels"], rate=int(default_speakers["defaultSampleRate"]), frames_per_buffer=CHUNK_SIZE, input=True, input_device_index=default_speakers["index"],stream_callback=callback) as stream:
                output.insert(END, "[+] The next %s seconds will be recorded and saved to %s\n\n" % (DURATION, folder))
                output.yview(END)
                time.sleep(DURATION)
            
            output.insert(END, "[+] The recording time is over and your file has been saved to %s\n" % (desktop))
            output.yview(END)
            wave_file.close()
        
        click_list.clear()
        output.insert(END, "[+] After recording your squeaklist is now cleared\n")
        output.yview(END)


root = Tk()
root.title("Squeak Music Alchemy")
root.iconbitmap("squeakicon.ico")
root.option_readfile("optionDB")
root.geometry("584x800")
root.resizable(0, 1)

frame = Frame(root)
leftButton = ImageTk.PhotoImage(Image.open('buttons\\left.png'))
button = Button(frame, image=leftButton, command=open_mouse_one)
button.pack(side=LEFT, padx=10)
rightButton = ImageTk.PhotoImage(Image.open('buttons\\right.png'))
button = Button(frame, image=rightButton, command=open_mouse_three)
button.pack(side=LEFT, padx=10)
sideButton1 = ImageTk.PhotoImage(Image.open('buttons\\side1.png'))
button = Button(frame, image=sideButton1, command=open_mouse_four)
button.pack(side=LEFT, padx=10)
sideButton2 = ImageTk.PhotoImage(Image.open('buttons\\side2.png'))
button = Button(frame, image=sideButton2, command=open_mouse_five)
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
volumeBtn.pack(side=LEFT, padx=(0, 10))

frame.pack(fill=X)

frame = Frame(root)
canvas = Canvas(frame, bg="bisque", width=500, height=300)
canvas.bind("<Button-1>", firstToKick)
canvas.bind("<Button-3>", firstToClap)
canvas.bind("<Button-4>", firstToHit)
canvas.bind("<Button-5>", firstToSnare)
canvas.pack(fill='both', expand = True, padx=10, pady=10)

background = ImageTk.PhotoImage(Image.open('wallpaper.jpg'))
canvas.create_image(0, 0, image=background, anchor=NW)

mytext = canvas.create_text(275, 150, fill='white', anchor="c", tags=['event'])

frame.pack(fill='both', expand = True)

root.option_add("*selectBackground", "#5db2ff")
root.option_add("*selectForeground", "white")
bigfont = font.Font(family="Segoe UI", size=13)
root.option_add("*TCombobox*Font", bigfont)

frame = Frame(root)
n = StringVar(value='--- No record duration selected ---') 
record_duration = ttk.Combobox(frame, textvariable=n)
record_duration['values'] = (
    '5.0',
    '10.0',
    '15.0',
    '30.0',
    '60.0')
record_duration.bind("<<ComboboxSelected>>", record_threaded)
record_duration.pack(fill=BOTH, expand=True)
frame.pack(fill=X, padx=10, pady=(0, 10))


frame = Frame(root)
scrollbar2 = Scrollbar(frame)
scrollbar2.pack(side=RIGHT, fill=Y)
output = Text(frame, font=("Segoe UI", 11))
output.pack(fill=BOTH, expand=True)
output.insert(END, "Status of squeak music playback, or squeakback\n")
output.insert(END, "Your current squeaklist will appear below as you create\n")
output.yview(END)
output.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=output.yview)
frame.pack(fill=BOTH, expand=True)

root.mainloop()