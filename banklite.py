#imports
from tkinter import *
import os
from PIL import ImageTk, Image
import random

#Main Screen
master = Tk()
master.title('Bank App')

#generate account number
def generate_account_number():
#Generate a 6-digit random account number
  return str(random.randint(100000,999999))

#Functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    mobile_number = temp_mobile_number.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "" or mobile_number == "":
        notif.config(fg="red",text="All fields requried * ")
        return

    #generate a unique account number
    account_number = generate_account_number()

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(mobile_number +'\n')
            new_file.write(account_number +'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account has been created with Account Number: {}".format(account_number))


def register():
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global temp_mobile_number
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    temp_mobile_number = StringVar()

    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')



    #Labels
    Label(register_screen, text="Please enter your details below to register", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=4,sticky=W)
    Label(register_screen, text="Mobile Number", font=('Calibri',12)).grid(row=5, sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=6,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=1)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=1)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=1)
    Entry(register_screen, textvariable=temp_mobile_number).grid(row=5, column=1)

    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Calibri',12)).grid(row=7,sticky=N,pady=10)

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    login_mobile_number = temp_mobile_number.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                #Labels
                Label(account_dashboard, text="Account Dashboard", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+name+" !!", font=('Calibri',12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details",font=('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Deposit",font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard, text="Withdraw",font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                Button(account_dashboard, text="Transfer Money", font=('Calibri', 12), width=30, command=transfer_money).grid(row=5, sticky=N, padx=10)
                Button(account_dashboard, text="Customer Support", font=('Calibri', 12), width=30, command=customer_support).grid(row=6, sticky=N, padx=10)
                Button(account_dashboard, text="Apply Loans", font=('Calibri', 12),width=30, command=apply_loan).grid(row=7,sticky=N,padx=10)

                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect!!")
                return
    login_notif.config(fg="red", text="No account found !!")

def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[6]
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    #Label
    Label(deposit_screen, text="Deposit", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance : Rs."+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen,font=('Calibri',12))
    deposit_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2,column=1)
    #Button
    Button(deposit_screen,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)

def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text='Amount is required!',fg="red")
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs."+str(updated_balance),fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')

def withdraw():
     #Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[6]
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    #Label
    Label(withdraw_screen, text="Withdraw", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : Rs."+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_screen,font=('Calibri',12))
    withdraw_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2,column=1)
    #Button
    Button(withdraw_screen,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required!',fg="red")
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[6]

    if float(withdraw_amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs."+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')


def personal_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_mobile_number = user_details[4]
    details_account_number = user_details[5]
    details_balance = user_details[6]
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name : "+details_name, font=('Calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen, text="Age : "+details_age, font=('Calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen, text="Gender : "+details_gender, font=('Calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen, text="Mobile Number : "+details_mobile_number, font=('Calibri',12)).grid(row=4,sticky=W)
    Label(personal_details_screen, text="Account Number : "+details_account_number, font=('Calibri',12)).grid(row=5,sticky=W)
    Label(personal_details_screen, text="Balance :Rs."+details_balance, font=('Calibri',12)).grid(row=6,sticky=W)
def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global temp_mobile_number
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    temp_mobile_number = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(login_screen, text="Mobile Number", font=('Calibri',12)).grid(row=3,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)
    Entry(login_screen, textvariable=temp_mobile_number).grid(row=3,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Calibri',12)).grid(row=5,sticky=W,pady=5,padx=5)
# ... (your existing code)




# Function to handle money transfer
def transfer_money():
    # Vars
    global transfer_notif
    global recipient_username_var
    global recipient_account_number_var
    global amount_var

    transfer_notif = Label(master, font=('Calibri', 12))
    transfer_notif.grid(row=6, sticky=N, pady=10)

    recipient_username_var = StringVar()
    recipient_account_number_var = StringVar()
    amount_var = StringVar()

    # Transfer Money Screen
    transfer_screen = Toplevel(master)
    transfer_screen.title('Transfer Money')

    # Labels
    Label(transfer_screen, text="Transfer Money", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(transfer_screen, text="Recipient Username:", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(transfer_screen, text="Recipient Account Number:", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(transfer_screen, text="Amount:", font=('Calibri', 12)).grid(row=3, sticky=W)

    # Entries
    Entry(transfer_screen, textvariable=recipient_username_var).grid(row=1, column=1)
    Entry(transfer_screen, textvariable=recipient_account_number_var).grid(row=2, column=1)
    Entry(transfer_screen, textvariable=amount_var).grid(row=3, column=1)

    # Button
    Button(transfer_screen, text="Transfer", command=transfer_money_process, font=('Calibri', 12)).grid(row=4, sticky=N, pady=10)

# Function to process money transfer
def transfer_money_process():
    recipient_username = recipient_username_var.get()
    recipient_account_number = recipient_account_number_var.get()
    amount = amount_var.get()

    # Validate input
    if not recipient_username or not recipient_account_number or not amount:
        transfer_notif.config(fg="red", text="All fields are required")
        return

    try:
        amount = float(amount)
    except ValueError:
        transfer_notif.config(fg="red", text="Invalid amount")
        return

    transfer_money_logic(recipient_username, recipient_account_number, amount)

# Function to handle money transfer logic
def transfer_money_logic(recipient_username, recipient_account_number, amount):
    sender_file_path = login_name
    recipient_file_path = recipient_username

    # Read sender's data
    with open(sender_file_path, 'r') as sender_file:
        sender_data = sender_file.readlines()
        sender_balance = float(sender_data[6].strip())

    # Read recipient's data
    with open(recipient_file_path, 'r') as recipient_file:
        recipient_data = recipient_file.readlines()
        recipient_balance = float(recipient_data[6].strip())

    # Check if sender has sufficient balance
    if sender_balance < amount:
        transfer_notif.config(fg="red", text="Insufficient funds for the transfer")
        return

    # Update balances
    sender_balance -= amount
    recipient_balance += amount

    # Write updated balances back to files
    with open(sender_file_path, 'r+') as sender_file:
        sender_data[6] = str(sender_balance) + '\n'
        sender_file.seek(0)
        sender_file.writelines(sender_data)
        sender_file.truncate()

    with open(recipient_file_path, 'r+') as recipient_file:
        recipient_data[6] = str(recipient_balance) + '\n'
        recipient_file.seek(0)
        recipient_file.writelines(recipient_data)
        recipient_file.truncate()

    # Display transaction overview
    transaction_overview = Toplevel(master)
    transaction_overview.title('Transaction Overview')

    Label(transaction_overview, text="Transaction Overview", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(transaction_overview, text=f"Sender: {login_name}", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(transaction_overview, text=f"Recipient: {recipient_username} ({recipient_account_number})", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(transaction_overview, text=f"Amount Transferred: Rs. {amount}", font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(transaction_overview, text=f"Sender's New Balance: Rs. {sender_balance}", font=('Calibri', 12)).grid(row=4, sticky=W)
    Label(transaction_overview, text=f"Recipient's New Balance: Rs. {recipient_balance}", font=('Calibri', 12)).grid(row=5, sticky=W)
def customer_support():
    support_screen = Toplevel(master)
    support_screen.title('Customer Support')

    # Labels
    Label(support_screen, text="Customer Support", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(support_screen, text="Enter your query below:", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(support_screen, text="Enter your Email ID :", font=('Calibri',12)).grid(row=2,sticky=W)

    # Entry for user query
    query_entry = Entry(support_screen, width=40)
    query_entry.grid(row=1, column=1, padx=10)

    # Entry for user email id
    email_entry = Entry(support_screen, width=40)
    email_entry.grid(row=2, column=1, padx=10)

    def submit_query():
        query = query_entry.get()
        email = email_entry.get()

        if query and email:
            # Append user query and email to the support file
            with open('customer_support_queries.txt', 'a') as support_file:
                support_file.write(f"Email: {email}\nQuery: {query}\n\n")

            Label(support_screen, text="Query submitted successfully!", font=('Calibri', 12), fg='green').grid(row=4, column=0, columnspan=2)
        else:
            Label(support_screen, text="Please enter both query and email!", font=('Calibri', 12), fg='red').grid(row=4, column=0, columnspan=2)

    # Button to submit query
    Button(support_screen, text="Submit Query", command=submit_query, font=('Calibri', 12)).grid(row=3, column=0, columnspan=2, pady=10)

def apply_loan():
    loan_screen = Toplevel(master)
    loan_screen.title('Apply for Loan')

    # Labels
    Label(loan_screen, text="Select Loan Type:", font=('Calibri', 12)).grid(row=0, sticky=W, pady=10)

    # Radio Buttons for Loan Types
    loan_type_var = StringVar()
    loan_type_var.set("Education")  # Default selection
    Radiobutton(loan_screen, text="Education Loan", variable=loan_type_var, value="Education", font=('Calibri', 12)).grid(row=1, sticky=W)
    Radiobutton(loan_screen, text="Home Loan", variable=loan_type_var, value="Home", font=('Calibri', 12)).grid(row=2, sticky=W)
    Radiobutton(loan_screen, text="Personal Loan", variable=loan_type_var, value="Personal", font=('Calibri', 12)).grid(row=3, sticky=W)

    # Button to proceed to loan application
    Button(loan_screen, text="Proceed", command=lambda: open_loan_application(loan_type_var.get()), font=('Calibri', 12)).grid(row=4, pady=10)

def open_loan_application(loan_type):
    loan_terms_screen = Toplevel(master)
    loan_terms_screen.title('Loan Terms and Conditions')

    # Label
    Label(loan_terms_screen, text="Terms and Conditions", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    
    # Terms and Conditions
    terms_and_conditions = get_loan_terms(loan_type)
    Label(loan_terms_screen, text=terms_and_conditions, font=('Calibri', 10), wraplength=400, justify=LEFT).grid(row=1, column=0, columnspan=2)

    # Checkbox for agreement
    agreement_var = IntVar()
    Checkbutton(loan_terms_screen, text="I agree", variable=agreement_var, font=('Calibri', 10)).grid(row=2, column=0, columnspan=2)

    # Button to proceed to loan application form
    Button(loan_terms_screen, text="Proceed", command=lambda: open_loan_application_form(loan_type, agreement_var.get()), font=('Calibri', 12)).grid(row=3, pady=10)

def open_loan_application_form(loan_type, agreement):
    if not agreement:
        return  # Exit if the user did not agree to terms and conditions

    loan_application_screen = Toplevel(master)
    loan_application_screen.title(f'{loan_type} Loan Application')

    # Labels
    Label(loan_application_screen, text=f'{loan_type} Loan Application', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(loan_application_screen, text="Enter Details Below:", font=('Calibri', 12)).grid(row=1, column=0, columnspan=2, sticky=W, pady=5)

    # Entry Fields
    Label(loan_application_screen, text="Principal Amount:", font=('Calibri', 12)).grid(row=2, column=0, sticky=W)
    principal_entry = Entry(loan_application_screen, width=40)
    principal_entry.grid(row=2, column=1, sticky=W, pady=5)

    Label(loan_application_screen, text="Time Period (in years):", font=('Calibri', 12)).grid(row=3, column=0, sticky=W)
    time_period_entry = Entry(loan_application_screen, width=40)
    time_period_entry.grid(row=3, column=1, sticky=W, pady=5)

    # Add university field only for Education Loan
    if loan_type == "Education":
        Label(loan_application_screen, text="University/School Name:", font=('Calibri', 12)).grid(row=4, column=0, sticky=W)
        university_entry = Entry(loan_application_screen, width=40)
        university_entry.grid(row=4, column=1, sticky=W, pady=5)

    # Button to submit application
    Button(loan_application_screen, text="Submit", command=lambda: process_loan_application(loan_type, university_entry.get() if loan_type == "Education" else None, principal_entry.get(), time_period_entry.get()), font=('Calibri', 12)).grid(row=5, column=0, columnspan=2, pady=10)


def process_loan_application(loan_type, university, principal, time_period):
    try:
        principal_amount = float(principal)
        time_period_years = float(time_period)

        # Interest rates for different loan types
        interest_rate = get_interest_rate(loan_type)

        # Calculate final amount
        interest = principal_amount * interest_rate * time_period_years
        final_amount = principal_amount + interest

        # Display overview
        overview_screen = Toplevel(master)
        overview_screen.title('Loan Overview')

        Label(overview_screen, text="Loan Overview", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
        Label(overview_screen, text=f"Loan Type: {loan_type}", font=('Calibri', 12)).grid(row=1, sticky=W)
        Label(overview_screen, text=f"University/School Name: {university}", font=('Calibri', 12)).grid(row=2, sticky=W)
        Label(overview_screen, text=f"Principal Amount: Rs. {principal_amount}", font=('Calibri', 12)).grid(row=3, sticky=W)
        Label(overview_screen, text=f"Interest Rate: {interest_rate * 100}%", font=('Calibri', 12)).grid(row=4, sticky=W)
        Label(overview_screen, text=f"Time Period: {time_period_years} years", font=('Calibri', 12)).grid(row=5, sticky=W)
        Label(overview_screen, text=f"Total Amount to be Paid: Rs. {final_amount}", font=('Calibri', 12)).grid(row=6, sticky=W)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers for principal and time period.")

def get_loan_terms(loan_type):
    if loan_type == "Education":
        return "If the loan is not paid properly, we will contact your university and your degree will be on hold."
    elif loan_type == "Home":
        return "If the loan is not paid properly, we will seize your house."
    elif loan_type == "Personal":
        return "If the loan is not paid properly, all your belongings will be seized."
    else:
        return ""

def get_interest_rate(loan_type):
    if loan_type == "Education":
        return 0.06
    elif loan_type == "Home":
        return 0.07
    elif loan_type == "Personal":
        return 0.09
    else:
        return 0.0  # Default to 0 if loan type is invalid

# ... (your existing code)


#Image import
img = Image.open('secure.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "BANKLITE", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "The most simple bank you've probably used!", font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Register", font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
