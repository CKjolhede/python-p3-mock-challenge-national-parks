class NationalPark:

    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance (value, str) and len(value) >= 3 and not hasattr(self, "name"):
            self._name = value
        else:
            return
                
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
        
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        visitors_list = [trip.visitor for trip in self.trips()]
        return len(visitors_list) if visitors_list else print(int("0"))
    
    def best_visitor(self):
        for visitor in self.visitors():
            num_visitor_trips = {visitor: visitor.total_visits_at_park(self)}
    
        sorted_dict = dict(sorted(num_visitor_trips.items(), key=lambda x: max(x[1]), reverse=True))
        return sorted_dict.keys[0]

class Trip:
    
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)


class Visitor:
    
    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return {trip.national_park for trip in self.trips}
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])