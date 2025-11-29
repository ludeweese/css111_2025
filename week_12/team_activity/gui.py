# team activity week 12
# This program creates a GUI that calculates the area of a rectangle.
# It demonstrates object-oriented programming with buttons, labels, and custom entry widgets.
# Stretch challenges completed: Clear button + Status bar with error messages.

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry  # Custom entry class with numeric validation


def main():
    """Create the Tk root window and the main frame."""
    root = tk.Tk()

    # Create main frame
    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    # Start GUI event loop
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window with labels, entry boxes, buttons, and status bar."""

    # ----- INPUT LABELS AND ENTRY BOXES -----
    lbl_width = Label(frm_main, text="Width:")
    ent_width = FloatEntry(frm_main, width=6, lower_bound=0.0, upper_bound=10000)

    lbl_height = Label(frm_main, text="Height:")
    ent_height = FloatEntry(frm_main, width=6, lower_bound=0.0, upper_bound=10000)

    # ----- OUTPUT LABEL -----
    lbl_area_text = Label(frm_main, text="Area:")
    lbl_area_result = Label(frm_main, width=10)

    # ----- CLEAR BUTTON (Stretch Challenge #1) -----
    btn_clear = Button(frm_main, text="Clear")

    # ----- STATUS BAR (Stretch Challenge #2) -----
    # Displays error messages for invalid input
    lbl_status = Label(frm_main, text="", anchor="w", fg="red")

    # ----- GRID LAYOUT -----
    lbl_width.grid(row=0, column=0, padx=3, pady=3, sticky="w")
    ent_width.grid(row=0, column=1, padx=3, pady=3)

    lbl_height.grid(row=1, column=0, padx=3, pady=3, sticky="w")
    ent_height.grid(row=1, column=1, padx=3, pady=3)

    lbl_area_text.grid(row=2, column=0, padx=3, pady=3, sticky="w")
    lbl_area_result.grid(row=2, column=1, padx=3, pady=3)

    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky="w")

    # Status bar goes at the bottom
    lbl_status.grid(row=4, column=0, padx=3, pady=3, columnspan=2, sticky="w")

    # ----- FUNCTIONS -----
    def calculate(event):
        """
        When the user types, try to read the numbers.
        If valid: compute area.
        If invalid: show an error message in the status bar.
        """
        try:
            width = ent_width.get()
            height = ent_height.get()

            area = width * height
            lbl_area_result.config(text=f"{area:.2f}")

            # Clear error message when input is valid
            lbl_status.config(text="")

        except ValueError:
            # Show error when input is invalid
            lbl_area_result.config(text="")
            lbl_status.config(text="Invalid input. Please enter valid numbers.", fg="red")

    def clear():
        """Clear all inputs, outputs, and status messages."""
        btn_clear.focus()
        ent_width.clear()
        ent_height.clear()
        lbl_area_result.config(text="")
        lbl_status.config(text="")
        ent_width.focus()  # Place cursor back in first box

    # ----- EVENT BINDINGS -----
    # Recalculate automatically when the user types
    ent_width.bind("<KeyRelease>", calculate)
    ent_height.bind("<KeyRelease>", calculate)

    # Clear button action
    btn_clear.config(command=clear)

    # Set initial cursor focus
    ent_width.focus()


# Run the program
if __name__ == "__main__":
    main()
