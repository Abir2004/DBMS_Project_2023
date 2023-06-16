import tkinter as tk  # Necessary Imports
import tkinter.ttk as ttk
import User_Mode_Page  # Included all pages that will be traversed in the GUI from this Page
import Dialogue_Box, Generate_Reports1, Candidate_Vote_Profile
import Queries


class Candidate_Votes(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, admin_id, elec_id
    ):  # __init__Function with multiple required Parameters to run queries on Database
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Candidate Wise Total Votes")
        self.master.geometry("1400x550")
        self.admin_id = admin_id
        self.elec_id = elec_id
        self.cand_id = None
        self.cand_name = None
        self.party = None

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
        # Button Positioning
        self.logout_button.grid(row=0, column=0)

        # Create and Position a Back Button if Admin Wants to Go Back to Previous Page
        self.back_button = tk.Button(
            self.master,
            text="Back",
            font=("Rockwell", 12, "bold"),
            command=self.Back,
        )
        self.back_button.grid(row=1, column=0)

        # Create and Position a Label to Showcase
        # Total Votes Casted, Query is used to
        # get data, Query in Queries.py
        self.cast_label = tk.Label(
            frame,
            text=f"Total Votes Casted in This Election are {Queries.get_Total_Votes(self.elec_id)}",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        self.cast_label.grid(row=0, column=0, padx=10, pady=10)

        # Create and Position a Label to Showcase
        # Winner of the Election, Query is used to
        # get data, Query in Queries.py
        self.winner_label = tk.Label(
            frame,
            text=f"Winner of this Election is {Queries.get_Winner(self.elec_id)[0]} from {Queries.get_Winner(self.elec_id)[1]}",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        self.winner_label.grid(row=1, column=0, padx=10, pady=10)

        self.cast2_label = tk.Label(
            frame,
            text="To View Candidate's Individual Performance\nDouble-Click on the Candidate",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.cast2_label.grid(row=8, column=0, padx=10, pady=10)

        # Making a treeview in Tkinter using styling,
        # to showcase all candidates in an election
        # For admin to generate a report from
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "Treeview",
            background="#CCCCCC",
            fieldbackground="#CCCCCC",
            font=("Rockwell", 16),
            rowheight=35,
            justify="center",
        )
        self.style.configure(
            "Treeview.Heading",
            font=("Rockwell", 16, "bold"),
        )

        self.tree = ttk.Treeview(frame)
        self.tree["columns"] = (
            "Candidate_ID",
            "Candidate_Name",
            "Party_Name",
        )
        self.tree.column("# 0", anchor=tk.CENTER, stretch=tk.NO, width=100)
        self.tree.column("# 1", anchor=tk.CENTER, stretch=tk.NO, width=150)
        self.tree.column("# 2", anchor=tk.CENTER, stretch=tk.NO, width=300)
        self.tree.column("# 3", anchor=tk.CENTER, stretch=tk.NO, width=300)

        self.tree.heading("#0", text="Rank")
        self.tree.heading("Candidate_ID", text="Candidate ID")
        self.tree.heading("Candidate_Name", text="Candidate Name")
        self.tree.heading("Party_Name", text="Party Name")

        i = 1
        for row in Queries.get_Ranks(self.elec_id):
            self.tree.insert(
                "",
                "end",
                text=i,
                values=(row[0], row[1], row[2]),
            )
            i += 1

        self.tree.grid(row=2, column=0)

        self.tree.bind("<Double-1>", self.on_click)
        # Treeview Ends

    # Defining Triggers for Double Clicks on any Candidate Entry
    def on_click(self, event):
        item = self.tree.focus()
        item_text = self.tree.item(item, "values")
        self.cand_id = item_text[0]
        self.cand_name = item_text[1]
        self.party = item_text[2]
        # If double-clicked Candidate's Vote Profile Opens up
        profile_window = tk.Toplevel(self.master)
        Candidate_Vote_Profile.Candidate_Vote_Profile(
            profile_window,
            self.admin_id,
            self.cand_id,
            self.elec_id,
            self.cand_name,
            self.party,
        )
        self.master.withdraw()

    # Bind the tree view to the on_click function

    # Command Executed by the Back Button
    # Leads to Generate_Reports1 GUI Page
    def Back(self):
        gen_window = tk.Toplevel(self.master)
        Generate_Reports1.Generate_Reports1(gen_window, self.admin_id)
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
#     app = Candidate_Votes(root, 1, 1)
#     app.mainloop()
