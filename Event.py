import pandas as pd

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
