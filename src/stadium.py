class WorldStadium:
    def __init__(self):
        self.zones = {}

    def add_zone(self, zone_name, audio_properties):
        """Adds a new audio zone with specified properties."""
        self.zones[zone_name] = audio_properties

    def remove_zone(self, zone_name):
        """Removes a zone from the stadium."""
        if zone_name in self.zones:
            del self.zones[zone_name]

    def simulate_audio(self):
        """Simulates audio across all zones. This is a placeholder for actual implementation."""
        for zone, properties in self.zones.items():
            print(f'Simulating audio in {zone} with properties: {properties}')

# Example usage:
stadium = WorldStadium()
stadium.add_zone('VIP', {'volume': 10, 'balance': 2})
stadium.add_zone('General', {'volume': 5, 'balance': 0})
stadium.simulate_audio()
