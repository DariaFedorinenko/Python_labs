from enum import Enum

class Age(Enum):
    for3month = 1
    for6month = 2
    forbirth = 3

class ExpirationDate(Enum):
    upto24months = 1
    upto4yesrs = 2
    indefinitey = 3


class ChildGoods:

    name = None
    age = 0.0
    produce = None
    expiration_date = None
    age_info = None

    def __str__(self):
        return  'Duration: '+str(self.age_info.name) + '||Name: ' + str(self.name) +'|| Expire period:'+ str(self.expiration_date.name)\
                            + ' ||Produce:' +str(self.produce)