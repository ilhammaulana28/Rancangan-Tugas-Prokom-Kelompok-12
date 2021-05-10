from tkinter import *
from PIL import Image, ImageTk


def frame_1(frame):
    frame.tkraise()

root = Tk()
root.geometry('499x500')
#  root.state('zoomed')
root.title('Soetta-Loka')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


logo = Image.open('logo soettaloka.png')
logo_ico = ImageTk.PhotoImage(logo)
root.wm_iconphoto(False, logo_ico)

main_page = Frame(root)
main_page.grid(row=0, column=0, sticky='nsew')
main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')
input_frame = Frame(root)
input_frame.grid(row=0, column=0, sticky='nsew')

for frame in (main_page, main_frame, input_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# main page
logo_mainpage = Image.open('logo soettaloka black resize.jpg')
logo_mainpage_ico = ImageTk.PhotoImage(logo_mainpage)
Label(main_page, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)

pesan_btm = Button(main_page, text='PESAN TIKET', bg='black', fg='#8cc53d', font='Helvetica 15 bold', command=lambda :frame_1(main_frame))
pesan_btm.place(x=250, y=450, anchor='center')


# frame 1
Label(main_frame, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)
top_label = Label(main_frame, text='Selamat Datang di Soetta-Loka\nMasukkan data diri anda!',
                  bg='black', fg='#8cc53d', font='Helvetica 15 bold')
top_label.grid(row=0, column=1, sticky='nsew')

label_nama = Label(main_frame, text='Nama', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=1, column=0, sticky='w')
label_ttl = Label(main_frame, text='TTL', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=2, column=0, sticky='w')
label_noktp = Label(main_frame, text='No. KTP', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=3, column=0, sticky='w')
label_anggota = Label(main_frame, text='No. Keanggotaan', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=4, column=0, sticky='w')

input_nama = Entry(main_frame, width=40, borderwidth=5)
input_ttl = Entry(main_frame, width=40, borderwidth=5)
input_noktp = Entry(main_frame, width=40, borderwidth=5)
input_anggota = Entry(main_frame, width=40, borderwidth=5)
input_nama.grid(row=1, column=1, columnspan=3)
input_ttl.grid(row=2, column=1, columnspan=3)
input_noktp.grid(row=3, column=1, columnspan=3)
input_anggota.grid(row=4, column=1, columnspan=3)


def cek_data1():
    Label(main_frame, text = 'Data diri', font='Helvetica 10 bold').grid(row=6, column=1, sticky='nsew')
    Label(main_frame, text='Nama' + '                      : ' + input_nama.get()).grid(row=7, column=1, sticky='w')
    Label(main_frame, text='TTL' + '                          : ' + input_ttl.get()).grid(row=8, column=1, sticky='w')
    Label(main_frame, text='No. KTP' + '                  : ' + input_noktp.get()).grid(row=9, column=1, sticky='w')
    Label(main_frame, text='No. Keanggotaan' + '  : ' + input_anggota.get()).grid(row=10, column=1, sticky='w')


tombol1 = Button(main_frame, text='Cek Data', width=10, command=cek_data1).grid(row=11, column=2, sticky='e')
tombol2 = Button(main_frame, text='Input', width=10, command=lambda :frame_1(input_frame)).grid(row=11, column=1, sticky='e')


# frame 2, input frame
Label(input_frame, text='On-Booking', font='Helvetica 10 bold').grid(row=0, column=1, sticky='nsew')
maskapai_label = Label(input_frame, text='Maskapai').grid(row=1, column=0, sticky='w')
asal_label = Label(input_frame, text='Departure').grid(row=2, column=0, sticky='w')
tujuan_label = Label(input_frame, text='Destination').grid(row=3, column=0, sticky='w')
waktu_label = Label(input_frame, text='Waktu keberangkatan').grid(row=4, column=0, sticky='w')
kelas_label = Label(input_frame, text='Kelas').grid(row=5, column=0, sticky='w')

maskapai_input = Entry(input_frame, width=40, borderwidth=5)
asal_input = Entry(input_frame, width=40, borderwidth=5)
tujuan_input = Entry(input_frame, width=40, borderwidth=5)
waktu_input = Entry(input_frame, width=40, borderwidth=5)
kelas_input = Entry(input_frame, width=40, borderwidth=5)
maskapai_input.grid(row=1, column=1, columnspan=3)
asal_input.grid(row=2, column=1, columnspan=3)
tujuan_input.grid(row=3, column=1, columnspan=3)
waktu_input.grid(row=4, column=1, columnspan=3)
kelas_input.grid(row=5, column=1, columnspan=3)

frame_1(main_page)
root.mainloop()
