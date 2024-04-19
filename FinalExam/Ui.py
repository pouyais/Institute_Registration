from tkinter import *
from tkinter import messagebox
from classdatabase import *



root = Tk()
root.geometry("600x480")
root.title("institue registration")

db = Database("D:/PythonTerm3/FinalExam/mydatabase.db")


def insert():

    db.insert(ent_name.get(),ent_lname.get(),ent_namecourse.get(),ent_password.get())
    clear()
    publish_list()


def clear():

    ent_lname.delete(0,END)
    ent_name.delete(0,END)
    ent_password.delete(0,END)
    ent_namecourse.delete(0,END)


def select_item(event):

    try:
        global item
        item = lst_box.get(lst_box.curselection())
        ent_lname.delete(0,END)
        ent_lname.insert(END,item[2])
        ent_name.delete(0,END)
        ent_name.insert(END,item[1])
        ent_password.delete(0,END)
        ent_password.insert(END,item[4])
        ent_namecourse.delete(0,END)
        ent_namecourse.insert(END,item[3])
    except IndexError:
        pass

def publish_list():

    lst_box.delete(0,END)
    rows = db.fetch()
    for ro in rows:
        lst_box.insert(END,ro)


def remove():

    mbbox = messagebox.askyesno(title="حذف آیتم",message="آیا مطمئن هستید که میخواهید این آیتم را حذف کنید؟")
    if mbbox == True:
        db.remove(item[0])
        clear()
        publish_list()
    else:
        pass


def exit():

    mbbox = messagebox.askyesno(title="خروج",message="آیا مطمئن هستید که میخواهید از برنامه خارج شوید؟")
    if mbbox == True:
        root.destroy()
    else:
        pass




def welcome():

    try:
        if ent_systempass.get() != "":
            passws = db.password(ent_systempass.get())
            list_passws = [i for i in passws[0]]
            if int(ent_systempass.get()) == list_passws[4]:
                messagebox.showinfo(title="خوش آمد",message=f"به سامانه خوش آمدید {list_passws[1]} {list_passws[2]}")
        elif ent_systempass.get() == "":
            messagebox.showinfo(title="ثبت نام",message="شما هنوز ثبت نام نکردید")
    except IndexError:
        messagebox.showinfo(title="ثبت نام",message="شما هنوز ثبت نام نکردید")
  


#***************************************Lables*****************************************************
lbl_lname = Label(root,text=" : نام خانوادگی")
lbl_lname.place(x=150,y=10)

lbl_name = Label(root,text=" : نام")
lbl_name.place(x=450,y=10)

lbl_password = Label(root,text=" : رمز ورود")
lbl_password.place(x=150,y=100)

lbl_namecourse = Label(root,text=" : نام دوره")
lbl_namecourse.place(x=450,y=100)

lbl_systempass = Label(root,text=" : رمز ورود")
lbl_systempass.place(x=460,y=440)

#***************************************Entries*****************************************************
ent_lname = Entry(root)
ent_lname.place(x=12,y=12)

ent_name = Entry(root)
ent_name.place(x=310,y=12)

ent_password = Entry(root)
ent_password.place(x=12,y=102)

ent_namecourse = Entry(root)
ent_namecourse.place(x=310,y=102)

ent_systempass = Entry(root,width=70)
ent_systempass.place(x=30,y=440)


#***************************************Listbox*****************************************************
lst_box = Listbox(root,width=60,height=14)
lst_box.place(x=12,y=180)

lst_box.bind("<<ListboxSelect>>",select_item)

#***************************************Buttons*****************************************************
btn_show_list = Button(root,text="مشاهده همه",width=14,height=1,command=publish_list)
btn_show_list.place(x=450,y=205)

btn_insert = Button(root,text="اضافه کردن",width=14,height=1,command=insert)
btn_insert.place(x=450,y=235)

btn_clear = Button(root,text="خالی کردن ورودیها",width=14,height=1,command=clear)
btn_clear.place(x=450,y=265)

btn_delete = Button(root,text="حذف کردن",width=14,height=1,command=remove)
btn_delete.place(x=450,y=295)

btn_exit = Button(root,text="خروج",width=14,height=1,command=exit)
btn_exit.place(x=450,y=325)

btn_entrance = Button(root,text="ورود به سامانه",width=14,height=1,command=welcome)
btn_entrance.place(x=450,y=355)

root.mainloop()