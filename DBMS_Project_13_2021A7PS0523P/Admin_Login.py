import tkinter as tk  # Necessary Imports
import User_Mode_Page  # Included all pages that will be traversed in the GUI from this Page
import Dialogue_Box
import Admin_Dashboard
import Queries


class Admin_Login(tk.Frame):  # Main GUI Class
    def __init__(self, master):  # __init__Function with admin_id Parameter
        super().__init__(master)
        self.master = master  # Next few lines set up the GUI window size and title
        self.master.title("Login As Admin...")
        self.master.geometry("600x320")

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a Exit Button if User Wants to Exit
        self.exit_button = tk.Button(
            self.master, text="Exit", font=("Rockwell", 12, "bold"), command=self.Exit
        )
        # Exit Button Positioning
        self.exit_button.grid(row=1, column=0)

        # Back Button to Go to the Previous Active Page
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        # Back Button Positioning
        self.back_button.grid(row=0, column=0)

        # Submit Button to Verify Credentials Entered in Admin_Login Page
        self.submit_button = tk.Button(
            frame, text="Submit", font=("Rockwell", 14, "bold"), command=self.submit
        )
        # Submit Button Positioning
        self.submit_button.grid(row=4, column=2)

        # Admin_Mode Disclaimer
        self.admin_label = tk.Label(
            frame,
            text="Admin Mode",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Admin_Label Positioning
        self.admin_label.grid(row=0, column=0, padx=10, pady=10)

        # Next Few Labels and Text Fields help
        # make a User Friendly GUI to take
        # Admin_ID and Password for Login Purposes
        self.admin_ID_label = tk.Label(
            frame,
            text="Enter Admin-ID :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # Admin_ID_label Positioning
        self.admin_ID_label.grid(row=1, column=0, padx=10, pady=10)

        self.get_ID = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # Get_ID Text Field Positioning
        self.get_ID.grid(row=1, column=2, padx=10, pady=10)

        self.password_label = tk.Label(
            frame,
            text="Enter Password :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # Password Label Positioning
        self.password_label.grid(row=2, column=0, padx=10, pady=10)

        self.get_Password = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # get_Password Text Field Positioning
        self.get_Password.grid(row=2, column=2, padx=10, pady=10)

    # Submit Function helps us Check whether a
    # valid admin is trying to login by cross-checking
    # submitted User-ID and Password with the Values
    # in our database
    def submit(self):
        # Retrieving Admin_ID and Password Entered by
        # Potential Admin
        admin_id = self.get_ID.get("1.0", "end-1c")
        pwd = self.get_Password.get("1.0", "end-1c")
        # Confirming if Admin_ID is not null and
        # displaying a dialogue box if it is null
        # Prompting the user to enter a value
        if len(admin_id) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Voter-ID")
            return
        # Confirming if Password is not null and
        # displaying a dialogue box if it is null
        # Prompting the user to enter a value
        if len(pwd) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Password")
            return
        # Queries.admin_Login(admin_id,pwd) Checks
        # entered values with the values in our database
        result = Queries.admin_Login(admin_id, pwd)
        if result == -1: #Result = -1 corresponds to incorrect Credentials
            dialogue_box = tk.Toplevel(self.master)
            #Displaying a Dialogue Box for Invalid Credentials
            Dialogue_Box.Dialogue_Box(dialogue_box, "Invalid Credentials!!!")
        else:
            #Valid Credentials
            #Dialogue Box showing Login Successful
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Login Successful!")
            # Relevant Admin_Dashboard with appropriate admin_id is opened
            admin_dash_box = tk.Toplevel(self.master)
            Admin_Dashboard.Admin_Dashboard(admin_dash_box, admin_id)
            self.master.withdraw()

    # Command Executed by the Back Button
    # Leads to User_Mode_Page GUI Page
    def Back(self):
        user_mode_window = tk.Toplevel(self.master)
        User_Mode_Page.User_Mode_Page(user_mode_window)
        self.master.withdraw()

    # Command Executed by the Exit Button
    # Leads to Program Termination
    def Exit(self):
        self.destroy()
        self.master.quit()


# if __name__ == "__main__": Lines Used to Test Out the GUI
#     root = tk.Tk()
#     app = Admin_Login(master=root)
#     app.mainloop()
