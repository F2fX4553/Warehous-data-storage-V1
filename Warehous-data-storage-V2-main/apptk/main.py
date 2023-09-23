from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import tkinter as tk
from db import Database
import sqlite3
import csv
import os
from tkinter import filedialog




db = Database("Storeg.db")





###########################################################
# window 1

window = tkinter.Tk()# window 1 login
freme = Frame(window) # bach kolch yji mstf f window mykonch 5ll chrol 9alb

window.iconbitmap('images/sibna.ico')
fg = "white"
font = "Arial"
bg = "#0E1E4B"
window.title("Store") #title window 1
window.configure(bg=bg)

window.resizable(False,False) # mmno3 tbdle hjm window
width = 600 # 3ard window 1
height = 450 # 3ard window 1
swidth = window.winfo_screenwidth() # yjib size 3ord ta3 window
sheight = window.winfo_screenheight() # yjib size tol ta3 window
x = (swidth - width) / 2 # y9om b3mliya hisabiya
y = (sheight - height) / 2 # y9om b3mliya hisabiya
window.geometry('%dx%d+%d+%d' %(width,height,x,y)) #ydi lhjm ta3 window li mditholo 66x450 o yhsb o ydirhali flwst

# Load the image
image = tkinter.PhotoImage(file="images/iconlogins.png")
# Create a label and add the image to it
label = tkinter.Label(freme,image=image)
label.config(width=600) # hadi hajm image bach ji lfo9

labelentryu = ttk.Label(text="USER NAME",background="#040A48",font=font,foreground='white') #label user name
labelentryp = ttk.Label(text="PASSWORD",background="#040A48",font=font,foreground='white') #label password

svuser = StringVar()
svpasswd= StringVar()
enteryuser = ttk.Entry( width=20,font='boold',textvariable=svuser) #entry username
enterypasswd = ttk.Entry(width=20,font='boold',textvariable=svpasswd) #enry password

buttonentr = ttk.Style()
buttonentr.configure('TButton',font = font,fg="#465D9E",bg="#465D9E")

buttonentr = ttk.Button(text="Enter",width=15,command= lambda :open_new_window())


freme.grid(row=0,column=0,columnspan=1) # hadi lfrim hakma ga3 window
label.grid(row=1,column=1,padx=0) # hadi lplasa ta3 image

labelentryu.place(x = 190,y = 150) # label user
labelentryp.place(x = 190,y = 230) # label password
enteryuser.place(x = 190,y = 170) # entry user
enterypasswd.place(x = 190,y = 250) #entry password
buttonentr.place(x=190,y=310) #button
def open_new_window():
    if svuser.get().strip() == '':
        messagebox.showinfo('','Enter the name !')
        enteryuser.focus()
    elif svpasswd.get().strip() == '':
        messagebox.showinfo('','Enter the password !')
        enterypasswd.focus()
    else:
        window.destroy()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        window2 = tkinter.Tk() #window 2


        window2.title("Store")  # title window 2
        window2.geometry('1350x600') #size window 2
        window2.iconbitmap('images/sibna.ico')
        window2.configure(bg=bg)

        #############################################
        menubar = Menu(window2)                      #
        filemenu = Menu(menubar, tearoff=0)          #
        filemenu.add_command(label="New",command=lambda :new())            #
        filemenu.add_command(label="Open",command=lambda :OpenFile())           #
        filemenu.add_command(label="Save",command= lambda :Save())           #
        filemenu.add_command(label="Print")          # menu window 2
        filemenu.add_separator()                     #
        filemenu.add_command(label="Exit",command=lambda : exit())           #
        menubar.add_cascade(label="File", menu=filemenu) #
        helpmenu = Menu(menubar, tearoff=0)              #
        helpmenu.add_command(label="About")              #
        menubar.add_cascade(label="Help", menu=helpmenu) #
        window2.config(menu=menubar)                     #

        titfream = ttk.Frame(window2)
        titfream.place(x=1,y=1)
        tatleee = ttk.Label(titfream,text="[ STOCKED ]", font='monospace', background="#465D9E",
                            foreground="white")  # label ta3 title
        tatleee.config(width=600)
        tatleee.pack()  # place ta3 title


    ###################### variable ===========================

        Number_var = StringVar()
        Quantite_var = StringVar()
        types_var = StringVar()
        Emplacement_var = StringVar()
        EntPlacer_litag_var =StringVar()
        Entcode_var = StringVar()
        search_var = StringVar()
        #search_by = StringVar()
        #del_var = StringVar()

    ###################### varibale end ############################

        #fream2 = ttk.Frame(window2,bootstyle="light")
        my_frame = ttk.Frame(window2)
        my_frame.place(x=1160,y=25,width=210,height=400)

        #fream2.place(x=1160,y=25,width=210,height=400)
        #lbl_ID = ttk.Label( my_frame,text='Numéro de série [ ID ]')
        #lbl_ID.pack(pady=2)
        #EntID = ttk.Entry( my_frame,textvariable=id_var,width=19,font='boold')
        #EntID.pack(pady=2)
        lbl_Name = ttk.Label( my_frame, text='Designation')
        lbl_Name.pack(pady=2)
        EntName = ttk.Entry( my_frame,textvariable=Number_var, width=19, font='boold')
        EntName.pack(pady=2)

        lbl_Quantite = ttk.Label( my_frame, text='Quantite')
        lbl_Quantite.pack(pady=2)
        EntQuantite = ttk.Entry( my_frame,textvariable=Quantite_var,width=19, font='boold')
        EntQuantite.pack(pady=2)

        lbl_type = ttk.Label( my_frame, text='Marque et type')
        lbl_type.pack(pady=2)
        Enttype = ttk.Entry( my_frame, textvariable=types_var,width=19, font='boold')
        Enttype.pack(pady=2)

        lbl_Emplacement = ttk.Label( my_frame, text='Ref fournisseur')
        lbl_Emplacement.pack(pady=2)
        EntEmplacement = ttk.Entry( my_frame, textvariable=Emplacement_var,width=19, font='boold')
        EntEmplacement.pack(pady=2)

        lbl_Placer = ttk.Label( my_frame, text='Case')
        lbl_Placer.pack(pady=2)
        EntPlacer = ttk.Entry( my_frame, textvariable=EntPlacer_litag_var,width=19, font='boold')
        EntPlacer.pack(pady=2)

        lbl_cod = ttk.Label(my_frame, text='Code')
        lbl_cod.pack(pady=2)
        Entcod = ttk.Entry(my_frame, textvariable=  Entcode_var, width=19, font='boold')
        Entcod.pack(pady=2)



        lbl_khat = ttk.Label( my_frame, text='---------------------------------------------', )
        lbl_khat.pack(pady=2)

        btn_frame = ttk.Frame(window2)
        btn_frame.place(x=1160, y=430, width=210, height=253)
        lab_title = ttk.Label(btn_frame,font=font,text='Panneau De Contrôle' , background="#0A790C")
        lab_title.pack(pady=2)

#--------------- buttons --------------------------------------
        add_btn = ttk.Button(btn_frame,text="Ajout ",width=15,command=lambda : Add_Piyasa())
        add_btn.place(x=33,y=33,width=150,height=30)
        clear_btn = ttk.Button(btn_frame,text="Champs vides",width=15,command=lambda :Clear())
        clear_btn.place(x=33,y=80,width=150,height=30)
        updatebtn = ttk.Button(btn_frame,text="Mettre à jour",width=15,command=lambda :Update())
        updatebtn.place(x=33,y=120,width=150,height=30)
        del_btn = ttk.Button(btn_frame,text="Supprimer",width=15,command=lambda :delet())
        del_btn.place(x=33,y=160,width=150,height=30)
        exit_btn = ttk.Button(btn_frame,text="Exit ",width=15,command=exit)
        exit_btn.place(x=33,y= 200,width=150,height=30)

#-------------------------------------search maneg----------------------------------------------------
        my_framesearch = ttk.Frame(window2)
        my_framesearch.place(x=1, y=25, width=1155, height=50)

        lblsearch = ttk.Label(my_framesearch,text='Recherche : ')
        lblsearch.place(x= 34,y=12)
        combo_searsh = ttk.Combobox(my_framesearch,justify='left',width=30)
        combo_searsh['value'] = ('ID','Designation','Quantite','Marque et type','Ref fournisseur','Case','Code')
        combo_searsh.place(x=120,y=12)
        searsh_entery = ttk.Entry(my_framesearch,textvariable=search_var,justify='left',font="boold")
        searsh_entery.place(x=350,y=12)

        search_bttoun = ttk.Button(my_framesearch,text='Search',width=25)
        search_bttoun.place(x=550,y=12)
        #--------------------------------------------

        #================= table ==========================================================================

        Dietals_Frame = ttk.Frame(window2)
        Dietals_Frame.place(x=1,y=79,width=1155,height=604)

        # scrol x - y
        scrol_x = Scrollbar(Dietals_Frame,orient=HORIZONTAL) # hada scrol ta3 ltht
        scrol_y = Scrollbar(Dietals_Frame,orient=VERTICAL) # hadi scrol ta3 ljnb

        # --- treeveiw ---

        Store_table = ttk.Treeview(Dietals_Frame,
                                     columns=('ID','Designation','Quantite','Marque et type','Ref fournisseur','Case','Code'),
        xscrollcommand = scrol_x.set,
        yscrollcommand = scrol_y.set)

        Store_table.place(x=18,y=1,width=1150,height=590)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_x.config(command= Store_table.xview)
        scrol_y.config(command=Store_table.xview)

        # hna rah ndif l5sais ta3 ljdwl



        # ================= table ==========================================================================
        Store_table.column('ID', width=100, anchor=tk.CENTER)
        Store_table.column('#0', width=0, anchor='w')

        # Set the columns
        Store_table['columns'] = ('ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseu', 'Case','Code')

        # Set the width of the columns
        Store_table.column('ID', width=100,anchor=tk.CENTER)
        Store_table.column('Designation', width=100, anchor=tk.CENTER)
        Store_table.column('Quantite', width=100,anchor=tk.CENTER)
        Store_table.column('Marque et type', width=100,anchor=tk.CENTER)
        Store_table.column('Ref fournisseu', width=100,anchor=tk.CENTER)
        Store_table.column('Case', width=150,anchor=tk.CENTER)
        Store_table.column('Code', width=150, anchor=tk.CENTER)

        # Set the headings
        Store_table.heading('ID', text='ID')
        Store_table.heading('Designation', text='Designation')
        Store_table.heading('Quantite', text='Quantite')
        Store_table.heading('Marque et type', text='Marque et type')
        Store_table.heading('Ref fournisseu', text='Ref fournisseu')
        Store_table.heading('Case', text='Case')
        Store_table.heading('Code', text='Code')

        # --------- con + add database ------

        def getData(event):
            selected_row = Store_table.focus()
            data = Store_table.item(selected_row)
            global row
            row = data["values"]
            Number_var.set(row[1])
            Quantite_var.set(row[2])
            types_var.set(row[3])
            Emplacement_var.set(row[4])
            EntPlacer_litag_var.set(row[5])
            Entcode_var.set(row[6])
        Store_table.bind("<ButtonRelease-1>", getData)



        def delet():
            db.remove(row[0])
            Clear()
            DispayAll()

        def DispayAll():
            Store_table.delete(*Store_table.get_children())
            for row in db.fetch():
                Store_table.insert("",END,values=row)
        def Clear():
            Number_var.set("")
            Quantite_var.set("")
            types_var.set("")
            Emplacement_var.set("")
            EntPlacer_litag_var.set("")
            Entcode_var.set("")

        def Add_Piyasa():
            if EntName.get() == "" or EntQuantite.get() == "" or Enttype.get() == "" or EntEmplacement.get() == "" or EntPlacer.get() == "" or  Entcod.get() == "":
                messagebox.showerror('','The fields are empty')
                return
            db.insert(
                EntName.get(),
                EntQuantite.get(),
                Enttype.get(),
                EntEmplacement.get(),
                EntPlacer.get(),
                Entcod.get()
            )

            messagebox.showinfo('','The item has been added')

            DispayAll()
        DispayAll()
        def Update():
            if EntName.get() == "" or EntQuantite.get() == "" or Enttype.get() == "" or EntEmplacement.get() == "" or EntPlacer.get() == "" or Entcod.get() == "":
                messagebox.showerror('', 'The fields are empty')
                return
            db.update(row[0],
                      EntName.get(),
                      EntQuantite.get(),
                      Enttype.get(),
                      EntEmplacement.get(),
                      EntPlacer.get(),
                      Entcod.get()
            )

            messagebox.showinfo('','Updated successfully')
            Clear()
            DispayAll()


        '''def Search():
            db.search(row[0],
                      EntName.get(),
                      EntQuantite.get(),
                      Enttype.get(),
                      EntEmplacement.get(),
                      EntPlacer.get(),
                      Entcod.get()
                      )
            if search_var.get() == "":
                messagebox.showerror('', 'keyword manfi')
                return
            keyword_to_search = search_var.get()
            rows = Store_table.get_children()
            for row in rows:
                if keyword_to_search in row[0]:
                    Store_table.selection_set(row)
                    Store_table.focus_set(row, 'column', 'Code')
                    break
            else:

                messagebox.showinfo('', 'element mnfound')'''

        def Save():

            #Storeg.db , story
            filename = filedialog.asksaveasfilename(initialdir=os.path.expanduser('~'), title='Save File',
                                                    filetypes=[('CSV Files', '*.csv')])

            if filename:
                conn = sqlite3.connect('Storeg.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM story')
                results = cursor.fetchall()
                conn.close()
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    for row in results:
                        writer.writerow(row)

        def OpenFile():



            ############################ dok ndiwr window ki ttfth t3tili ljdwl ki n3bz 3la button open##################################################
            filename = filedialog.askopenfilename(initialdir=os.path.expanduser('~'), title='Open File',
                                                  filetypes=[('CSV Files', '*.csv')])

            if filename:
                with open(filename, 'r') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')

                    Store_table = ttk.Treeview(Dietals_Frame,
                                               columns=(
                                               'ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseur',
                                               'Case', 'Code'),
                                               xscrollcommand=scrol_x.set,
                                               yscrollcommand=scrol_y.set)

                    Store_table.place(x=18, y=1, width=1150, height=590)
                    scrol_x.pack(side=BOTTOM, fill=X)
                    scrol_y.pack(side=LEFT, fill=Y)
                    scrol_x.config(command=Store_table.xview)
                    scrol_y.config(command=Store_table.xview)

                    # hna rah ndif l5sais ta3 ljdwl

                    # ================= table ==========================================================================
                    Store_table.column('ID', width=100, anchor=tk.CENTER)
                    Store_table.column('#0', width=0, anchor='w')

                    # Set the columns
                    Store_table['columns'] = (
                    'ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseu', 'Case', 'Code')

                    # Set the width of the columns
                    Store_table.column('ID', width=100, anchor=tk.CENTER)
                    Store_table.column('Designation', width=100, anchor=tk.CENTER)
                    Store_table.column('Quantite', width=100, anchor=tk.CENTER)
                    Store_table.column('Marque et type', width=100, anchor=tk.CENTER)
                    Store_table.column('Ref fournisseu', width=100, anchor=tk.CENTER)
                    Store_table.column('Case', width=150, anchor=tk.CENTER)
                    Store_table.column('Code', width=150, anchor=tk.CENTER)

                    # Set the headings
                    Store_table.heading('ID', text='ID')
                    Store_table.heading('Designation', text='Designation')
                    Store_table.heading('Quantite', text='Quantite')
                    Store_table.heading('Marque et type', text='Marque et type')
                    Store_table.heading('Ref fournisseu', text='Ref fournisseu')
                    Store_table.heading('Case', text='Case')
                    Store_table.heading('Code', text='Code')

                    for row in reader:
                        Store_table.insert('', 'end', values=row)

 #################### window3 ki ndir new t5rojli #################################

        def new():
            message = messagebox.askyesno("Question", "Do you want to continue?")
            if message :
                # Storeg.db , story
                filename = filedialog.asksaveasfilename(initialdir=os.path.expanduser('~'), title='Save File',
                                                        filetypes=[('CSV Files', '*.csv')])
                if filename:
                    conn = sqlite3.connect('Storeg.db')
                    cursor = conn.cursor()
                    cursor.execute('SELECT * FROM story')
                    results = cursor.fetchall()
                    conn.close()
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',')
                        for row in results:
                            writer.writerow(row)
            window2.destroy()

            def Removes():
                db.removes()

            window3 = tkinter.Tk(Removes())  # window 3

            window3.title("Store")  # title window 2
            window3.geometry('1350x600')  # size window 2
            window3.iconbitmap('images/icon.ico')
            window3.configure(bg=bg)

            #############################################
            menubar = Menu(window3)  #
            filemenu = Menu(menubar, tearoff=0)  #
            filemenu.add_command(label="New", command=lambda: new())  #
            filemenu.add_command(label="Open", command=lambda: OpenFile())  #
            filemenu.add_command(label="Save", command=lambda: Save())  #
            filemenu.add_command(label="Print")  # menu window 2
            filemenu.add_separator()  #
            filemenu.add_command(label="Exit", command=lambda: exit())  #
            menubar.add_cascade(label="File", menu=filemenu)  #
            helpmenu = Menu(menubar, tearoff=0)  #
            helpmenu.add_command(label="About")  #
            menubar.add_cascade(label="Help", menu=helpmenu)  #
            window3.config(menu=menubar)  #

            titfream = ttk.Frame(window3)
            titfream.place(x=1, y=1)
            tatleee = ttk.Label(titfream, text="[ STOCKED ]", font='monospace', background="#465D9E",
                                foreground="white")  # label ta3 title
            tatleee.config(width=600)
            tatleee.pack()  # place ta3 title

            ###################### variable ===========================

            Number_var = StringVar()
            Quantite_var = StringVar()
            types_var = StringVar()
            Emplacement_var = StringVar()
            EntPlacer_litag_var = StringVar()
            Entcode_var = StringVar()
            search_var = StringVar()
            # search_by = StringVar()
            # del_var = StringVar()

            ###################### varibale end ############################

            # fream2 = ttk.Frame(window2,bootstyle="light")
            my_frame = ttk.Frame(window3)
            my_frame.place(x=1160, y=25, width=210, height=400)

            # fream2.place(x=1160,y=25,width=210,height=400)
            # lbl_ID = ttk.Label( my_frame,text='Numéro de série [ ID ]')
            # lbl_ID.pack(pady=2)
            # EntID = ttk.Entry( my_frame,textvariable=id_var,width=19,font='boold')
            # EntID.pack(pady=2)
            lbl_Name = ttk.Label(my_frame, text='Designation')
            lbl_Name.pack(pady=2)
            EntName = ttk.Entry(my_frame, textvariable=Number_var, width=19, font='boold')
            EntName.pack(pady=2)

            lbl_Quantite = ttk.Label(my_frame, text='Quantite')
            lbl_Quantite.pack(pady=2)
            EntQuantite = ttk.Entry(my_frame, textvariable=Quantite_var, width=19, font='boold')
            EntQuantite.pack(pady=2)

            lbl_type = ttk.Label(my_frame, text='Marque et type')
            lbl_type.pack(pady=2)
            Enttype = ttk.Entry(my_frame, textvariable=types_var, width=19, font='boold')
            Enttype.pack(pady=2)

            lbl_Emplacement = ttk.Label(my_frame, text='Ref fournisseur')
            lbl_Emplacement.pack(pady=2)
            EntEmplacement = ttk.Entry(my_frame, textvariable=Emplacement_var, width=19, font='boold')
            EntEmplacement.pack(pady=2)

            lbl_Placer = ttk.Label(my_frame, text='Case')
            lbl_Placer.pack(pady=2)
            EntPlacer = ttk.Entry(my_frame, textvariable=EntPlacer_litag_var, width=19, font='boold')
            EntPlacer.pack(pady=2)

            lbl_cod = ttk.Label(my_frame, text='Code')
            lbl_cod.pack(pady=2)
            Entcod = ttk.Entry(my_frame, textvariable=Entcode_var, width=19, font='boold')
            Entcod.pack(pady=2)

            lbl_khat = ttk.Label(my_frame, text='---------------------------------------------', )
            lbl_khat.pack(pady=2)

            btn_frame = ttk.Frame(window3)
            btn_frame.place(x=1160, y=430, width=210, height=253)
            lab_title = ttk.Label(btn_frame, font=font, text='Panneau De Contrôle', background="#0A790C")
            lab_title.pack(pady=2)

            # --------------- buttons --------------------------------------
            add_btn = ttk.Button(btn_frame, text="Ajout ", width=15, command=lambda: Add_Piyasa())
            add_btn.place(x=33, y=33, width=150, height=30)
            clear_btn = ttk.Button(btn_frame, text="Champs vides", width=15, command=lambda: Clear())
            clear_btn.place(x=33, y=80, width=150, height=30)
            updatebtn = ttk.Button(btn_frame, text="Mettre à jour", width=15, command=lambda: Update())
            updatebtn.place(x=33, y=120, width=150, height=30)
            del_btn = ttk.Button(btn_frame, text="Supprimer", width=15, command=lambda: delet())
            del_btn.place(x=33, y=160, width=150, height=30)
            exit_btn = ttk.Button(btn_frame, text="Exit ", width=15, command=exit)
            exit_btn.place(x=33, y=200, width=150, height=30)

            # -------------------------------------search maneg----------------------------------------------------
            my_framesearch = ttk.Frame(window3)
            my_framesearch.place(x=1, y=25, width=1155, height=50)

            lblsearch = ttk.Label(my_framesearch, text='Recherche : ')
            lblsearch.place(x=34, y=12)
            combo_searsh = ttk.Combobox(my_framesearch, justify='left', width=30)
            combo_searsh['value'] = (
                'ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseur', 'Case', 'Code')
            combo_searsh.place(x=120, y=12)
            searsh_entery = ttk.Entry(my_framesearch, textvariable=search_var, justify='left', font="boold")
            searsh_entery.place(x=350, y=12)

            search_bttoun = ttk.Button(my_framesearch, text='Search', width=25)
            search_bttoun.place(x=550, y=12)
            # --------------------------------------------

            # ================= table ==========================================================================

            Dietals_Frame = ttk.Frame(window3)
            Dietals_Frame.place(x=1, y=79, width=1155, height=604)

            # scrol x - y
            scrol_x = Scrollbar(Dietals_Frame, orient=HORIZONTAL)  # hada scrol ta3 ltht
            scrol_y = Scrollbar(Dietals_Frame, orient=VERTICAL)  # hadi scrol ta3 ljnb

            # --- treeveiw ---

            Store_table = ttk.Treeview(Dietals_Frame,
                                       columns=(
                                           'ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseur', 'Case',
                                           'Code'),
                                       xscrollcommand=scrol_x.set,
                                       yscrollcommand=scrol_y.set)

            Store_table.place(x=18, y=1, width=1150, height=590)
            scrol_x.pack(side=BOTTOM, fill=X)
            scrol_y.pack(side=LEFT, fill=Y)
            scrol_x.config(command=Store_table.xview)
            scrol_y.config(command=Store_table.xview)

            # hna rah ndif l5sais ta3 ljdwl

            # ================= table ==========================================================================
            Store_table.column('ID', width=100, anchor=tk.CENTER)
            Store_table.column('#0', width=0, anchor='w')

            # Set the columns
            Store_table['columns'] = (
                'ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseu', 'Case', 'Code')

            # Set the width of the columns
            Store_table.column('ID', width=100, anchor=tk.CENTER)
            Store_table.column('Designation', width=100, anchor=tk.CENTER)
            Store_table.column('Quantite', width=100, anchor=tk.CENTER)
            Store_table.column('Marque et type', width=100, anchor=tk.CENTER)
            Store_table.column('Ref fournisseu', width=100, anchor=tk.CENTER)
            Store_table.column('Case', width=150, anchor=tk.CENTER)
            Store_table.column('Code', width=150, anchor=tk.CENTER)

            # Set the headings
            Store_table.heading('ID', text='ID')
            Store_table.heading('Designation', text='Designation')
            Store_table.heading('Quantite', text='Quantite')
            Store_table.heading('Marque et type', text='Marque et type')
            Store_table.heading('Ref fournisseu', text='Ref fournisseu')
            Store_table.heading('Case', text='Case')
            Store_table.heading('Code', text='Code')



            # --------- con + add database ------

            def getData(event):
                selected_row = Store_table.focus()
                data = Store_table.item(selected_row)
                global row
                row = data["values"]
                Number_var.set(row[1])
                Quantite_var.set(row[2])
                types_var.set(row[3])
                Emplacement_var.set(row[4])
                EntPlacer_litag_var.set(row[5])
                Entcode_var.set(row[6])

            Store_table.bind("<ButtonRelease-1>", getData)

            def delet():
                db.remove(row[0])
                Clear()
                DispayAll()

            def DispayAll():
                Store_table.delete(*Store_table.get_children())
                for row in db.fetch():
                    Store_table.insert("", END, values=row)

            def Clear():
                Number_var.set("")
                Quantite_var.set("")
                types_var.set("")
                Emplacement_var.set("")
                EntPlacer_litag_var.set("")
                Entcode_var.set("")

            def Add_Piyasa():
                if EntName.get() == "" or EntQuantite.get() == "" or Enttype.get() == "" or EntEmplacement.get() == "" or EntPlacer.get() == "" or Entcod.get() == "":
                    messagebox.showerror('', 'The fields are empty')
                    return
                db.insert(
                    EntName.get(),
                    EntQuantite.get(),
                    Enttype.get(),
                    EntEmplacement.get(),
                    EntPlacer.get(),
                    Entcod.get()
                )

                messagebox.showinfo('', 'The item has been added')

                DispayAll()

            DispayAll()

            def Update():
                if EntName.get() == "" or EntQuantite.get() == "" or Enttype.get() == "" or EntEmplacement.get() == "" or EntPlacer.get() == "" or Entcod.get() == "":
                    messagebox.showerror('', 'The fields are empty')
                    return
                db.update(row[0],
                          EntName.get(),
                          EntQuantite.get(),
                          Enttype.get(),
                          EntEmplacement.get(),
                          EntPlacer.get(),
                          Entcod.get()
                          )

                messagebox.showinfo('', 'Updated successfully')
                Clear()
                DispayAll()

            '''def Search():
                db.search(row[0],
                          EntName.get(),
                          EntQuantite.get(),
                          Enttype.get(),
                          EntEmplacement.get(),
                          EntPlacer.get(),
                          Entcod.get()
                          )
                if search_var.get() == "":
                    messagebox.showerror('', 'keyword manfi')
                    return
                keyword_to_search = search_var.get()
                rows = Store_table.get_children()
                for row in rows:
                    if keyword_to_search in row[0]:
                        Store_table.selection_set(row)
                        Store_table.focus_set(row, 'column', 'Code')
                        break
                else:

                    messagebox.showinfo('', 'element mnfound')'''

            def Save():

                # Storeg.db , story
                filename = filedialog.asksaveasfilename(initialdir=os.path.expanduser('~'), title='Save File',
                                                        filetypes=[('CSV Files', '*.csv')])

                if filename:
                    conn = sqlite3.connect('Storeg.db')
                    cursor = conn.cursor()
                    cursor.execute('SELECT * FROM story')
                    results = cursor.fetchall()
                    conn.close()
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',')
                        for row in results:
                            writer.writerow(row)

            def OpenFile():

                ############################ dok ndiwr window ki ttfth t3tili ljdwl ki n3bz 3la button open##################################################
                filename = filedialog.askopenfilename(initialdir=os.path.expanduser('~'), title='Open File',
                                                      filetypes=[('CSV Files', '*.csv')])

                if filename:
                    with open(filename, 'r') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')

                        Store_table = ttk.Treeview(Dietals_Frame,
                                                   columns=(
                                                       'ID', 'Designation', 'Quantite', 'Marque et type',
                                                       'Ref fournisseur',
                                                       'Case', 'Code'),
                                                   xscrollcommand=scrol_x.set,
                                                   yscrollcommand=scrol_y.set)

                        Store_table.place(x=18, y=1, width=1150, height=590)
                        scrol_x.pack(side=BOTTOM, fill=X)
                        scrol_y.pack(side=LEFT, fill=Y)
                        scrol_x.config(command=Store_table.xview)
                        scrol_y.config(command=Store_table.xview)

                        # hna rah ndif l5sais ta3 ljdwl

                        # ================= table ==========================================================================
                        Store_table.column('ID', width=100, anchor=tk.CENTER)
                        Store_table.column('#0', width=0, anchor='w')

                        # Set the columns
                        Store_table['columns'] = (
                            'ID', 'Designation', 'Quantite', 'Marque et type', 'Ref fournisseu', 'Case', 'Code')

                        # Set the width of the columns
                        Store_table.column('ID', width=100, anchor=tk.CENTER)
                        Store_table.column('Designation', width=100, anchor=tk.CENTER)
                        Store_table.column('Quantite', width=100, anchor=tk.CENTER)
                        Store_table.column('Marque et type', width=100, anchor=tk.CENTER)
                        Store_table.column('Ref fournisseu', width=100, anchor=tk.CENTER)
                        Store_table.column('Case', width=150, anchor=tk.CENTER)
                        Store_table.column('Code', width=150, anchor=tk.CENTER)

                        # Set the headings
                        Store_table.heading('ID', text='ID')
                        Store_table.heading('Designation', text='Designation')
                        Store_table.heading('Quantite', text='Quantite')
                        Store_table.heading('Marque et type', text='Marque et type')
                        Store_table.heading('Ref fournisseu', text='Ref fournisseu')
                        Store_table.heading('Case', text='Case')
                        Store_table.heading('Code', text='Code')

                        for row in reader:
                            Store_table.insert('', 'end', values=row)


                window3.mainloop() # istd3a window 3

        window2.mainloop() # istd3a windowo 2




window.mainloop() # istd3a window 1 login





