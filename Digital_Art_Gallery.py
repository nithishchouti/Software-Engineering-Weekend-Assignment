import matplotlib.pyplot as plt
import urllib.request

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
