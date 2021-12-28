from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
import threading
from main import execute

#Set 
root = ThemedTk(theme='breeze')
root.geometry('500x600')
root.title('Crypto Tracker')
root.iconbitmap(r'tticon.ico')


# Frame cho phan tieu de
labelFrame = Frame(root)
labelFrame.pack(pady=30)

label = Label(labelFrame,text = "Crypto Tracker",font='Times 36',fg='#1b45c5')
label.pack()
sublabel = Label(labelFrame,text= "Nhập thông tin.",font='Times 12',fg='#1b45c5')
sublabel.pack()

#frame cho phan form
form = Canvas(root,height=290)
form.pack()

# Khung nhap chat id
chatid = Label(root,text='chat id Telegram',font='Recoleta 9')
chatidEntry = ttk.Entry(root,width=38)
form.create_window(106,10,window=chatid)
form.create_window(189,35,window=chatidEntry)

# Check box loại tiền ảo
type = Label(root,text='loại tiền ảo',font='Recoleta 9')
checkType = StringVar()
bitcoinEntry = Checkbutton(root,text='Bitcoin',variable=checkType, onvalue='Bitcoin')
ethereumEntry = Checkbutton(root, text='Ethereum',variable=checkType, onvalue='Ethereum')
bitcoinEntry.deselect()
ethereumEntry.deselect()
form.create_window(89,60,window= type)
form.create_window(100,85,window=bitcoinEntry)
form.create_window(180,85,window=ethereumEntry)

# khung nhập thời gian định kỳ
donvi_tg = StringVar()
donvi_tg.set('giây')
interval = Label(root,text='định kỳ',font='Recoleta 9')
intervalEntry = ttk.Entry(root, width = 38)
w = ttk.OptionMenu(root, donvi_tg,'     ',"giờ", "phút", "giây")
form.create_window(76,105,window= interval)
form.create_window(189,130,window=intervalEntry)
form.create_window(296.5,130,window= w)

# Khung nhập số cập nhật
amount = Label(root,text='số lần cập nhật',font='Recoleta 9')
amountEntry = ttk.Entry(root, width = 38)
form.create_window(101,155,window= amount)
form.create_window(189,180,window=amountEntry)

# Khung nhập mức nguy hiểm
threshold = Label(root,text='mức nguy hiểm',font='Recoleta 9')
thresholdEntry = ttk.Entry(root, width = 38)
form.create_window(101,205,window= threshold)
form.create_window(189,230,window=thresholdEntry)

#Check box loại tiền tệ
fiat = Label(root,text='loại tiền tệ',font='Recoleta 9')
checkFiat = StringVar()
vndEntry = Checkbutton(root,text='VND',variable=checkFiat, onvalue='VND')
usdEntry = Checkbutton(root,text='USD',variable=checkFiat, onvalue='USD')
vndEntry.deselect()
usdEntry.deselect()
form.create_window(92,283,window=vndEntry)
form.create_window(168,283,window=usdEntry)
form.create_window(87,257,window= fiat)

#Gắn cờ để dừng luồng chạy song song
stop_thread = False
# Xử lý để gửi thông báo
def xuly():
    try:
        # Lấy input từ entry
        chat_id = chatidEntry.get()
        loai_tien_ao = checkType.get()
        if loai_tien_ao == "Bitcoin":
            loai_tien_ao = 0
        else:
            loai_tien_ao = 1
            
        if donvi_tg.get() == 'giờ': # Chuyển đơn vị thời gian sang giây
            time_interval = float(intervalEntry.get()) * 3600
        elif donvi_tg.get() == 'phút':
            time_interval = float(intervalEntry.get()) * 60
        else:
            time_interval = int(intervalEntry.get())
        amount = int(amountEntry.get())
        threshold = int(thresholdEntry.get())
        fiat = checkFiat.get()
        messagebox.showinfo(message="Thông báo định kỳ đang được gửi đến bạn !!",title="Crypto Tracker")
        while True:
            execute(chat_id,loai_tien_ao,time_interval,amount,threshold,fiat)
            if stop_thread == True: # Dừng thread
                break
    except:
        messagebox.showinfo(message="Vui lòng nhập thông tin đúng !!",title="Crypto Tracker")

# Click nút start
def onclick():
    global stop_thread
    stop_thread = False
    run = threading.Thread(target=xuly)
    run.start()
# Click nút stop
def onclick2():
    global stop_thread
    stop_thread = True
    messagebox.showinfo(message="Đã dừng gửi thông báo !!",title="Crypto Tracker")

# Nút start và stop
buttons = Canvas(root,height=60)
buttons.pack()
start_button = PhotoImage(file='power.png')
startB = ttk.Button(root,image=start_button,command=onclick)
buttons.create_window(120,70,window=startB)
stop_button = PhotoImage(file='power-off.png')
stopB = ttk.Button(root,image=stop_button,command=onclick2)
buttons.create_window(260,70,window=stopB)

root.mainloop()

