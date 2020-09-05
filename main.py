from tkinter import *
from tkinter import messagebox
from WriterCSV import *

root = Tk()
root.title("Приложение для автомобилистов by Eclezzio")
root.geometry("800x400+100+100")

def send():
    arr = [
        ['Имя', 'Фамилия', 'Дата рождения', 'Количество Л.С.', 'Номер авто', 'VIN', 'Пробег'],
        [entry_name.get(), entry_surname.get(), entry_birthday.get(), entry_ls.get(), entry_num.get(), entry_vin.get(), entry_km.get()]
    ]

    arr2 = []

    from_arr_2x_to_arr_1x(arr, arr2)
    write_file(arr2, f'{entry_name.get()}_{entry_surname.get()}.csv')

    messagebox.showinfo("Успешно", f"Данные успешно внесены в документ {entry_name.get()}_{entry_surname.get()}.csv")

label_name = Label(text="Имя: ", bd=1, height=2, width=4)
label_name.grid(row=2, column=2, padx=20, pady=20)

entry_name = Entry(bd=2)
entry_name.grid(row=2, column=3)

label_surname = Label(text="Фамилия: ", bd=1, height=2, width=8)
label_surname.grid(row=2, column=5, padx=20, pady=20)

entry_surname = Entry(bd=2)
entry_surname.grid(row=2, column=6)

label_birthday = Label(text="Дата рождения: ", bd=1, height=2, width=12)
label_birthday.grid(row=2, column=8, padx=20, pady=20)

entry_birthday = Entry(bd=2)
entry_birthday.grid(row=2, column=9)

label_ls = Label(text="Количество л.с.: ", bd=1, height=2, width=14)
label_ls.grid(row=4, column=2, padx=20, pady=20)

entry_ls = Entry(bd=2)
entry_ls.grid(row=4, column=3)

label_num = Label(text="Номер авто: ", bd=1, height=2, width=10)
label_num.grid(row=4, column=5, padx=20, pady=20)

entry_num = Entry(bd=2)
entry_num.grid(row=4, column=6)

label_vin = Label(text="VIN", bd=1, height=2, width=5)
label_vin.grid(row=4, column=8, padx=20, pady=20)

entry_vin = Entry(bd=2)
entry_vin.grid(row=4, column=9)

label_km = Label(text="Пробег", bd=1, height=2, width=7)
label_km.grid(row=6, column=2, padx=20, pady=20)

entry_km = Entry(bd=2)
entry_km.grid(row=6, column=3)

btn_send = Button(text="Отправить", bd=2, command=send, justify=CENTER, height=4, width=10)
btn_send.grid(row=7, column=8)

root.mainloop()
