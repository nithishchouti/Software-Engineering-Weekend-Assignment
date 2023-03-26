import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

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
            
#2nd content

class Event:
    def __init__(self, name, date, time, location, staff=[]):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.staff = staff
        
    def add_staff(self, staff):
        self.staff.append(staff)
        
class Exhibition:
    def __init__(self, name, start_date, end_date, location, staff=[]):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.staff = staff
        
    def add_staff(self, staff):
        self.staff.append(staff)
        
class EventExhibitionManagementSystem:
    def __init__(self):
        self.events = []
        self.exhibitions = []
        
    def add_event(self, name, date, time, location, staff=[]):
        event = Event(name, date, time, location, staff)
        self.events.append(event)
        
    def add_exhibition(self, name, start_date, end_date, location, staff=[]):
        exhibition = Exhibition(name, start_date, end_date, location, staff)
        self.exhibitions.append(exhibition)
        
    def get_events(self):
        events_df = pd.DataFrame(columns=["Name", "Date", "Time", "Location"])
        for event in self.events:
            events_df = events_df.append({"Name": event.name, "Date": event.date, "Time": event.time, "Location": event.location}, ignore_index=True)
        return events_df
    
    def get_exhibitions(self):
        exhibitions_df = pd.DataFrame(columns=["Name", "Start Date", "End Date", "Location"])
        for exhibition in self.exhibitions:
            exhibitions_df = exhibitions_df.append({"Name": exhibition.name, "Start Date": exhibition.start_date, "End Date": exhibition.end_date, "Location": exhibition.location}, ignore_index=True)
        return exhibitions_df

#3rd content

class Artist:
    def __init__(self, name, genre, location, portfolio, availability):
        self.name = name
        self.genre = genre
        self.location = location
        self.portfolio = portfolio
        self.availability = availability
        
class ArtistManagementSystem:
    def __init__(self):
        self.artists = []
        
    def add_artist(self, name, genre, location, portfolio, availability):
        artist = Artist(name, genre, location, portfolio, availability)
        self.artists.append(artist)
        
    def get_artists(self):
        artists_df = pd.DataFrame(columns=["Name", "Genre", "Location", "Portfolio", "Availability"])
        for artist in self.artists:
            artists_df = artists_df.append({"Name": artist.name, "Genre": artist.genre, "Location": artist.location, "Portfolio": artist.portfolio, "Availability": artist.availability}, ignore_index=True)
        return artists_df

#4th content

class DigitalArt:
    def __init__(self, name, artist, genre, image_url):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.image_url = image_url
        
    def display_image(self):
        img = urllib.request.urlopen(self.image_url)
        img_arr = plt.imread(img, format='jpg')
        plt.imshow(img_arr)
        plt.show()
        
class DigitalArtGallery:
    def __init__(self):
        self.artworks = []
        
    def add_artwork(self, name, artist, genre, image_url):
        artwork = DigitalArt(name, artist, genre, image_url)
        self.artworks.append(artwork)
        
    def display_artwork(self, name):
        for artwork in self.artworks:
            if artwork.name == name:
                artwork.display_image()

#5th content

class EventTicket:
    def __init__(self, event_name, date, time, location, price, availability):
        self.event_name = event_name
        self.date = date
        self.time = time
        self.location = location
        self.price = price
        self.availability = availability
        
class ExhibitionTicket:
    def __init__(self, exhibition_name, start_date, end_date, location, price, availability):
        self.exhibition_name = exhibition_name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.price = price
        self.availability = availability
        
class TicketingReservationSystem:
    def __init__(self):
        self.event_tickets = []
        self.exhibition_tickets = []
        
    def add_event_ticket(self, event_name, date, time, location, price, availability):
        event_ticket = EventTicket(event_name, date, time, location, price, availability)
        self.event_tickets.append(event_ticket)
        
    def add_exhibition_ticket(self, exhibition_name, start_date, end_date, location, price, availability):
        exhibition_ticket = ExhibitionTicket(exhibition_name, start_date, end_date, location, price, availability)
        self.exhibition_tickets.append(exhibition_ticket)
        
    def get_event_tickets(self):
        event_tickets_df = pd.DataFrame(columns=["Event Name", "Date", "Time", "Location", "Price", "Availability"])
        for event_ticket in self.event_tickets:
            event_tickets_df = event_tickets_df.append({"Event Name": event_ticket.event_name, "Date": event_ticket.date, "Time": event_ticket.time, "Location": event_ticket.location, "Price": event_ticket.price, "Availability": event_ticket.availability}, ignore_index=True)
        return event_tickets_df
    
    def get_exhibition_tickets(self):
        exhibition_tickets_df = pd.DataFrame(columns=["Exhibition Name", "Start Date", "End Date", "Location", "Price", "Availability"])
        for exhibition_ticket in self.exhibition_tickets:
            exhibition_tickets_df = exhibition_tickets_df.append({"Exhibition Name": exhibition_ticket.exhibition_name, "Start Date": exhibition_ticket.start_date, "End Date": exhibition_ticket.end_date, "Location": exhibition_ticket.location, "Price": exhibition_ticket.price, "Availability": exhibition_ticket.availability}, ignore_index=True)
        return exhibition_tickets_df

#6th content

class PaymentSystem:
    def __init__(self):
        self.transactions = []
        
    def process_transaction(self, amount, payment_method, transaction_time):
        transaction = {"amount": amount, "payment_method": payment_method, "transaction_time": transaction_time}
        self.transactions.append(transaction)
        return "Transaction successful"
    
    def get_transactions(self):
        return self.transactions

TicketBookingSystem()
#7th content

def test_digital_art_gallery():
    gallery = DigitalArtGallery()
    gallery.add_artwork("Mona Lisa", "Leonardo da Vinci", "Renaissance", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mona_Lisa.jpg/402px-Mona_Lisa.jpg")
    gallery.add_artwork("Starry Night", "Vincent van Gogh", "Post-Impressionism", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/400px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg")
    gallery.display_artwork("Mona Lisa")

def test_ticketing_reservation_system():
    ticketing = TicketingReservationSystem()
    ticketing.add_event_ticket("Theater Performance", "2023-04-15", "8:00 PM", "Mumbai", 500, 100)
    ticketing.add_exhibition_ticket("Indian Heritage", "2023-05-01", "2023-05-31", "Delhi", 250, 500)
    event_tickets = ticketing.get_event_tickets()
    exhibition_tickets = ticketing.get_exhibition_tickets()
    assert len(event_tickets) == 1
    assert len(exhibition_tickets) == 1

def test_payment_system():
    payment = PaymentSystem()
    payment.process_transaction(1000, "Credit Card", "2023-03-26 10:00:00")
    payment.process_transaction(2000, "PayPal", "2023-03-26 10:10:00")
    transactions = payment.get_transactions()
    assert len(transactions) == 2

if __name__ == "__main__":
    test_digital_art_gallery()
    test_ticketing_reservation_system()
    test_payment_system()
    print("All tests passed!")

#8th content

class DigitalArtGallery:
    def __init__(self):
        self.artworks = []
        
    def add_artwork(self, title, artist, era, image_url):
        artwork = {"title": title, "artist": artist, "era": era, "image_url": image_url}
        self.artworks.append(artwork)
        
    def display_artwork(self, title):
        for artwork in self.artworks:
            if artwork["title"] == title:
                print(f"Title: {artwork['title']}")
                print(f"Artist: {artwork['artist']}")
                print(f"Era: {artwork['era']}")
                print(f"Image URL: {artwork['image_url']}")
                break
                
class TicketingReservationSystem:
    def __init__(self):
        self.event_tickets = []
        self.exhibition_tickets = []
        
    def add_event_ticket(self, event_name, date, time, location, price, quantity):
        ticket = {"event_name": event_name, "date": date, "time": time, "location": location, "price": price, "quantity": quantity}
        self.event_tickets.append(ticket)
        
    def add_exhibition_ticket(self, exhibition_name, start_date, end_date, location, price, quantity):
        ticket = {"exhibition_name": exhibition_name, "start_date": start_date, "end_date": end_date, "location": location, "price": price, "quantity": quantity}
        self.exhibition_tickets.append(ticket)
        
    def get_event_tickets(self):
        return self.event_tickets
    
    def get_exhibition_tickets(self):
        return self.exhibition_tickets
    
class PaymentSystem:
    def __init__(self):
        self.transactions = []
        
    def process_transaction(self, amount, payment_method, transaction_time):
        transaction = {"amount": amount, "payment_method": payment_method, "transaction_time": transaction_time}
        self.transactions.append(transaction)
        return "Transaction successful"
    
    def get_transactions(self):
        return self.transactions
    
def test_digital_art_gallery():
    gallery = DigitalArtGallery()
    gallery.add_artwork("Mona Lisa", "Leonardo da Vinci", "Renaissance", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mona_Lisa.jpg/402px-Mona_Lisa.jpg")
    gallery.add_artwork("Starry Night", "Vincent van Gogh", "Post-Impressionism", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/400px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg")
    gallery.display_artwork("Mona Lisa")

def test_ticketing_reservation_system():
    ticketing = TicketingReservationSystem()
    ticketing.add_event_ticket("Theater Performance", "2023-04-15", "8:00 PM", "Mumbai", 500, 100)
    ticketing.add_exhibition_ticket("Indian Heritage", "2023-05-01", "2023-05-31", "Delhi", 250, 500)
    event_tickets = ticketing.get_event_tickets()
    exhibition_tickets = ticketing.get_exhibition_tickets()
    assert len(event_tickets) == 1
    assert len(exhibition_tickets) == 1

def test_payment_system():
    payment = PaymentSystem()
    payment.process_transaction(1000, "Credit Card", "2023-03-26 10:00:00")
    payment.process_transaction(2000, "PayPal", "2023-03-26 10")
    assert len(payment.get_transactions()) == 2

def run_tests():
    test_digital_art_gallery()
    test_ticketing_reservation_system()
    test_payment_system()
    print("All tests passed")

if __name__ == "__main__":
    TicketBookingSystem()
    run_tests()