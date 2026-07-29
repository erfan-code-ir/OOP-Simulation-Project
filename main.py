from person import Person
from engineer import Engineer
from teacher import Teacher
from worker import Worker
from work_place import WorkPlace, WorkPlaceIsFull
from mine import Mine
from school import School
from company import Company



raha = Engineer(name="Raha", age=30)
sara = Teacher(name="Sara", age=25)
taha = Worker(name="Taha", age=22)

print(len(Person.instances))
for p in Person.instances:
    print(f"{p.name} | {p.get_job()} | Lvl: {p.level}")



kavir_mine = Mine(name="Kavir Mine")
danesh_school = School(name="Danish School")
pishro_company = Company(name="Pishro Company")

print(len(WorkPlace.instances))
for wp in WorkPlace.instances:
    print(f"{wp.name} | {wp.get_expertise()} | Lvl: {wp.level} | Cap: {wp.capacity}")



try:
    kavir_mine.hire(taha)
    danesh_school.hire(sara)
    pishro_company.hire(raha)
    print(f"{taha.name} -> {taha.work_place.name}")
    print(f"{sara.name} -> {sara.work_place.name}")
    print(f"{raha.name} -> {raha.work_place.name}")
except WorkPlaceIsFull as e:
    print(e)



print(f"{taha.name} Income: {taha.calc_income()}")
print(f"{taha.name} Cost: {taha.calc_life_cost()}")
print(f"{taha.name} Net: {taha.calc()}")
