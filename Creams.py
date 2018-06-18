from ChildGoods import ChildGoods, Age


class Creams(ChildGoods):
    age_info = Age.for6month

    def __init__(self, name, produce, expiration_date):
        self.name = name
        self.produce = produce
        self.expiration_date = expiration_date