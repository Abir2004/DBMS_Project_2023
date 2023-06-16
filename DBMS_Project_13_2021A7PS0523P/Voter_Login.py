import tkinter as tk  # Necessary Imports
import User_Mode_Page  # Included all pages that will be traversed in the GUI from this Page
import Dialogue_Box
import Voter_Register, Voter_Dashboard
import Queries


class Voter_Login(tk.Frame):  # Main GUI Class
    def __init__(self, master):  # __init__Function
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Login As Voter...")
        self.master.geometry("700x350")

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Creating and Positioning an Exit Button if Voter Wants to Exit the Program
        self.exit_button = tk.Button(
            self.master, text="Exit", font=("Rockwell", 12, "bold"), command=self.Exit
        )
        self.exit_button.grid(row=1, column=0)

        # Creating and Positioning a Back Button if Voter Wants to Go Back to Previous Page
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        self.back_button.grid(row=0, column=0)

        # Creating and Positioning a Login Button for Voters
        self.login_button = tk.Button(
            frame, text="Login", font=("Rockwell", 16, "bold"), command=self.login
        )
        self.login_button.grid(row=4, column=2)

        # Creating and Positioning a Register Button for New Voters who want to Vote
        self.register_button = tk.Button(
            frame,
            text="Don't have credentials?\nRegister now and get your Voter-ID",
            font=("Rockwell", 16, "bold"),
            command=self.Register,
        )
        self.register_button.grid(row=0, column=0)

        # Window Label, Disclaimer to Voter
        self.voter_label = tk.Label(
            frame,
            text="Voter Mode",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        self.voter_label.grid(row=0, column=2, padx=10, pady=10)

        # Next 2 labels and Text Fields take the
        # Input of Voter_Id and Password
        self.voter_ID_label = tk.Label(
            frame,
            text="Enter Voter-ID :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.voter_ID_label.grid(row=1, column=0, padx=10, pady=10)

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

        self.get_Password.grid(row=2, column=2, padx=10, pady=10)

    # Login Function Implemented by the Login_Button
    def login(self):
        # Retrieving Data Entered by Voters
        voter_id = self.get_ID.get("1.0", "end-1c")
        pwd = self.get_Password.get("1.0", "end-1c")
        #Checking whether all Values are not empty
        if len(voter_id) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Voter-ID")
            return
        if len(pwd) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Password")
            return
        #Result is the voter_login query, Query can be found in Queries.py
        result = Queries.voter_Login(voter_id, pwd)
        if result == -1: #Result = -1 indicates wrong credentials
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Invalid Credentials!!!")
        else:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Login Successful!")
            #Appropriate Dialogue Boxes shown in both cases
            dashboard = tk.Toplevel(self.master)
            Voter_Dashboard.Voter_Dashboard(dashboard, voter_id)
            self.master.withdraw()
            #Voter Dashboard is accessed if voter successfully logs in.

    # Function Implemented by the Register_Button
    # Open the Voter Registration Page using tkinter
    def Register(self):
        voter_reg_window = tk.Toplevel(self.master)
        Voter_Register.Voter_Register(voter_reg_window)
        self.master.withdraw()

    # Command Executed by the Back Button
    # Leads to Voter_Login GUI Page
    def Back(self):
        user_mode_window = tk.Toplevel(self.master)
        User_Mode_Page.User_Mode_Page(user_mode_window)
        self.master.withdraw()

    # Command Executed by the Exit Button
    # Leads to Program Termination
    def Exit(self):
        self.destroy()
        self.master.destroy()


# if __name__ == "__main__": Lines Used to Test Out the GUI
#     root = tk.Tk()
#     app = Voter_Login(master=root)
#     app.mainloop()
