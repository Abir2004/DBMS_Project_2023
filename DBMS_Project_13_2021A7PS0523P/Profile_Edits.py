import tkinter as tk  # Necessary Imports
import Voter_Login  # Included all pages that will be traversed in the GUI from this Page
import Voter_Dashboard, Dialogue_Box
import Queries

# This Page is accessed by Voters


class Profile_Edits(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, voter_id
    ):  # __init__Function with multiple required Parameters to run queries on Database
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Edit Voter Profile")
        self.master.geometry("1000x550")
        self.voter_id = voter_id

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Creating and Positioning a Logout Button if Voter Wants to Logout
        self.logout_button = tk.Button(
            self.master,
            text="Logout",
            font=("Rockwell", 12, "bold"),
            command=self.Logout,
        )
        self.logout_button.grid(row=0, column=0)

        # Creating and Positioning a Back Button if Voter Wants to Go Back to Previous Page
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        self.back_button.grid(row=1, column=0)

        # Creating and Positioning an Update Button so Voters Can Update their profiles
        self.update_button = tk.Button(
            frame,
            text="Update Profile",
            font=("Rockwell", 16, "bold"),
            command=self.Update,
        )
        self.update_button.grid(row=8, column=2)

        # Creating and Positioning a Delete Button so Voters Can Delete their profiles
        self.delete_button = tk.Button(
            frame,
            text="Delete Profile",
            font=("Rockwell", 16, "bold"),
            command=self.Delete,
        )
        self.delete_button.grid(row=8, column=0, pady=5)

        # Next Few Labels and Text Fields help
        # make a User Friendly GUI to Display
        # Necessary Information about the Voter
        self.win_label = tk.Label(
            frame,
            text=f"Profile Details of Voter {self.voter_id}",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        self.win_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_label = tk.Label(
            frame,
            text="Password :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # self.l will contain all details of the Voter with a given Voter_ID
        self.l = Queries.get_Voter_Details(self.voter_id)

        #Taking all necessary information from Voter through Labels and Text Fields
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
        self.get_Password.insert("end-1c", self.l[1])

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
        self.get_Name.insert("end-1c", self.l[2])

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
        self.get_Email.insert("end-1c", self.l[3])

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
        self.get_Phone.insert("end-1c", self.l[5])

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
        self.get_Address.insert("end-1c", self.l[4])

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
        self.get_DOB.insert("end-1c", self.l[6])
        # End of Profile Details

    # Function implemented by the Update Button
    def Update(self):
        # Retrieve All Relevant Info
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
        # Check if it is a valid phone number
        if len(phone) != 10:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Invalid Phone Number!!!")
        # Next few statements analyse the correctness of the date
        l = dob.split("-")
        if len(l) != 3:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth in Invalid Format!!!"
            )
        if len(l[0]) != 4 or len(l[1]) != 2 or len(l[2]) != 2:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth in Invalid Format!!!"
            )
            return
        can = True
        for i in l[0]:
            if not (48 <= ord(i) <= 57):
                can = False
        for i in l[1]:
            if not (48 <= ord(i) <= 57):
                can = False
        if not (1 <= int(l[1]) <= 12):
            can = False
        if not (1 <= int(l[2]) <= 31):
            can = False
        for i in l[2]:
            if not (48 <= ord(i) <= 57):
                can = False
        if not can:
            #Date is in incorrect format, will be reported
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth in Invalid Format!!!"
            )
            return
        #Queries.update_Voter updates Voter table 
        # with the new details about the voter
        result = Queries.update_Voter(
            self.voter_id, pwd, name, email, address, phone, dob
        )
        if result == -1:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth in Invalid Format!!!"
            )
        else:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Profile Updated!")
            #Profile Successfully Updated

    # Command Executed by the Back Button
    # Leads to Voter_Dashboard GUI Page
    def Back(self):
        voter_dash_window = tk.Toplevel(self.master)
        Voter_Dashboard.Voter_Dashboard(voter_dash_window, self.voter_id)
        self.master.withdraw()

    #Function Implememnted by the Delete Function
    #Deletes the Profile of the specific voter and all its votes as well
    def Delete(self):
        Queries.delete_Voter(self.voter_id)
        dialogue_box = tk.Toplevel(self.master)
        Dialogue_Box.Dialogue_Box(dialogue_box, "Profile Deleted")
        voter_login_window = tk.Toplevel(self.master)
        Voter_Login.Voter_Login(voter_login_window)
        self.master.withdraw()

    # Command Executed by the Logout Button
    # Leads to User_Mode_Page GUI Page
    def Logout(self):
        dialogue_box = tk.Toplevel(self.master)
        Dialogue_Box.Dialogue_Box(dialogue_box, "Logout Successful")
        voter_login_window = tk.Toplevel(self.master)
        Voter_Login.Voter_Login(voter_login_window)
        self.master.withdraw()


# if __name__ == "__main__": Lines Used to Test Out the GUI
#     root = tk.Tk()
#     app = Profile_Edits(root, 4)
#     app.mainloop()
