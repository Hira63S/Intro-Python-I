# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class WayPoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon) # because LatLon is the parent class
        self.name = name # we do not call lat and lon again because we are inheriting from the parent class
    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"

# repr and string are very similar, repr will just print it out even if you just type it
# repr is more general
# return whatever is in repr
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(WayPoint):
    def __init__(self, name, lat, lon, difficulty, size):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}, {self.difficulty}, {self.size}"
g = Geocache("LA", "22", "33", 4, 2)
print(g)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = WayPoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", "dif 1.5", "size 2", 44.05, -121.41556)

# Print it--also make this print more nicely
print(geocache)
