import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku di tekan") 
    label2.pack()

label = tkinter.Label(main_window, text= "halo guys \n ini adalah GUI sederhana \n dengan enggunakan python" )
tombol = tkinter.Button(main_window, text= "tekan", command = event_tekan) 

label.pack()
tombol.pack()
main_window.mainloop()