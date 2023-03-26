import requests
import json
import unittest

# Define the API endpoint
api_endpoint = "https://api.publicdomain.com/artists"

# Define a function to retrieve artist data from the API
def get_artist_data(artist_id):
    url = f"{api_endpoint}/{artist_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# Define a function to display artist data
def display_artist_data(artist_id):
    artist_data = get_artist_data(artist_id)
    if artist_data:
        print(f"Artist: {artist_data['name']}")
        print(f"Bio: {artist_data['bio']}")
        print(f"Artworks: {artist_data['artworks']}")
    else:
        print(f"No data available for artist with ID {artist_id}")

# Define a unit test class for the display_artist_data function
class TestDisplayArtistData(unittest.TestCase):
    
    def test_valid_artist_id(self):
        expected_output = "Artist: Leonardo da Vinci\nBio: Italian artist, engineer, and scientist of the Renaissance.\nArtworks: Mona Lisa, The Last Supper"
        self.assertEqual(display_artist_data(1), expected_output)
        
    def test_invalid_artist_id(self):
        expected_output = "No data available for artist with ID 999"
        self.assertEqual(display_artist_data(999), expected_output)

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
