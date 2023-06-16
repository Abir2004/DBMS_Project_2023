import tkinter as tk  # Necessary Imports
import Voter_Login  # Included all pages that will be traversed in the GUI from this Page
import Register_Confirmation_Box
import Dialogue_Box

#This Page is accessed by Voters

class Voter_Register(tk.Frame): #Main GUI Class
    def __init__(self, master): # __init__Function
        super().__init__(master)
        self.master = master   # Next few lines set up the GUI window size and title, attributes
        self.master.title("Register Voter")
        self.master.geometry("1100x640")

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

        # Creating and Positioning a Register Button for Voters
        self.register_button = tk.Button(
            frame, text="Register", font=("Rockwell", 16, "bold"), command=self.register
        )
        self.register_button.grid(row=8, column=1)

        # Welcome Message for the Voter
        self.welcome_label = tk.Label(
            frame,
            text="Voter Registration",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        self.welcome_label.grid(row=0, column=1, padx=10, pady=10)

        # Taking all necessary information from Voter through Labels and Text Fields for Registration
        self.password_label = tk.Label(
            frame,
            text="Enter Preferred Password :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

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

        self.get_Password.grid(row=1, column=2, padx=10, pady=10)

        self.name_label = tk.Label(
            frame,
            text="Enter Your Name :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.name_label.grid(row=2, column=0, padx=10, pady=10)

        self.get_Name = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Name.grid(row=2, column=2, padx=10, pady=10)

        self.email_label = tk.Label(
            frame,
            text="Enter Your Email :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.email_label.grid(row=3, column=0, padx=10, pady=10)

        self.get_Email = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Email.grid(row=3, column=2, padx=10, pady=10)

        self.phone_label = tk.Label(
            frame,
            text="Enter Your Phone Number :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.phone_label.grid(row=4, column=0, padx=10, pady=10)

        self.get_Phone = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Phone.grid(row=4, column=2, padx=10, pady=10)

        self.address_label = tk.Label(
            frame,
            text="Enter Your Address :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.address_label.grid(row=5, column=0, padx=10, pady=10)

        self.get_Address = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Address.grid(row=5, column=2, padx=10, pady=10)

        self.dob_label = tk.Label(
            frame,
            text="Enter Your Date of Birth (YYYY-MM-DD) :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.dob_label.grid(row=6, column=0, padx=10, pady=10)

        self.get_DOB = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_DOB.grid(row=6, column=2, padx=10, pady=10)

        # Disclaimer for Voter, so he doesn't register twice
        self.disc_label = tk.Label(
            frame,
            text="If already registered, Press Back and Login.",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.disc_label.grid(row=10, column=1, padx=10, pady=10)

    # Register function called by the Register Button, does some precalculation of data entered
    # and sends it for further processing
    def register(self):
        # Retrieving Information Entered by Voter
        pwd = self.get_Password.get("1.0", "end-1c")
        name = self.get_Name.get("1.0", "end-1c")
        email = self.get_Email.get("1.0", "end-1c")
        phone = self.get_Phone.get("1.0", "end-1c")
        address = self.get_Address.get("1.0", "end-1c")
        dob = self.get_DOB.get("1.0", "end-1c")
        # Check if all Field are Not Empty
        if len(name) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Your Name")
            return
        if len(pwd) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Password")
            return
        if len(email) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Your Email")
            return
        if len(phone) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Phone Number")
            return
        if len(address) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Your Address")
            return
        if len(dob) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Date of Birth")
            return
        # Passing it on to Register_Confirmation_Box
        reg_confirm_window = tk.Toplevel(self.master)
        Register_Confirmation_Box.Register_Confirmation_Box(
            reg_confirm_window,
            "Are these details \nto the best of \nyour knowledge?",
            pwd,
            name,
            email,
            address,
            phone,
            dob,
        )
        # Register_Confirmation_Box takes all parameters and processes it further for registration

    # Command Executed by the Back Button
    # Leads to Voter_Login GUI Page
    def Back(self):
        voter_login_window = tk.Toplevel(self.master)
        Voter_Login.Voter_Login(voter_login_window)
        self.master.withdraw()

    # Command Executed by the Exit Button
    # Leads to Program Termination
    def Exit(self):
        self.destroy()
        self.master.quit()


if __name__ == "__main__": #Lines Used to Test Out the GUI
    root = tk.Tk()
    app = Voter_Register(master=root)
    app.mainloop()
