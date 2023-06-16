import tkinter as tk  # Necessary Imports
import Admin_Login  # Included all pages that will be traversed in the GUI from this Page
import Set_Elections
import Candidate_Register, Dialogue_Box, User_Mode_Page
import Generate_Reports1, Delete_Voters


class Admin_Dashboard(tk.Frame):  # Main GUI Class
    def __init__(self, master, admin_id):  # __init__Function with admin_id Parameter
        super().__init__(master)
        self.master = master  # Next few lines set up the GUI window size and title
        self.master.title("Admin Dashboard")
        self.master.geometry("550x500")
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
        self.logout_button.grid(row=0, column=0)  # Positioning the Logout Button

        # Back Button to Go to the Previous Active Page
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        self.back_button.grid(row=1, column=0)  # Positioning the Back Button

        # Admin_ID_Label Helps establish a Forefront Title for the Page, Welcome Message Shown
        self.admin_ID_label = tk.Label(
            frame,
            text=f"Welcome Admin {self.admin_id}",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        self.admin_ID_label.grid(
            row=0, column=0, padx=10, pady=10
        )  # Positioning the Welcome Label

        # create the buttons inside the frame
        # 4 Buttons Needed
        # First Button is the Set-Up Elections Button, which will allow Admin to Set-Up Elections
        self.set_up_elections_button = tk.Button(
            frame,
            text="Set Up Elections",
            command=self.Set_Up_Elections,
            padx=20,
            pady=20,
            bg="#CCCCCC",
            font=("Rockwell", 20, "bold"),
        )
        # Set-Up Election Button Positioning
        self.set_up_elections_button.grid(row=1, column=0, padx=10, pady=10)

        # Second Button Add_Candidates allows Admin to Add Candidates to Elections
        self.add_candidate_button = tk.Button(
            frame,
            text="Add Candidate",
            command=self.Add_Candidate,
            padx=20,
            pady=20,
            bg="#CCCCCC",
            font=("Rockwell", 20, "bold"),
        )
        # Add_Candidates Button Positioning
        self.add_candidate_button.grid(row=2, column=0, padx=10, pady=10)

        # Third Button Helps Admin Generate Vote Statistics and Candidate Vote Profiles
        self.vote_reports_button = tk.Button(
            frame,
            text="Generate Vote Reports",
            command=self.Gen_Report,
            padx=20,
            pady=20,
            bg="#CCCCCC",
            font=("Rockwell", 20, "bold"),
        )
        # Vote_Reports Button Positioning
        self.vote_reports_button.grid(row=3, column=0, padx=10, pady=10)

        # Fourth Button Helps Admin Delete Specific Voter Profiles
        self.del_voter_button = tk.Button(
            frame,
            text="Delete Voters",
            command=self.Delete_Voters,
            padx=20,
            pady=20,
            bg="#CCCCCC",
            font=("Rockwell", 20, "bold"),
        )
        # Del_Voter Button Positioning
        self.del_voter_button.grid(row=4, column=0, padx=10, pady=10)

    # Command Executed by the Set_Up_Elections Button
    # Leads to Set_Elections GUI Page
    def Set_Up_Elections(self):
        set_elec_window = tk.Toplevel(self.master)
        Set_Elections.Set_Elections(set_elec_window, self.admin_id)
        self.master.withdraw()

    # Command Executed by the Add_Candidates Button
    # Leads to Candidate_Register GUI Page
    def Add_Candidate(self):
        add_cand_window = tk.Toplevel(self.master)
        Candidate_Register.Candidate_Register(add_cand_window, self.admin_id)
        self.master.withdraw()

    # Command Executed by the Vote_Reports Button
    # Leads to Generate_Reports1 GUI Page
    def Gen_Report(self):
        gen_window = tk.Toplevel(self.master)
        Generate_Reports1.Generate_Reports1(gen_window, self.admin_id)
        self.master.withdraw()

    # Command Executed by the Add_Candidates Button
    # Leads to Candidate_Register GUI Page
    def Delete_Voters(self):
        del_window = tk.Toplevel(self.master)
        Delete_Voters.Delete_Voters(del_window, self.admin_id)
        self.master.withdraw()

    # Command Executed by the Back Button
    # Leads to Admin_Login GUI Page
    def Back(self):
        admin_login_window = tk.Toplevel(self.master)
        Admin_Login.Admin_Login(admin_login_window)
        self.master.withdraw()

    # Command Executed by the Logout Button
    # Leads to User_Mode_Page GUI Page
    def Logout(self):
        dialogue_box = tk.Toplevel(self.master)
        Dialogue_Box.Dialogue_Box(dialogue_box, "Logout Successful")
        user_window = tk.Toplevel(self.master)
        User_Mode_Page.User_Mode_Page(user_window)
        self.master.withdraw()


if __name__ == "__main__":  # Lines Used to Test Out the GUI
    root = tk.Tk()
    app = Admin_Dashboard(root, 1)
    app.mainloop()
