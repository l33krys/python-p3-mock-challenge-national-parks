from statistics import mode;
class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{self.name}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park is self]))
    
    def total_visits(self):
        total = len([park_visits for park_visits in Trip.all if park_visits.national_park is self])
        if total > 0:
            return total
        else:
            return 0
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park is self]
        return mode(visitors)   


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    def __repr__(self):
        return f"{self.visitor}, {self.national_park}, {self.start_date}, {self.end_date}"
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
    

class Visitor:

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{self.name}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor is self]))
    
    def total_visits_at_park(self, park):
        if isinstance(park, NationalPark):
            return len([trip for trip in Trip.all if trip.visitor is self and trip.national_park is park])