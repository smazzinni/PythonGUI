from tkinter import *
import backend


def getId(event):
    global get_selected_id
    index = l_box.curselection()[0]
    get_selected_id = l_box.get(index)
    e1.delete(0,END)
    e1.insert(END,get_selected_id[1])
    e2.delete(0,END)
    e2.insert(END,get_selected_id[3])
    e3.delete(0,END)
    e3.insert(END,get_selected_id[2])
    e4.delete(0,END)
    e4.insert(END,get_selected_id[4])


# def UpdateRow(event):
#     global get_selected_row
#     index = l_box.curselection()[0]
#     get_selected_row = l_box.get(index)
#     print(get_selected_row)




def view_command():
    l_box.delete(0, END)
    for row in backend.view():
        l_box.insert(END, row)

def search_command():
    l_box.delete(0, END)
    for row in backend.search(tit_text.get(),aut_text.get(),year_text.get(),isbn_text.get(),):
        l_box.insert(END, row) #title,author,year,isbn)

def add_command():
    backend.insert(tit_text.get(),aut_text.get(),year_text.get(),isbn_text.get())
    l_box.delete(0, END)
    l_box.insert(END,(tit_text.get(),aut_text.get(),year_text.get(),isbn_text.get()))

def update_command():

    print(get_selected_id[0],tit_text.get(),aut_text.get(),year_text.get(),isbn_text.get())
    backend.update(get_selected_id[0],tit_text.get(),aut_text.get(),year_text.get(),isbn_text.get())



def delete_command():
    # print(get_selected_id[0])
    backend.delete(get_selected_id[0])


window = Tk()

l1 = Label(window, text="Author")
l1.grid(row=0, column=0)
aut_text = StringVar()
e1 = Entry(window, textvariable=aut_text)
e1.grid(row=0, column=1)

l2 = Label(window, text="ISBN")
l2.grid(row=1, column=0)

isbn_text = StringVar()
e2 = Entry(window, textvariable=isbn_text)
e2.grid(row=1, column=1)

l3 = Label(window, text="Title")
l3.grid(row=0, column=2)

tit_text = StringVar()
e3 = Entry(window, textvariable=tit_text)
e3.grid(row=0, column=3)

l4 = Label(window, text="Year")
l4.grid(row=1, column=2)

year_text = StringVar()
e4 = Entry(window, textvariable=year_text)
e4.grid(row=1, column=3)


b_view = Button(window, text="View All", width=12, command=view_command)
b_view.grid(row=2, column=3)

b_search = Button(window, text="Search Entry", width=12, command=search_command)
b_search.grid(row=3, column=3)

b_Add = Button(window, text="Add Entry", width=12, command=add_command)
b_Add.grid(row=4, column=3)

b_Update = Button(window, text="Update Entry", width=12, command=update_command)
b_Update.grid(row=5, column=3)

b_Delete = Button(window, text="Delete Entry", width=12, command=delete_command)
b_Delete.grid(row=6, column=3)

b_close = Button(window, text="Close", width=12, command=window.destroy)
b_close.grid(row=7, column=3)

l_box= Listbox(window, height=8, width=40)
l_box.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

l_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=l_box.yview)

l_box.bind('<<ListboxSelect>>', getId)


window.mainloop()