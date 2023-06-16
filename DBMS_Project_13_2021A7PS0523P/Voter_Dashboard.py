import tkinter as tk  # Necessary Imports
import tkinter.ttk as ttk
from datetime import (
    date,
    datetime,
)  # Included all pages that will be traversed in the GUI from this Page
import Voter_Login
import Dialogue_Box, See_Candidates, Profile_Edits
import Queries


class Voter_Dashboard(tk.Frame):  # Main GUI Class
    def __init__(self, master, voter_id):  # __init__Function with voter_id Parameter
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Voter Dashboard")
        self.master.geometry("1400x600")
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

        # Creating and Positioning an Edit/Delete Button if Voter Wants to Update/Delete their profile
        self.edit_profile_button = tk.Button(
            self.master,
            text="Edit/Delete Profile",
            font=("Rockwell", 12, "bold"),
            command=self.Edit,
        )
        self.edit_profile_button.grid(row=1, column=0)

        # Welcome labels which look good in the GUI
        self.voter_ID_label = tk.Label(
            frame,
            text=f"Welcome Voter {self.voter_id}",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        self.voter_ID_label.grid(row=0, column=0, padx=10, pady=10)

        # Setup for a treeview of elections for voters.
        self.cast_label = tk.Label(
            frame,
            text="To View Candidates Double-Click on\nCorresponding Election Entry",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # Label Positioning
        self.cast_label.grid(row=2, column=0, padx=10, pady=10)

        # Making a treeview in Tkinter using styling,
        # to showcase all elections which are ongoing or which
        # scheduled in the future
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

        self.tree = ttk.Treeview(frame, show="headings")
        self.tree["columns"] = (
            "Election_ID",
            "Election_Title",
            "Election_Start_Date",
            "Election_End_Date",
            "Voting_Status",
        )
        self.tree.column("# 1", anchor=tk.CENTER, stretch=tk.NO, width=100)
        self.tree.column("# 2", anchor=tk.CENTER, stretch=tk.NO, width=300)
        self.tree.column("# 3", anchor=tk.CENTER, stretch=tk.NO, width=300)
        self.tree.column("# 4", anchor=tk.CENTER, stretch=tk.NO, width=300)
        self.tree.column("# 5", anchor=tk.CENTER, stretch=tk.NO, width=300)

        self.tree.heading("Election_ID", text="Election ID")
        self.tree.heading("Election_Title", text="Election Title")
        self.tree.heading("Election_Start_Date", text="Voting Begins On")
        self.tree.heading("Election_End_Date", text="Voting Ends On")
        self.tree.heading("Voting_Status", text="Voting Status")

        i = 1
        for row in Queries.get_Elections():
            s1 = row[1].strftime("%d %B %Y")
            s2 = row[2].strftime("%d %B %Y")
            s4 = row[1].strftime("%Y/%m/%d")
            d = date.today()
            s3 = d.strftime("%Y/%m/%d")
            d1 = datetime.strptime(s4, "%Y/%m/%d")
            d2 = datetime.strptime(s3, "%Y/%m/%d")
            delta = d1 - d2
            if delta.days > 0:
                self.tree.insert(
                    "",
                    "end",
                    values=(row[0], row[3], s1, s2, "Voting Yet To Start"),
                )
            else:
                self.tree.insert(
                    "",
                    "end",
                    values=(row[0], row[3], s1, s2, "Voting Started"),
                )
            i += 1

        self.tree.grid(row=1, column=0)

        self.tree.bind("<Double-1>", self.on_click)
        # End of TreeView

    # Defining Triggers for Double Clicks on any Election Entry
    def on_click(self, event):
        item = self.tree.focus()
        item_text = self.tree.item(item, "values")
        # If you double-click on an election, you will be able to see the
        # list of candidates participating
        if item_text[4] == "Voting Started":
            cand_window = tk.Toplevel(self.master)
            See_Candidates.See_Candidates(cand_window, self.voter_id, item_text[0], 1)
            self.master.withdraw()
        else:
            cand_window = tk.Toplevel(self.master)
            See_Candidates.See_Candidates(cand_window, self.voter_id, item_text[0], 0)
            self.master.withdraw()
            # Appropriate windows made

    # Bind the tree view to the on_click function

    # Command Executed by the Edit/Delete Button
    # Leads to Profile_Edits GUI Page
    def Edit(self):
        edits_window = tk.Toplevel(self.master)
        Profile_Edits.Profile_Edits(edits_window, self.voter_id)
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
#     app = Voter_Dashboard(master=root, voter_id=5)
#     app.mainloop()
