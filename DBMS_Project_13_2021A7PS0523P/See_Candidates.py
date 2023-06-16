import tkinter as tk  # Necessary Imports
import tkinter.ttk as ttk
import Dialogue_Box  # Included all pages that will be traversed in the GUI from this Page
import Voter_Dashboard, Confirm_Vote
import User_Mode_Page
import Queries

# This Page is made for Voters


class See_Candidates(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, voter_id, elec_id, status
    ):  # __init__Function with multiple parameters
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Candidates Standing Up")
        self.master.geometry("1000x600")
        self.voter_id = voter_id
        self.elec_id = elec_id
        self.cand_id = None
        self.status = status

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

        # Creating and Positioning a Cast Button if Voter Wants to Cast a Vote to a Candidate
        self.cast_button = tk.Button(
            frame,
            text="Cast Vote",
            font=("Rockwell", 20, "bold"),
            command=self.Cast_Vote,
        )
        self.cast_button.grid(row=2, column=0)

        # Setup for a treeview of elections for voters.
        self.win_label = tk.Label(
            frame,
            text="Candidates Standing in the Election",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        # Label_Positioning
        self.win_label.grid(row=0, column=0, padx=10, pady=10)

        # Making a treeview in Tkinter using styling,
        # to showcase all candidates who are standing in the
        # election being viewed
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "Treeview",
            background="#CCCCCC",
            fieldbackground="#CCCCCC",
            font=("Rockwell", 16),
            rowheight=30,
            justify="center",
        )
        self.style.configure(
            "Treeview.Heading",
            font=("Rockwell", 16, "bold"),
        )

        self.tree = ttk.Treeview(frame)
        self.tree["columns"] = ("Candidate_ID", "Name", "Party_Name")
        self.tree.column("# 0", anchor=tk.CENTER, stretch=tk.NO, width=100)
        self.tree.column("# 1", anchor=tk.CENTER, stretch=tk.NO, width=150)
        self.tree.column("# 2", anchor=tk.CENTER, stretch=tk.NO, width=300)
        self.tree.column("# 3", anchor=tk.CENTER, stretch=tk.NO, width=300)

        self.tree.heading("#0", text="Serial No.")
        self.tree.heading("Candidate_ID", text="Candidate ID")
        self.tree.heading("Name", text="Candidate Name")
        self.tree.heading("Party_Name", text="Party")

        i = 1
        for row in Queries.get_Candidates(self.elec_id):
            self.tree.insert(
                "",
                "end",
                text=i,
                values=(row[0], row[1], row[2]),
            )
            i += 1

        self.tree.grid(row=1, column=0)

        self.tree.bind("<ButtonRelease-1>", self.on_click)
        # End of TreeView

    # Defining Triggers for Clicks on any Candidate
    # Helps Selecting the Candidate who the Voter wants to Vote For
    def on_click(self, event):
        item = self.tree.focus()
        item_text = self.tree.item(item, "values")
        self.cand_id = item_text[0]

    # Function Implemented by the Cast Button
    def Cast_Vote(self):
        # Status is 1 when Elections are ongoing
        # First Check if Elections have started or not
        # Also check whether Voter has selected a candidate
        # Show appropriate dialogue boxes for the cases
        if self.status == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Voting has not started!!!")
            return
        if self.cand_id == None:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "No Candidate Selected!!!")
            return
        # Confirm_Vote takes values fo Voter_id, Candidate_ID and Elec_ID
        # and Casts the Vote after running a few more checks
        vote_window = tk.Toplevel(self.master)
        Confirm_Vote.Confirm_Vote(
            vote_window, self.voter_id, self.cand_id, self.elec_id
        )
        # Vote Casted

    # Command Executed by the Back Button
    # Leads to Voter_Dashboard GUI Page
    def Back(self):
        voter_dash_window = tk.Toplevel(self.master)
        Voter_Dashboard.Voter_Dashboard(voter_dash_window, self.voter_id)
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
#     app = See_Candidates(root, 1, 11, 0)
#     app.mainloop()
