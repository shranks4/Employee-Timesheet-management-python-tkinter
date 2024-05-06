import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tkinter import messagebox


con = pymysql.connect(host='localhost', user='root', password='root')
mycursor = con.cursor()
global root
root = tk.Tk()
root.geometry("1400x700+110+100")
root.title('Timesheet')
root.config(bg='#C7CEB6')

f = "Bahnschrift Light"
b = "#5ED3AC"
def hours_worked():
    i = int(Hours_am1.get())
    count1 = int(Hours_am2.get()) - i

    count2 = int(Hours_pm2.get()) - int(Hours_pm1.get())
    count = count1 + count2
    return count

def displayData():
    mycursor.execute('use sample')
    mycursor.execute('SELECT * FROM Info')
    data = mycursor.fetchall()

    for Data in data:
        table.insert('', 'end', value=(Data[0], Data[1], Data[2], Data[3], Data[4], Data[5], Data[6], Data[7], Data[8]))



def next_page():

    global new_window
    new_window = tk.Toplevel()
    new_window.geometry("400x550+800+300")
    new_window.title('Add Timesheet')
    new_window.config(bg='#9BB474')

    bacg='#9BB474'

    # Calender
    global cal
    cal = DateEntry(new_window, width=12, year=2024, month=4, day=3,
                    background='green', foreground='white', borderwidth=2)
    cal.config(font="Helvetica")
    cal.place(relx=0.22, rely=0.14, anchor="center")



    date = Label(new_window, text='Date:', font=(f, 13), bg=bacg)
    date.place(relx=0.1, rely=0.09, anchor="center")

    day = Label(new_window, text='Day of the week:', font=(f, 13), bg=bacg)
    day.place(relx=0.7, rely=0.09, anchor="center")

    global txt
    txt = Text(new_window, height=1.3, width=15, borderwidth=2)
    txt.place(relx=0.7, rely=0.14, anchor="center")

    AM = Label(new_window, text='AM', font=(f, 16), bg=bacg)
    AM.place(relx=0.1, rely=0.25, anchor="center")

    timein = Label(new_window, text='Time in:', font=(f, 13), bg=bacg)
    timein.place(relx=0.14, rely=0.32, anchor="center")

    # combobox

    variable1 = tk.StringVar()
    variable2 = tk.StringVar()
    variable3 = tk.StringVar()
    variable4 = tk.StringVar()
    variable5 = tk.StringVar()
    variable6 = tk.StringVar()
    variable7 = tk.StringVar()
    variable8 = tk.StringVar()

    # HOURS AM1
    global Hours_am1
    Hours_am1 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable1,values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14','15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
    Hours_am1.place(relx=0.12, rely=0.38, anchor="center")
    variable1.set('Hrs')


    # MINS AM1
    global Mins_am1
    Mins_am1 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable2,
                            values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                                    '51', '52', '53', '54', '55', '56', '57', '58', '59'])
    variable2.set('Min')
    Mins_am1.place(relx=0.25, rely=0.38, anchor="center")

    timeout = Label(new_window, text='Time out:', font=(f, 13), bg=bacg)
    timeout.place(relx=0.65, rely=0.32, anchor="center")

    # HOURS AM2
    global Hours_am2
    Hours_am2 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable3,
                             values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
    Hours_am2.place(relx=0.62, rely=0.38, anchor="center")
    variable3.set('Hrs')


    # MINS AM2
    global Mins_am2
    Mins_am2 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable4,
                            values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                                    '51', '52', '53', '54', '55', '56', '57', '58', '59'])
    variable4.set('Min')
    Mins_am2.place(relx=0.75, rely=0.38, anchor="center")


    PM = Label(new_window, text='PM', font=(f, 16), bg=bacg)
    PM.place(relx=0.1, rely=0.5, anchor="center")

    timein2 = Label(new_window, text='Time in:', font=(f, 13), bg=bacg)
    timein2.place(relx=0.14, rely=0.58, anchor="center")

    timeout2 = Label(new_window, text='Time out:', font=(f, 13), bg=bacg)
    timeout2.place(relx=0.65, rely=0.58, anchor="center")

    # HOURS PM1
    global Hours_pm1
    Hours_pm1 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable5,
                             values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
    Hours_pm1.place(relx=0.12, rely=0.64, anchor="center")
    variable5.set('Hrs')

    # MINS PM1
    global Mins_pm1
    Mins_pm1 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable6,
                            values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                                    '51', '52', '53', '54', '55', '56', '57', '58', '59'])
    variable6.set('Min')
    Mins_pm1.place(relx=0.25, rely=0.64, anchor="center")


    # HOURS PM2
    global Hours_pm2
    Hours_pm2 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable7,
                             values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
    Hours_pm2.place(relx=0.62, rely=0.64, anchor="center")
    variable7.set('Hrs')


    # MINS PM2
    global Mins_pm2
    Mins_pm2 = ttk.Combobox(new_window, width=4, height=14, textvariable=variable8,
                            values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                                    '51', '52', '53', '54', '55', '56', '57', '58', '59'])
    variable8.set('Min')
    Mins_pm2.place(relx=0.75, rely=0.64, anchor="center")


    # TASKS
    Task = Label(new_window, text="Task", font=(f, 16), bg=bacg)
    Task.place(relx=0.1, rely=0.72, anchor="center")
    global t
    t = tk.Text(new_window, width=44, height=5, fg='firebrick1', )
    t.place(relx=0.5, rely=0.84, anchor="center")

    add_button = ttk.Style()
    add_button.configure('.', font=(f, 13))
    add_button = ttk.Button(new_window, text='Add Timesheet', command=sql_connect)
    add_button.place(relx=0.8, rely=0.96, anchor='center')



text = tk.Label(root, text='Timesheet', font=(f, 20), bg='#D6EBB3', fg='black', padx=10, pady=5, borderwidth=2, relief='groove')
text.place(relx=0.1, rely=0.1, anchor='center')

#Tree view
table = ttk.Treeview(root, columns=('ID', 'Date', 'dow', 'Timein_am', 'Timeout_am', 'Timein_pm', 'Timeout_pm', 'Worked_hours', 'task'), show='headings')
table.heading('ID', text='ID')
table.heading('Date', text='Date')
table.heading('dow', text='Day of the week')
table.heading('Timein_am', text='Time in(AM)')
table.heading('Timeout_am', text='Time out(AM)')
table.heading('Timein_pm', text='Time in(PM)')
table.heading('Timeout_pm', text='Time out(PM)')
table.heading('Worked_hours', text='Worked Hours')
table.heading('task', text='Task')
table.pack(padx=30, pady=150, fill='both', expand='True')

k = 135

table.column('ID', minwidth=80, width=80, stretch=False)
table.column('Date', minwidth=k, width=k, stretch=False)
table.column('dow', minwidth=k, width=k, stretch=False)
table.column("Timein_am", minwidth=k, width=k, stretch=False)
table.column("Timeout_am", minwidth=k, width=k, stretch=False)
table.column('Timein_pm', minwidth=k, width=k, stretch=False)
table.column('Timeout_pm', minwidth=k, width=k, stretch=False)
table.column('Worked_hours', minwidth=k, width=k, stretch=False)
table.column('task', minwidth=350, width=350, stretch=False)
displayData()

#add timesheet button


button_style = ttk.Style()
button_style.theme_use('alt')
button_style.configure(
    'Custom.TButton',
    foreground='white',
    background='#4CAF50',
    font=(f, 14, 'bold'),
    padding=5,
    borderwidth=2,
    relief='flat')

# Define hover style for the button
button_style.map(
    'Custom.TButton',
    background=[('active', '#45a049')],  # Darker shade of green when button is clicked
    relief=[('pressed', 'sunken')])

# Create the button with custom style
button = ttk.Button(root, text='Add Timesheet', command=next_page, style='Custom.TButton')
button.place(relx=0.8, rely=0.1, anchor='center')

def delete_selected_row(event):

    focused_item = table.focus()

    if focused_item:
        # Get the identifier (e.g., primary key) of the focused item
        item_values = table.item(focused_item, 'values')
        if item_values:
            item_id = item_values[0]

            try:
                con = pymysql.connect(host='localhost', user='root', password='root')
                mycursor = con.cursor()

                mycursor.execute("USE sample")

            # Execute the DELETE query
                query = "DELETE FROM Info WHERE id = %s"
                mycursor.execute(query, (item_id,))

            # Commit the transaction
                con.commit()

            # Close the cursor and connection
                mycursor.close()
                con.close()

            # Delete the focused item from the Treeview
                table.delete(focused_item)
                print("Row deleted successfully")
            except pymysql.connect.Error as e:
                print("Error:", e)
def sql_connect():

    if (t.get("1.0", "end-1c") == '' or Hours_am1.get() == 'Hrs' or Hours_am2.get() == 'Hrs' or Hours_pm1.get() == 'Hrs' or Hours_pm2.get() == 'Hrs' or
            Mins_am1.get() == 'Min' or Mins_am2.get() == 'Min' or Mins_pm1.get() == 'Min' or Mins_am1.get() == 'Min'):
        messagebox.showerror('Error', 'All Fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue')
            return
        try:
            query = 'create database sample'
            mycursor.execute(query)
            query = 'use sample'
            mycursor.execute(query)
        except:
            query = 'use sample'
            mycursor.execute(query)

        query = 'insert into Info(dates, dow, Timein_am, Timeout_am, Timein_pm, Timeout_pm, Worked_hours, task) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query, (cal.get(), txt.get("1.0", "end-1c"), Hours_am1.get() + ":" + Mins_am1.get(),
                                 Hours_am2.get() + ":" + Mins_am2.get(), Hours_pm1.get() + ":" + Mins_pm1.get(),
                                 Hours_pm2.get() + ":" + Mins_pm2.get(), hours_worked(), t.get("1.0", "end-1c")))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Timesheet added successfully')

        new_window.destroy()
def refre():
    for row in table.get_children():
        table.delete(row)
    con = pymysql.connect(host='localhost', user='root', password='root')
    mycursor2 = con.cursor()

    mycursor2.execute('use sample')
    mycursor2.execute('SELECT * FROM Info')
    data = mycursor2.fetchall()
    for Data2 in data:
        table.insert('', 'end', value=(Data2[0], Data2[1], Data2[2], Data2[3], Data2[4], Data2[5], Data2[6], Data2[7], Data2[8]))
def edit_selected_item():
    # Get the selected item from the Treeview
    selected_item = table.focus()

    # Ensure that an item is selected
    if selected_item:
        # Get the data of the selected item
        item_data = table.item(selected_item)

        # Retrieve the values of the selected item
        item_values = item_data['values']

        # Create a new window for editing
        edit_window = tk.Toplevel()
        edit_window.title('Edit Timesheet')
        edit_window.geometry('700x400')

        # Labels and entry widgets for editing
        date_label = tk.Label(edit_window, text='Date:')
        date_label.grid(row=0, column=0, padx=10, pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.insert(0, item_values[1])  # Insert the existing date into the entry widget
        date_entry.grid(row=0, column=1, padx=10, pady=5)

        dow_label = tk.Label(edit_window, text='Day of the week:')
        dow_label.grid(row=1, column=0, padx=10, pady=5)
        dow_entry = tk.Entry(edit_window)
        dow_entry.insert(0, item_values[2])  # Insert the existing date into the entry widget
        dow_entry.grid(row=1, column=1, padx=10, pady=5)

        Timein_am_label = tk.Label(edit_window, text='Time in(AM):')
        Timein_am_label.grid(row=2, column=0, padx=10, pady=5)
        Timein_am_entry = tk.Entry(edit_window)
        Timein_am_entry.insert(0, item_values[3])  # Insert the existing date into the entry widget
        Timein_am_entry.grid(row=2, column=1, padx=10, pady=5)

        Timeout_am_label = tk.Label(edit_window, text='Time out(AM):')
        Timeout_am_label.grid(row=0, column=2, padx=10, pady=5)
        Timeout_am_entry = tk.Entry(edit_window)
        Timeout_am_entry.insert(0, item_values[4])  # Insert the existing date into the entry widget
        Timeout_am_entry.grid(row=0, column=3, padx=10, pady=5)

        Timein_pm_label = tk.Label(edit_window, text='Time in(PM):')
        Timein_pm_label.grid(row=1, column=2, padx=10, pady=5)
        Timein_pm_entry = tk.Entry(edit_window)
        Timein_pm_entry.insert(0, item_values[5])  # Insert the existing date into the entry widget
        Timein_pm_entry.grid(row=1, column=3, padx=10, pady=5)

        Timeout_pm_label = tk.Label(edit_window, text='Time out(PM):')
        Timeout_pm_label.grid(row=2, column=2, padx=10, pady=5)
        Timeout_pm_entry = tk.Entry(edit_window)
        Timeout_pm_entry.insert(0, item_values[6])  # Insert the existing date into the entry widget
        Timeout_pm_entry.grid(row=2, column=3, padx=10, pady=5)

        worked_hours_label = tk.Label(edit_window, text='Worked Hours:')
        worked_hours_label.grid(row=3, column=2, padx=10, pady=5)
        worked_hours_entry = tk.Entry(edit_window)
        worked_hours_entry.insert(0, item_values[7])  # Insert the existing date into the entry widget
        worked_hours_entry.grid(row=3, column=3, padx=10, pady=5)

        task_label = tk.Label(edit_window, text='Task:')
        task_label.grid(row=3, column=0, padx=10, pady=5)
        task_entry = tk.Text(edit_window, width=30, height=5)  # Set the height to 5 lines
        task_entry.insert(tk.END, item_values[8])  # Insert the existing text into the Text widget
        task_entry.grid(row=3, column=1, padx=10, pady=5)


        # Function to update the Treeview and MySQL database with the edited data
        def update_treeview_and_database():
            # Get the edited values from the entry widgets
            edited_date = date_entry.get()
            edited_task = task_entry.get("1.0", "end")
            edited_dow = dow_entry.get()
            edited_timein_am = Timein_am_entry.get()
            edited_timeout_am = Timeout_am_entry.get()
            edited_timein_pm = Timein_pm_entry.get()
            edited_timeout_pm = Timeout_pm_entry.get()
            edited_worked_hours = worked_hours_entry.get()



            # Update the Treeview with the edited data
            table.item(selected_item, values=(edited_date, edited_dow, edited_timein_am, edited_timeout_am, edited_timein_pm, edited_timeout_pm, edited_worked_hours, edited_task))

            # Update the MySQL database
            update_query = "UPDATE Info SET dates = %s, dow = %s, Timein_am = %s, Timeout_am = %s, Timein_pm = %s, Timeout_pm = %s, worked_hours = %s, task = %s  WHERE id = %s"
            update_values = (edited_date, edited_dow, edited_timein_am, edited_timeout_am, edited_timein_pm, edited_timeout_pm, edited_worked_hours, edited_task, item_values[0])  # Assuming the id is the third column
            mycursor.execute(update_query, update_values)
            con.commit()

            # Close the edit window
            edit_window.destroy()

        # Button to update the Treeview and MySQL database with the edited data
        update_button = ttk.Button(edit_window, text='Update', command=update_treeview_and_database)
        update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


#Refresh button
re_style = ttk.Style()
re_style.theme_use('alt')
re_style.configure('Green.TButton', foreground='green', font=(f, 13))
refresh_button = ttk.Button(root, text='Refresh', command=refre, style='Green.TButton')
refresh_button.place(relx=0.8, rely=0.9, anchor='center')


#Delete button

delete_style = ttk.Style()
delete_style.configure('Red.TButton', foreground='red', font=(f, 13))
delete_button = ttk.Button(root, text='Delete', style='Red.TButton')
delete_button.place(relx=0.7, rely=0.9, anchor='center')
delete_button.bind("<Button-1>", delete_selected_row)


#Edit button

edit_style = ttk.Style()
edit_style.theme_use('alt')
edit_style.configure('Yellow.TButton', foreground='yellow', font=(f, 13))
edit_button = ttk.Button(root, text='Edit', command=edit_selected_item, style='Yellow.TButton')
edit_button.place(relx=0.6, rely=0.9, anchor='center')

root.mainloop()

