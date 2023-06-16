import tkinter as tk  # Necessary Imports
import Dialogue_Box  # Included all pages that will be traversed in the GUI from this Page
import Queries

# This Page helps complete the Registration Process for a Voter


class Register_Confirmation_Box(tk.Frame):  # Main GUI Class
    def __init__(
        self, master, message, pwd, name, email, address, phone, dob
    ):  # __init__Function with multiple Parameter
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Confirmation")
        self.master.geometry("400x150")
        self.pwd = pwd
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.dob = dob

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Message for a confirmation box
        # To gather only the correct details from a voter
        self.message_label = tk.Label(
            frame,
            text=message,
            padx=0,
            pady=0,
            bg="#FFFFFF",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        # Label Positioning
        self.message_label.grid(row=0, column=1, padx=10, pady=10)

        # Creating and Positioning a Logout Button if Voter is sure to Register
        self.yes_button = tk.Button(
            frame, text="YES", font=("Rockwell", 20, "bold"), command=self.Yes
        )
        self.yes_button.grid(row=2, column=0)

        # Creating and Positioning a Logout Button if Voter Wants to Opt out of Registration
        self.no_button = tk.Button(
            frame, text="NO", font=("Rockwell", 20, "bold"), command=self.No
        )
        self.no_button.grid(row=2, column=2)

        # create the buttons inside the frame

    # Function Implemented by the Yes_Button
    def Yes(self):
        # Checking if Phone Number is of 10 digits
        # Shows Appropriate Dialogue Box, if invalid
        if len(self.phone) != 10:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Invalid Phone Number!!!")
            return
        # Now we check if DOB given is in proper format
        # Appropraite Dialogue Boxes shown again
        l = self.dob.split("-")
        if len(l) != 3:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth\nin Invalid Format!!!"
            )
            return
        if len(l[0]) != 4 or len(l[1]) != 2 or len(l[2]) != 2:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth\nin Invalid Format!!!"
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
            # Last check for invalid Date Of Birth
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box, "Date Of Birth\nin Invalid Format!!!"
            )
            return
        # Date of Birth and other details are ok
        # Queries.add_Voter() takes all these details
        # adds a new voter to the vote table
        # result stores the voter_id of the new voter
        # Query in Queries.py
        result = Queries.add_Voter(
            self.pwd, self.name, self.email, self.address, self.phone, self.dob
        )
        if result == -1:
            # Result = -1 implies Voter is ineligible to register
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Not Eligible To Vote!!!")
        elif result == -2:
            # Result = -2 implies Voter has already registered
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(dialogue_box, "Voter Already Registered")
        else:
            dialogue_box = tk.Toplevel(self.master)
            Dialogue_Box.Dialogue_Box(
                dialogue_box,
                f"Registration Successful!\nUse the following details to Login.\nIssued Voter-ID is {result}\nPassword is {self.pwd}",
            )
            # Successful Registration
            # Display Box shows the Assigned VoterId and Password to the Voter
        self.master.withdraw()

    # Function Implemented by the No_Button
    def No(self):
        self.master.withdraw()


# if __name__ == "__main__": Lines used to test out the GUI
#     root = tk.Tk()
#     app = Register_Confirmation_Box(
#         root,
#         "Are You Sure?",
#         "912412",
#         "912412",
#         "912412",
#         "912412",
#         "912412",
#         "912412",
#     )
#     app.mainloop()
