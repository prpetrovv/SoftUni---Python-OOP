import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for page_index in range(len(self.photos)):
            for spot_index in range(4 - len(self.photos[page_index])):
                self.photos[page_index].append(label)
                return f"{label} photo added successfully on page {page_index + 1} slot {len(self.photos[page_index])}"
        return "No more free slots"

    def display(self):
        result = ["-----------"]
        for i in range(self.pages):
            result.append(' '.join(['[]' for element in self.photos[i]]) + "\n-----------")
        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
