class Supermarket:
    total_number_of_workers = 0

    def __init__(self, name_of_supermarket="Dasha", area="2.000 sq.m", work_time="with 09:00 to 22:00",
                 number_of_workers=1200, number_of_divisions=15):
        self.name_of_supermarket = name_of_supermarket
        self.area = area
        self.work_time = work_time
        self.number_of_workers = number_of_workers
        self.number_of_divisions = number_of_divisions
        Supermarket.total_number_of_workers += self.number_of_workers

    def to_string(self):
        print(
            "Name of supermarket:" + self.name_of_supermarket + "; Area:" + self.area + "; Work time:" + self.work_time +
            "; Number of workers: " + self.number_of_workers + "; Number of divisions: " + self.number_of_workers)

    def print_sum(self):
        print(
            "The supermarket is called " + self.name_of_supermarket + "it has number of workers" + self.number_of_workers)

    @staticmethod
    def print_static_sum():
        print("Total number of workers of supermarket =" + str(Supermarket.number_of_workers))


if __name__ == '__main__':
    dasha = Supermarket()
    aushan = Supermarket("Aushan", "1.500 sq.m", "with 08:00 to 23:00", 1000, 10)
    silpo = Supermarket("Silpo", "1.750 sq.m", "with 09:00 to 23:00", 1250)

    dasha.to_string()
    aushan.to_string()
    silpo.to_string()

    dasha.print_sum()
    aushan.print_sum()
    silpo.print_sum()
    Supermarket.print_static_sum()
