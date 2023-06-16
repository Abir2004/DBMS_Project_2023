import tkinter as tk  # Necessary Imports
import User_Mode_Page  # Included all pages that will be traversed in the GUI from this Page
import Admin_Dashboard
import Dialogue_Box
import Queries


class Candidate_Register(tk.Frame):  # Main GUI Class
    def __init__(self, master, admin_id):  # __init__Function with admin_id Parameter
        super().__init__(master)
        self.master = master  # Next few lines set up the GUI window size and title
        self.master.title("Register Candidate")
        self.master.geometry("1000x400")
        self.admin_id = admin_id

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a Logout Button if Admin Wants to Logout
        self.logout_button = tk.Button(
            self.master,
            text="Logout",
            font=("Rockwell", 12, "bold"),
            command=self.Logout,
        )
        # Logout Button Positioning
        self.logout_button.grid(row=0, column=0)

        # Back Button to Go to the Previous Active Page
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        # Back Button Positioning
        self.back_button.grid(row=1, column=0)

        # Register Button to Go to the Register New Candidates
        self.register_button = tk.Button(
            frame, text="Register", font=("Rockwell", 16, "bold"), command=self.register
        )
        # Register_Button Positioning
        self.register_button.grid(row=8, column=2)

        # Win_Label presents function of the Page
        self.win_label = tk.Label(
            frame,
            text="Add Candidates",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # win_label Positioning
        self.win_label.grid(row=0, column=0, padx=10, pady=10)

        # Next Few Labels and Text Fields help
        # make a User Friendly GUI to take
        # Necessary Details for Candidate Registration
        self.name_label = tk.Label(
            frame,
            text="Enter the Candidate's Name :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # name_label Positioning
        self.name_label.grid(row=1, column=0, padx=10, pady=10)

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
        # get_Name Text Field Positioning
        self.get_Name.grid(row=1, column=2, padx=10, pady=10)

        self.dob_label = tk.Label(
            frame,
            text="Enter the Candidate's Date of Birth (YYYY-MM-DD) :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # dob_label Positioning
        self.dob_label.grid(row=2, column=0, padx=10, pady=10)

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
        # get_DOB Text Field Positioning
        self.get_DOB.grid(row=2, column=2, padx=10, pady=10)

        self.party_label = tk.Label(
            frame,
            text="Enter Candidate's Party :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # party_label Positioning
        self.party_label.grid(row=3, column=0, padx=10, pady=10)

        self.get_Party = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # get_Party Text Field Positioning
        self.get_Party.grid(row=3, column=2, padx=10, pady=10)

        self.elec_label = tk.Label(
            frame,
            text="Enter Election-ID for the Candidate :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # elec_label Positioning
        self.elec_label.grid(row=4, column=0, padx=10, pady=10)

        self.get_Elec = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # get_Elec Text Field Positioning
        self.get_Elec.grid(row=4, column=2, padx=10, pady=10)

    # Register Function takes the Values entered
    # into the Text Fields by the Admin and
    # Registers the Candidate for the Given Election
    # To ensure no candidate is registered twice,
    # SQL Backend and Python Scripts in Queries.py are Used
    def register(self):
        # Retrieving Information Entered by Admin
        name = self.get_Name.get("1.0", "end-1c")
        party = self.get_Party.get("1.0", "end-1c")
        elec = self.get_Elec.get("1.0", "end-1c")
        dob = self.get_DOB.get("1.0", "end-1c")
        # Confirming if name is not null and
        # displaying a dialogue box if it is null
        # Prompting the user to enter a value
        if len(name) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Candidate Name")
            return
        # Confirming if party is not null and
        # displaying a dialogue box if it is null
        # Prompting the user to enter a value
        if len(party) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Party Name")
            return
        # Confirming if Elec_ID is not null and
        # displaying a dialogue box if it is null
        # Prompting the user to enter a value
        if len(elec) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Election-ID")
            return
        # Confirming if DOB is not null and
        # displaying a dialogue box if it is null
        # Prompting the user to enter a value
        if len(dob) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Date of Birth")
            return
        l = dob.split("-")
        if len(l) != 3:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election Start Date in Invalid Format!!!"
            )
            return
        # Next few lines test if DOB is in correct
        # required format
        if len(l[0]) != 4 or len(l[1]) != 2 or len(l[2]) != 2:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election Start Date in Invalid Format!!!"
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
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date of Birth in Invalid Format!!!"
            )
            return
        # DOB Format Verified and Dialogue Boxes shown appropriately
        x = Queries.add_Candidate(name, dob, party, self.admin_id, elec)
        if x == -1:  # X is -1 when Candidate is a Minor
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Candidate Not Eligible to Stand for Elections!!!"
            )
        else:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Candidate Added to Elections")
            # Appropriate Dialogue Boxes Shown
            # Candidate Registered

    # Command Executed by the Back Button
    # Leads to Admin_Dashboard GUI Page
    def Back(self):
        admin_dash_window = tk.Toplevel(self.master)
        Admin_Dashboard.Admin_Dashboard(admin_dash_window, self.admin_id)
        self.master.withdraw()

    # Command Executed by the Logout Button
    # Leads to User_Mode_Page GUI Page
    def Logout(self):
        dialogue_box = tk.Toplevel(self.master)
        Dialogue_Box.Dialogue_Box(dialogue_box, "Logout Successful")
        user_window = tk.Toplevel(self.master)
        User_Mode_Page.User_Mode_Page(user_window)
        self.master.withdraw()


# if __name__ == "__main__": Lines Used to Test Out the GUI
#     root = tk.Tk()
#     app = Candidate_Register(root, 1)
#     app.mainloop()
