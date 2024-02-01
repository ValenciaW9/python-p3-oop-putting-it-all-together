class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def __str__(self):
        return f"{self.color} {self.brand} in size {self.size}"
