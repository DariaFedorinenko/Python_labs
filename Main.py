from ChildGoodsManager import ChildGoodsManager
from Diapers import Diapers
from Puree import Puree
from Creams import Creams
from ChildGoods import *


if __name__=='__main__':
    manager = ChildGoodsManager()

    puree = Puree("Rudolf", "apple and carrot", ExpirationDate.upto24months)
    diapers = Diapers("Dada","for girls and boys" , ExpirationDate.indefinitey)
    creams = Creams("Hipp", "Germany", ExpirationDate.upto4yesrs)

    manager.goods = [puree, diapers, creams]
    print("Initial list:")
    for good in manager.goods:
        print(str(good))
    print("\n")

    goods = manager.find_by_age(Age.for6month)
    print("Method of finding instrument: ")
    for good in goods:
        print(str(good))
    print("\n")

    manager.sort_by_age()
    print("Sorted list:")
    for good in manager.goods:
        print(str(good))
    print("\n")











