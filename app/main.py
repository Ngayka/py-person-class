class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self

    def add_husband(self, husband: "Person") -> None:
        self.husband = husband

    def add_wife(self, wife: "Person") -> None:
        self.wife = wife


def create_person_list(people: list) -> list:
    person_list = []

    for one in people:
        name = one.get("name")
        age = one.get("age")
        husband_name = one.get("husband")
        wife_name = one.get("wife")

        if name in Person.people:
            person = Person.people[name]
        else:
            person = Person(name=name, age=age)
            person_list.append(person)

        if husband_name:
            if husband_name in Person.people:
                husband = Person.people[husband_name]
            else:
                husband = Person(name=husband_name, age=0)
                person_list.append(husband)
            person.add_husband(husband)

        if wife_name:
            if wife_name in Person.people:
                wife = Person.people[wife_name]
            else:
                wife = Person(name=wife_name, age=0)
                person_list.append(wife)
            person.add_wife(wife)

    return list(Person.people.values())

