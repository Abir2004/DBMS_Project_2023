import tkinter as tk  # Necessary Imports
import Admin_Dashboard  # Included all pages that will be traversed in the GUI from this Page
import User_Mode_Page
import Dialogue_Box
import Queries

# This Window is for Admins


class Set_Elections(tk.Frame):  # Main GUI Class
    def __init__(self, master, admin_id):  # __init__Function with admin_id parameter
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Set Up Elections")
        self.master.geometry("1100x500")
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

        # Creating and Positioning an Edit/Delete Button if Admin Wants to Update/Delete their profile
        self.back_button = tk.Button(
            self.master, text="Back", font=("Rockwell", 12, "bold"), command=self.Back
        )
        self.back_button.grid(row=1, column=0)

        # Creating and Positioning a Setup Button for Admins to watch elections
        self.setup_button = tk.Button(
            frame, text="Set Up", font=("Rockwell", 16, "bold"), command=self.SetUp
        )
        self.setup_button.grid(row=8, column=2)

        # Window Title
        self.win_label = tk.Label(
            frame,
            text="Election Set-Up",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        #Label Posititiong
        self.win_label.grid(row=0, column=0, padx=10, pady=10)

        #Next few Labels and Text Fields are used to take information
        #about the Election schedule from Admin
        self.title_label = tk.Label(
            frame,
            text="Enter Election Title :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.title_label.grid(row=1, column=0, padx=10, pady=10)

        self.get_Title = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Title.grid(row=1, column=2, padx=10, pady=10)

        self.start_label = tk.Label(
            frame,
            text="Enter the Election Start Date (YYYY-MM-DD) :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.start_label.grid(row=2, column=0, padx=10, pady=10)

        self.get_Start = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_Start.grid(row=2, column=2, padx=10, pady=10)

        self.end_label = tk.Label(
            frame,
            text="Enter the Election End Date (YYYY-MM-DD) :",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )
        self.end_label.grid(row=3, column=0, padx=10, pady=10)

        self.get_End = tk.Text(
            frame,
            height=2,
            width=30,
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 16, "bold"),
        )

        self.get_End.grid(row=3, column=2, padx=10, pady=10)

        #Information Taken

    # Function implemented by the Setup Button
    # Used to insert Elections into the Database
    def SetUp(self):
        #Retrieving Information given by Admin
        title = self.get_Title.get("1.0", "end-1c")
        start = self.get_Start.get("1.0", "end-1c")
        end = self.get_End.get("1.0", "end-1c")
        # Checking whether all fields are Not Empty
        if len(title) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Election Title")
            return
        if len(start) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Election Start Date")
            return
        if len(end) == 0:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Enter Election End Date")
            return
        # Checking if Start and End Dates are in proper format
        l = start.split("-")
        if len(l) != 3:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election Start Date in Invalid Format!!!"
            )
            return
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
            #Start Date in Invalid Format
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election Start Date in Invalid Format!!!"
            )
            return
        l = end.split("-")
        if len(l) != 3:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election End Date in Invalid Format!!!"
            )
            return
        if len(l[0]) != 4 or len(l[1]) != 2 or len(l[2]) != 2:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election End Date in Invalid Format!!!"
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
            #Start Date in Invalid Format
            #Appropriate Dialogue Boxes Shown for Appropriate Cases
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election End Date in Invalid Format!!!"
            )
            return
        #All Information is good to insert
        #Queries.add_Election() adds an eletion to the Election Database table
        #Query in Queries.py
        x = Queries.add_Election(start, end, title, self.admin_id)
        if x == -1:
            # If Election Start and End Date get jumbled still Dialogue 
            # Box is created and Election is not inserted into the table
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Election Start Date is After Election End Date!!!"
            )
        else:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Election Set Up Successfully")
            #Appropriate Dialogue Boxes Shown
            #Elections Inserted Successfully

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
#     app = Set_Elections(root, 2)
#     app.mainloop()
