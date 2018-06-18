from ChildGoods import ChildGoods, Age


class Puree(ChildGoods):
    age_info = Age.for3month


    def __init__(self ,name ,produce ,expiration_date ):
        self.name = name
        self.produce = produce
        self.expiration_date = expiration_date