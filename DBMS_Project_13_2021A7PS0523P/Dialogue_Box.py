import tkinter as tk

# This is a simple GUI Page to display a
# message to the User and has been repeatedly in
# the project.


class Dialogue_Box(tk.Frame):  # Main GUI Class
    def __init__(self, master, message):
        super().__init__(master)
        self.master = master
        self.master.title("Message")
        self.master.geometry("400x200")

        # create a frame in the center of the window
        frame = tk.Frame(self.master, bg="#FFFFFF")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Message Label to display the message
        # appropriately
        self.message_label = tk.Label(
            frame,
            text=message,
            padx=0,
            pady=0,
            bg="#FFFFFF",
            fg="Black",
            font=("Rockwell", 24, "bold"),
        )
        self.message_label.grid(row=0, column=0, padx=10, pady=10)

        # Ok Button to close Pop-up
        self.ok_button = tk.Button(
            frame, text="Ok", font=("Rockwell", 20, "bold"), command=self.Ok
        )
        self.ok_button.grid(row=1, column=0)

        # create the buttons inside the frame

    # Function Run by Ok Button
    def Ok(self):
        self.master.withdraw()


# if __name__ == "__main__": Lines Used to Test Out the GUI
#     root = tk.Tk()
#     app = Dialogue_Box(master=root, message="Are You Sure?")
#     app.mainloop()
