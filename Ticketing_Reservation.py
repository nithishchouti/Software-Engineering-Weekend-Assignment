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
