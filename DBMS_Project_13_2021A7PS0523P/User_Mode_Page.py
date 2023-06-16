import tkinter as tk  # Necessary Imports
import Admin_Login  # Included all pages that will be traversed in the GUI from this Page
import Voter_Login


class User_Mode_Page(tk.Frame):  # Main GUI Class
    def __init__(self, master):  # __init__Function with voter_id Parameter
        super().__init__(master)
        self.master = (
            master  # Next few lines set up the GUI window size and title, attributes
        )
        self.master.title("Choose User Mode...")
        self.master.geometry("1000x400")

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Creating and Positioning an Exit Button if Voter Wants to Exit the Program
        self.exit_button = tk.Button(
            self.master, text="Exit", font=("Rockwell", 12, "bold"), command=self.Exit
        )
        self.exit_button.grid(row=0, column=0)

        # Welcome Label to the Program
        self.welcome_label = tk.Label(
            frame,
            text="Welcome to the Voting Management System!",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        # Label Positioning
        self.welcome_label.grid(row=0, column=1, padx=10, pady=10)

        self.mode_label = tk.Label(
            frame,
            text="Choose Your Mode",
            padx=0,
            pady=0,
            bg="#CCCCCC",
            fg="Black",
            font=("Rockwell", 20, "bold"),
        )
        self.mode_label.grid(row=1, column=1, padx=10, pady=10)

        # create the buttons inside the frame
        # Following are 2 buttons which provide access
        # to the Admin_Login Page and the Voter_Login_Page
        # respectively
        self.admin_mode_button = tk.Button(
            frame,
            text="Admin Mode",
            command=self.admin_mode,
            padx=20,
            pady=20,
            bg="#CCCCCC",
            font=("Rockwell", 16, "bold"),
        )
        # Button Positioning
        self.admin_mode_button.grid(row=2, column=0, padx=10, pady=10)

        self.voter_mode_button = tk.Button(
            frame,
            text="Voter Mode",
            command=self.voter_mode,
            padx=20,
            pady=20,
            bg="#CCCCCC",
            font=("Rockwell", 16, "bold"),
        )
        # Button Positioning
        self.voter_mode_button.grid(row=2, column=2, padx=10, pady=10)

    # Function Executed by Admin_Mode Button
    # Opens a Window to Admin_Login to set up and manage elections
    def admin_mode(self):
        admin_login_window = tk.Toplevel(self.master)
        Admin_Login.Admin_Login(admin_login_window)
        self.master.withdraw()

    # Function Executed by Voter_Mode Button
    # Opens a Window to Voter_Login to set up and manage elections
    def voter_mode(self):
        voter_login_window = tk.Toplevel(self.master)
        Voter_Login.Voter_Login(voter_login_window)
        self.master.withdraw()

    # Command Executed by the Exit Button
    # Leads to Program Termination
    def Exit(self):
        self.destroy()
        self.master.quit()


if __name__ == "__main__":  # Start Running Application From Here
    root = tk.Tk()
    app = User_Mode_Page(master=root)
    app.mainloop()
