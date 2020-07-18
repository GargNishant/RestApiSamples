# Create your models here.


class Destination:
    id: int
    name: str
    image: str
    desc: str
    price: float

    def to_json_map(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "desc": self.desc,
            "price": self.price
        }





