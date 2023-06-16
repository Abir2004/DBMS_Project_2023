import tkinter as tk  # Necessary Imports
import Candidate_Votes, User_Mode_Page
import Dialogue_Box  # Included all pages that will be traversed in the GUI from this Page
import Queries


class Candidate_Vote_Profile(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, admin_id, cand_id, elec_id, name, party
    ):  # __init__Function with multiple required Parameters to run queries on Database
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Register Voter")
        self.master.geometry("1400x330")
        self.admin_id = admin_id
        self.cand_id = cand_id
        self.elec_id = elec_id
        self.name = name
        self.party = party

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

        # Create a Back Button if Admin Wants to Go Back to previous Page
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        # Back Button Positioning
        self.back_button.grid(row=1, column=0)

        # Next Few Labels Help in Giving
        # Details about Candidate's Performance in
        # This particular election. Generating Reports
        self.elec_title_label = tk.Label(
            frame,
            text=f"{Queries.get_Election_Title(self.elec_id)} Candidate Report",  # Query to Get Election Title for Display, Query in Queries.py
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Label Positioning
        self.elec_title_label.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(
            frame,
            text=f"Candidate Name : {self.name}",  # Query to Get Candidate Name, Query in Queries.py
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Label Positioning
        self.name_label.grid(row=1, column=0, padx=10, pady=10)

        self.party_label = tk.Label(
            frame,
            text=f"Candidate's Party : {self.party}",  # Query to Get Party Name, Query in Queries.py
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Label Positioning
        self.party_label.grid(row=1, column=2, padx=10, pady=10)

        self.votes_label = tk.Label(
            frame,
            text=f"Candidate Received {Queries.get_Vote(self.cand_id,self.elec_id)} Votes",  # Query to Get Votes Received by the Candidate, Query in Queries.py
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Label Positioning
        self.votes_label.grid(row=2, column=1, padx=10, pady=10)

        self.vote_percent_label = tk.Label(
            frame,
            text=f"Vote Percentage is {Queries.get_Vote_Percentage(self.cand_id,self.elec_id)}% of the Total Votes",  # Query to Get Votes Received by the Candidate in Percentage, Query in Queries.py
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Label Positioning
        self.vote_percent_label.grid(row=3, column=1, padx=10, pady=10)

    # Command Executed by the Back Button
    # Leads to Admin_Dashboard GUI Page
    def Back(self):
        cand_votes_window = tk.Toplevel(self.master)
        Candidate_Votes.Candidate_Votes(cand_votes_window, self.admin_id, self.elec_id)
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
#     app = Candidate_Vote_Profile(master=root)
#     app.mainloop()
