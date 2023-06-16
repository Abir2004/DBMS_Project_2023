import tkinter as tk  # Necessary Imports
import tkinter.ttk as ttk
from datetime import date, datetime
import User_Mode_Page  # Included all pages that will be traversed in the GUI from this Page
import Dialogue_Box, Admin_Dashboard, Candidate_Votes
import Queries

# This Page is accessed by Admins


class Generate_Reports1(tk.Frame):  # Main GUI Class
    def __init__(self, master, admin_id):  # __init__Function with admin_id Parameter
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Elections List")
        self.master.geometry("1400x500")
        self.admin_id = admin_id

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Creating and Positioning a Logout Button if Admin Wants to Logout
        self.logout_button = tk.Button(
            self.master,
            text="Logout",
            font=("Rockwell", 12, "bold"),
            command=self.Logout,
        )
        self.logout_button.grid(row=0, column=0)

        # Creating and Positioning a Back Button if Admin Wants to Go Back to Previous Page
        self.back_button = tk.Button(
            self.master,
            text="Back",
            font=("Rockwell", 12, "bold"),
            command=self.Back,
        )
        self.back_button.grid(row=1, column=0)

        # Instruction for the Admin to ease Working
        self.cast_label = tk.Label(
            frame,
            text="To View Candidate-Wise Votes Double-Click on\nCorresponding Election Entry",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        # Instruction Placement
        self.cast_label.grid(row=1, column=0, padx=10, pady=10)

        # Making a treeview in Tkinter using styling,
        # to showcase all elections which have ever been scheduled
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

        self.tree = ttk.Treeview(frame, show=["headings"])
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
        for row in Queries.get_All_Elections():
            s1 = row[1].strftime("%d %B %Y")
            s2 = row[2].strftime("%d %B %Y")
            s4 = row[1].strftime("%Y/%m/%d")
            s5 = row[2].strftime("%Y/%m/%d")
            d = date.today()
            s3 = d.strftime("%Y/%m/%d")
            d1 = datetime.strptime(s4, "%Y/%m/%d")
            d2 = datetime.strptime(s3, "%Y/%m/%d")
            d3 = datetime.strptime(s5, "%Y/%m/%d")
            delta = d1 - d2
            delta2 = d3 - d2
            if delta2.days < 0:
                self.tree.insert(
                    "",
                    "end",
                    values=(row[0], row[3], s1, s2, "Voting Finished"),
                )
            elif delta.days <= 0:
                self.tree.insert(
                    "",
                    "end",
                    values=(row[0], row[3], s1, s2, "Voting in Progress"),
                )
            else:
                self.tree.insert(
                    "",
                    "end",
                    values=(row[0], row[3], s1, s2, "Voting Not Started"),
                )
            i += 1

        self.tree.grid(row=0, column=0)

        self.tree.bind("<Double-1>", self.on_click)
        # Treeview Ends

    # Defining Triggers for Double Clicks on any Election Entry
    def on_click(self, event):
        item = self.tree.focus()
        item_text = self.tree.item(item, "values")
        # Reports Generated only for Finished Elections
        if item_text[4] == "Voting Finished":
            # If double-clicked Candidate's of that Election pop up
            cand_window = tk.Toplevel(self.master)
            Candidate_Votes.Candidate_Votes(cand_window, self.admin_id, item_text[0])
            self.master.withdraw()
        elif item_text[4] == "Voting in Progress":
            dialogue = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue, "Election in Progress.\nCannot Generate Reports."
            )
        else:
            # Appropriate Dialogue Boxes
            dialogue = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue, "Election Has Not Started Yet.\nCannot Generate Reports."
            )

    # Bind the tree view to the on_click function

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
#     app = Generate_Reports1(root, 2)
#     app.mainloop()
