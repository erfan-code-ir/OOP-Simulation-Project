import math
from work_place import WorkPlace, Consts

class School(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "school"
        self.calc_capacity()

    def calc_capacity(self) -> None:

        
        self.capacity = int(math.sqrt(self.level))

    def calc_costs(self) -> int:

        
        costs = Consts.BASE_PLACE_COST * int(math.sqrt(self.level))
        return int(costs)
