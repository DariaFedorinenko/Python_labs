from ChildGoods import ChildGoods, Age


class Diapers(ChildGoods):
    age_info = Age.forbirth

    def __init__(self, name, produce, expiration_date):
        self.name = name
        self.produce = produce
        self.expiration_date = expiration_date