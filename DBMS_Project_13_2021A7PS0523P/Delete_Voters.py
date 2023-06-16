import tkinter as tk  # Necessary Imports
import Admin_Login  # Included all pages that will be traversed in the GUI from this Page
import Admin_Dashboard, Dialogue_Box, User_Mode_Page
import Queries

# This Page is accessed by Voters


class Delete_Voters(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, voter_id
    ):  # __init__Function with multiple required Parameters to run queries on Database
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Edit Voter Profile")
        self.master.geometry("600x400")
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

        # Creating and Positioning a Delete Button so Admins Can Delete Voter Profiles
        self.delete_button = tk.Button(
            frame,
            text="Delete Profile",
            font=("Rockwell", 16, "bold"),
            command=self.Delete,
        )
        self.delete_button.grid(row=3, column=0, pady=5)

        # Next Few Labels and Text Fields help
        # make a User Friendly GUI to get
        # Voter-ID to delete
        self.win_label = tk.Label(
            frame,
            text=f"Delete Voters",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        self.win_label.grid(row=0, column=0, padx=10, pady=10)

        self.voter_id_label = tk.Label(
            frame,
            text="Enter Voter-ID to Delete :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.voter_id_label.grid(row=1, column=0, padx=10, pady=10)

        self.get_Voter_ID = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Voter_ID.grid(row=1, column=2, padx=10, pady=10)

    # Command Executed by the Back Button
    # Leads to Voter_Dashboard GUI Page
    def Back(self):
        admin_dash_window = tk.Toplevel(self.master)
        Admin_Dashboard.Admin_Dashboard(admin_dash_window, self.voter_id)
        self.master.withdraw()

    # Function Implememnted by the Delete Function
    # Deletes the Profile of the specific voter and all its votes as well
    def Delete(self):
        vid = self.get_Voter_ID.get("1.0", "end-1c")
        if len(vid) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter a Voter-ID")
            return
        Queries.delete_Voter(vid)
        dialogue_box = tk.Toplevel(self.master)
        Dialogue_Box.Dialogue_Box(dialogue_box, "Profile Deleted")
        admin_dash_window = tk.Toplevel(self.master)
        Admin_Dashboard.Admin_Dashboard(admin_dash_window, self.voter_id)
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
#     app = Profile_Edits(root, 4)
#     app.mainloop()
