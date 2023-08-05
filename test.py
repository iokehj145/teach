import customtkinter
from Sorte import Sort
customtkinter.set_appearance_mode("Dark")
app = customtkinter.CTk()
def button_callback(fn):
    N = result.get()
    if N:
        try:
            N = int(N)
            arr = Sort(N)
            arr.array, count = arr.fun_sel(fn)
            counter = "Час: "+ str(count)
            Text1.configure(text=counter,text_color="#fff")
        except ValueError:
            counter= "Проблеми із типом зміної"
            Text1.configure(text=counter,text_color="#FF0606",font=("Roboto", 35))
    else:
        counter= "Введіть число"
        Text1.configure(text=counter,text_color="#FF0606",font=("Roboto", 35))
app.title("Yaric app")
app.geometry("1200x700")
app.minsize(1200, 700)
Font1 = ("Roboto", 35)
cor_y = 130
pad_x = 30
customtkinter.deactivate_automatic_dpi_awareness()
counter = "Час: "
result = customtkinter.CTkEntry(app,width=400,height=50,border_width=2,corner_radius=2,border_color="#728FCE", placeholder_text="Кіл.елементів.мас",font=Font1)
bu_2 = customtkinter.CTkButton(app, width=300, height=60, text="Вибіркове", font=Font1, fg_color="#071a91", border_color="#000000", command=lambda: button_callback(2))
bu_1 = customtkinter.CTkButton(app, width=300, height=60, border_width=0, corner_radius=8, text="Бульбошкове", font=Font1, fg_color="#071a91", command=lambda: button_callback(5))
bu_3 = customtkinter.CTkButton(app, width=300, height=60, border_width=0, corner_radius=8, text="Вставкою", font=Font1, fg_color="#071a91", command=lambda: button_callback(3))
bu_4 = customtkinter.CTkButton(app, width=300, height=60, border_width=0, corner_radius=8, text="Бого сор.", font=Font1, fg_color="#071a91", command=lambda: button_callback(4))
bu_5 = customtkinter.CTkButton(app, width=300, height=60, border_width=0, corner_radius=8, text="Швидке", font=Font1, fg_color="#071a91", command=lambda: button_callback(1))
bu_6 = customtkinter.CTkButton(app, width=300, height=60, border_width=0, corner_radius=8, text="Злиттям", font=Font1, fg_color="#071a91", command=lambda: button_callback(6))
Text1 = customtkinter.CTkLabel(app, text=counter,width=200,height=50, fg_color="transparent",font=("Roboto", 50))
bu_1.grid(row=1, column=0, padx=pad_x, pady=(cor_y, 200), sticky="w"), bu_2.grid(row=1, column=1, padx=pad_x, pady=(cor_y, 200)), bu_3.grid(row=1, column=2, pady=(cor_y, 200), sticky="w"), result.grid(row=0, column=1, padx=pad_x, pady=(cor_y/1, 0), sticky="w")
bu_4.grid(row=1, column=0, padx=pad_x, pady=(cor_y*1.5, 0), sticky="w"), bu_5.grid(row=1, column=1, padx=pad_x*3, pady=(cor_y*1.5, 0), sticky="w"), bu_6.grid(row=1, column=2, pady=(cor_y*1.5, 0), sticky="w")
Text1.grid(row=2, column=1, padx=pad_x,  sticky="w")
app.mainloop()