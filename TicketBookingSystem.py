import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TicketBookingSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ticket Booking System")
        self.window.geometry("400x300")
        
        self.event_label = ttk.Label(self.window, text="Select Event:")
        self.event_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.event_combo = ttk.Combobox(self.window, values=["Event 1", "Event 2", "Event 3"])
        self.event_combo.grid(column=1, row=0, padx=10, pady=10)
        
        self.ticket_label = ttk.Label(self.window, text="Select Number of Tickets:")
        self.ticket_label.grid(column=0, row=1, padx=10, pady=10)
        
        self.ticket_spinbox = ttk.Spinbox(self.window, from_=1, to=10)
        self.ticket_spinbox.grid(column=1, row=1, padx=10, pady=10)
        
        self.price_label = ttk.Label(self.window, text="Price per Ticket: 100")
        self.price_label.grid(column=0, row=2, padx=10, pady=10)
        
        self.total_label = ttk.Label(self.window, text="Total Price: 0")
        self.total_label.grid(column=1, row=2, padx=10, pady=10)
        
        self.book_button = ttk.Button(self.window, text="Book Tickets", command=self.book_tickets)
        self.book_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        
        self.window.mainloop()
    
    def book_tickets(self):
        event = self.event_combo.get()
        tickets = int(self.ticket_spinbox.get())
        total_price = tickets * 100
        
        result = messagebox.askquestion("Confirmation", f"Are you sure you want to book {tickets} tickets for {event} for a total of {total_price}?")
        
        if result == "yes":
            messagebox.showinfo("Success", f"{tickets} tickets booked for {event} for a total of {total_price}")
        else:
            messagebox.showinfo("Cancelled", "Ticket booking cancelled")
            
TicketBookingSystem()
