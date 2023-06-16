import tkinter as tk  # Necessary Imports
import Dialogue_Box  # Included all pages that will be traversed in the GUI from this Page
import Queries
import Voter_Dashboard


class Confirm_Vote(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, voter_id, cand_id, elec_id
    ):  # __init__Function with multiple required Parameters to run queries on Database
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Confirmation")
        self.master.geometry("900x200")
        self.voter_id = voter_id
        self.cand_id = cand_id
        self.elec_id = elec_id

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create and Positioning a Label which
        # Asks Confirmation from Voter to Cast Vote
        self.message_label = tk.Label(
            frame,
            text="Are You Sure You want to Vote For this Candidate?\nActions Cannot be Undone.",
            padx=0,
            pady=0,
            bg="#FFFFFF",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        self.message_label.grid(row=0, column=1, padx=10, pady=10)

        # Button YES to Cast Vote
        self.yes_button = tk.Button(
            frame, text="YES", font=("Rockwell", 16, "bold"), command=self.Yes
        )
        self.yes_button.grid(row=2, column=0)

        # Button NO to not Cast Vote
        self.no_button = tk.Button(
            frame, text="NO", font=("Rockwell", 16, "bold"), command=self.No
        )
        self.no_button.grid(row=2, column=2)

        # create the buttons inside the frame

    # Function run by YES Button
    def Yes(self):
        x = Queries.add_Vote(
            self.voter_id, self.cand_id, self.elec_id
        )  # Query to Add Vote to Vote Table, Query in Queries.py
        if x == -1:  # X = -1 means Person has already Voted
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "You have Already Voted!!!")
        else:
            # Appropriate Dialogue Boxes
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Vote Casted")
            # After Casting Vote Redirects to Dashboard
            voter_dash = tk.Toplevel(self.master)
            Voter_Dashboard.Voter_Dashboard(voter_dash, self.voter_id)
        self.master.withdraw()

    # Function run by NO button
    def No(self):
        self.master.withdraw()


# if __name__ == "__main__": Lines Used to Test Out the GUI
#     root = tk.Tk()
#     app = Confirm_Vote(root, "912412", "912412", "912412")
#     app.mainloop()
