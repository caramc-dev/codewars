class CelestialBody:
    def __init__(self, name, mass_kg, radius_km):
        self.name = name
        self.mass_kg = mass_kg
        self.radius_km = radius_km

    def surface_gravity(self):
        G = 6.674e-11
        return (G * self.mass_kg) / (self.radius_km * 1000) ** 2

    def __str__(self):
        return f"Celestial Body: {self.name}"


class Planet(CelestialBody):
    def __init__(self, name, mass_kg, radius_km, distance_from_sun_km, num_moons=0):
        super().__init__(name, mass_kg, radius_km)
        self.distance_from_sun_km = distance_from_sun_km
        self.num_moons = num_moons

    def __str__(self):
        return f"Planet: {self.name} (moons: {self.num_moons})"

    def __lt__(self, other):
        return self.distance_from_sun_km < other.distance_from_sun_km


class Star(CelestialBody):
    def __init__(self, name, mass_kg, radius_km, star_type):
        super().__init__(name, mass_kg, radius_km)
        self.star_type = star_type

    def __str__(self):
        return f"Star: {self.name} ({self.star_type})"


class SolarSystem:
    def __init__(self, name):
        self.name = name
        self._bodies = []

    def add_body(self, body):
        return self._bodies.append(body)

    def get_planets(self):
        return [body for body in self._bodies if isinstance(body, Planet)]

    def get_planets_by_distance(self):
        return sorted(self.get_planets())

    def closest_planet(self):
        planets = self.get_planets()
        if not planets:
            return None
        else:
            return min(planets)

    def furthest_planet(self):
        planets = self.get_planets()
        if not planets:
            return None
        else:
            return max(planets)

    def __str__(self):
        return f"Solar System: {self.name} ({len(self._bodies)} bodies)"


sun = Star("Sun", 1.99e30, 695_700, "Yellow Dwarf")
mercury = Planet("Mercury", 3.30e23, 2_440,    57_900_000, num_moons=0)
earth = Planet("Earth",   5.97e24, 6_371,   149_600_000, num_moons=1)
mars = Planet("Mars",    6.42e23, 3_390,   227_900_000, num_moons=2)

system = SolarSystem("Our Solar System")
for body in [sun, mercury, earth, mars]:
    system.add_body(body)

print(system)
print(system.closest_planet())
print(system.furthest_planet())
# Expected: Planet: Mars (moons: 2)

print([str(p) for p in system.get_planets_by_distance()])
# Expected: ['Planet: Mercury (moons: 0)', 'Planet: Earth (moons: 1)', 'Planet: Mars (moons: 2)']

print(round(earth.surface_gravity(), 2))
# Expected: 9.82  (approximately, using the simplified formula)

print(mercury < earth)
# Expected: True  (Mercury is closer to the sun)