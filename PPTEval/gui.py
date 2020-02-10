import tkinter as tk
import sys
import main
import tkinter
from datetime import datetime
# ---- Weather functions -------------------------------------------------------
def weather_window():
    weather_window = tk.Toplevel()
    main_window.withdraw()
    weather_window.configure()
    weather_window.geometry("500x480")





# ---------- Main GUI functions ------------------------------------------------
def cancel():
    login_window.destroy()
    main_window.destroy()
    sys.exit()
def email_confirmation():
    if '@gmail' or '@yahoo' in email_en.get():
        main_window.deiconify()
        login_window.destroy()
    else:
        tk.messagebox.showerror("Error","Invalid Email Address.")



def call_back():
    print("Information collected")

# -------- Primary window configurations ---------------------------------------
main_window = tk.Tk()
login_window = tk.Toplevel(main_window)
# -------- Main window configurations ------------------------------------------
main_window.resizable(0,0)
main_window.title("PPT's Weather and Email Service")
main_window.configure()
main_window.geometry("500x480")
heading_label = tk.Label(main_window, text= "Weather forecast and Email interface" \
                ,font = ("Arial", 10), fg = 'black').grid(row = 0, column = 2)

# --------------------Main window configurations(Weather) ---------------------#

weather_button_text = "View the weather forecast for \n \
the next 5 days in 3 hour intervals"
weather_button = tk.Button(main_window,text = weather_button_text,\
                         command = weather_window)
weather_button.grid(row = 6, column = 1)

# ---------- Login window configurations ---------------------------------------
login_window.title("PPT's Weather and Email Service")
login_window.configure()
login_window.geometry("240x240")
# ------------------------------------------------------------------------------



# -------- Email and password login details: -----------------------------------
# TODO --- Implement a validation method
tk.Label(login_window,text = "Email address").grid(row = 1)
email_en = tk.Entry(login_window)
email_en.grid(row = 1,column = 1)
email = email_en.get()
reg = login_window.register(email_confirmation)
tk.Label(login_window,text = "Email Password").grid(row = 2)
password_en = tk.Entry(login_window)
password_en.grid(row = 2,column = 1)
password = password_en.get()
# ------------------------------------------------------------------------------
tk.Button(login_window,text = "Login",command = email_confirmation).grid(row = 3,column = 1)
tk.Button(login_window,text = "Cancel Login", command = cancel).grid(row = 4,column = 1)

# ------ Weather Window --------------------------------------------------------

main_window.withdraw()
main_window.mainloop()

#Making the buttons for the choices
#choice_label = tk.Label(window,text="Would you like to view the weather or send an email?").grid(column = 5,row = 3)
#weather_button = tk.Button(window,text = "View the forecast")
#weather_button.grid(column = 3,row = 4)
#email_button = tk.Button(window,text = "Send an email")
#email_button.grid(column = 3,row = 6)
#login(window)
#lst = get_input(window)
#print(lst)
