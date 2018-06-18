from Puree import *
from Creams import *
from Diapers import *


class ChildGoodsManager:


    def __init__(self):
        self.goods = []
        pass

    def sort_by_age(self):
        self.goods.sort(key = lambda a : a.age_info.name)

    def find_by_age(self, age_info):
        foundGoods = []

        for good in self.goods:
            if good.age_info == age_info:
                foundGoods.append(good)

        return foundGoods


odd=([1, 2] ,{ 12 : "aaaa"})
print(odd)






