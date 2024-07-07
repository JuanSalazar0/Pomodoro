#Juan Salazar 25/05/2024
#Last update 29/06/2024
#---------------------------Libreias DEL PROYECTO------------------------------------
from customtkinter import *
import time
import threading
import pywhatkit
from plyer import notification
#Define el tiempo de concentracion y de descanso en minutos, time in minutos for rest (r_timer) and concentration time (c_timer)
c_timer=25
r_timer=5
#Arreglo de musica 
music=["this playlist will make you feel like a 19th century villain",
       "Study with Me in Skyrim | College of Winterhold Library | 25/5 Pomodoro Timer [2hr] [4K]",
       "Fallout New Vegas Radio - All Songs - Low data use",
       "MedievaLo-Fi | Lofi Beats for the Medieval Knight you always wanted to be"]

#---------------------------Inicio del programa------------------------------------
app = CTk()
set_appearance_mode("dark") #podemos hacer la funcion de modo oscuro o con luz
app.geometry("250x270") #Tamaño de la ventana principal
#PANTALLA DE INCIO
frame_settings = CTkFrame(master=app, fg_color="#6C9D7C", #Frame (color verde)
                        border_color="#15BF00", border_width=2)
frame_settings.pack(expand=True)
frame_settings._set_dimensions(width=180, height=200)
frame_settings.place(relx=0.5, rely=0.43,anchor="center")

bar_label= CTkLabel(master=frame_settings, text="Settings", 
                  font=("Arial black",13),text_color="black")
bar_label.place(relx=0.50, rely=0.125,anchor="center")

switch_var1 = StringVar(value="on")
switchbar = CTkSwitch(master=frame_settings, text="Progress Bar",
                        border_color="black",text_color="black",
                        variable=switch_var1, onvalue="on", offvalue="off")
switchbar.place(relx=0.50, rely=0.30,anchor="center")

switch_var2 = StringVar(value="on")
switchttime = CTkSwitch(master=frame_settings, text="Timer",
                        border_color="black",text_color="black",
                        variable=switch_var2, onvalue="on", offvalue="off")
switchttime.place(relx=0.46, rely=0.5,anchor="center")

musica1 = CTkLabel(master=frame_settings, text="Music on YT", 
                  font=("Arial black",13),text_color="black")
musica1.place(relx=0.50, rely=0.65,anchor="center")

optionmenu_var = StringVar(value="No music")
optionmenu = CTkOptionMenu(master=frame_settings,
                           values=["19th century villain", "Skyrim", "Fallout NV","MedievaLo-Fi","No music"],
                           variable=optionmenu_var,
                           corner_radius=12)
optionmenu.place(relx=0.50, rely=0.8,anchor="center")

#Los valores de los botones de settings regresan un string
def start():
    btn.after(10,frame_settings.destroy)
    btn.after(10,btn.destroy)
    musicYT()
    #print(f"Este el estaedo del timer: {switchttime.get()}")
    #print(f"Este el estaedo de la barra: {switchbar.get()}")
    
    thread1 = threading.Thread(target=timepo25)
    thread1.start()
    
def musicYT():
    x=optionmenu.get()
    if x == "19th century villain": y=0
    if x == "Skyrim": y=1
    if x == "Fallout NV": y=2
    if x == "MedievaLo-Fi": y=3
    if x == "No music": y=4
    if y == 4:
        pass
    else:
        pywhatkit.playonyt(music[y])

def noti(t_concen_on):
    if(t_concen_on == TRUE):
        notification.notify(
            title="Concentrate!",
            message="Es hora de trabajar en eso que deseas",
            app_name="Pomodoro de JP",
            app_icon="timer.ico",

        ) 
    else:
        notification.notify(
            title="Descansa",
            message="Es necesario descansar, esto no es una carrera es un marathon",
            app_name="Pomodoro de JP",
            app_icon="timer.ico",
        )        

def timepo25():
    app.geometry("260x180")
    flag4work=0
    btnquit = CTkButton(master=app, text="Quit", corner_radius=32, 
                hover_color="red",command=quit, width=80, height=28)
    btnquit.place(relx=0.95, rely=0.82, anchor="se")
    noti(TRUE)
    while flag4work != 4:
        title_label= CTkLabel(master=app, text="Concentration:", 
                  font=("Arial black",20),text_color="white")
        title_label.place(relx=0.50, rely=0.30,anchor="center")

        if switchttime.get() == "on":
            timer_label= CTkLabel(master=app, text="25 minutes", 
                        font=("Arial black",20),text_color="white")
            timer_label.place(relx=0.50, rely=0.45,anchor="center")
        
        if switchbar.get() == "on":
            progressbar = CTkProgressBar(master=app, orientation="horizontal",
                                        width=250, height=20, corner_radius=12,
                                        progress_color="green")   
            progressbar.place(relx=0.50, rely=0.60,anchor="center")
            progressbar.set(0)
        
        textcount=f"Number of pomodoros: {flag4work}"
        count_label= CTkLabel(master=app, text=textcount, 
                    font=("Arial",10),text_color="white")
        count_label.place(relx=0.50, rely=0.82,anchor="se")

        i25 = c_timer*60 #Tiempo pomodoro hora
        sp25 = i25 #variable auxiliar qde barra
        while True:
            x= (1-((1*i25)/sp25))
            if switchbar.get() == "on":progressbar.set(x)
            if switchttime.get() == "on":
                minutes=int(i25/60)
                seconds=int(i25%60)
                timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
            i25 -= 1
            #print(i25)
            if i25 < 0:
                break
            time.sleep(1)
        noti(FALSE)
        flag4work=flag4work+1
        textcount=f"Number of pomodoros: {flag4work}"
        count_label= CTkLabel(master=app, text=textcount, 
                    font=("Arial",10),text_color="white")
        count_label.place(relx=0.50, rely=0.82,anchor="se")

        #Inicio descanso
        title_label.destroy()

        title_label= CTkLabel(master=app, text="Rest:", 
                  font=("Arial black",20),text_color="white")
        title_label.place(relx=0.50, rely=0.30,anchor="center")

        if switchttime.get() == "on":
            timer_label= CTkLabel(master=app, text="5 minutes", 
                        font=("Arial black",20),text_color="white")
            timer_label.place(relx=0.50, rely=0.45,anchor="center")

        if switchbar.get() == "on":
            progressbar = CTkProgressBar(master=app, orientation="horizontal",
                                        width=250, height=20, corner_radius=12,
                                        progress_color="green")   
            progressbar.place(relx=0.50, rely=0.60,anchor="center")
            progressbar.set(0)
        
        i5 = r_timer*60 #Tiempo descanso hora 
        sp5 = i5 #variable auxiliar qde barra 
        while True:
            x= (1-((1*i5)/sp5))
            if switchbar.get() == "on":progressbar.set(x)
            if switchttime.get() == "on":
                minutes=int(i5/60)
                seconds=int(i5%60)
                timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
            i5 -= 1
            #print(i5)
            if i5 < 0:
                break
            time.sleep(1)
        title_label.destroy()
        noti(TRUE)

    #final pomodoro
    title_label= CTkLabel(master=app, text="Congrats!", 
                  font=("Arial black",20),text_color="white")
    title_label.place(relx=0.50, rely=0.30,anchor="center")
    timer_label= CTkLabel(master=app, text="You finished", 
                    font=("Arial black",20),text_color="white")
    timer_label.place(relx=0.50, rely=0.45,anchor="center")
    textcount=f"Number of pomodoros: {flag4work}"
    count_label= CTkLabel(master=app, text=textcount, 
                    font=("Arial",10),text_color="white")
    count_label.place(relx=0.50, rely=0.82,anchor="se")
    
btn = CTkButton(master=app, text="Start", corner_radius=32, 
                hover_color="green",command=start)
btn.place(relx=0.5, rely=0.9, anchor="center")
app.mainloop()
