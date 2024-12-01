class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.husband = None
        self.wife = None

        Person.people[self.name] = self

    def add_husband(self, husband: str) -> None:
        self.husband = husband

    def add_wife(self, wife: str) -> None:
        self.wife = wife


def create_person_list(people: list) -> list:
    person_list = []

    for one in people:
        name = one.get("name")
        age = one.get("age")
        husband = one.get("husband")
        wife = one.get("wife")

        person = Person(name=name, age=age)
        person_list.append(person)
        if husband:
            person.add_husband(husband)
        if wife:
            person.add_wife(wife)
    return person_list

