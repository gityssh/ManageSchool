import tkinter
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog, ttk
background_colour = "SkyBlue4"
# bi functional variables = img, lic, sm, ins
bi_img = None
bi_driver_lic = None
bi_veh_sm_card_copy = None
bi_veh_ins_copy = None

# try to create table if not exists
try:
    my_database_ct = sqlite3.connect('Database.db')
    my_cursor_ct = my_database_ct.cursor()
    def create_table_sqlite():
        # Student Table
        my_cursor_ct.execute(""" CREATE TABLE IF NOT EXISTS student_data(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                global_student_id INT(25),
                                name VARCHAR(30) NOT NULL,
                                class VARCHAR(20),
                                roll_no INT,
                                class_teacher_name VARCHAR(30),
                                gender VARCHAR(5),
                                age INT,
                                cast VARCHAR(20),
                                phone_no INT,
                                image BLOB,
                                address VARCHAR(80),
                                education VARCHAR(15),
                                father_name VARCHAR(30),
                                mother_name VARCHAR(30),
                                admission_date TEXT,
                                admission_form_no INT,
                                fee_submitted INT,
                                fee_submission_date TEXT,
                                adhar_no INT,
                                register_no INT,
                                blood_group VARCHAR(4),
                                TAG VARCHAR(15) );        """)

        # Teacher Table
        my_cursor_ct.execute(""" CREATE TABLE IF NOT EXISTS teacher_data(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    name VARCHAR(30) NOT NULL,
                                    gender VARCHAR(5),
                                    age INT,
                                    teacher_of_class VARCHAR(20),
                                    subject VARCHAR(10),
                                    phone_no INT,
                                    image BLOB,
                                    address VARCHAR(80),
                                    education VARCHAR(15),
                                    salry INT,
                                    joining_date TEXT,
                                    adhar_no INT,
                                    TAG VARCHAR(15) );        """)

        # Bus Driver Table
        my_cursor_ct.execute(""" CREATE TABLE IF NOT EXISTS driver_data(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        name VARCHAR(30) NOT NULL,
                                        gender VARCHAR(5),
                                        age INT,
                                        phone_no INT,
                                        image BLOB,
                                        address VARCHAR(80),
                                        joining_date TEXT,
                                        adhar_no INT,
                                        travel_rout VARCHAR(40),
                                        vehicle_no VARCHAR(15),
                                        driving_license_copy BLOB,
                                        vehicle_smart_card_copy BLOB,
                                        vehicle_insurance_copy BLOB,
                                        TAG VARCHAR(15) );        """)

        # Worker Table
        my_cursor_ct.execute(""" CREATE TABLE IF NOT EXISTS worker_data(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                        name VARCHAR(30) NOT NULL,
                                        gender VARCHAR(5),
                                        age INT,
                                        phone_no INT,
                                        image BLOB,
                                        address VARCHAR(80),
                                        joining_date TEXT,
                                        adhar_no INT,
                                        salry INT,
                                        TAG VARCHAR(15) );        """)


        my_database_ct.commit()
        my_cursor_ct.close()
        my_database_ct.close()

    create_table_sqlite()
except Exception:
    pass



def write_binary_image(file, img):
    with open(file, 'wb') as w:
        w.write(img)


def read_binary_image(filename):
    try:
        with open(filename, 'rb') as file:
            binary_img = file.read()
        return binary_img
    except FileNotFoundError:
        pass


def add_new_student():
    but_frame.place_forget()
    search_entry.place_forget()
    search_button.place_forget()

    def on_add_new_but():
        msg_box_con = tkinter.messagebox.askquestion("Confirmation", "Do you want to save the new data ?")
        if msg_box_con == "yes":
            global bi_img
            st_glob_id = entry_glob_id.get()
            st_name = entry_name.get()
            st_class = entry_class.get()
            st_roll = entry_roll.get()
            st_class_teacher = entry_class_teacher.get()
            st_gender = entry_gender_text.get()
            st_age = entry_age.get()
            st_cast = entry_cast.get()
            st_phone = entry_ph.get()
            st_img = bi_img
            st_add = entry_add.get()
            st_edu = entry_edu.get()
            st_f_name = entry_f_name.get()
            st_m_name = entry_m_name.get()
            st_adm_date = entry_ad_date.get()
            st_ad_form_no = entry_ad_form_no.get()
            st_fee_subm = entry_fee_subm.get()
            st_fee_subm_date = entry_fee_subm_date.get()
            st_adhar_no = entry_adh_no.get()
            st_reg_no = entry_reg_no.get()
            st_bld_g = entry_bl_g.get()
            st_TAG = entry_TAG_text.get()
            bi_img = None

            if st_name == "":
                pass
            else:
                my_database_as = sqlite3.connect("Database.db")
                my_cur_add_stu = my_database_as.cursor()
                my_cur_add_stu.execute("""SELECT id FROM student_data""")
                give_id = my_cur_add_stu.fetchall()
                if not give_id:
                    my_cur_add_stu.execute("""INSERT INTO student_data(id, name) VALUES(100, 'id_counter')""")
                    my_database_as.commit()
                else:
                    pass
                query = ''' INSERT INTO 
                                student_data(global_student_id, name, class, roll_no, class_teacher_name, gender, age, cast, phone_no, image, address, education, father_name, mother_name, admission_date, admission_form_no, fee_submitted, fee_submission_date, adhar_no, register_no, blood_group, TAG)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                                '''
                st_tuple = (st_glob_id, st_name, st_class, st_roll, st_class_teacher, st_gender, st_age, st_cast, st_phone, st_img, st_add, st_edu, st_f_name, st_m_name, st_adm_date, st_ad_form_no, st_fee_subm, st_fee_subm_date, st_adhar_no, st_reg_no, st_bld_g, st_TAG)
                my_cur_add_stu.execute(query, st_tuple)
                my_database_as.commit()

                query_check = f'''SELECT id, name, class, address, image FROM student_data 
                                                    WHERE 
                                                    name='{st_name}' AND
                                                    class='{st_class}' AND
                                                    address='{st_add}';'''
                my_cur_add_stu.execute(query_check)
                check = my_cur_add_stu.fetchall()
                my_cur_add_stu.close()
                my_database_as.close()
                st_id_check = ''
                st_name_check = ''
                st_class_check = ''
                st_add_check = ''
                st_img_check = ''
                for col in check:
                    st_id_check = col[0]
                    st_name_check = col[1]
                    st_class_check = col[2]
                    st_add_check = col[3]
                    st_img_check = col[4]

                if st_name_check == st_name and st_class_check == st_class and st_add_check == st_add and st_img_check == st_img:
                    tkinter.messagebox.showinfo("Status", f"Data is inserted successfully in the database\nStudent Id = {st_id_check}")
                else:
                    tkinter.messagebox.showerror("Status", f"Failed to Add data")


        else:
            pass

    def on_add_image_button_add_new_student_frame():
        global bi_img
        path = filedialog.askopenfilename()
        bi_img = read_binary_image(path)
        try:
            resize_img = Image.open(path)
            resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
            resize_img.save("nres_img.ppm", "ppm")
            open_img = ImageTk.PhotoImage(Image.open('nres_img.ppm'))
            save_img.destroy()
            add_image.create_image(0, 0, image=open_img, anchor="nw")
            add_new_frame.mainloop()
        except AttributeError:
            pass

    add_new_frame = tkinter.Frame(main_window, width=1200, height=650, bg=background_colour)
    add_new_frame.place(x=80, y=30)

    # add new students labels and entries
    label_add_data = tkinter.Label(add_new_frame, text="Add Data in Below Columns", font=("bold", 12), bg=background_colour, fg="white")
    label_add_data.place(x=100, y=20)

    label_glob_id = tkinter.Label(add_new_frame, text="Global Student ID:", bg=background_colour, fg="white", font=("bold", 10))
    label_glob_id.place(x=0, y=65)
    entry_glob_id_text = tkinter.StringVar()
    entry_glob_id = tkinter.Entry(add_new_frame, text=entry_glob_id_text, width=40)
    entry_glob_id.place(x=150, y=65)

    label_name = tkinter.Label(add_new_frame, text="Student Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_name.place(x=0, y=115)
    entry_name_text = tkinter.StringVar()
    entry_name = tkinter.Entry(add_new_frame, text=entry_name_text, width=40)
    entry_name.place(x=150, y=115)

    label_class = tkinter.Label(add_new_frame, text="Student Class :", bg=background_colour, fg="white", font=("bold", 10))
    label_class.place(x=0, y=165)
    entry_class_text = tkinter.StringVar()
    entry_class = tkinter.Entry(add_new_frame, text=entry_class_text, width=40)
    entry_class.place(x=150, y=165)

    label_roll = tkinter.Label(add_new_frame, text="Roll No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_roll.place(x=0, y=215)
    entry_roll_text = tkinter.StringVar()
    entry_roll = tkinter.Entry(add_new_frame, text=entry_roll_text, width=40)
    entry_roll.place(x=150, y=215)

    label_class_teacher = tkinter.Label(add_new_frame, text="Class Teacher Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_class_teacher.place(x=0, y=265)
    entry_class_teacher_text = tkinter.StringVar()
    entry_class_teacher = tkinter.Entry(add_new_frame, text=entry_class_teacher_text, width=40)
    entry_class_teacher.place(x=150, y=265)

    label_gender = tkinter.Label(add_new_frame, text="Student Gender :", bg=background_colour, fg="white", font=("bold", 10))
    label_gender.place(x=0, y=315)
    entry_gender_text = tkinter.StringVar()
    entry_gender_text.set(0)
    entry_gender_m = tkinter.Radiobutton(add_new_frame, text="Male", variable=entry_gender_text, value="M", bg=background_colour)
    entry_gender_m.place(x=150, y=315)
    entry_gender_f = tkinter.Radiobutton(add_new_frame, text="Female", variable=entry_gender_text, value="F", bg=background_colour)
    entry_gender_f.place(x=220, y=315)

    label_age = tkinter.Label(add_new_frame, text="Student Age :", bg=background_colour, fg="white", font=("bold", 10))
    label_age.place(x=0, y=365)
    entry_age_text = tkinter.StringVar()
    entry_age = tkinter.Entry(add_new_frame, text=entry_age_text, width=40)
    entry_age.place(x=150, y=365)

    label_cast = tkinter.Label(add_new_frame, text="Student Cast :", bg=background_colour, fg="white", font=("bold", 10))
    label_cast.place(x=0, y=415)
    entry_cast_text = tkinter.StringVar()
    entry_cast = tkinter.Entry(add_new_frame, text=entry_cast_text, width=40)
    entry_cast.place(x=150, y=415)

    label_ph = tkinter.Label(add_new_frame, text="Student Ph.No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_ph.place(x=0, y=465)
    entry_ph_text = tkinter.StringVar()
    entry_ph = tkinter.Entry(add_new_frame, text=entry_ph_text, width=40)
    entry_ph.place(x=150, y=465)

    add_image = tkinter.Canvas(add_new_frame, width=200, height=260)
    add_image.place(x=500, y=100)
    add_leb_image = tkinter.Label(add_new_frame, text="Student Image", bg=background_colour, fg="white", font=("bold", 10))
    add_leb_image.place(x=500, y=65)
    add_but_img = tkinter.PhotoImage(file="add_image.png")
    save_img = tkinter.Button(add_new_frame, image=add_but_img, bd=0, relief="groove", command=on_add_image_button_add_new_student_frame)
    save_img.place(x=580, y=200)


    label_add = tkinter.Label(add_new_frame, text="Student Add :", bg=background_colour, fg="white", font=("bold", 10))
    label_add.place(x=0, y=515)
    entry_add_text = tkinter.StringVar()
    entry_add = tkinter.Entry(add_new_frame, text=entry_add_text, width=40)
    entry_add.place(x=150, y=515)

    label_edu = tkinter.Label(add_new_frame, text=" Student Education :", bg=background_colour, fg="white", font=("bold", 10))
    label_edu.place(x=0, y=565)
    entry_edu_text = tkinter.StringVar()
    entry_edu = tkinter.Entry(add_new_frame, text=entry_edu_text, width=40)
    entry_edu.place(x=150, y=565)

    label_f_name = tkinter.Label(add_new_frame, text=" Father's Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_f_name.place(x=750, y=65)
    entry_f_name_text = tkinter.StringVar()
    entry_f_name = tkinter.Entry(add_new_frame, text=entry_f_name_text, width=40)
    entry_f_name.place(x=900, y=65)

    label_m_name = tkinter.Label(add_new_frame, text=" Mother's Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_m_name.place(x=750, y=115)
    entry_m_name_text = tkinter.StringVar()
    entry_m_name = tkinter.Entry(add_new_frame, text=entry_m_name_text, width=40)
    entry_m_name.place(x=900, y=115)

    label_ad_date = tkinter.Label(add_new_frame, text=" Admission Date :", bg=background_colour, fg="white", font=("bold", 10))
    label_ad_date.place(x=750, y=165)
    entry_ad_date_text = tkinter.StringVar()
    entry_ad_date = tkinter.Entry(add_new_frame, text=entry_ad_date_text, width=40)
    entry_ad_date.place(x=900, y=165)

    label_ad_form_no = tkinter.Label(add_new_frame, text=" Admission Form No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_ad_form_no.place(x=750, y=215)
    entry_ad_form_no_text = tkinter.StringVar()
    entry_ad_form_no = tkinter.Entry(add_new_frame, text=entry_ad_form_no_text, width=40)
    entry_ad_form_no.place(x=900, y=215)

    label_fee_subm = tkinter.Label(add_new_frame, text=" Fee Submitted :", bg=background_colour, fg="white", font=("bold", 10))
    label_fee_subm.place(x=750, y=265)
    entry_fee_subm_text = tkinter.StringVar()
    entry_fee_subm = tkinter.Entry(add_new_frame, text=entry_fee_subm_text, width=40)
    entry_fee_subm.place(x=900, y=265)

    label_fee_subm_date = tkinter.Label(add_new_frame, text=" Fee Submission Date :", bg=background_colour, fg="white", font=("bold", 10))
    label_fee_subm_date.place(x=750, y=315)
    entry_fee_subm_date_text = tkinter.StringVar()
    entry_fee_subm_date = tkinter.Entry(add_new_frame, text=entry_fee_subm_date_text, width=40)
    entry_fee_subm_date.place(x=900, y=315)

    label_adh_no = tkinter.Label(add_new_frame, text=" Adhar No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_adh_no.place(x=750, y=365)
    entry_adh_no_text = tkinter.StringVar()
    entry_adh_no = tkinter.Entry(add_new_frame, text=entry_adh_no_text, width=40)
    entry_adh_no.place(x=900, y=365)

    label_reg_no = tkinter.Label(add_new_frame, text=" G.Reg. No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_reg_no.place(x=750, y=415)
    entry_reg_no_text = tkinter.StringVar()
    entry_reg_no = tkinter.Entry(add_new_frame, text=entry_reg_no_text, width=40)
    entry_reg_no.place(x=900, y=415)

    label_bl_g = tkinter.Label(add_new_frame, text="Blood Group :", bg=background_colour, fg="white", font=("bold", 10))
    label_bl_g.place(x=750, y=465)
    entry_bl_g_text = tkinter.StringVar()
    entry_bl_g = tkinter.Entry(add_new_frame, text=entry_bl_g_text, width=40)
    entry_bl_g.place(x=900, y=465)

    label_TAG = tkinter.Label(add_new_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
    label_TAG.place(x=750, y=515)
    options_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
    entry_TAG_text = tkinter.StringVar()
    entry_TAG = tkinter.OptionMenu(add_new_frame, entry_TAG_text, *options_for_TAG)
    entry_TAG.config(relief="raised", bd=0)
    entry_TAG.place(x=900, y=515)


    def cancel_fun():
        add_new_frame.destroy()
        but_frame.place(x=80, y=80)
        search_entry.place(x=50, y=30)
        search_button.place(x=300, y=28)
        but_frame_func()

    # save changes button
    save_but = tkinter.Button(add_new_frame, text="Save", command=on_add_new_but, width=10, relief="groove")
    save_but.place(x=1070, y=620)

    cancel_but = tkinter.Button(add_new_frame, text="Cancel", command=cancel_fun, width=10, relief="groove")
    cancel_but.place(x=970, y=620)

    add_new_frame.mainloop()

def show_all_student():
    search_entry.config(state='disabled')
    search_button.config(state='disabled')
    but_frame.place_forget()

    def select_rec():
        reco = tree_view.focus()
        if reco == "":
            pass
        else:
            temp = tree_view.item(reco)
            cmp = temp['values']
            search_entry.config(state='normal')
            search_button.config(state='normal')
            search_entry.insert(0, cmp[0])
            tree_view_frame.destroy()
            on_search_button()


    tree_view_frame = tkinter.Frame(main_window, width=1100, height=530, bg=background_colour)
    tree_view_frame.place(x=80, y=100)


    tree_view = ttk.Treeview(tree_view_frame, columns=("", "", "", "", ""), height=24, selectmode="browse")
    tree_view.place(x=0, y=30)
    scroll_bar = ttk.Scrollbar(tree_view_frame, orient='vertical', command=tree_view.yview)
    scroll_bar.place(x=975, y=30, height=500)

    tree_view.configure(yscrollcommand=scroll_bar.set)


    tree_view.heading('#0', text='No.', anchor="w")
    tree_view.column("#0", width=60)
    tree_view.heading('#1', text='Id No.', anchor="center")
    tree_view.column("#1", width=60)
    tree_view.heading('#2', text='Name', anchor="center")
    tree_view.column("#2", width=250)
    tree_view.heading('#3', text='Class', anchor="center")
    tree_view.column("#3", width=100)
    tree_view.heading('#4', text='Address', anchor="center")
    tree_view.column("#4", width=300)
    tree_view.heading('#5', text='Phone No.', anchor="center")
    tree_view.column("#5", width=200)


    style = ttk.Style()
    style.configure("Treeview.Heading", foreground='black', font=('bold', 10))
    my_database_show_all_student = sqlite3.connect("Database.db")
    my_cur_show_stu = my_database_show_all_student.cursor()
    my_cur_show_stu.execute("SELECT id, name, class, address, phone_no FROM student_data WHERE id>100 ORDER BY name")
    read = my_cur_show_stu.fetchall()
    my_cur_show_stu.close()
    my_database_show_all_student.close()

    total_record = tkinter.Label(tree_view_frame, text=f"Total Record = {len(read)}", bg=background_colour, font=("bold", 10), fg="gold")
    total_record.place(x=0, y=0)

    i = 1
    for col in read:
        tree_view.insert("", "end", text=i, values=(col[0], col[1], col[2], col[3], col[4]))
        i += 1

    def cancel():
        tree_view_frame.destroy()
        search_entry.config(state='normal')
        search_button.config(state='normal')
        but_frame.place(x=80, y=80)

    open_but = tkinter.Button(tree_view_frame, text="Open", relief="groove", width=10, command=select_rec)
    open_but.place(x=1000, y=30)

    cancel_but = tkinter.Button(tree_view_frame, text="Cancel", relief="groove", width=10, command=cancel)
    cancel_but.place(x=1000, y=80)


def add_new_teacher():
    but_frame.place_forget()
    search_entry.place_forget()
    search_button.place_forget()

    def on_add_new_but():
        msg_box_con = tkinter.messagebox.askquestion("Confirmation", "Do you want to save the new data ?")
        if msg_box_con == "yes":
            global bi_img
            name = entry_name.get()
            gen = entry_gender_text.get()
            age = entry_age.get()
            t_class = entry_class.get()
            sub = entry_sub.get()
            ph = entry_ph.get()
            img = bi_img
            add = entry_add.get()
            edu = entry_edu.get()
            sal = entry_sal.get()
            jo_date = entry_jd.get()
            adh_no = entry_adh_no.get()
            TAG = entry_TAG_text.get()
            bi_img = None

            if name == "":
                pass
            else:
                my_database_insert_teacher = sqlite3.connect("Database.db")
                my_cur_insert_teacher = my_database_insert_teacher.cursor()
                my_cur_insert_teacher.execute("""SELECT id FROM teacher_data""")
                give_id = my_cur_insert_teacher.fetchall()
                if not give_id:
                    my_cur_insert_teacher.execute("""INSERT INTO teacher_data(id, name) VALUES(5000, 'id_counter')""")
                    my_database_insert_teacher.commit()
                else:
                    pass
                query = f'''INSERT INTO  teacher_data(name, gender, age, teacher_of_class, subject, phone_no, image, address, education, salry, joining_date, adhar_no, TAG) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); '''

                tuple_ = (name, gen, age, t_class, sub, ph, img, add, edu, sal, jo_date, adh_no, TAG)
                my_cur_insert_teacher.execute(query, tuple_)
                my_database_insert_teacher.commit()

                query_check = f'''SELECT id, name, teacher_of_class, image FROM teacher_data
                                                        WHERE 
                                                        name='{name}' AND
                                                        teacher_of_class='{t_class}';
                                                  '''
                my_cur_insert_teacher.execute(query_check)
                check = my_cur_insert_teacher.fetchall()
                my_cur_insert_teacher.close()
                my_database_insert_teacher.close()
                id_check = ''
                name_check = ''
                te_of_class = ''
                img_check = ''
                for col in check:
                    id_check = col[0]
                    name_check = col[1]
                    te_of_class = col[2]
                    img_check = col[3]
                if name_check == name and te_of_class == t_class and img_check == img :
                    tkinter.messagebox.showinfo("Status",
                                                f"Data is inserted successfully in the database\nTeacher Id = {id_check}")
                else:
                    tkinter.messagebox.showerror("Status", f"Failed to Add data")

    def on_add_image_button_add_new_student_frame():
        global bi_img
        path = filedialog.askopenfilename()
        bi_img = read_binary_image(path)
        try:
            resize_img = Image.open(path)
            resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
            resize_img.save("nres_img.ppm", "ppm")
            open_img = ImageTk.PhotoImage(Image.open('nres_img.ppm'))
            save_img.destroy()
            add_image.create_image(0, 0, image=open_img, anchor="nw")
            add_new_frame.mainloop()
        except AttributeError:
            pass

    add_new_frame = tkinter.Frame(main_window, width=1200, height=650, bg=background_colour)
    add_new_frame.place(x=80, y=30)

    # add new students labels and entries
    label_add_data = tkinter.Label(add_new_frame, text="Add Data in Below Columns", font=("bold", 12),
                                   bg=background_colour, fg="white")
    label_add_data.place(x=100, y=20)

    label_name = tkinter.Label(add_new_frame, text="Teacher Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_name.place(x=0, y=65)
    entry_name_text = tkinter.StringVar()
    entry_name = tkinter.Entry(add_new_frame, text=entry_name_text, width=40)
    entry_name.place(x=150, y=65)

    label_gender = tkinter.Label(add_new_frame, text="Teacher Gender :", bg=background_colour, fg="white", font=("bold", 10))
    label_gender.place(x=0, y=115)
    entry_gender_text = tkinter.StringVar()
    entry_gender_text.set(0)
    entry_gender_m = tkinter.Radiobutton(add_new_frame, text="Male", variable=entry_gender_text, value="M", bg=background_colour)
    entry_gender_m.place(x=150, y=115)
    entry_gender_f = tkinter.Radiobutton(add_new_frame, text="Female", variable=entry_gender_text, value="F", bg=background_colour)
    entry_gender_f.place(x=220, y=115)

    label_age = tkinter.Label(add_new_frame, text="Teacher Age :", bg=background_colour, fg="white", font=("bold", 10))
    label_age.place(x=0, y=165)
    entry_age_text = tkinter.StringVar()
    entry_age = tkinter.Entry(add_new_frame, text=entry_age_text, width=40)
    entry_age.place(x=150, y=165)

    label_class = tkinter.Label(add_new_frame, text="Teacher Of Class :", bg=background_colour, fg="white", font=("bold", 10))
    label_class.place(x=0, y=215)
    entry_class_text = tkinter.StringVar()
    entry_class = tkinter.Entry(add_new_frame, text=entry_class_text, width=40)
    entry_class.place(x=150, y=215)

    label_sub = tkinter.Label(add_new_frame, text="Teaching subject :", bg=background_colour, fg="white", font=("bold", 10))
    label_sub.place(x=0, y=265)
    entry_sub_text = tkinter.StringVar()
    entry_sub = tkinter.Entry(add_new_frame, text=entry_sub_text, width=40)
    entry_sub.place(x=150, y=265)

    label_ph = tkinter.Label(add_new_frame, text="Teacher Ph.No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_ph.place(x=0, y=315)
    entry_ph_text = tkinter.StringVar()
    entry_ph = tkinter.Entry(add_new_frame, text=entry_ph_text, width=40)
    entry_ph.place(x=150, y=315)

    add_image = tkinter.Canvas(add_new_frame, width=200, height=260)
    add_image.place(x=500, y=100)
    add_leb_image = tkinter.Label(add_new_frame, text="Teacher Image :", bg=background_colour, fg="white", font=("bold", 10))
    add_leb_image.place(x=500, y=65)
    add_but_img = tkinter.PhotoImage(file="add_image.png")
    save_img = tkinter.Button(add_new_frame, image=add_but_img, bd=0, relief="groove",
                              command=on_add_image_button_add_new_student_frame)
    save_img.place(x=580, y=200)


    label_add = tkinter.Label(add_new_frame, text="Teacher Add :", bg=background_colour, fg="white", font=("bold", 10))
    label_add.place(x=0, y=365)
    entry_add_text = tkinter.StringVar()
    entry_add = tkinter.Entry(add_new_frame, text=entry_add_text, width=40)
    entry_add.place(x=150, y=365)

    label_edu = tkinter.Label(add_new_frame, text="Teacher edu. :", bg=background_colour, fg="white", font=("bold", 10))
    label_edu.place(x=0, y=415)
    entry_edu_text = tkinter.StringVar()
    entry_edu = tkinter.Entry(add_new_frame, text=entry_edu_text, width=40)
    entry_edu.place(x=150, y=415)

    label_sal = tkinter.Label(add_new_frame, text="Teacher Salary :", bg=background_colour, fg="white", font=("bold", 10))
    label_sal.place(x=0, y=465)
    entry_sal_text = tkinter.StringVar()
    entry_sal = tkinter.Entry(add_new_frame, text=entry_sal_text, width=40)
    entry_sal.place(x=150, y=465)

    label_jd = tkinter.Label(add_new_frame, text="Joining Date :", bg=background_colour, fg="white", font=("bold", 10))
    label_jd.place(x=0, y=515)
    entry_jd_text = tkinter.StringVar()
    entry_jd = tkinter.Entry(add_new_frame, text=entry_jd_text, width=40)
    entry_jd.place(x=150, y=515)

    label_adh_no = tkinter.Label(add_new_frame, text="Adhar No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_adh_no.place(x=0, y=565)
    entry_adh_no_text = tkinter.StringVar()
    entry_adh_no = tkinter.Entry(add_new_frame, text=entry_adh_no_text, width=40)
    entry_adh_no.place(x=150, y=565)

    label_TAG = tkinter.Label(add_new_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
    label_TAG.place(x=750, y=65)
    option_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
    entry_TAG_text = tkinter.StringVar()
    entry_TAG = tkinter.OptionMenu(add_new_frame, entry_TAG_text, *option_for_TAG)
    entry_TAG.config(relief="raised", bd=0)
    entry_TAG.place(x=900, y=65)



    def cancel_fun():
        add_new_frame.destroy()
        but_frame.place(x=80, y=80)
        search_entry.place(x=50, y=30)
        search_button.place(x=300, y=28)
        but_frame_func()

    # save changes button
    save_but = tkinter.Button(add_new_frame, text="Save", command=on_add_new_but, width=10, relief="groove")
    save_but.place(x=1070, y=620)

    cancel_but = tkinter.Button(add_new_frame, text="Cancel", command=cancel_fun, width=10, relief="groove")
    cancel_but.place(x=970, y=620)

    add_new_frame.mainloop()

def show_all_teacher():
    search_entry.config(state='disabled')
    search_button.config(state='disabled')
    but_frame.place_forget()

    def select_rec():
        reco = tree_view.focus()
        if reco == "":
            pass
        else:
            temp = tree_view.item(reco)
            cmp = temp['values']
            search_entry.config(state='normal')
            search_button.config(state='normal')
            search_entry.insert(0, cmp[0])
            tree_view_frame.destroy()
            on_search_button()

    tree_view_frame = tkinter.Frame(main_window, width=1100, height=530, bg=background_colour)
    tree_view_frame.place(x=80, y=100)

    tree_view = ttk.Treeview(tree_view_frame, columns=("", "", "", "", ""), height=24, selectmode="browse")
    tree_view.place(x=0, y=30)
    scroll_bar = ttk.Scrollbar(tree_view_frame, orient='vertical', command=tree_view.yview)
    scroll_bar.place(x=975, y=30, height=500)

    tree_view.configure(yscrollcommand=scroll_bar.set)

    tree_view.heading('#0', text='No.', anchor="w")
    tree_view.column("#0", width=60)
    tree_view.heading('#1', text='Id No.', anchor="center")
    tree_view.column("#1", width=60)
    tree_view.heading('#2', text='Name', anchor="center")
    tree_view.column("#2", width=250)
    tree_view.heading('#3', text='Address', anchor="center")
    tree_view.column("#3", width=300)
    tree_view.heading('#4', text='Phone No.', anchor="center")
    tree_view.column("#4", width=100)
    tree_view.heading('#5', text='Education', anchor="center")
    tree_view.column("#5", width=200)

    style = ttk.Style()
    style.configure("Treeview.Heading", foreground='black', font=('bold', 10))

    my_database_show_all_teacher = sqlite3.connect("Database.db")
    my_cur_show_all_teacher = my_database_show_all_teacher.cursor()
    my_cur_show_all_teacher.execute(
        "SELECT id, name, address, phone_no, education FROM teacher_data WHERE id>5000 ORDER BY name")
    read = my_cur_show_all_teacher.fetchall()
    my_cur_show_all_teacher.close()
    my_database_show_all_teacher.close()

    total_record = tkinter.Label(tree_view_frame, text=f"Total Record = {len(read)}", bg=background_colour,
                                 font=("bold", 10), fg="gold")
    total_record.place(x=0, y=0)

    i = 1
    for col in read:
        tree_view.insert("", "end", text=i, values=(col[0], col[1], col[2], col[3], col[4]))
        i += 1

    def cancel():
        tree_view_frame.destroy()
        search_entry.config(state='normal')
        search_button.config(state='normal')
        but_frame.place(x=80, y=80)

    open_but = tkinter.Button(tree_view_frame, text="Open", relief="groove", width=10, command=select_rec)
    open_but.place(x=1000, y=30)

    cancel_but = tkinter.Button(tree_view_frame, text="Cancel", relief="groove", width=10, command=cancel)
    cancel_but.place(x=1000, y=80)


def add_new_driver():
    but_frame.place_forget()
    search_entry.place_forget()
    search_button.place_forget()

    def on_add_new_but():
        msg_box_con = tkinter.messagebox.askquestion("Confirmation", "Do you want to save the new data ?")
        if msg_box_con == "yes":
            global bi_img
            global bi_driver_lic
            global bi_veh_sm_card_copy
            global bi_veh_ins_copy
            name = entry_name.get()
            gen = entry_gender_text.get()
            age = entry_age.get()
            ph = entry_ph.get()
            img = bi_img
            add = entry_add.get()
            jo_date = entry_jo_date.get()
            adh_no = entry_adh_no.get()
            tr_rout = entry_t_rout.get()
            v_no = entry_v_no.get()
            v_lic = bi_driver_lic
            v_sm = bi_veh_sm_card_copy
            v_ins = bi_veh_ins_copy
            TAG = entry_TAG_text.get()
            bi_img = None
            bi_driver_lic = None
            bi_veh_sm_card_copy = None
            bi_veh_ins_copy = None

            if name == "":
                tkinter.messagebox.showwarning("Warring", "Insert at least Name. ?")
                pass
            else:
                my_database_add_driver = sqlite3.connect("Database.db")
                my_cur_add_driver = my_database_add_driver.cursor()
                my_cur_add_driver.execute("""SELECT id FROM driver_data""")
                give_id = my_cur_add_driver.fetchall()
                if not give_id:
                    my_cur_add_driver.execute("""INSERT INTO driver_data(id, name) VALUES(6000, 'id_counter')""")
                    my_database_add_driver.commit()
                else:
                    pass
                query = f'''INSERT INTO driver_data(name, gender, age, phone_no, image, address, joining_date, adhar_no, travel_rout, vehicle_no, driving_license_copy, vehicle_smart_card_copy, vehicle_insurance_copy, TAG)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                tuple_ = (name, gen, age, ph, img, add, jo_date, adh_no, tr_rout, v_no, v_lic, v_sm, v_ins, TAG)
                my_cur_add_driver.execute(query, tuple_)
                my_database_add_driver.commit()


                query_check = f'''SELECT id, name, address, gender, image FROM driver_data 
                                                            WHERE 
                                                            name='{name}' AND
                                                            address='{add}' AND            
                                                            gender='{gen}';
                                                      '''
                my_cur_add_driver.execute(query_check)
                check = my_cur_add_driver.fetchall()
                my_cur_add_driver.close()
                my_database_add_driver.close()
                id_check = ''
                name_check = ''
                add_check = ''
                gen_check = ''
                img_check = ''
                for col in check:
                    id_check = col[0]
                    name_check = col[1]
                    add_check = col[2]
                    gen_check = col[3]
                    img_check = col[4]
                if name_check == name and add_check == add and gen_check == gen and img_check == img:
                    tkinter.messagebox.showinfo("Status",
                                                f"Data is inserted successfully in the database\nTeacher Id = {id_check}")
                else:
                    tkinter.messagebox.showerror("Status", f"Failed to Add data")

    def on_add_image_button_add_new_student_frame():
        global bi_img
        path = filedialog.askopenfilename()
        bi_img = read_binary_image(path)
        try:
            resize_img = Image.open(path)
            resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
            resize_img.save("nres_img.ppm", "ppm")
            open_img = ImageTk.PhotoImage(Image.open('nres_img.ppm'))
            save_img.destroy()
            add_image.create_image(0, 0, image=open_img, anchor="nw")
            add_new_frame.mainloop()
        except AttributeError:
            pass

    add_new_frame = tkinter.Frame(main_window, width=1200, height=650, bg=background_colour)
    add_new_frame.place(x=80, y=30)

    # add new students labels and entries
    label_add_data = tkinter.Label(add_new_frame, text="Add Data in Below Columns", font=("bold", 12),
                                   bg=background_colour, fg="white")
    label_add_data.place(x=100, y=20)

    label_name = tkinter.Label(add_new_frame, text="Driver Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_name.place(x=0, y=65)
    entry_name_text = tkinter.StringVar()
    entry_name = tkinter.Entry(add_new_frame, text=entry_name_text, width=40)
    entry_name.place(x=150, y=65)

    leble_gender = tkinter.Label(add_new_frame, text="Driver Gender :", bg=background_colour, fg="white", font=("bold", 10))
    leble_gender.place(x=0, y=115)
    entry_gender_text = tkinter.StringVar()
    entry_gender_text.set(0)
    entry_gender_m = tkinter.Radiobutton(add_new_frame, text="Male", variable=entry_gender_text, value="M", bg=background_colour)
    entry_gender_m.place(x=150, y=115)
    entry_gender_f = tkinter.Radiobutton(add_new_frame, text="Female", variable=entry_gender_text, value="F", bg=background_colour)
    entry_gender_f.place(x=220, y=115)

    label_age = tkinter.Label(add_new_frame, text="Driver Age :", bg=background_colour, fg="white", font=("bold", 10))
    label_age.place(x=0, y=165)
    entry_age_text = tkinter.StringVar()
    entry_age = tkinter.Entry(add_new_frame, text=entry_age_text, width=40)
    entry_age.place(x=150, y=165)

    label_ph = tkinter.Label(add_new_frame, text="Driver Ph.No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_ph.place(x=0, y=215)
    entry_ph_text = tkinter.StringVar()
    entry_ph = tkinter.Entry(add_new_frame, text=entry_ph_text, width=40)
    entry_ph.place(x=150, y=215)

    add_image = tkinter.Canvas(add_new_frame, width=200, height=260)
    add_image.place(x=500, y=100)
    add_leb_image = tkinter.Label(add_new_frame, text="Driver Image :", bg=background_colour, fg="white", font=("bold", 10))
    add_leb_image.place(x=500, y=65)
    add_but_img = tkinter.PhotoImage(file="add_image.png")
    save_img = tkinter.Button(add_new_frame, image=add_but_img, bd=0, relief="groove", command=on_add_image_button_add_new_student_frame)
    save_img.place(x=580, y=200)

    label_add = tkinter.Label(add_new_frame, text="Driver Add :", bg=background_colour, fg="white", font=("bold", 10))
    label_add.place(x=0, y=265)
    entry_add_text = tkinter.StringVar()
    entry_add = tkinter.Entry(add_new_frame, text=entry_add_text, width=40)
    entry_add.place(x=150, y=265)

    label_jo_date = tkinter.Label(add_new_frame, text="Joining Date :", bg=background_colour, fg="white", font=("bold", 10))
    label_jo_date.place(x=0, y=315)
    entry_jo_date_text = tkinter.StringVar()
    entry_jo_date = tkinter.Entry(add_new_frame, text=entry_jo_date_text, width=40)
    entry_jo_date.place(x=150, y=315)

    label_adh_no = tkinter.Label(add_new_frame, text="Adhar No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_adh_no.place(x=0, y=365)
    entry_adh_no_text = tkinter.StringVar()
    entry_adh_no = tkinter.Entry(add_new_frame, text=entry_adh_no_text, width=40)
    entry_adh_no.place(x=150, y=365)

    label_t_rout = tkinter.Label(add_new_frame, text="Travel Rout :", bg=background_colour, fg="white", font=("bold", 10))
    label_t_rout.place(x=0, y=415)
    entry_t_rout_text = tkinter.StringVar()
    entry_t_rout = tkinter.Entry(add_new_frame, text=entry_t_rout_text, width=40)
    entry_t_rout.place(x=150, y=415)

    label_v_no = tkinter.Label(add_new_frame, text="Vehicle No. :", bg=background_colour, fg="white", font=("bold", 10))
    label_v_no.place(x=0, y=465)
    entry_v_no_text = tkinter.StringVar()
    entry_v_no = tkinter.Entry(add_new_frame, text=entry_v_no_text, width=40)
    entry_v_no.place(x=150, y=465)

    label_v_lic = tkinter.Label(add_new_frame, text="Vehicle Documents :", bg=background_colour, fg="white", font=("bold", 10))
    label_v_lic.place(x=720, y=65)

    def on_add_lic():
        global bi_driver_lic
        path = filedialog.askopenfilename()
        bi_driver_lic = read_binary_image(path)
    entry_v_lic = tkinter.Button(add_new_frame, text="Add Driving License", bd=1, command=on_add_lic)
    entry_v_lic.place(x=850, y=65)

    def on_add_sm_card():
        global bi_veh_sm_card_copy
        path = filedialog.askopenfilename()
        bi_veh_sm_card_copy = read_binary_image(path)
    entry_v_sm = tkinter.Button(add_new_frame, text="Add veh. Smart card", bd=1, command=on_add_sm_card)
    entry_v_sm.place(x=850, y=100)

    def on_add_ins():
        global bi_veh_ins_copy
        path = filedialog.askopenfilename()
        bi_veh_ins_copy = read_binary_image(path)
    entry_v_in = tkinter.Button(add_new_frame, text="Add veh. Insurance", bd=1, command=on_add_ins)
    entry_v_in.place(x=850, y=135)


    label_TAG = tkinter.Label(add_new_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
    label_TAG.place(x=0, y=515)
    option_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
    entry_TAG_text = tkinter.StringVar()
    entry_TAG = tkinter.OptionMenu(add_new_frame, entry_TAG_text, *option_for_TAG)
    entry_TAG.config(relief="raised", bd=0)
    entry_TAG.place(x=150, y=515)


    def cancel_fun():
        add_new_frame.destroy()
        but_frame.place(x=80, y=80)
        search_entry.place(x=50, y=30)
        search_button.place(x=300, y=28)
        but_frame_func()

    # save changes button
    save_but = tkinter.Button(add_new_frame, text="Save", command=on_add_new_but, width=10, relief="groove")
    save_but.place(x=1070, y=620)

    cancel_but = tkinter.Button(add_new_frame, text="Cancel", command=cancel_fun, width=10, relief="groove")
    cancel_but.place(x=970, y=620)

    add_new_frame.mainloop()

def show_all_driver():
    search_entry.config(state='disabled')
    search_button.config(state='disabled')
    but_frame.place_forget()

    def select_rec():
        reco = tree_view.focus()
        if reco == "":
            pass
        else:
            temp = tree_view.item(reco)
            cmp = temp['values']
            search_entry.config(state='normal')
            search_button.config(state='normal')
            search_entry.insert(0, cmp[0])
            tree_view_frame.destroy()
            on_search_button()


    tree_view_frame = tkinter.Frame(main_window, width=1100, height=530, bg=background_colour)
    tree_view_frame.place(x=80, y=100)

    tree_view = ttk.Treeview(tree_view_frame, columns=("", "", "", "", ""), height=24, selectmode="browse")
    tree_view.place(x=0, y=30)
    scroll_bar = ttk.Scrollbar(tree_view_frame, orient='vertical', command=tree_view.yview)
    scroll_bar.place(x=975, y=30, height=500)

    tree_view.configure(yscrollcommand=scroll_bar.set)

    tree_view.heading('#0', text='No.', anchor="w")
    tree_view.column("#0", width=60)
    tree_view.heading('#1', text='Id No.', anchor="center")
    tree_view.column("#1", width=60)
    tree_view.heading('#2', text='Name', anchor="center")
    tree_view.column("#2", width=250)
    tree_view.heading('#3', text='Address', anchor="center")
    tree_view.column("#3", width=300)
    tree_view.heading('#4', text='Phone No.', anchor="center")
    tree_view.column("#4", width=100)
    tree_view.heading('#5', text='Traveling Rout', anchor="center")
    tree_view.column("#5", width=200)

    style = ttk.Style()
    style.configure("Treeview.Heading", foreground='black', font=('bold', 10))

    my_database_show_driver = sqlite3.connect("Database.db")
    my_cur_show_driver = my_database_show_driver.cursor()
    my_cur_show_driver.execute(
        "SELECT id, name, address, phone_no, travel_rout FROM driver_data WHERE id>6000 ORDER BY name")
    read = my_cur_show_driver.fetchall()
    my_cur_show_driver.close()
    my_database_show_driver.close()

    total_record = tkinter.Label(tree_view_frame, text=f"Total Record = {len(read)}", bg=background_colour,
                                 font=("bold", 10), fg="gold")
    total_record.place(x=0, y=0)

    i = 1
    for col in read:
        tree_view.insert("", "end", text=i, values=(col[0], col[1], col[2], col[3], col[4]))
        i += 1

    def cancel():
        tree_view_frame.destroy()
        search_entry.config(state='normal')
        search_button.config(state='normal')
        but_frame.place(x=80, y=80)

    open_but = tkinter.Button(tree_view_frame, text="Open", relief="groove", width=10, command=select_rec)
    open_but.place(x=1000, y=30)

    cancel_but = tkinter.Button(tree_view_frame, text="Cancel", relief="groove", width=10, command=cancel)
    cancel_but.place(x=1000, y=80)


def add_new_worker():
    but_frame.place_forget()
    search_entry.place_forget()
    search_button.place_forget()

    def on_add_new_but():
        msg_box_con = tkinter.messagebox.askquestion("Confirmation", "Do you want to save the new data ?")
        if msg_box_con == "yes":
            global bi_img
            name = entry_name.get()
            gen = entry_gender_text.get()
            age = entry_age.get()
            ph = entry_ph.get()
            img = bi_img
            add = entry_add.get()
            jo_date = entry_jo_date.get()
            adh = entry_adh.get()
            sal = entry_sal.get()
            TAG = entry_TAG_text.get()
            bi_img = None

            if name == "":
                tkinter.messagebox.showwarning("Warring", "You should have to type attlist name")
                pass
            else:
                my_database_add_worker = sqlite3.connect("Database.db")
                my_cur_add_worker = my_database_add_worker.cursor()
                my_cur_add_worker.execute("""SELECT id FROM worker_data""")
                give_id = my_cur_add_worker.fetchall()
                if not give_id:
                    my_cur_add_worker.execute("""INSERT INTO worker_data(id, name) VALUES(7000, 'id_counter')""")
                    my_database_add_worker.commit()
                else:
                    pass
                query = f'''INSERT INTO  worker_data(name, gender, age, phone_no, image, address, joining_date, adhar_no, salry, TAG) 
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''


                tuple_ = (name, gen, age, ph, img, add, jo_date, adh, sal, TAG)
                my_cur_add_worker.execute(query, tuple_)
                my_database_add_worker.commit()

                query_check = f'''SELECT id, name, address FROM worker_data
                                                                WHERE 
                                                                name='{name}' AND
                                                                address='{add}';
                                                          '''
                my_cur_add_worker.execute(query_check)
                check = my_cur_add_worker.fetchall()
                my_cur_add_worker.close()
                my_database_add_worker.close()
                id_check = ''
                name_check = ''
                add_check = ''

                for col in check:
                    id_check = col[0]
                    name_check = col[1]
                    add_check = col[2]

                if name_check == name and add_check == add:
                    tkinter.messagebox.showinfo("Status",
                                                f"Data is inserted successfully in the database\nTeacher Id = {id_check}")
                else:
                    tkinter.messagebox.showerror("Status", f"Failed to Add data")

        else:
            pass

    def on_add_image_button_add_new_student_frame():
        global bi_img
        path = filedialog.askopenfilename()
        bi_img = read_binary_image(path)
        try:
            resize_img = Image.open(path)
            resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
            resize_img.save("nres_img.ppm", "ppm")
            open_img = ImageTk.PhotoImage(Image.open('nres_img.ppm'))
            save_img.destroy()
            add_image.create_image(0, 0, image=open_img, anchor="nw")
            add_new_frame.mainloop()
        except AttributeError:
            pass

    add_new_frame = tkinter.Frame(main_window, width=1200, height=650, bg=background_colour)
    add_new_frame.place(x=80, y=30)

    # add new students labels and entries
    label_add_data = tkinter.Label(add_new_frame, text="Add Data in Below Columns", font=("bold", 12),
                                   bg=background_colour, fg="white")
    label_add_data.place(x=100, y=20)

    label_name = tkinter.Label(add_new_frame, text="Worker Name :", bg=background_colour, fg="white", font=("bold", 10))
    label_name.place(x=0, y=65)
    entry_name_text = tkinter.StringVar()
    entry_name = tkinter.Entry(add_new_frame, text=entry_name_text, width=40)
    entry_name.place(x=150, y=65)

    lebel_gender = tkinter.Label(add_new_frame, text="Worker Gender :", bg=background_colour, fg="white",
                                 font=("bold", 10))
    lebel_gender.place(x=0, y=115)
    entry_gender_text = tkinter.StringVar()
    entry_gender_text.set(0)
    entry_gender_m = tkinter.Radiobutton(add_new_frame, text="Male", variable=entry_gender_text, value="M",
                                         bg=background_colour)
    entry_gender_m.place(x=150, y=115)
    entry_gender_f = tkinter.Radiobutton(add_new_frame, text="Female", variable=entry_gender_text, value="F",
                                         bg=background_colour)
    entry_gender_f.place(x=220, y=115)

    label_age = tkinter.Label(add_new_frame, text="Worker Age :", bg=background_colour, fg="white", font=("bold", 10))
    label_age.place(x=0, y=165)
    entry_age_text = tkinter.StringVar()
    entry_age = tkinter.Entry(add_new_frame, text=entry_age_text, width=40)
    entry_age.place(x=150, y=165)

    label_ph = tkinter.Label(add_new_frame, text="Worker Ph.No. :", bg=background_colour, fg="white",
                             font=("bold", 10))
    label_ph.place(x=0, y=215)
    entry_ph_text = tkinter.StringVar()
    entry_ph = tkinter.Entry(add_new_frame, text=entry_ph_text, width=40)
    entry_ph.place(x=150, y=215)

    add_image = tkinter.Canvas(add_new_frame, width=200, height=260)
    add_image.place(x=500, y=100)
    add_leb_image = tkinter.Label(add_new_frame, text="Worker Image :", bg=background_colour, fg="white",
                                  font=("bold", 10))
    add_leb_image.place(x=500, y=65)
    add_but_img = tkinter.PhotoImage(file="add_image.png")
    save_img = tkinter.Button(add_new_frame, image=add_but_img, bd=0, relief="groove",
                              command=on_add_image_button_add_new_student_frame)
    save_img.place(x=580, y=200)

    label_add = tkinter.Label(add_new_frame, text="Worker Add :", bg=background_colour, fg="white", font=("bold", 10))
    label_add.place(x=0, y=265)
    entry_add_text = tkinter.StringVar()
    entry_add = tkinter.Entry(add_new_frame, text=entry_add_text, width=40)
    entry_add.place(x=150, y=265)

    label_jo_date = tkinter.Label(add_new_frame, text="Joining Date :", bg=background_colour, fg="white", font=("bold", 10))
    label_jo_date.place(x=0, y=315)
    entry_jo_date_text = tkinter.StringVar()
    entry_jo_date = tkinter.Entry(add_new_frame, text=entry_jo_date_text, width=40)
    entry_jo_date.place(x=150, y=315)

    label_adh = tkinter.Label(add_new_frame, text="Adhar No. :", bg=background_colour, fg="white",
                                  font=("bold", 10))
    label_adh.place(x=0, y=365)
    entry_adh_text = tkinter.StringVar()
    entry_adh = tkinter.Entry(add_new_frame, text=entry_adh_text, width=40)
    entry_adh.place(x=150, y=365)

    label_sal = tkinter.Label(add_new_frame, text="Salary :", bg=background_colour, fg="white",
                              font=("bold", 10))
    label_sal.place(x=0, y=415)
    entry_sal_text = tkinter.StringVar()
    entry_sal = tkinter.Entry(add_new_frame, text=entry_sal_text, width=40)
    entry_sal.place(x=150, y=415)

    label_TAG = tkinter.Label(add_new_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
    label_TAG.place(x=0, y=465)
    option_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
    entry_TAG_text = tkinter.StringVar()
    entry_TAG = tkinter.OptionMenu(add_new_frame, entry_TAG_text, *option_for_TAG)
    entry_TAG.config(relief="raised", bd=0)
    entry_TAG.place(x=150, y=465)


    def cancel_fun():
        add_new_frame.destroy()
        but_frame.place(x=80, y=80)
        search_entry.place(x=50, y=30)
        search_button.place(x=300, y=28)
        but_frame_func()

    # save changes button
    save_but = tkinter.Button(add_new_frame, text="Save", command=on_add_new_but, width=10, relief="groove")
    save_but.place(x=1070, y=620)

    cancel_but = tkinter.Button(add_new_frame, text="Cancel", command=cancel_fun, width=10, relief="groove")
    cancel_but.place(x=970, y=620)

    add_new_frame.mainloop()

def show_all_worker():
    search_entry.config(state='disabled')
    search_button.config(state='disabled')
    but_frame.place_forget()

    def select_rec():
        reco = tree_view.focus()
        if reco == "":
            pass
        else:
            temp = tree_view.item(reco)
            cmp = temp['values']
            search_entry.config(state='normal')
            search_button.config(state='normal')
            search_entry.insert(0, cmp[0])
            tree_view_frame.destroy()
            on_search_button()

    tree_view_frame = tkinter.Frame(main_window, width=1100, height=530, bg=background_colour)
    tree_view_frame.place(x=80, y=100)

    tree_view = ttk.Treeview(tree_view_frame, columns=("", "", "", "", ""), height=24, selectmode="browse")
    tree_view.place(x=0, y=30)
    scroll_bar = ttk.Scrollbar(tree_view_frame, orient='vertical', command=tree_view.yview)
    scroll_bar.place(x=975, y=30, height=500)

    tree_view.configure(yscrollcommand=scroll_bar.set)

    tree_view.heading('#0', text='No.', anchor="w")
    tree_view.column("#0", width=60)
    tree_view.heading('#1', text='Id No.', anchor="center")
    tree_view.column("#1", width=60)
    tree_view.heading('#2', text='Name', anchor="center")
    tree_view.column("#2", width=250)
    tree_view.heading('#3', text='Address', anchor="center")
    tree_view.column("#3", width=300)
    tree_view.heading('#4', text='Phone No.', anchor="center")
    tree_view.column("#4", width=100)
    tree_view.heading('#5', text='Salary', anchor="center")
    tree_view.column("#5", width=200)

    style = ttk.Style()
    style.configure("Treeview.Heading", foreground='black', font=('bold', 10))
    my_database_show_all_worker = sqlite3.connect("Database.db")
    my_cur_show_all_worker = my_database_show_all_worker.cursor()
    my_cur_show_all_worker.execute(
        "SELECT id, name, address, phone_no, salry FROM worker_data WHERE id>7000 ORDER BY name")
    read = my_cur_show_all_worker.fetchall()
    my_cur_show_all_worker.close()
    my_database_show_all_worker.close()

    total_record = tkinter.Label(tree_view_frame, text=f"Total Record = {len(read)}", bg=background_colour,
                                 font=("bold", 10), fg="gold")
    total_record.place(x=0, y=0)

    i = 1
    for col in read:
        tree_view.insert("", "end", text=i, values=(col[0], col[1], col[2], col[3], col[4]))
        i += 1

    def cancel():
        tree_view_frame.destroy()
        search_entry.config(state='normal')
        search_button.config(state='normal')
        but_frame.place(x=80, y=80)

    open_but = tkinter.Button(tree_view_frame, text="Open", relief="groove", width=10, command=select_rec)
    open_but.place(x=1000, y=30)

    cancel_but = tkinter.Button(tree_view_frame, text="Cancel", relief="groove", width=10, command=cancel)
    cancel_but.place(x=1000, y=80)


def but_frame_func():
    search_entry.config(state="normal")
    search_button.config(state='normal')

    add_student_button_photo = tkinter.PhotoImage(file="add_student_image.png")
    add_student_button = tkinter.Button(but_frame, bd=0, bg=background_colour, fg="gold", relief="groove", text="Add Student",
                                        font=("bold", 11), image=add_student_button_photo, compound="top", command=add_new_student)
    add_student_button.place(x=5, y=10)

    add_teacher_button_photo = tkinter.PhotoImage(file="add_teacher_image.png")
    add_teacher_button = tkinter.Button(but_frame, bd=0, bg=background_colour, fg="gold", relief="groove", text="Add Teacher",
                                        font=("bold", 11), image=add_teacher_button_photo, compound="top", command=add_new_teacher)
    add_teacher_button.place(x=5, y=150)

    add_bus_driver_button_photo = tkinter.PhotoImage(file="add_bus_driver_image.png")
    add_bus_driver_button = tkinter.Button(but_frame, bd=0, bg=background_colour, fg="gold", relief="groove", text="Add Bus Driver",
                                        font=("bold", 11), image=add_bus_driver_button_photo, compound="top", command=add_new_driver)
    add_bus_driver_button.place(x=5, y=300)

    add_worker_button_photo = tkinter.PhotoImage(file="add_worker_image.png")
    add_worker_button = tkinter.Button(but_frame, bd=0, bg=background_colour, fg="gold", relief="groove", text="Add Worker",
                                       font=("bold", 11), image=add_worker_button_photo, compound="top", command=add_new_worker)
    add_worker_button.place(x=5, y=450)

    all_student_button = tkinter.Button(but_frame, text="Show all Students", width=20, height=2, relief="groove",
                                        font=("bold", 10), bg=background_colour, fg="white", command=show_all_student)
    all_student_button.place(x=140, y=50)

    all_teacher_button = tkinter.Button(but_frame, text="Show all Teachers", width=20, height=2, relief="groove",
                                        font=("bold", 10), bg=background_colour, fg="white", command=show_all_teacher)
    all_teacher_button.place(x=140, y=190)

    all_driver_button = tkinter.Button(but_frame, text="Show all Bus Driver", width=20, height=2, relief="groove",
                                       font=("bold", 10), bg=background_colour, fg="white", command=show_all_driver)
    all_driver_button.place(x=140, y=340)

    all_worker_button = tkinter.Button(but_frame, text="Show all Workers", width=20, height=2, relief="groove",
                                       font=("bold", 10), bg=background_colour, fg="white", command=show_all_worker)
    all_worker_button.place(x=140, y=490)

    but_frame.mainloop()


def on_search_button():
    value = search_entry.get()
    search_entry.delete(0, 'end')

    def show_student_data(student_value):

        st_id = ""
        st_glob_id = ""
        st_name = ""
        st_class = ""
        st_roll_no = ""
        st_class_teacher_name = ""
        st_gender = ""
        st_age = ""
        st_cast = ""
        st_phone_no = ""
        st_image = ""
        st_add = ""
        st_edu = ""
        st_f_name = ""
        st_m_name = ""
        st_adm_date = ""
        st_adm_form_no = ""
        st_fee_submitted = ""
        st_fee_submitted_date = ""
        st_adhar_no = ""
        st_reg_no = ""
        st_bl_g = ""
        st_TAG = ""

        query = f''' SELECT * FROM student_data 
                             WHERE name='{student_value}' 
                                   OR id='{student_value}'
                                   OR global_student_id='{student_value}' 
                                    '''

        my_database_read_student = sqlite3.connect("Database.db")
        my_cursor_read_student = my_database_read_student.cursor()
        my_cursor_read_student.execute(query)
        read = my_cursor_read_student.fetchall()
        my_cursor_read_student.close()
        my_database_read_student.close()
        for col in read:
            st_id = col[0]
            st_glob_id = col[1]
            st_name = col[2]
            st_class = col[3]
            st_roll_no = col[4]
            st_class_teacher_name = col[5]
            st_gender = col[6]
            st_age = col[7]
            st_cast = col[8]
            st_phone_no = col[9]
            st_image = col[10]
            st_add = col[11]
            st_edu = col[12]
            st_f_name = col[13]
            st_m_name = col[14]
            st_adm_date = col[15]
            st_adm_form_no = col[16]
            st_fee_submitted = col[17]
            st_fee_submitted_date = col[18]
            st_adhar_no = col[19]
            st_reg_no = col[20]
            st_bl_g = col[21]
            st_TAG = col[22]


        if st_id == "":
            return "No"

        else:

            def on_edit_button():

                def on_edit_save_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation", "Do you want to save this changes?")
                    if msg == "yes":
                        global bi_img
                        get_st_glob_id = edit_entry_student_glob_id.get()
                        get_st_name = edit_entry_student_name.get()
                        get_st_class = edit_entry_student_class.get()
                        get_st_roll = edit_entry_student_roll_no.get()
                        get_st_class_te_name = edit_entry_student_cls_te_name.get()
                        get_st_gen = gender.get()
                        get_st_age = edit_entry_student_age.get()
                        get_st_cast = edit_entry_student_cast.get()
                        get_st_ph = edit_entry_student_ph.get()
                        get_st_img = bi_img
                        get_st_add = edit_entry_student_add.get()
                        get_st_edu = edit_entry_student_edu.get()
                        get_st_f_name = edit_entry_student_f_name.get()
                        get_st_m_name = edit_entry_student_m_name.get()
                        get_st_adm_date = edit_entry_student_adm_date.get()
                        get_st_adm_form_no = edit_entry_student_adm_f_no.get()
                        get_st_fee_subm = edit_entry_student_fee_sub.get()
                        get_st_fee_subm_date = edit_entry_student_fee_sub_date.get()
                        get_st_adh_no = edit_entry_student_adh_no.get()
                        get_st_reg_no = edit_entry_student_reg_no.get()
                        get_st_bl_g = edit_entry_student_bl_g.get()
                        get_st_TAG = edit_entry_student_TAG_text.get()
                        bi_img = None

                        if get_st_glob_id == "":
                            get_st_glob_id = st_glob_id
                        if get_st_name == "":
                            get_st_name = st_name
                        if get_st_class == "":
                            get_st_class = st_class
                        if get_st_roll == "":
                            get_st_roll = st_roll_no
                        if get_st_class_te_name == "":
                            get_st_class_te_name = st_class_teacher_name
                        if get_st_gen == "0":
                            get_st_gen = st_gender
                        if get_st_age == "":
                            get_st_age = st_age
                        if get_st_cast == "":
                            get_st_cast = st_cast
                        if get_st_ph == "":
                            get_st_ph = st_phone_no
                        if get_st_img is None:
                            get_st_img = st_image
                        if get_st_add == "":
                            get_st_add = st_add
                        if get_st_edu == "":
                            get_st_edu = st_edu
                        if get_st_f_name == "":
                            get_st_f_name = st_f_name
                        if get_st_m_name == "":
                            get_st_m_name = st_m_name
                        if get_st_adm_date == "":
                            get_st_adm_date = st_adm_date
                        if get_st_adm_form_no == "":
                            get_st_adm_form_no = st_adm_form_no
                        if get_st_fee_subm == "":
                            get_st_fee_subm = st_fee_submitted
                        if get_st_fee_subm_date == "":
                            get_st_fee_subm_date = st_fee_submitted_date
                        if get_st_adh_no == "":
                            get_st_adh_no = st_adhar_no
                        if get_st_reg_no == "":
                            get_st_reg_no = st_reg_no
                        if get_st_bl_g == "":
                            get_st_bl_g = st_bl_g
                        if get_st_TAG == "":
                            get_st_TAG = st_TAG


                        query_update_data = f'''
                                            UPDATE student_data 
                                                SET 
                                                global_student_id=?,
                                                name=?, 
                                                class=?,
                                                roll_no=?,
                                                class_teacher_name=?,
                                                gender=?,
                                                age=?,
                                                cast=?,
                                                phone_no=?,
                                                image=?,
                                                address=?,
                                                education=?,
                                                father_name=?,
                                                mother_name=?,
                                                admission_date=?,
                                                admission_form_no=?,
                                                fee_submitted=?,
                                                fee_submission_date=?,               
                                                adhar_no=?,
                                                register_no=?,
                                                blood_group=?,
                                                TAG=?
                                                WHERE id = {st_id}  
                                             '''
                        tuple_update = (get_st_glob_id, get_st_name, get_st_class, get_st_roll, get_st_class_te_name, get_st_gen, get_st_age, get_st_cast, get_st_ph, get_st_img, get_st_add, get_st_edu, get_st_f_name, get_st_m_name, get_st_adm_date, get_st_adm_form_no, get_st_fee_subm, get_st_fee_subm_date, get_st_adh_no, get_st_reg_no, get_st_bl_g, get_st_TAG)
                        my_database_up_student = sqlite3.connect("Database.db")
                        my_cursor_update_student = my_database_up_student.cursor()
                        my_cursor_update_student.execute(query_update_data, tuple_update)
                        my_database_up_student.commit()
                        query_update_check = f'''SELECT id, name, class, address, image FROM student_data
                                                WHERE
                                                id={st_id}; '''
                        my_cursor_update_student.execute(query_update_check)
                        update_check = my_cursor_update_student.fetchall()
                        my_cursor_update_student.close()
                        my_database_up_student.close()

                        up_ch_id = ''
                        up_ch_name = ''
                        up_ch_class = ''
                        up_ch_add = ''
                        up_ch_img = ''
                        for up_col in update_check:
                            up_ch_id = up_col[0]
                            up_ch_name = up_col[1]
                            up_ch_class = up_col[2]
                            up_ch_add = up_col[3]
                            up_ch_img = up_col[4]
                        if up_ch_name == get_st_name and up_ch_class == get_st_class and up_ch_add == get_st_add and up_ch_img == get_st_img:
                            tkinter.messagebox.showinfo(f"Status of Id no.= {up_ch_id}",
                                                        "Data is Updated successfully")
                        else:
                            tkinter.messagebox.showerror("Status", "Failed to update data !!!")


                def on_add_image_button_edit_frame():
                    global bi_img
                    path = filedialog.askopenfilename()
                    bi_img = read_binary_image(path)
                    try:
                        re_image = Image.open(path)
                        re_image = re_image.resize((200, 260), Image.ANTIALIAS)
                        re_image.save("nres_img.ppm", "ppm")
                        open_img = ImageTk.PhotoImage(Image.open("nres_img.ppm"))
                        edit_img.destroy()
                        edit_image.create_image(0, 0, image=open_img, anchor="nw")
                        student_edit_frame.mainloop()
                    except AttributeError:
                        pass
                    student_edit_frame.mainloop()
                    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ON Add Image BUTTON END IN edit frame @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                def on_delete_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation",
                                                         "Do yo want to delete this record, Note if you delete it will permanently delete the record.")
                    if msg == "yes":
                        my_database_del_student = sqlite3.connect("Database.db")
                        my_cursor_del_student = my_database_del_student.cursor()
                        my_cursor_del_student.execute(f"DELETE FROM student_data WHERE id={st_id}")
                        msg_ = tkinter.messagebox.askquestion("Confirm Again", "Are you sure...!!!")
                        if msg_ == "yes":
                            my_database_del_student.commit()
                        else:
                            pass

                        my_cursor_del_student.execute(f"SELECT id FROM student_data WHERE id={st_id}")
                        delete_read = my_cursor_del_student.fetchall()
                        my_database_del_student.close()
                        if not delete_read:
                            tkinter.messagebox.showinfo(f"Status of Id= {st_id}, Name= {st_name}",
                                                        "Record Successfully deleted from database.")
                        else:
                            tkinter.messagebox.showwarning("Status", "Record is not deleted from database.")

                    else:
                        pass

                student_frame.place_forget()

                student_edit_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
                student_edit_frame.place(x=20, y=30)

                # edit_frame = labels and Entries and buttons
                edit_label_old_data = tkinter.Label(student_edit_frame, text="Old Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data.place(x=100, y=0)
                edit_label_old_data = tkinter.Label(student_edit_frame, text="Insert New Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data.place(x=340, y=0)

                edit_label_old_data_ = tkinter.Label(student_edit_frame, text="Old Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data_.place(x=850, y=0)
                edit_label_old_data_ = tkinter.Label(student_edit_frame, text="Insert New Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data_.place(x=1100, y=0)
                
                # Labels and Entries
                edit_label_student_glob_id = tkinter.Label(student_edit_frame, text="Student Global ID:", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_glob_id.place(x=0, y=75)
                edit_label_student_glob_id_ans = tkinter.Label(student_edit_frame, text=st_glob_id, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_glob_id_ans.place(x=150, y=75)
                edit_entry_student_glob_id_text = tkinter.StringVar()
                edit_entry_student_glob_id = tkinter.Entry(student_edit_frame, text=edit_entry_student_glob_id_text, width=30)
                edit_entry_student_glob_id.place(x=320, y=75)

                edit_label_student_name = tkinter.Label(student_edit_frame, text="Student Name:", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_name.place(x=0, y=125)
                edit_label_student_name_ans = tkinter.Label(student_edit_frame, text=st_name, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_name_ans.place(x=150, y=125)
                edit_entry_student_name_text = tkinter.StringVar()
                edit_entry_student_name = tkinter.Entry(student_edit_frame, text=edit_entry_student_name_text, width=30)
                edit_entry_student_name.place(x=320, y=125)

                edit_label_student_class = tkinter.Label(student_edit_frame, text="Student Class :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_class.place(x=0, y=175)
                edit_label_student_class_ans = tkinter.Label(student_edit_frame, text=st_class, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_class_ans.place(x=150, y=175)
                edit_entry_student_class_text = tkinter.StringVar()
                edit_entry_student_class = tkinter.Entry(student_edit_frame, text=edit_entry_student_class_text, width=30)
                edit_entry_student_class.place(x=320, y=175)

                edit_label_student_roll_no = tkinter.Label(student_edit_frame, text="Student Roll No. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_roll_no.place(x=0, y=225)
                edit_label_student_roll_no_ans = tkinter.Label(student_edit_frame, text=st_roll_no, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_roll_no_ans.place(x=150, y=225)
                edit_entry_student_roll_no_text = tkinter.StringVar()
                edit_entry_student_roll_no = tkinter.Entry(student_edit_frame, text=edit_entry_student_roll_no_text, width=30)
                edit_entry_student_roll_no.place(x=320, y=225)

                edit_label_student_cls_te_name = tkinter.Label(student_edit_frame, text="Class Teacher Name :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_cls_te_name.place(x=0, y=275)
                edit_label_student_cls_te_name_ans = tkinter.Label(student_edit_frame, text=st_class_teacher_name, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_cls_te_name_ans.place(x=150, y=275)
                edit_entry_student_cls_te_name_text = tkinter.StringVar()
                edit_entry_student_cls_te_name = tkinter.Entry(student_edit_frame, text=edit_entry_student_cls_te_name_text, width=30)
                edit_entry_student_cls_te_name.place(x=320, y=275)

                edit_label_student_gen = tkinter.Label(student_edit_frame, text="Student Gender:", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_gen.place(x=0, y=325)
                edit_re_gen = "-"
                if st_gender == "F":
                    edit_re_gen = "Female"
                if st_gender == "M":
                    edit_re_gen = "Male"
                edit_student_gender = tkinter.Label(student_edit_frame, text=edit_re_gen, bg=background_colour, fg="gold", font=("bold", 10))
                edit_student_gender.place(x=150, y=325)
                gender = tkinter.StringVar()
                gender.set(0)
                edit_leb_student_gender_m = tkinter.Radiobutton(student_edit_frame, text="Male", variable=gender, value="M", bg=background_colour, fg="black", font=("bold", 10))
                edit_leb_student_gender_m.place(x=320, y=325)
                edit_leb_student_gender_f = tkinter.Radiobutton(student_edit_frame, text="Female", variable=gender, value="F", bg=background_colour, fg="black", font=("bold", 10))
                edit_leb_student_gender_f.place(x=380, y=325)

                edit_label_student_age = tkinter.Label(student_edit_frame, text="Student Age :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_age.place(x=0, y=375)
                edit_label_student_age_ans = tkinter.Label(student_edit_frame, text=st_age, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_age_ans.place(x=150, y=375)
                edit_entry_student_age_text = tkinter.StringVar()
                edit_entry_student_age = tkinter.Entry(student_edit_frame, text=edit_entry_student_age_text, width=30)
                edit_entry_student_age.place(x=320, y=375)

                edit_label_student_cast = tkinter.Label(student_edit_frame, text="Student Cast :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_cast.place(x=0, y=425)
                edit_label_student_cast_ans = tkinter.Label(student_edit_frame, text=st_cast, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_cast_ans.place(x=150, y=425)
                edit_entry_student_cast_text = tkinter.StringVar()
                edit_entry_student_cast = tkinter.Entry(student_edit_frame, text=edit_entry_student_cast_text, width=30)
                edit_entry_student_cast.place(x=320, y=425)

                edit_label_student_ph = tkinter.Label(student_edit_frame, text="Student Ph.No. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_ph.place(x=0, y=475)
                edit_label_student_ph_ans = tkinter.Label(student_edit_frame, text=st_phone_no, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_ph_ans.place(x=150, y=475)
                edit_entry_student_ph_text = tkinter.StringVar()
                edit_entry_student_ph = tkinter.Entry(student_edit_frame, text=edit_entry_student_ph_text, width=30)
                edit_entry_student_ph.place(x=320, y=475)

                edit_image = tkinter.Canvas(student_edit_frame, width=200, height=260)
                edit_image.place(x=530, y=100)
                edit_leb_image = tkinter.Label(student_edit_frame, text="Student Image", bg=background_colour, fg="white", font=("bold", 10))
                edit_leb_image.place(x=530, y=75)

                edit_but_img = tkinter.PhotoImage(file="add_image.png")
                edit_img = tkinter.Button(student_edit_frame, image=edit_but_img, bd=0, relief="groove", command=on_add_image_button_edit_frame)
                edit_img.place(x=605, y=200)


                edit_label_student_add = tkinter.Label(student_edit_frame, text="Student Add :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_add.place(x=0, y=525)
                edit_label_student_add_ans = tkinter.Label(student_edit_frame, text=st_add, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_add_ans.place(x=150, y=525)
                edit_entry_student_add_text = tkinter.StringVar()
                edit_entry_student_add = tkinter.Entry(student_edit_frame, text=edit_entry_student_add_text, width=30)
                edit_entry_student_add.place(x=320, y=525)

                edit_label_student_edu = tkinter.Label(student_edit_frame, text="Student Education :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_edu.place(x=0, y=575)
                edit_label_student_edu_ans = tkinter.Label(student_edit_frame, text=st_edu, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_edu_ans.place(x=150, y=575)
                edit_entry_student_edu_text = tkinter.StringVar()
                edit_entry_student_edu = tkinter.Entry(student_edit_frame, text=edit_entry_student_edu_text, width=30)
                edit_entry_student_edu.place(x=320, y=575)

                edit_label_student_f_name = tkinter.Label(student_edit_frame, text="Father's Name :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_f_name.place(x=750, y=75)
                edit_label_student_f_name_ans = tkinter.Label(student_edit_frame, text=st_f_name, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_f_name_ans.place(x=900, y=75)
                edit_entry_student_f_name_text = tkinter.StringVar()
                edit_entry_student_f_name = tkinter.Entry(student_edit_frame, text=edit_entry_student_f_name_text, width=30)
                edit_entry_student_f_name.place(x=1070, y=75)

                edit_label_student_m_name = tkinter.Label(student_edit_frame, text="Mother's Name :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_m_name.place(x=750, y=125)
                edit_label_student_m_name_ans = tkinter.Label(student_edit_frame, text=st_m_name, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_m_name_ans.place(x=900, y=125)
                edit_entry_student_m_name_text = tkinter.StringVar()
                edit_entry_student_m_name = tkinter.Entry(student_edit_frame, text=edit_entry_student_m_name_text, width=30)
                edit_entry_student_m_name.place(x=1070, y=125)

                edit_label_student_adm_date = tkinter.Label(student_edit_frame, text="Admission Date :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_adm_date.place(x=750, y=175)
                edit_label_student_adm_date_ans = tkinter.Label(student_edit_frame, text=st_adm_date, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_adm_date_ans.place(x=900, y=175)
                edit_entry_student_adm_date_text = tkinter.StringVar()
                edit_entry_student_adm_date = tkinter.Entry(student_edit_frame, text=edit_entry_student_adm_date_text, width=30)
                edit_entry_student_adm_date.place(x=1070, y=175)

                edit_label_student_adm_f_no = tkinter.Label(student_edit_frame, text="Admission Form No. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_adm_f_no.place(x=750, y=225)
                edit_label_student_adm_f_no_ans = tkinter.Label(student_edit_frame, text=st_adm_form_no, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_adm_f_no_ans.place(x=900, y=225)
                edit_entry_student_adm_f_no_text = tkinter.StringVar()
                edit_entry_student_adm_f_no = tkinter.Entry(student_edit_frame, text=edit_entry_student_adm_f_no_text, width=30)
                edit_entry_student_adm_f_no.place(x=1070, y=225)

                edit_label_student_fee_sub = tkinter.Label(student_edit_frame, text="Fee Submitted :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_fee_sub.place(x=750, y=275)
                edit_label_student_fee_sub_ans = tkinter.Label(student_edit_frame, text=st_fee_submitted, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_fee_sub_ans.place(x=900, y=275)
                edit_entry_student_fee_sub_text = tkinter.StringVar()
                edit_entry_student_fee_sub = tkinter.Entry(student_edit_frame, text=edit_entry_student_fee_sub_text, width=30)
                edit_entry_student_fee_sub.place(x=1070, y=275)

                edit_label_student_fee_sub_date = tkinter.Label(student_edit_frame, text="Fee Submission Data:", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_fee_sub_date.place(x=750, y=325)
                edit_label_student_fee_sub_date_ans = tkinter.Label(student_edit_frame, text=st_fee_submitted_date, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_fee_sub_date_ans.place(x=900, y=325)
                edit_entry_student_fee_sub_date_text = tkinter.StringVar()
                edit_entry_student_fee_sub_date = tkinter.Entry(student_edit_frame, text=edit_entry_student_fee_sub_date_text, width=30)
                edit_entry_student_fee_sub_date.place(x=1070, y=325)

                edit_label_student_adh_no = tkinter.Label(student_edit_frame, text="Adhar No. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_adh_no.place(x=750, y=375)
                edit_label_student_adh_no_ans = tkinter.Label(student_edit_frame, text=st_adhar_no, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_adh_no_ans.place(x=900, y=375)
                edit_entry_student_adh_no_text = tkinter.StringVar()
                edit_entry_student_adh_no = tkinter.Entry(student_edit_frame, text=edit_entry_student_adh_no_text, width=30)
                edit_entry_student_adh_no.place(x=1070, y=375)

                edit_label_student_reg_no = tkinter.Label(student_edit_frame, text="G.Reg. No. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_reg_no.place(x=750, y=425)
                edit_label_student_reg_no_ans = tkinter.Label(student_edit_frame, text=st_reg_no, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_reg_no_ans.place(x=900, y=425)
                edit_entry_student_reg_no_text = tkinter.StringVar()
                edit_entry_student_reg_no = tkinter.Entry(student_edit_frame, text=edit_entry_student_reg_no_text, width=30)
                edit_entry_student_reg_no.place(x=1070, y=425)

                edit_label_student_bl_g = tkinter.Label(student_edit_frame, text="Blood Group :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_bl_g.place(x=750, y=475)
                edit_label_student_bl_g_ans = tkinter.Label(student_edit_frame, text=st_bl_g, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_bl_g_ans.place(x=900, y=475)
                edit_entry_student_bl_g_text = tkinter.StringVar()
                edit_entry_student_bl_g = tkinter.Entry(student_edit_frame, text=edit_entry_student_bl_g_text, width=30)
                edit_entry_student_bl_g.place(x=1070, y=475)

                edit_label_student_TAG = tkinter.Label(student_edit_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_student_TAG.place(x=750, y=525)
                edit_label_student_TAG_ans = tkinter.Label(student_edit_frame, text=st_TAG, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_student_TAG_ans.place(x=900, y=525)
                options_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
                edit_entry_student_TAG_text = tkinter.StringVar()
                edit_entry_student_TAG = tkinter.OptionMenu(student_edit_frame, edit_entry_student_TAG_text, *options_for_TAG)
                edit_entry_student_TAG.place(x=1070, y=525)
                edit_entry_student_TAG.config(relief="raised", bd=0)


                # This function is used to destroy() the edit frame and go back to on_search_button function
                def cancel_but():
                    student_edit_frame.destroy()
                    student_frame.place(x=50, y=30)

                # edit_frame - Buttons
                edit_button_save = tkinter.Button(student_edit_frame, text="Save Changes", width=14,relief="groove", command=on_edit_save_button_edit_frame)
                edit_button_save.place(x=1150, y=620)
                edit_button_cancel = tkinter.Button(student_edit_frame, text="Cancel", width=10, relief="groove", command=cancel_but)
                edit_button_cancel.place(x=1050, y=620)
                edit_button_delete = tkinter.Button(student_edit_frame, text="Delete Record", width=14, relief="groove", command=on_delete_button_edit_frame)
                edit_button_delete.place(x=920, y=620)

                student_edit_frame.mainloop()


            # placement of main frame
            student_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
            student_frame.place(x=50, y=30)

            # main frame = labels and Entries and buttons
            # adding gender image with Tag, name in the form of label
            if st_gender == "M":
                gen_img_logo = "img_gender_male.png"
            elif st_gender == "F":
                gen_img_logo = "img_gender_female.png"
            else:
                gen_img_logo = "img_gender_male.png"

            img_gender = ImageTk.PhotoImage(Image.open(gen_img_logo))
            label_student_name = tkinter.Label(student_frame, image=img_gender, text=f" {st_name}", width=400, anchor="nw",
                                               font=("bold", 15), compound="left", bg=background_colour, fg="gold")
            label_student_name.place(x=0, y=0)

            label_student_glob_id = tkinter.Label(student_frame, text="Student ID:", bg=background_colour, fg="white",
                                             font=("bold", 10))
            label_student_glob_id.place(x=0, y=65)
            entry_student_glob_id = tkinter.Label(student_frame, text=st_id, width=30, anchor="nw", font=("bold", 14),
                                             bg=background_colour, fg="gold")
            entry_student_glob_id.place(x=150, y=65)

            label_student_id = tkinter.Label(student_frame, text="Global Student ID:", bg=background_colour, fg="white",
                                                  font=("bold", 10))
            label_student_id.place(x=0, y=115)
            entry_student_id = tkinter.Label(student_frame, text=st_glob_id, width=30, anchor="nw", font=("bold", 14),
                                             bg=background_colour, fg="gold")
            entry_student_id.place(x=150, y=115)

            label_student_class = tkinter.Label(student_frame, text="Student Class :", bg=background_colour, fg="white",
                                                font=("bold", 10))
            label_student_class.place(x=0, y=165)
            entry_student_class = tkinter.Label(student_frame, text=st_class, width=30, anchor="nw", font=("bold", 14),
                                                bg=background_colour, fg="gold")
            entry_student_class.place(x=150, y=165)

            label_student_roll_no = tkinter.Label(student_frame, text="Student Roll No. :", bg=background_colour, fg="white",
                                                font=("bold", 10))
            label_student_roll_no.place(x=0, y=215)
            entry_student_roll_no = tkinter.Label(student_frame, text=st_roll_no, width=30, anchor="nw", font=("bold", 14),
                                                bg=background_colour, fg="gold")
            entry_student_roll_no.place(x=150, y=215)

            label_student_cls_name = tkinter.Label(student_frame, text="Class Teacher Name :", bg=background_colour, fg="white",
                                                  font=("bold", 10))
            label_student_cls_name.place(x=0, y=265)
            entry_student_cls_name = tkinter.Label(student_frame, text=st_class_teacher_name, width=30, anchor="nw",
                                                  font=("bold", 14),
                                                  bg=background_colour, fg="gold")
            entry_student_cls_name.place(x=150, y=265)


            label_student_gender = tkinter.Label(student_frame, text="Student gender:", bg=background_colour, fg="white",
                                                 font=("bold", 10))
            label_student_gender.place(x=0, y=315)
            re_gen = ""
            if st_gender == "F":
                re_gen = "Female"
            if st_gender == "M":
                re_gen = "Male"
            entry_student_gender = tkinter.Label(student_frame, text=re_gen, bg=background_colour, fg="gold",
                                                 font=("bold", 14))
            entry_student_gender.place(x=150, y=315)


            label_student_age = tkinter.Label(student_frame, text="Student Age :", bg=background_colour,
                                                   fg="white",
                                                   font=("bold", 10))
            label_student_age.place(x=0, y=365)
            entry_student_age = tkinter.Label(student_frame, text=st_age, width=30, anchor="nw",
                                                   font=("bold", 14),
                                                   bg=background_colour, fg="gold")
            entry_student_age.place(x=150, y=365)


            label_student_cast = tkinter.Label(student_frame, text="Student Cast :", bg=background_colour, fg="white",
                                              font=("bold", 10))
            label_student_cast.place(x=0, y=415)
            entry_student_cast = tkinter.Label(student_frame, text=st_cast, width=30, anchor="nw", font=("bold", 14),
                                              bg=background_colour, fg="gold")
            entry_student_cast.place(x=150, y=415)


            label_student_ph = tkinter.Label(student_frame, text="Student Ph.No. :", bg=background_colour, fg="white",
                                             font=("bold", 10))
            label_student_ph.place(x=0, y=465)
            entry_student_ph = tkinter.Label(student_frame, text=st_phone_no, width=30, anchor="nw", font=("bold", 14),
                                             bg=background_colour, fg="gold")
            entry_student_ph.place(x=150, y=465)

            # Image of Student
            label_for_image = tkinter.Label(student_frame, text="Student Image:", font=("Bold", 10), bg=background_colour,
                                            fg="white")
            label_for_image.place(x=1050, y=65)
            canvas_frame = tkinter.Canvas(student_frame, width=200, height=267, bg="White")
            canvas_frame.place(x=1050, y=90)
            try:
                write_binary_image('got_image_from_mysql_db.jpg', st_image)
                resize_img = Image.open('got_image_from_mysql_db.jpg')
                resize_img = resize_img.resize((200, 267), Image.ANTIALIAS)
                resize_img.save("nres_img.ppm", "ppm")
                got_image = ImageTk.PhotoImage(file='nres_img.ppm')
                canvas_frame.create_image(0, 0, anchor="nw", image=got_image)
            except TypeError:
                pass

            label_student_add = tkinter.Label(student_frame, text="Student Add :", bg=background_colour, fg="white",
                                              font=("bold", 10))
            label_student_add.place(x=0, y=515)
            entry_student_add = tkinter.Label(student_frame, text=st_add, width=30, anchor="nw", font=("bold", 14),
                                              bg=background_colour, fg="gold")
            entry_student_add.place(x=150, y=515)


            label_student_edu = tkinter.Label(student_frame, text="Student Education :", bg=background_colour, fg="white",
                                             font=("bold", 10))
            label_student_edu.place(x=0, y=565)
            entry_student_edu = tkinter.Label(student_frame, text=st_edu, width=30, anchor="nw", font=("bold", 14),
                                             bg=background_colour, fg="gold")
            entry_student_edu.place(x=150, y=565)


            label_student_f_name = tkinter.Label(student_frame, text="Father's Name :", bg=background_colour, fg="white",
                                              font=("bold", 10))
            label_student_f_name.place(x=500, y=65)
            entry_student_f_name = tkinter.Label(student_frame, text=st_f_name, width=30, anchor="nw", font=("bold", 14),
                                              bg=background_colour, fg="gold")
            entry_student_f_name.place(x=650, y=65)

            label_student_m_name = tkinter.Label(student_frame, text="Mother's Name :", bg=background_colour, fg="white",
                                                 font=("bold", 10))
            label_student_m_name.place(x=500, y=115)
            entry_student_m_name = tkinter.Label(student_frame, text=st_m_name, width=30, anchor="nw", font=("bold", 14),
                                                 bg=background_colour, fg="gold")
            entry_student_m_name.place(x=650, y=115)

            label_student_adm_date = tkinter.Label(student_frame, text="Admission Date :", bg=background_colour, fg="white",
                                                 font=("bold", 10))
            label_student_adm_date.place(x=500, y=165)
            entry_student_adm_date = tkinter.Label(student_frame, text=st_adm_date, width=30, anchor="nw", font=("bold", 14),
                                                 bg=background_colour, fg="gold")
            entry_student_adm_date.place(x=650, y=165)

            label_student_adm_f_no = tkinter.Label(student_frame, text="Admission Form No. :", bg=background_colour, fg="white",
                                                 font=("bold", 10))
            label_student_adm_f_no.place(x=500, y=215)
            entry_student_adm_f_no = tkinter.Label(student_frame, text=st_adm_form_no, width=30, anchor="nw",
                                                 font=("bold", 14),
                                                 bg=background_colour, fg="gold")
            entry_student_adm_f_no.place(x=650, y=215)

            label_student_fee_sub = tkinter.Label(student_frame, text="Fee Submitted :", bg=background_colour, fg="white",
                                                   font=("bold", 10))
            label_student_fee_sub.place(x=500, y=265)
            entry_student_fee_sub = tkinter.Label(student_frame, text=st_fee_submitted, width=30, anchor="nw", font=("bold", 14),
                                                   bg=background_colour, fg="gold")
            entry_student_fee_sub.place(x=650, y=265)

            label_student_fee_sub_date = tkinter.Label(student_frame, text="Fee Submission Date :", bg=background_colour, fg="white",
                                                  font=("bold", 10))
            label_student_fee_sub_date.place(x=500, y=315)
            entry_student_fee_sub_date = tkinter.Label(student_frame, text=st_fee_submitted_date, width=30, anchor="nw", font=("bold", 14),
                                                  bg=background_colour, fg="gold")
            entry_student_fee_sub_date.place(x=650, y=315)


            label_student_adh_no = tkinter.Label(student_frame, text="Adhar No. :", bg=background_colour, fg="white",
                                                       font=("bold", 10))
            label_student_adh_no.place(x=500, y=365)
            entry_student_adh_no = tkinter.Label(student_frame, text=st_adhar_no, width=30, anchor="nw", font=("bold", 14),
                                                       bg=background_colour, fg="gold")
            entry_student_adh_no.place(x=650, y=365)


            label_student_reg_no = tkinter.Label(student_frame, text="G.Reg. No. :", bg=background_colour, fg="white", font=("bold", 10))
            label_student_reg_no.place(x=500, y=415)
            entry_student_reg_no = tkinter.Label(student_frame, text=st_reg_no, width=30, anchor="nw", font=("bold", 14),
                                                 bg=background_colour, fg="gold")
            entry_student_reg_no.place(x=650, y=415)


            label_student_bl_g = tkinter.Label(student_frame, text="Blood Group :", bg=background_colour, fg="white",
                                                 font=("bold", 10))
            label_student_bl_g.place(x=500, y=465)
            entry_student_bl_g = tkinter.Label(student_frame, text=st_bl_g, width=30, anchor="nw",
                                                 font=("bold", 14),
                                                 bg=background_colour, fg="gold")
            entry_student_bl_g.place(x=650, y=465)


            label_student_tag = tkinter.Label(student_frame, text="TAG :", bg=background_colour, fg="white",
                                               font=("bold", 10))
            label_student_tag.place(x=500, y=515)
            entry_student_tag = tkinter.Label(student_frame, text=st_TAG, width=30, anchor="nw",
                                               font=("bold", 14),
                                               bg=background_colour, fg="gold")
            entry_student_tag.place(x=650, y=515)


            def cancel():
                student_frame.destroy()
                search_entry.place(x=50, y=30)
                search_button.place(x=300, y=28)
                but_frame.place(x=80, y=80)

            # button to edit data of student
            edit_data_button = tkinter.Button(student_frame, text="Edit Data", width=10, relief="groove", command=on_edit_button)
            edit_data_button.place(x=1150, y=620)

            cancel_button = tkinter.Button(student_frame, text="Cancel", width=10, relief="groove", command=cancel)
            cancel_button.place(x=1050, y=620)

            student_frame.mainloop()

    def show_teacher_data(teacher_value):

        te_id = ""
        te_name = ""
        te_gen = ""
        te_age = ""
        te_of_class = ""
        te_sub = ""
        te_phone = ""
        te_img = ""
        te_add = ""
        te_edu = ""
        te_salary = ""
        te_jo_date = ""
        te_adhar_no = ""
        te_TAG = ""

        my_database_te_data = sqlite3.connect("Database.db")
        my_cursor_te_data = my_database_te_data.cursor()
        query = f'''SELECT * FROM teacher_data
                        WHERE id = '{teacher_value}' or name = '{teacher_value}';
                '''
        my_cursor_te_data.execute(query)
        read = my_cursor_te_data.fetchall()
        my_cursor_te_data.close()
        my_database_te_data.close()

        for col in read:
            te_id = col[0]
            te_name = col[1]
            te_gen = col[2]
            te_age = col[3]
            te_of_class = col[4]
            te_sub = col[5]
            te_phone = col[6]
            te_img = col[7]
            te_add = col[8]
            te_edu = col[9]
            te_salary = col[10]
            te_jo_date = col[11]
            te_adhar_no = col[12]
            te_TAG = col[13]

        if te_id == "":
            return "No"

        else:

            def on_edit_button():

                def on_edit_save_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation ", "Do you want to update record ?")

                    if msg == "yes":
                        global bi_img
                        up_te_name = edit_entry_teacher_name.get()
                        up_te_gen = gender.get()
                        up_te_age = edit_entry_teacher_age.get()
                        up_te_of_cl = edit_entry_teacher_of_cl.get()
                        up_te_sub = edit_entry_teacher_sub.get()
                        up_te_ph = edit_entry_teacher_ph.get()
                        up_te_img = bi_img
                        up_te_add = edit_entry_teacher_add.get()
                        up_te_edu = edit_entry_teacher_edu.get()
                        up_te_sal = edit_entry_teacher_sal.get()
                        up_te_jo_date = edit_entry_teacher_jo_date.get()
                        up_te_adh = edit_entry_teacher_adh_no.get()
                        up_te_TAG = edit_entry_te_TAG_text.get()
                        bi_img = None

                        if up_te_name == "":
                            up_te_name = te_name
                        if up_te_gen == "0":
                            up_te_gen = te_gen
                        if up_te_age == "":
                            up_te_age = te_age
                        if up_te_of_cl == "":
                            up_te_of_cl = te_of_class
                        if up_te_sub == "":
                            up_te_sub = te_sub
                        if up_te_ph == "":
                            up_te_ph = te_phone
                        if up_te_img is None:
                            up_te_img = te_img
                        if up_te_add == "":
                            up_te_add = te_add
                        if up_te_edu == "":
                            up_te_edu = te_edu
                        if up_te_sal == "":
                            up_te_sal =te_salary
                        if up_te_jo_date == "":
                            up_te_jo_date = te_jo_date
                        if up_te_adh == "":
                            up_te_adh = te_adhar_no
                        if up_te_TAG == "":
                            up_te_TAG =te_TAG

                        update_query = f'''  UPDATE teacher_data 
                                                SET 
                                                name=?,
                                                gender=?,
                                                age=?,
                                                teacher_of_class=?,
                                                subject=?,
                                                phone_no=?,
                                                image=?,
                                                address=?,
                                                education=?,
                                                salry=?,
                                                joining_date=?,
                                                adhar_no=?,
                                                TAG=?
                                                WHERE id={te_id};
                                       '''
                        my_database_up_te = sqlite3.connect("Database.db")
                        my_cursor_up_te = my_database_up_te.cursor()
                        up_te_tuple = (up_te_name, up_te_gen, up_te_age, up_te_of_cl, up_te_sub, up_te_ph, up_te_img,up_te_add, up_te_edu, up_te_sal, up_te_jo_date, up_te_adh, up_te_TAG )
                        my_cursor_up_te.execute(update_query, up_te_tuple)
                        my_database_up_te.commit()

                        my_cursor_up_te.execute(f'''SELECT id, name, address, image FROM teacher_data WHERE id={te_id}''')
                        up_read = my_cursor_up_te.fetchall()
                        my_cursor_up_te.close()
                        my_database_up_te.close()
                        up_ch_id = ''
                        up_ch_name = ''
                        up_ch_add = ''
                        up_ch_img = ''

                        for up_col in up_read:
                            up_ch_id = up_col[0]
                            up_ch_name = up_col[1]
                            up_ch_add = up_col[2]
                            up_ch_img = up_col[3]

                        if up_ch_name == up_te_name and up_ch_add == up_te_add and up_ch_img == up_te_img:
                            tkinter.messagebox.showinfo(f"Status of Id no.= {up_ch_id}", "Data is Updated successfully")
                        else:
                            tkinter.messagebox.showerror("Status", "Failed to update data !!!")

                def on_add_image_button_edit_frame():
                    global bi_img
                    path = filedialog.askopenfilename()
                    bi_img = read_binary_image(path)
                    try:
                        re_img = Image.open(path)
                        re_img = re_img.resize((200, 260), Image.ANTIALIAS)
                        re_img.save("nres_img.ppm", "ppm")
                        photo = ImageTk.PhotoImage(Image.open("nres_img.ppm"))
                        edit_img.destroy()
                        edit_image.create_image(0, 0, image=photo,  anchor="nw")
                        teacher_edit_frame.mainloop()
                    except AttributeError:
                        pass

                def on_delete_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation", "Do you want to delete this Record, Note if you delete the record it will permanently delete...")
                    if msg == "yes":
                        my_database_del_te = sqlite3.connect("Database.db")
                        my_cursor_del_te = my_database_del_te.cursor()
                        my_cursor_del_te.execute(f'''DELETE FROM teacher_data WHERE id={te_id};''')
                        msg_ = tkinter.messagebox.askquestion("Confirm Again", "Are you sure...!!!")
                        if msg_ == "yes":
                            my_database_del_te.commit()
                        else:
                            pass
                        my_cursor_del_te.execute(f'''SELECT id FROM teacher_data WHERE id={te_id}''')
                        delete_read = my_cursor_del_te.fetchall()
                        if not delete_read:
                            tkinter.messagebox.showinfo(f"Status of Id= {te_id}, Name= {te_name}", "Record Successfully deleted from database.")
                        else:
                            tkinter.messagebox.showwarning("Status", "Record is not deleted from database.")
                    else:
                        pass

                teacher_frame.place_forget()

                teacher_edit_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
                teacher_edit_frame.place(x=20, y=30)

                # edit_frame = labels and Entries and buttons
                edit_label_old_data = tkinter.Label(teacher_edit_frame, text="Old Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data.place(x=50, y=0)
                edit_label_old_data = tkinter.Label(teacher_edit_frame, text="Insert New Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data.place(x=300, y=0)

                edit_label_old_data_ = tkinter.Label(teacher_edit_frame, text="Old Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data_.place(x=850, y=0)
                edit_label_old_data_ = tkinter.Label(teacher_edit_frame, text="Insert New Data:", font=("bold", 12), bg=background_colour, fg="white")
                edit_label_old_data_.place(x=1100, y=0)


                # Labels and Entries
                edit_label_teacher_name = tkinter.Label(teacher_edit_frame, text="Teacher Name:", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_teacher_name.place(x=0, y=75)
                edit_label_teacher_name_ans = tkinter.Label(teacher_edit_frame, text=te_name, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_name_ans.place(x=150, y=75)
                edit_entry_teacher_name_text = tkinter.StringVar()
                edit_entry_teacher_name = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_name_text, width=30)
                edit_entry_teacher_name.place(x=320, y=75)

                edit_label_teacher_gen = tkinter.Label(teacher_edit_frame, text="Teacher Gender:", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_teacher_gen.place(x=0, y=125)
                edit_re_gen = ""
                if te_gen == "F":
                    edit_re_gen = "Female"
                if te_gen == "M":
                    edit_re_gen = "Male"
                edit_teacher_gender = tkinter.Label(teacher_edit_frame, text=edit_re_gen, bg=background_colour, fg="gold", font=("bold", 10))
                edit_teacher_gender.place(x=150, y=125)
                gender = tkinter.StringVar()
                gender.set(0)
                edit_leb_teacher_gender_m = tkinter.Radiobutton(teacher_edit_frame, text="Male", variable=gender, value="M", bg=background_colour, fg="black", font=("bold", 10))
                edit_leb_teacher_gender_m.place(x=320, y=125)
                edit_leb_teacher_gender_f = tkinter.Radiobutton(teacher_edit_frame, text="Female", variable=gender, value="F", bg=background_colour, fg="black", font=("bold", 10))
                edit_leb_teacher_gender_f.place(x=390, y=125)

                edit_label_teacher_age = tkinter.Label(teacher_edit_frame, text="Teacher Age :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_teacher_age.place(x=0, y=175)
                edit_label_teacher_age_ans = tkinter.Label(teacher_edit_frame, text=te_age, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_age_ans.place(x=150, y=175)
                edit_entry_teacher_age_text = tkinter.StringVar()
                edit_entry_teacher_age = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_age_text, width=30)
                edit_entry_teacher_age.place(x=320, y=175)

                edit_label_teacher_of_cl = tkinter.Label(teacher_edit_frame, text="Teacher of Class :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_teacher_of_cl.place(x=0, y=225)
                edit_label_teacher_of_cl_ans = tkinter.Label(teacher_edit_frame, text=te_of_class, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_of_cl_ans.place(x=150, y=225)
                edit_entry_teacher_of_cl_text = tkinter.StringVar()
                edit_entry_teacher_of_cl = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_of_cl_text, width=30)
                edit_entry_teacher_of_cl.place(x=320, y=225)

                edit_label_teacher_sub = tkinter.Label(teacher_edit_frame, text="Subject :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_teacher_sub.place(x=0, y=275)
                edit_label_teacher_sub_ans = tkinter.Label(teacher_edit_frame, text=te_sub, width=20, anchor="nw",
                                                             bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_sub_ans.place(x=150, y=275)
                edit_entry_teacher_sub_text = tkinter.StringVar()
                edit_entry_teacher_sub = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_sub_text, width=30)
                edit_entry_teacher_sub.place(x=320, y=275)

                edit_label_teacher_ph = tkinter.Label(teacher_edit_frame, text="Teacher Ph.No. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_teacher_ph.place(x=0, y=325)
                edit_label_teacher_ph_ans = tkinter.Label(teacher_edit_frame, text=te_phone, width=20, anchor="nw",
                                                          bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_ph_ans.place(x=150, y=325)
                edit_entry_teacher_ph_text = tkinter.StringVar()
                edit_entry_teacher_ph = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_ph_text, width=30)
                edit_entry_teacher_ph.place(x=320, y=325)

                edit_leb_image = tkinter.Label(teacher_edit_frame, text="Student Image", bg=background_colour, fg="white", font=("bold", 10))
                edit_leb_image.place(x=530, y=75)
                edit_image = tkinter.Canvas(teacher_edit_frame, width=200, height=260)
                edit_image.place(x=530, y=100)
                edit_but_img = tkinter.PhotoImage(file="add_image.png")
                edit_img = tkinter.Button(teacher_edit_frame, image=edit_but_img, bd=0, relief="groove", command=on_add_image_button_edit_frame)
                edit_img.place(x=605, y=200)

                edit_label_teacher_add = tkinter.Label(teacher_edit_frame, text="Teacher Add :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_teacher_add.place(x=0, y=375)
                edit_label_teacher_add_ans = tkinter.Label(teacher_edit_frame, text=te_add, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_add_ans.place(x=150, y=375)
                edit_entry_teacher_add_text = tkinter.StringVar()
                edit_entry_teacher_add = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_add_text, width=30)
                edit_entry_teacher_add.place(x=320, y=375)

                edit_label_teacher_edu = tkinter.Label(teacher_edit_frame, text="Teacher Edu. :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_teacher_edu.place(x=0, y=425)
                edit_label_teacher_edu_ans = tkinter.Label(teacher_edit_frame, text=te_edu, width=20, anchor="nw",  bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_edu_ans.place(x=150, y=425)
                edit_entry_teacher_edu_text = tkinter.StringVar()
                edit_entry_teacher_edu = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_edu_text, width=30)
                edit_entry_teacher_edu.place(x=320, y=425)

                edit_label_teacher_sal = tkinter.Label(teacher_edit_frame, text="Teacher Salary :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_teacher_sal.place(x=0, y=475)
                edit_label_teacher_sal_ans = tkinter.Label(teacher_edit_frame, text=te_salary, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_sal_ans.place(x=150, y=475)
                edit_entry_teacher_sal_text = tkinter.StringVar()
                edit_entry_teacher_sal = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_sal_text, width=30)
                edit_entry_teacher_sal.place(x=320, y=475)

                edit_label_teacher_jo_date = tkinter.Label(teacher_edit_frame, text="Joining date :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_teacher_jo_date.place(x=0, y=525)
                edit_label_teacher_jo_date_ans = tkinter.Label(teacher_edit_frame, text=te_jo_date, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_jo_date_ans.place(x=150, y=525)
                edit_entry_teacher_jo_date_text = tkinter.StringVar()
                edit_entry_teacher_jo_date = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_jo_date_text, width=30)
                edit_entry_teacher_jo_date.place(x=320, y=525)

                edit_label_teacher_adh_no = tkinter.Label(teacher_edit_frame, text="Adhar No. :", bg=background_colour,
                                                           fg="white", font=("bold", 10))
                edit_label_teacher_adh_no.place(x=0, y=575)
                edit_label_teacher_adh_no_ans = tkinter.Label(teacher_edit_frame, text=te_adhar_no, width=20, anchor="nw",
                                                               bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_teacher_adh_no_ans.place(x=150, y=575)
                edit_entry_teacher_adh_no_text = tkinter.StringVar()
                edit_entry_teacher_adh_no = tkinter.Entry(teacher_edit_frame, text=edit_entry_teacher_adh_no_text, width=30)
                edit_entry_teacher_adh_no.place(x=320, y=575)

                edit_label_te_TAG = tkinter.Label(teacher_edit_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
                edit_label_te_TAG.place(x=750, y=75)
                edit_label_te_TAG_ans = tkinter.Label(teacher_edit_frame, text=te_TAG, width=20, anchor="nw", bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_te_TAG_ans.place(x=850, y=75)
                options_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
                edit_entry_te_TAG_text = tkinter.StringVar()
                edit_entry_te_TAG = tkinter.OptionMenu(teacher_edit_frame, edit_entry_te_TAG_text, *options_for_TAG)
                edit_entry_te_TAG.place(x=1070, y=75)
                edit_entry_te_TAG.config(relief="raised", bd=0)



                # This function is used to destroy() the edit frame and go back to on_search_button function
                def cancel_but():
                    teacher_edit_frame.destroy()
                    teacher_frame.place(x=50, y=30)

                # edit_frame - Buttons
                edit_button_save = tkinter.Button(teacher_edit_frame, text="Save Changes", width=14, relief="groove", command=on_edit_save_button_edit_frame)
                edit_button_save.place(x=1150, y=620)
                edit_button_cancel = tkinter.Button(teacher_edit_frame, text="Cancel", width=10, relief="groove", command=cancel_but)
                edit_button_cancel.place(x=1050, y=620)
                edit_button_delete = tkinter.Button(teacher_edit_frame, text="Delete Record", width=14, relief="groove",  command=on_delete_button_edit_frame)
                edit_button_delete.place(x=920, y=620)

                teacher_edit_frame.mainloop()


            teacher_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
            teacher_frame.place(x=50, y=30)

            if te_gen == "M":
                gen_img_logo = "img_gender_male.png"
            elif te_gen == "F":
                gen_img_logo = "img_gender_female.png"
            else:
                gen_img_logo = "img_gender_male.png"

            img_gender = ImageTk.PhotoImage(Image.open(gen_img_logo))
            name_leb = tkinter.Label(teacher_frame, image=img_gender, compound="left", width=400, text = f" {te_name}", font=("bold", 15), bg=background_colour, fg="gold", anchor="nw")
            name_leb.place(x=0, y=0)

            id_leb = tkinter.Label(teacher_frame, text="Teacher ID:", bg=background_colour, fg="white", font=("bold", 10))
            id_leb.place(x=0, y=65)
            entry_id_leb = tkinter.Label(teacher_frame, text=te_id, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_id_leb.place(x=150, y=65)

            gen_leb = tkinter.Label(teacher_frame, text="Teacher gender:", bg=background_colour, fg="white", font=("bold", 10))
            gen_leb.place(x=0, y=115)
            re_gen = ""
            if te_gen == "F":
                re_gen = "Female"
            if te_gen == "M":
                re_gen = "Male"
            entry_gen_leb = tkinter.Label(teacher_frame, text=re_gen, bg=background_colour, fg="gold", font=("bold", 14))
            entry_gen_leb.place(x=150, y=115)

            add_age = tkinter.Label(teacher_frame, text="Teacher Age :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            add_age.place(x=0, y=165)
            entry_age_leb = tkinter.Label(teacher_frame, text=te_age, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_age_leb.place(x=150, y=165)

            add_class = tkinter.Label(teacher_frame, text="Teacher Of Class :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            add_class.place(x=0, y=215)
            entry_class_leb = tkinter.Label(teacher_frame, text=te_of_class, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_class_leb.place(x=150, y=215)

            add_sub = tkinter.Label(teacher_frame, text="Teacher Sub :", bg=background_colour, fg="white",
                                      font=("bold", 10))
            add_sub.place(x=0, y=265)
            entry_sub_leb = tkinter.Label(teacher_frame, text=te_sub, width=30, anchor="nw", font=("bold", 14),
                                            bg=background_colour, fg="gold")
            entry_sub_leb.place(x=150, y=265)

            ph_leb = tkinter.Label(teacher_frame, text="Teacher Ph.No. :", bg=background_colour, fg="white",
                                   font=("bold", 10))
            ph_leb.place(x=0, y=315)
            entry_ph_leb = tkinter.Label(teacher_frame, text=te_phone, width=30, anchor="nw", font=("bold", 14),
                                         bg=background_colour, fg="gold")
            entry_ph_leb.place(x=150, y=315)

            # Image of Teacher
            img_leb = tkinter.Label(teacher_frame, text="Teacher Image:", font=("Bold", 10), bg=background_colour,
                                    fg="white")
            img_leb.place(x=1050, y=65)
            canvas_frame = tkinter.Canvas(teacher_frame, width=200, height=260, bg=background_colour)
            canvas_frame.place(x=1050, y=90)
            try:
                write_binary_image('got_image_from_mysql_db.jpg', te_img)
                resize_img = Image.open('got_image_from_mysql_db.jpg')
                resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
                resize_img.save('nres_img.ppm', 'ppm')
                got_image = ImageTk.PhotoImage(file='nres_img.ppm')
                canvas_frame.create_image(0, 0, anchor="nw", image=got_image)
            except TypeError:
                pass

            add_leb = tkinter.Label(teacher_frame, text="Teacher Add :", bg=background_colour, fg="white", font=("bold", 10))
            add_leb.place(x=0, y=365)
            entry_add_leb = tkinter.Label(teacher_frame, text=te_add, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_add_leb.place(x=150, y=365)

            edu_leb = tkinter.Label(teacher_frame, text="Teacher Edu. :", bg=background_colour, fg="white", font=("bold", 10))
            edu_leb.place(x=0, y=415)
            entry_edu_leb = tkinter.Label(teacher_frame, text=te_edu, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_edu_leb.place(x=150, y=415)

            sal_leb = tkinter.Label(teacher_frame, text="Teacher Salary :", bg=background_colour, fg="white", font=("bold", 10))
            sal_leb.place(x=0, y=465)
            entry_sal_leb = tkinter.Label(teacher_frame, text=te_salary, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_sal_leb.place(x=150, y=465)

            jo_date_leb = tkinter.Label(teacher_frame, text="Joining Date :", bg=background_colour, fg="white", font=("bold", 10))
            jo_date_leb.place(x=0, y=515)
            entry_jo_date_leb = tkinter.Label(teacher_frame, text=te_jo_date, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_jo_date_leb.place(x=150, y=515)

            adh_leb = tkinter.Label(teacher_frame, text="Adhar No. :", bg=background_colour, fg="white", font=("bold", 10))
            adh_leb.place(x=0, y=565)
            entry_adh_leb = tkinter.Label(teacher_frame, text=te_adhar_no, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_adh_leb.place(x=150, y=565)

            TAG_leb = tkinter.Label(teacher_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
            TAG_leb.place(x=500, y=65)
            entry_TAG_leb = tkinter.Label(teacher_frame, text=te_TAG, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_TAG_leb.place(x=650, y=65)


            def cancel():
                teacher_frame.destroy()
                search_entry.place(x=50, y=30)
                search_button.place(x=300, y=28)
                but_frame.place(x=80, y=80)

            # button to edit data of student
            edit_data_button = tkinter.Button(teacher_frame, text="Edit Data", width=10, relief="groove", command=on_edit_button)
            edit_data_button.place(x=1150, y=620)

            cancel_button = tkinter.Button(teacher_frame, text="Cancel", width=10, relief="groove", command=cancel)
            cancel_button.place(x=1050, y=620)

            teacher_frame.mainloop()

    def show_bus_driver_data(driver_value):

        d_id = ""
        d_name = ""
        d_gen = ""
        d_age = ""
        d_phone = ""
        d_img = ""
        d_add = ""
        d_jo_date = ""
        d_adh_no = ""
        d_tr_rout = ""
        d_v_no = ""
        d_lic = ""
        d_v_sm = ""
        d_v_ins = ""
        d_TAG = ""

        my_database_show_driver = sqlite3.connect("Database.db")
        my_cursor_show_driver =  my_database_show_driver.cursor()
        query = f'''SELECT * FROM driver_data
                                WHERE id = '{driver_value}' or name = '{driver_value}';
                        '''
        my_cursor_show_driver.execute(query)
        read = my_cursor_show_driver.fetchall()
        my_cursor_show_driver.close()
        my_database_show_driver.close()
        for col in read:
            d_id = col[0]
            d_name = col[1]
            d_gen = col[2]
            d_age = col[3]
            d_phone = col[4]
            d_img = col[5]
            d_add = col[6]
            d_jo_date = col[7]
            d_adh_no = col[8]
            d_tr_rout = col[9]
            d_v_no = col[10]
            d_lic = col[11]
            d_v_sm = col[12]
            d_v_ins = col[13]
            d_TAG = col[14]

        if d_id == "":
            return "No"

        else:

            def on_edit_button():

                def on_edit_save_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation ", "Do you want to update record ?")

                    if msg == "yes":
                        global bi_img
                        global bi_driver_lic
                        global bi_veh_sm_card_copy
                        global bi_veh_ins_copy
                        up_d_name = edit_entry_d_name.get()
                        up_d_gen = gender.get()
                        up_d_age = edit_entry_d_age.get()
                        up_d_ph = edit_entry_d_ph.get()
                        up_d_img = bi_img
                        up_d_add = edit_entry_d_add.get()
                        up_d_jo_date = edit_entry_d_jo_date.get()
                        up_d_adh = edit_entry_adh.get()
                        up_d_rout = edit_entry_v_rout.get()
                        up_d_v_no = edit_entry_v_no.get()
                        up_d_dr_lic = bi_driver_lic
                        up_d_v_sm = bi_veh_sm_card_copy
                        up_d_v_ins = bi_veh_ins_copy
                        up_d_TAG = edit_entry_d_TAG_text.get()
                        bi_img = None
                        bi_driver_lic = None
                        bi_veh_sm_card_copy = None
                        bi_veh_ins_copy = None

                        if up_d_name == "":
                            up_d_name = d_name
                        if up_d_gen == "0":
                            up_d_gen = d_gen
                        if up_d_age == "":
                            up_d_age = d_age
                        if up_d_ph == "":
                            up_d_ph = d_phone
                        if up_d_img is None:
                            up_d_img = d_img
                        if up_d_add == "":
                            up_d_add = d_add
                        if up_d_jo_date == "":
                            up_d_jo_date = d_jo_date
                        if up_d_adh == "":
                            up_d_adh = d_adh_no
                        if up_d_rout == "":
                            up_d_rout = d_tr_rout
                        if up_d_v_no == "":
                            up_d_v_no = d_v_no
                        if up_d_dr_lic is None:
                            up_d_dr_lic = d_lic
                        if up_d_v_sm is None:
                            up_d_v_sm = d_v_sm
                        if up_d_v_ins is None:
                            up_d_v_ins = d_v_ins
                        if up_d_TAG == "":
                            up_d_TAG = d_TAG

                        update_query = f'''  UPDATE driver_data 
                                                        SET 
                                                        name=?,
                                                        gender=?,
                                                        age=?,
                                                        phone_no=?,
                                                        image=?,
                                                        address=?,
                                                        joining_date=?,
                                                        adhar_no=?,
                                                        travel_rout=?,
                                                        vehicle_no=?,
                                                        driving_license_copy=?,
                                                        vehicle_smart_card_copy=?,
                                                        vehicle_insurance_copy=?,
                                                        TAG=?                                                        
                                                        WHERE id={d_id}; '''

                        up_te_tuple = (up_d_name, up_d_gen, up_d_age, up_d_ph, up_d_img, up_d_add, up_d_jo_date, up_d_adh, up_d_rout, up_d_v_no, up_d_dr_lic, up_d_v_sm, up_d_v_ins, up_d_TAG)
                        my_database_up_driver = sqlite3.connect('Database.db')
                        my_cursor_up_driver = my_database_up_driver.cursor()
                        my_cursor_up_driver.execute(update_query, up_te_tuple)
                        my_database_up_driver.commit()

                        my_cursor_up_driver.execute(f''' SELECT id, name, address FROM driver_data WHERE id={d_id}''')
                        up_read = my_cursor_up_driver.fetchall()
                        my_cursor_up_driver.close()
                        my_database_up_driver.close()

                        up_ch_id = ''
                        up_ch_name = ''
                        up_ch_add = ''

                        for up_col in up_read:
                            up_ch_id = up_col[0]
                            up_ch_name = up_col[1]
                            up_ch_add = up_col[2]


                        if up_ch_name == up_d_name and up_ch_add == up_d_add:
                            tkinter.messagebox.showinfo(f"Status of Id no.= {up_ch_id}",
                                                        "Data is Updated successfully")
                        else:
                            tkinter.messagebox.showerror("Status", "Failed to update data !!!")

                    else:
                        pass

                def on_add_image_button_edit_frame():
                    global bi_img
                    path = filedialog.askopenfilename()
                    bi_img = read_binary_image(path)
                    try:
                        re_img = Image.open(path)
                        re_img = re_img.resize((200, 260), Image.ANTIALIAS)
                        re_img.save("nres_img.ppm", "ppm")
                        photo = ImageTk.PhotoImage(Image.open("nres_img.ppm"))
                        edit_img.destroy()
                        edit_image.create_image(0, 0, image=photo, anchor="nw")
                        driver_edit_frame.mainloop()
                    except AttributeError:
                        pass

                def on_delete_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation",
                                                         "Do you want to delete this Record, Note if you delete the record it will permanently delete...")
                    if msg == "yes":
                        my_database_del_driver = sqlite3.connect("Database.db")
                        my_cursor_del_driver = my_database_del_driver.cursor()
                        my_cursor_del_driver.execute(f'''DELETE FROM driver_data WHERE id={d_id};''')
                        msg_ = tkinter.messagebox.askquestion("Confirm Again", "Are you sure...!!!")
                        if msg_ == "yes":
                            my_database_del_driver.commit()
                        else:
                            pass
                        my_cursor_del_driver.execute(
                            f'''SELECT id FROM driver_data WHERE id={d_id}''')
                        delete_read = my_cursor_del_driver.fetchall()
                        my_cursor_del_driver.close()
                        my_database_del_driver.close()
                        if not delete_read:
                            tkinter.messagebox.showinfo(f"Status of Id= {d_id}, Name= {d_name}",
                                                        "Record Successfully deleted from database.")
                        else:
                            tkinter.messagebox.showwarning("Status", "Record is not deleted from database.")
                    else:
                        pass

                driver_frame.place_forget()

                driver_edit_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
                driver_edit_frame.place(x=20, y=30)

                # edit_frame = labels and Entries and buttons
                edit_label_old_data = tkinter.Label(driver_edit_frame, text="Old Data:", font=("bold", 12),
                                                    bg=background_colour, fg="white")
                edit_label_old_data.place(x=50, y=0)
                edit_label_old_data = tkinter.Label(driver_edit_frame, text="Insert New Data:", font=("bold", 12),
                                                    bg=background_colour, fg="white")
                edit_label_old_data.place(x=300, y=0)


                # Labels and Entries
                edit_label_d_name = tkinter.Label(driver_edit_frame, text="Driver Name:", bg=background_colour,
                                                        fg="white", font=("bold", 10))
                edit_label_d_name.place(x=0, y=75)
                edit_label_d_name_ans = tkinter.Label(driver_edit_frame, text=d_name, width=20, anchor="nw",
                                                            bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_d_name_ans.place(x=150, y=75)
                edit_entry_d_name_text = tkinter.StringVar()
                edit_entry_d_name = tkinter.Entry(driver_edit_frame, text=edit_entry_d_name_text, width=30)
                edit_entry_d_name.place(x=320, y=75)

                edit_label_d_gen = tkinter.Label(driver_edit_frame, text="Driver Gender:", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_d_gen.place(x=0, y=125)
                edit_re_gen = ""
                if d_gen == "F":
                    edit_re_gen = "Female"
                if d_gen == "M":
                    edit_re_gen = "Male"
                edit_d_gender = tkinter.Label(driver_edit_frame, text=edit_re_gen, bg=background_colour,
                                                    fg="gold", font=("bold", 10))
                edit_d_gender.place(x=150, y=125)
                gender = tkinter.StringVar()
                gender.set(0)
                edit_leb_d_gender_m = tkinter.Radiobutton(driver_edit_frame, text="Male", variable=gender,
                                                                value="M", bg=background_colour, fg="black",
                                                                font=("bold", 10))
                edit_leb_d_gender_m.place(x=320, y=125)
                edit_leb_d_gender_f = tkinter.Radiobutton(driver_edit_frame, text="Female", variable=gender,
                                                                value="F", bg=background_colour, fg="black",
                                                                font=("bold", 10))
                edit_leb_d_gender_f.place(x=400, y=125)


                edit_label_d_age = tkinter.Label(driver_edit_frame, text="Driver Age :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_d_age.place(x=0, y=175)
                edit_label_d_age_ans = tkinter.Label(driver_edit_frame, text=d_age, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_d_age_ans.place(x=150, y=175)
                edit_entry_d_age_text = tkinter.StringVar()
                edit_entry_d_age = tkinter.Entry(driver_edit_frame, text=edit_entry_d_age_text, width=30)
                edit_entry_d_age.place(x=320, y=175)

                edit_label_d_ph = tkinter.Label(driver_edit_frame, text="Driver Ph.No. :", bg=background_colour,
                                                      fg="white", font=("bold", 10))
                edit_label_d_ph.place(x=0, y=225)
                edit_label_d_ph_ans = tkinter.Label(driver_edit_frame, text=d_phone, width=20, anchor="nw",
                                                          bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_d_ph_ans.place(x=150, y=225)
                edit_entry_d_ph_text = tkinter.StringVar()
                edit_entry_d_ph = tkinter.Entry(driver_edit_frame, text=edit_entry_d_ph_text, width=30)
                edit_entry_d_ph.place(x=320, y=225)

                edit_leb_image = tkinter.Label(driver_edit_frame, text="Driver Image", bg=background_colour,
                                               fg="white", font=("bold", 10))
                edit_leb_image.place(x=530, y=75)
                edit_image = tkinter.Canvas(driver_edit_frame, width=200, height=260)
                edit_image.place(x=530, y=100)
                edit_but_img = tkinter.PhotoImage(file="add_image.png")
                edit_img = tkinter.Button(driver_edit_frame, image=edit_but_img, bd=0, relief="groove",
                                          command=on_add_image_button_edit_frame)
                edit_img.place(x=605, y=200)


                edit_label_d_add = tkinter.Label(driver_edit_frame, text="Driver Add :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_d_add.place(x=0, y=275)
                edit_label_d_add_ans = tkinter.Label(driver_edit_frame, text=d_add, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_d_add_ans.place(x=150, y=275)
                edit_entry_d_add_text = tkinter.StringVar()
                edit_entry_d_add = tkinter.Entry(driver_edit_frame, text=edit_entry_d_add_text, width=30)
                edit_entry_d_add.place(x=320, y=275)

                edit_label_d_jo_date = tkinter.Label(driver_edit_frame, text="Joining Date :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_d_jo_date.place(x=0, y=325)
                edit_label_d_jo_date_ans = tkinter.Label(driver_edit_frame, text=d_jo_date, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_d_jo_date_ans.place(x=150, y=325)
                edit_entry_d_jo_date_text = tkinter.StringVar()
                edit_entry_d_jo_date = tkinter.Entry(driver_edit_frame, text=edit_entry_d_jo_date_text, width=30)
                edit_entry_d_jo_date.place(x=320, y=325)

                edit_label_adh = tkinter.Label(driver_edit_frame, text="Adhar No. :", bg=background_colour,
                                                     fg="white", font=("bold", 10))
                edit_label_adh.place(x=0, y=375)
                edit_label_adh_ans = tkinter.Label(driver_edit_frame, text=d_adh_no, width=20, anchor="nw",
                                                         bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_adh_ans.place(x=150, y=375)
                edit_entry_adh_text = tkinter.StringVar()
                edit_entry_adh = tkinter.Entry(driver_edit_frame, text=edit_entry_adh_text, width=30)
                edit_entry_adh.place(x=320, y=375)

                edit_label_v_rout = tkinter.Label(driver_edit_frame, text="Vehicle rout :", bg=background_colour,
                                                fg="white", font=("bold", 10))
                edit_label_v_rout.place(x=0, y=425)
                edit_label_v_rout_ans = tkinter.Label(driver_edit_frame, text=d_tr_rout, width=20, anchor="nw",
                                                    bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_v_rout_ans.place(x=150, y=425)
                edit_entry_v_rout_text = tkinter.StringVar()
                edit_entry_v_rout = tkinter.Entry(driver_edit_frame, text=edit_entry_v_rout_text, width=30)
                edit_entry_v_rout.place(x=320, y=425)

                edit_label_v_no = tkinter.Label(driver_edit_frame, text="Vehicle No. :", bg=background_colour,
                                               fg="white", font=("bold", 10))
                edit_label_v_no.place(x=0, y=475)
                edit_label_v_no_ans = tkinter.Label(driver_edit_frame, text=d_v_no, width=20, anchor="nw",
                                                   bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_v_no_ans.place(x=150, y=475)
                edit_entry_v_no_text = tkinter.StringVar()
                edit_entry_v_no = tkinter.Entry(driver_edit_frame, text=edit_entry_v_no_text, width=30)
                edit_entry_v_no.place(x=320, y=475)

                edit_label_d_TAG = tkinter.Label(driver_edit_frame, text="TAG :", bg=background_colour, fg="white",
                                                  font=("bold", 10))
                edit_label_d_TAG.place(x=0, y=525)
                edit_label_d_TAG_ans = tkinter.Label(driver_edit_frame, text=d_TAG, width=20, anchor="nw",
                                                      bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_d_TAG_ans.place(x=150, y=525)
                options_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
                edit_entry_d_TAG_text = tkinter.StringVar()
                edit_entry_d_TAG = tkinter.OptionMenu(driver_edit_frame, edit_entry_d_TAG_text, *options_for_TAG)
                edit_entry_d_TAG.place(x=320, y=525)
                edit_entry_d_TAG.config(relief="raised", bd=0)

                label_v_lic = tkinter.Label(driver_edit_frame, text="Vehicle Documents :", bg=background_colour, fg="white",
                                            font=("bold", 10))
                label_v_lic.place(x=750, y=65)

                def on_add_lic():
                    global bi_driver_lic
                    path = filedialog.askopenfilename()
                    bi_driver_lic = read_binary_image(path)

                entry_v_lic = tkinter.Button(driver_edit_frame, text="Add Driving License", bd=1, command=on_add_lic)
                entry_v_lic.place(x=900, y=65)

                def on_add_sm_card():
                    global bi_veh_sm_card_copy
                    path = filedialog.askopenfilename()
                    bi_veh_sm_card_copy = read_binary_image(path)

                entry_v_sm = tkinter.Button(driver_edit_frame, text="Add veh. Smart card", bd=1, command=on_add_sm_card)
                entry_v_sm.place(x=900, y=100)

                def on_add_ins():
                    global bi_veh_ins_copy
                    path = filedialog.askopenfilename()
                    bi_veh_ins_copy = read_binary_image(path)

                entry_v_in = tkinter.Button(driver_edit_frame, text="Add veh. Insurance", bd=1, command=on_add_ins)
                entry_v_in.place(x=900, y=135)




                # This function is used to destroy() the edit frame and go back to on_search_button function
                def cancel_but():
                    driver_edit_frame.destroy()
                    driver_frame.place(x=50, y=30)

                # edit_frame - Buttons
                edit_button_save = tkinter.Button(driver_edit_frame, text="Save Changes", width=14, relief="groove",
                                                  command=on_edit_save_button_edit_frame)
                edit_button_save.place(x=1150, y=620)
                edit_button_cancel = tkinter.Button(driver_edit_frame, text="Cancel", width=10, relief="groove",
                                                    command=cancel_but)
                edit_button_cancel.place(x=1050, y=620)
                edit_button_delete = tkinter.Button(driver_edit_frame, text="Delete Record", width=14, relief="groove",
                                                    command=on_delete_button_edit_frame)
                edit_button_delete.place(x=920, y=620)

                driver_edit_frame.mainloop()

            def driver_v_doc():
                try:
                    write_binary_image('doc_/Driver_car_License_copy.png', d_lic)
                    write_binary_image('doc_/Driver_car_smart_card_copy.png', d_v_sm)
                    write_binary_image('doc_/Driver_car_insurance_copy.png', d_v_ins)
                    filedialog.askopenfilename(initialdir="doc_")
                except TypeError:
                    tkinter.messagebox.showinfo("Information", "Documents are Absent.\nTry to Add Documents")


            driver_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
            driver_frame.place(x=50, y=30)

            if d_gen == "M":
                gen_img_logo = "img_gender_male.png"
            elif d_gen == "F":
                gen_img_logo = "img_gender_female.png"
            else:
                gen_img_logo = "img_gender_male.png"

            img_gender = ImageTk.PhotoImage(Image.open(gen_img_logo))
            name_leb = tkinter.Label(driver_frame, image=img_gender, compound="left", width=400, text=f" {d_name}",
                                     font=("bold", 15), bg=background_colour, fg="gold", anchor="nw")
            name_leb.place(x=0, y=0)

            id_leb = tkinter.Label(driver_frame, text="Driver ID:", bg=background_colour, fg="white",
                                   font=("bold", 10))
            id_leb.place(x=0, y=65)
            entry_id_leb = tkinter.Label(driver_frame, text=d_id, width=30, anchor="nw", font=("bold", 14),
                                         bg=background_colour, fg="gold")
            entry_id_leb.place(x=150, y=65)

            gen_leb = tkinter.Label(driver_frame, text="Driver gender:", bg=background_colour, fg="white", font=("bold", 10))
            gen_leb.place(x=0, y=115)
            re_gen = ""
            if d_gen == "F":
                re_gen = "Female"
            if d_gen == "M":
                re_gen = "Male"
            entry_gen_leb = tkinter.Label(driver_frame, text=re_gen, bg=background_colour, fg="gold", font=("bold", 14))
            entry_gen_leb.place(x=150, y=115)

            age_leb = tkinter.Label(driver_frame, text="Driver Age :", bg=background_colour, fg="white", font=("bold", 10))
            age_leb.place(x=0, y=165)
            entry_age_leb = tkinter.Label(driver_frame, text=d_age, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_age_leb.place(x=150, y=165)

            ph_leb = tkinter.Label(driver_frame, text="Driver ph.No. :", bg=background_colour, fg="white", font=("bold", 10))
            ph_leb.place(x=0, y=215)
            entry_ph_leb = tkinter.Label(driver_frame, text=d_phone, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_ph_leb.place(x=150, y=215)

            # Image of Teacher
            img_leb = tkinter.Label(driver_frame, text="Driver Image:", font=("Bold", 10), bg=background_colour, fg="white")
            img_leb.place(x=1050, y=65)
            canvas_frame = tkinter.Canvas(driver_frame, width=200, height=260, bg=background_colour)
            canvas_frame.place(x=1050, y=90)
            try:
                write_binary_image('got_image_from_mysql_db.jpg', d_img)
                resize_img = Image.open('got_image_from_mysql_db.jpg')
                resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
                resize_img.save("nres_img.ppm", "ppm")
                got_image = ImageTk.PhotoImage(file='nres_img.ppm')
                canvas_frame.create_image(0, 0, anchor="nw", image=got_image)
            except TypeError:
                pass
            
            add_leb = tkinter.Label(driver_frame, text="Driver Add :", bg=background_colour, fg="white", font=("bold", 10))
            add_leb.place(x=0, y=265)
            entry_add_leb = tkinter.Label(driver_frame, text=d_add, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_add_leb.place(x=150, y=265)

            jo_date_leb = tkinter.Label(driver_frame, text="Joining Date :", bg=background_colour, fg="white", font=("bold", 10))
            jo_date_leb.place(x=0, y=315)
            entry_jo_date_leb = tkinter.Label(driver_frame, text=d_jo_date, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_jo_date_leb.place(x=150, y=315)

            adh_no_leb = tkinter.Label(driver_frame, text="Adhar No. :", bg=background_colour, fg="white", font=("bold", 10))
            adh_no_leb.place(x=0, y=365)
            entry_adh_no_leb = tkinter.Label(driver_frame, text=d_adh_no, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_adh_no_leb.place(x=150, y=365)

            tr_rout_leb = tkinter.Label(driver_frame, text="Travel Rout :", bg=background_colour, fg="white", font=("bold", 10))
            tr_rout_leb.place(x=0, y=415)
            entry_tr_rout_leb = tkinter.Label(driver_frame, text=d_tr_rout, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_tr_rout_leb.place(x=150, y=415)

            v_no_leb = tkinter.Label(driver_frame, text="Vehicle No. :", bg=background_colour, fg="white", font=("bold", 10))
            v_no_leb.place(x=0, y=465)
            entry_v_no_leb = tkinter.Label(driver_frame, text=d_v_no, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_v_no_leb.place(x=150, y=465)

            TAG_leb = tkinter.Label(driver_frame, text="TAG :", bg=background_colour, fg="white", font=("bold", 10))
            TAG_leb.place(x=0, y=515)
            entry_TAG_leb = tkinter.Label(driver_frame, text=d_TAG, width=30, anchor="nw", font=("bold", 14), bg=background_colour, fg="gold")
            entry_TAG_leb.place(x=150, y=515)


            lic_leb = tkinter.Label(driver_frame, text="Vehicle Documents :", bg=background_colour, fg="white", font=("bold", 10))
            lic_leb.place(x=500, y=65)
            doc_img = tkinter.PhotoImage(file='driver_doc_img.png')
            entry_lic_leb = tkinter.Button(driver_frame, image=doc_img, bd=1, bg=background_colour, command=driver_v_doc)
            entry_lic_leb.place(x=650, y=65)


            def cancel():
                driver_frame.destroy()
                search_entry.place(x=50, y=30)
                search_button.place(x=300, y=28)
                but_frame.place(x=80, y=80)

            # button to edit data of student
            edit_data_button = tkinter.Button(driver_frame, text="Edit Data", width=10, relief="groove", command=on_edit_button)
            edit_data_button.place(x=1150, y=620)

            cancel_button = tkinter.Button(driver_frame, text="Cancel", width=10, relief="groove", command=cancel)
            cancel_button.place(x=1050, y=620)

            driver_frame.mainloop()

    def show_worker(worker_value):

        w_id = ""
        w_name = ""
        w_gen = ""
        w_age = ""
        w_phone = ""
        w_img = ""
        w_add = ""
        w_jo_date = ""
        w_adhar_no = ""
        w_sal = ""
        w_TAG = ""

        my_database_show_worker = sqlite3.connect("Database.db")
        my_cursor_show_worker = my_database_show_worker.cursor()
        query = f'''SELECT * FROM worker_data
                                        WHERE id = '{worker_value}' or name = '{worker_value}';
                                '''
        my_cursor_show_worker.execute(query)
        read = my_cursor_show_worker.fetchall()
        my_cursor_show_worker.close()
        my_database_show_worker.close()
        for col in read:
            w_id = col[0]
            w_name = col[1]
            w_gen = col[2]
            w_age = col[3]
            w_phone = col[4]
            w_img = col[5]
            w_add = col[6]
            w_jo_date = col[7]
            w_adhar_no = col[8]
            w_sal = col[9]
            w_TAG = col[10]

        if w_id == "":
            return "No"

        else:

            def on_edit_button():

                def on_edit_save_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation ", "Do you want to update record ?")

                    if msg == "yes":
                        global bi_img
                        up_name = edit_entry_name.get()
                        up_gen = gender.get()
                        up_age = edit_entry_age.get()
                        up_ph = edit_entry_ph.get()
                        up_img = bi_img
                        up_add = edit_entry_add.get()
                        up_jo_date = edit_entry_jo_date.get()
                        up_adh_no = edit_entry_adh.get()
                        up_sal = edit_entry_sal.get()
                        up_TAG = edit_entry_w_TAG_text.get()
                        bi_img = None

                        if up_name == "":
                            up_name = w_name
                        if up_gen == "0":
                            up_gen = w_gen
                        if up_age == "":
                            up_age = w_age
                        if up_ph == "":
                            up_ph = w_phone
                        if up_img is None:
                            up_img = w_img
                        if up_add == "":
                            up_add = w_add
                        if up_jo_date == "":
                            up_jo_date = w_jo_date
                        if up_adh_no == "":
                            up_adh_no = w_adhar_no
                        if up_sal == "":
                            up_sal = w_sal
                        if up_TAG == "":
                            up_TAG = w_TAG


                        update_query = f'''  UPDATE worker_data 
                                                                SET 
                                                                name=?,
                                                                gender=?,
                                                                age=?,
                                                                phone_no=?,
                                                                image=?,
                                                                address=?,
                                                                joining_date=?,
                                                                adhar_no=?,
                                                                salry=?,
                                                                TAG=?                                                               
                                                                WHERE id={w_id};
                                                       '''
                        up_te_tuple = (up_name, up_gen, up_age, up_ph, up_img, up_add, up_jo_date, up_adh_no, up_sal, up_TAG)
                        my_database_up_worker = sqlite3.connect("Database.db")
                        my_cursor_up_worker = my_database_up_worker.cursor()
                        my_cursor_up_worker.execute(update_query, up_te_tuple)
                        my_database_up_worker.commit()

                        my_cursor_up_worker.execute(f''' SELECT id, name, address FROM worker_data WHERE id={w_id}''')
                        up_read = my_cursor_up_worker.fetchall()
                        my_cursor_up_worker.close()
                        my_database_up_worker.close()
                        up_ch_id = ''
                        up_ch_name = ''
                        up_ch_add = ''

                        for up_col in up_read:
                            up_ch_id = up_col[0]
                            up_ch_name = up_col[1]
                            up_ch_add = up_col[2]

                        if up_ch_name == up_name and up_ch_add == up_add:
                            tkinter.messagebox.showinfo(f"Status of Id no.= {up_ch_id}",
                                                        "Data is Updated successfully")
                        else:
                            tkinter.messagebox.showerror("Status", "Failed to update data !!!")


                    else:
                        pass

                def on_add_image_button_edit_frame():
                    global bi_img
                    path = filedialog.askopenfilename()
                    bi_img = read_binary_image(path)
                    try:
                        re_img = Image.open(path)
                        re_img = re_img.resize((200, 260), Image.ANTIALIAS)
                        re_img.save("nres_img.ppm", "ppm")
                        photo = ImageTk.PhotoImage(Image.open('nres_img.ppm'))
                        edit_img.destroy()
                        edit_image.create_image(0, 0, image=photo, anchor="nw")
                        worker_edit_frame.mainloop()
                    except AttributeError:
                        pass

                def on_delete_button_edit_frame():
                    msg = tkinter.messagebox.askquestion("Confirmation",
                                                         "Do you want to delete this Record, Note if you delete the record it will permanently delete...")
                    if msg == "yes":
                        my_database_del_worker = sqlite3.connect("Database.db")
                        my_cursor_del_worker = my_database_del_worker.cursor()
                        my_cursor_del_worker.execute(f'''DELETE FROM worker_data WHERE id={w_id};''')
                        msg_ = tkinter.messagebox.askquestion("Confirm Again", "Are you sure...!!!")
                        if msg_ == "yes":
                            my_database_del_worker.commit()
                        else:
                            pass
                        my_cursor_del_worker.execute(
                            f'''SELECT id FROM worker_data WHERE id={w_id}''')
                        delete_read = my_cursor_del_worker.fetchall()
                        my_cursor_del_worker.close()
                        my_database_del_worker.close()

                        if not delete_read:
                            tkinter.messagebox.showinfo(f"Status of Id= {w_id}, Name= {w_name}",
                                                        "Record Successfully deleted from database.")
                        else:
                            tkinter.messagebox.showwarning("Status", "Record is not deleted from database.")
                    else:
                        pass

                worker_frame.place_forget()

                worker_edit_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
                worker_edit_frame.place(x=50, y=30)

                # edit_frame = labels and Entries and buttons
                edit_label_old_data = tkinter.Label(worker_edit_frame, text="Old Data:", font=("bold", 12),
                                                    bg=background_colour, fg="white")
                edit_label_old_data.place(x=50, y=0)
                edit_label_old_data = tkinter.Label(worker_edit_frame, text="Insert New Data:", font=("bold", 12),
                                                    bg=background_colour, fg="white")
                edit_label_old_data.place(x=300, y=0)

                # Labels and Entries
                edit_label_name = tkinter.Label(worker_edit_frame, text="Worker Name:", bg=background_colour,
                                                        fg="white", font=("bold", 10))
                edit_label_name.place(x=0, y=75)
                edit_label_name_ans = tkinter.Label(worker_edit_frame, text=w_name, width=20, anchor="nw",
                                                            bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_name_ans.place(x=150, y=75)
                edit_entry_name_text = tkinter.StringVar()
                edit_entry_name = tkinter.Entry(worker_edit_frame, text=edit_entry_name_text, width=30)
                edit_entry_name.place(x=320, y=75)

                edit_label_gen = tkinter.Label(worker_edit_frame, text="Worker Gender:", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_gen.place(x=0, y=125)
                edit_re_gen = ""
                if w_gen == "F":
                    edit_re_gen = "Female"
                if w_gen == "M":
                    edit_re_gen = "Male"
                edit_gender = tkinter.Label(worker_edit_frame, text=edit_re_gen, bg=background_colour,
                                                    fg="gold", font=("bold", 10))
                edit_gender.place(x=150, y=125)
                gender = tkinter.StringVar()
                gender.set(0)
                edit_leb_gender_m = tkinter.Radiobutton(worker_edit_frame, text="Male", variable=gender,
                                                                value="M", bg=background_colour, fg="black",
                                                                font=("bold", 10))
                edit_leb_gender_m.place(x=320, y=125)
                edit_leb_gender_f = tkinter.Radiobutton(worker_edit_frame, text="Female", variable=gender,
                                                                value="F", bg=background_colour, fg="black",
                                                                font=("bold", 10))
                edit_leb_gender_f.place(x=390, y=125)

                edit_label_age = tkinter.Label(worker_edit_frame, text="Worker Age :", bg=background_colour,
                                               fg="white", font=("bold", 10))
                edit_label_age.place(x=0, y=175)
                edit_label_age_ans = tkinter.Label(worker_edit_frame, text=w_age, width=20, anchor="nw",
                                                   bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_age_ans.place(x=150, y=175)
                edit_entry_age_text = tkinter.StringVar()
                edit_entry_age = tkinter.Entry(worker_edit_frame, text=edit_entry_age_text, width=30)
                edit_entry_age.place(x=320, y=175)

                edit_label_ph = tkinter.Label(worker_edit_frame, text="Worker Ph.No. :", bg=background_colour,
                                              fg="white", font=("bold", 10))
                edit_label_ph.place(x=0, y=225)
                edit_label_ph_ans = tkinter.Label(worker_edit_frame, text=w_phone, width=20, anchor="nw",
                                                  bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_ph_ans.place(x=150, y=225)
                edit_entry_ph_text = tkinter.StringVar()
                edit_entry_ph = tkinter.Entry(worker_edit_frame, text=edit_entry_ph_text, width=30)
                edit_entry_ph.place(x=320, y=225)

                edit_leb_image = tkinter.Label(worker_edit_frame, text="Worker Image", bg=background_colour,
                                               fg="white", font=("bold", 10))
                edit_leb_image.place(x=570, y=75)
                edit_image = tkinter.Canvas(worker_edit_frame, width=200, height=260)
                edit_image.place(x=570, y=100)
                edit_but_img = tkinter.PhotoImage(file="add_image.png")
                edit_img = tkinter.Button(worker_edit_frame, image=edit_but_img, bd=0, relief="groove",
                                          command=on_add_image_button_edit_frame)
                edit_img.place(x=645, y=200)

                edit_label_add = tkinter.Label(worker_edit_frame, text="Worker Add :", bg=background_colour,
                                                       fg="white", font=("bold", 10))
                edit_label_add.place(x=0, y=275)
                edit_label_add_ans = tkinter.Label(worker_edit_frame, text=w_add, width=20, anchor="nw",
                                                           bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_add_ans.place(x=150, y=275)
                edit_entry_add_text = tkinter.StringVar()
                edit_entry_add = tkinter.Entry(worker_edit_frame, text=edit_entry_add_text, width=30)
                edit_entry_add.place(x=320, y=275)

                edit_label_jo_date = tkinter.Label(worker_edit_frame, text="Joining Date :", bg=background_colour,
                                               fg="white", font=("bold", 10))
                edit_label_jo_date.place(x=0, y=325)
                edit_label_jo_date_ans = tkinter.Label(worker_edit_frame, text=w_jo_date, width=20, anchor="nw",
                                                   bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_jo_date_ans.place(x=150, y=325)
                edit_entry_jo_date_text = tkinter.StringVar()
                edit_entry_jo_date = tkinter.Entry(worker_edit_frame, text=edit_entry_jo_date_text, width=30)
                edit_entry_jo_date.place(x=320, y=325)

                edit_label_adh = tkinter.Label(worker_edit_frame, text="Adhar No. :", bg=background_colour,
                                                      fg="white", font=("bold", 10))
                edit_label_adh.place(x=0, y=375)
                edit_label_adh_ans = tkinter.Label(worker_edit_frame, text=w_adhar_no, width=20, anchor="nw",
                                                          bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_adh_ans.place(x=150, y=375)
                edit_entry_adh_text = tkinter.StringVar()
                edit_entry_adh = tkinter.Entry(worker_edit_frame, text=edit_entry_adh_text, width=30)
                edit_entry_adh.place(x=320, y=375)

                edit_label_sal = tkinter.Label(worker_edit_frame, text="Salary :", bg=background_colour,
                                               fg="white", font=("bold", 10))
                edit_label_sal.place(x=0, y=425)
                edit_label_sal_ans = tkinter.Label(worker_edit_frame, text=w_sal, width=20, anchor="nw",
                                                   bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_sal_ans.place(x=150, y=425)
                edit_entry_sal_text = tkinter.StringVar()
                edit_entry_sal = tkinter.Entry(worker_edit_frame, text=edit_entry_sal_text, width=30)
                edit_entry_sal.place(x=320, y=425)

                edit_label_w_TAG = tkinter.Label(worker_edit_frame, text="TAG :", bg=background_colour, fg="white",
                                                 font=("bold", 10))
                edit_label_w_TAG.place(x=0, y=475)
                edit_label_w_TAG_ans = tkinter.Label(worker_edit_frame, text=w_TAG, width=20, anchor="nw",
                                                     bg=background_colour, fg="gold", font=("bold", 10))
                edit_label_w_TAG_ans.place(x=150, y=475)
                options_for_TAG = ["STUDENT", "TEACHER", "DRIVER", "WORKER", "PRINCIPAL", "ASSISTANT", "OTHER"]
                edit_entry_w_TAG_text = tkinter.StringVar()
                edit_entry_w_TAG = tkinter.OptionMenu(worker_edit_frame, edit_entry_w_TAG_text, *options_for_TAG)
                edit_entry_w_TAG.place(x=320, y=475)
                edit_entry_w_TAG.config(relief="raised", bd=0)

                # This function is used to destroy() the edit frame and go back to on_search_button function
                def cancel_but():
                    worker_edit_frame.destroy()
                    worker_frame.place(x=50, y=30)

                # edit_frame - Buttons
                edit_button_save = tkinter.Button(worker_edit_frame, text="Save Changes", width=14, relief="groove",
                                                  command=on_edit_save_button_edit_frame)
                edit_button_save.place(x=1150, y=620)
                edit_button_cancel = tkinter.Button(worker_edit_frame, text="Cancel", width=10, relief="groove",
                                                    command=cancel_but)
                edit_button_cancel.place(x=1050, y=620)
                edit_button_delete = tkinter.Button(worker_edit_frame, text="Delete Record", width=14, relief="groove",
                                                    command=on_delete_button_edit_frame)
                edit_button_delete.place(x=920, y=620)

                worker_edit_frame.mainloop()


            worker_frame = tkinter.Frame(main_window, width=1300, height=650, bg=background_colour)
            worker_frame.place(x=50, y=30)

            if w_gen == "M":
                gen_img_logo = "img_gender_male.png"
            elif w_gen == "F":
                gen_img_logo = "img_gender_female.png"
            else:
                gen_img_logo = "img_gender_male.png"

            img_gender = ImageTk.PhotoImage(Image.open(gen_img_logo))
            name_leb = tkinter.Label(worker_frame, image=img_gender, compound="left", width=400, text=f" {w_name}",
                                     font=("bold", 15), bg=background_colour, fg="gold", anchor="nw")
            name_leb.place(x=0, y=0)

            id_leb = tkinter.Label(worker_frame, text="Worker ID:", bg=background_colour, fg="white",
                                   font=("bold", 10))
            id_leb.place(x=0, y=65)
            entry_id_leb = tkinter.Label(worker_frame, text=w_id, width=30, anchor="nw", font=("bold", 14),
                                         bg=background_colour, fg="gold")
            entry_id_leb.place(x=150, y=65)

            gen_leb = tkinter.Label(worker_frame, text="Worker gender:", bg=background_colour, fg="white",
                                    font=("bold", 10))
            gen_leb.place(x=0, y=115)
            re_gen = ""
            if w_gen == "F":
                re_gen = "Female"
            if w_gen == "M":
                re_gen = "Male"
            entry_gen_leb = tkinter.Label(worker_frame, text=re_gen, bg=background_colour, fg="gold",
                                          font=("bold", 14))
            entry_gen_leb.place(x=150, y=115)

            age_leb = tkinter.Label(worker_frame, text="Worker Age :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            age_leb.place(x=0, y=165)
            entry_age_leb = tkinter.Label(worker_frame, text=w_age, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_age_leb.place(x=150, y=165)

            ph_leb = tkinter.Label(worker_frame, text="Worker ph.No. :", bg=background_colour, fg="white",
                                   font=("bold", 10))
            ph_leb.place(x=0, y=215)
            entry_ph_leb = tkinter.Label(worker_frame, text=w_phone, width=30, anchor="nw", font=("bold", 14),
                                         bg=background_colour, fg="gold")
            entry_ph_leb.place(x=150, y=215)

            # Image of Teacher
            img_leb = tkinter.Label(worker_frame, text="Worker Image:", font=("Bold", 10), bg=background_colour,
                                    fg="white")
            img_leb.place(x=500, y=0)
            canvas_frame = tkinter.Canvas(worker_frame, width=200, height=260, bg=background_colour)
            canvas_frame.place(x=500, y=24)
            try:
                write_binary_image('got_image_from_mysql_db.jpg', w_img)
                resize_img = Image.open("got_image_from_mysql_db.jpg")
                resize_img = resize_img.resize((200, 260), Image.ANTIALIAS)
                resize_img.save("nres_img.ppm", "ppm")
                got_image = ImageTk.PhotoImage(file='nres_img.ppm')
                canvas_frame.create_image(0, 0, anchor="nw", image=got_image)
            except TypeError:
                pass


            add_leb = tkinter.Label(worker_frame, text="Worker Add :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            add_leb.place(x=0, y=265)
            entry_add_leb = tkinter.Label(worker_frame, text=w_add, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_add_leb.place(x=150, y=265)

            jo_date_leb = tkinter.Label(worker_frame, text="Joining Date :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            jo_date_leb.place(x=0, y=315)
            entry_jo_date_leb = tkinter.Label(worker_frame, text=w_jo_date, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_jo_date_leb.place(x=150, y=315)

            adh_leb = tkinter.Label(worker_frame, text="Adhar No. :", bg=background_colour, fg="white",
                                        font=("bold", 10))
            adh_leb.place(x=0, y=365)
            entry_adh_leb = tkinter.Label(worker_frame, text=w_adhar_no, width=30, anchor="nw", font=("bold", 14),
                                              bg=background_colour, fg="gold")
            entry_adh_leb.place(x=150, y=365)

            sal_leb = tkinter.Label(worker_frame, text="Salary :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            sal_leb.place(x=0, y=415)
            entry_sal_leb = tkinter.Label(worker_frame, text=w_sal, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_sal_leb.place(x=150, y=415)

            TAG_leb = tkinter.Label(worker_frame, text="TAG :", bg=background_colour, fg="white",
                                    font=("bold", 10))
            TAG_leb.place(x=0, y=465)
            entry_TAG_leb = tkinter.Label(worker_frame, text=w_TAG, width=30, anchor="nw", font=("bold", 14),
                                          bg=background_colour, fg="gold")
            entry_TAG_leb.place(x=150, y=465)


            def cancel():
                worker_frame.destroy()
                search_entry.place(x=50, y=30)
                search_button.place(x=300, y=28)
                but_frame.place(x=80, y=80)

            # button to edit data of student
            edit_data_button = tkinter.Button(worker_frame, text="Edit Data", width=12, relief="groove", command=on_edit_button)
            edit_data_button.place(x=1150, y=620)

            cancel_button = tkinter.Button(worker_frame, text="Cancel", width=10, relief="groove", command=cancel)
            cancel_button.place(x=1050, y=620)

            worker_frame.mainloop()


    if value == "":
        pass
    else:
        search_entry.place_forget()
        search_button.place_forget()
        but_frame.place_forget()

        student_search = show_student_data(value)
        print("Student search = ", student_search)

        teacher_search = show_teacher_data(value)
        print("Teacher Search = ", teacher_search)

        driver_search = show_bus_driver_data(value)
        print("Driver search = ", driver_search)

        worker_search = show_worker(value)
        print("Worker search = ", worker_search)

        if student_search == "No" and teacher_search == "No" and driver_search == "No" and worker_search == "No":
            but_frame.place(x=80, y=80)
            search_entry.place(x=50, y=30)
            search_button.place(x=300, y=28)
            tkinter.messagebox.showinfo(f"Info of {value}", f"The Data is not available. Named={value}\n You can try by Searching in show all fields. or\n You can Add new Data.")


# @@@@@@@@@@@@@@@@@ Main CODE @@@@@@@@@@@@@@@@

main_window = tkinter.Tk()
main_window.geometry("1200x600+20+20")
main_window.title("School Management System")
main_window.config(bg=background_colour)
main_window.iconbitmap('Engine_icon.ico')

menu = tkinter.Menu(main_window)
main_window.config(menu=menu)

file_ = tkinter.Menu(menu)
file_.add_command(label="Exit", command=main_window.destroy)
menu.add_cascade(label="File", menu=file_)

def on_con_us():
    con_win = tkinter.Tk()
    con_win.geometry("300x100")
    con_win.title("Contact Us")
    tkinter.Label(con_win, text="Not Given").pack()
    con_win.mainloop()
edit = tkinter.Menu(menu)
edit.add_command(label="contact us", command=on_con_us)
menu.add_cascade(label="Help", menu=edit)

def on_ab_us():
    con_win = tkinter.Tk()
    con_win.geometry("600x150")
    con_win.title("About Us")
    tkinter.Label(con_win, text="School Management Software-").place(x=2, y=0)
    tkinter.Label(con_win, text="1)Enables you to store and use the data ex. Student, Teacher, Driver and Worker.").place(x=2, y=20)
    tkinter.Label(con_win, text="2)Data can be modify.").place(x=2, y=40)
    tkinter.Label(con_win, text="3)We can store name, class, address, phone No., Image, documents, etc...").place(x=2, y=60)
    con_win.mainloop()
about_us = tkinter.Menu(menu)
about_us.add_command(label="About software", command=on_ab_us)
menu.add_cascade(label="About Us", menu=about_us)

# Search Entry
def entry_bind(event):
    on_search_button()


search_text = tkinter.StringVar()
search_entry = tkinter.Entry(main_window, text=search_text, width=40, bd=1)
search_entry.place(x=50, y=30)
search_entry.bind("<Return>", entry_bind)

search_img = tkinter.PhotoImage(file='search_img.png')
search_button = tkinter.Button(main_window, image=search_img, text=" Search", width=80, bg='white', relief="groove", command=on_search_button, compound='left')
search_button.place(x=300, y=28)


# but_frame to show all the add and show button present on main_window
but_frame = tkinter.Frame(main_window, width=1000, height=600, bg=background_colour)
but_frame.place(x=80, y=80)

but_frame_func()

main_window.mainloop()

# @@@@@@@@@@@@@@@@@ Main CODE END@@@@@@@@@@@@@@@@


