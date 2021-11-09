class Product:
    def __init__(self, name, price, link, images):
        self.name = name
        self.price = price
        self.link = link
        self.images = images
        #self.time = time

    def add_image(self, image):
        self.images.append(image)
    
