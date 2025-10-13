"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
def main():
    forget(my_group, "Jill", "John")
    add_person(my_group, "Maya", 30, "Engineer", {"friend": "Jill"})
    print(f"average age:", average_age(my_group))

if __name__ == "__main__":
    my_group = {
        "Jill": {
            "age": 26,
            "job": "Biologist",
            "connection": {"friend": "Zalika", "partner": "John"},
        },
        "Zalika": {"age": 28, "job": "Artist", "connection": {"friend": "Jill"}},
        "John": {"age": 27, "job": "Writer", "connection": {"partner": "Jill"}},
        "Nash": {
            "age": 34,
            "job": "Chef",
            "connection": {"cousin": "John", "landlord": "Zalika"},
        },
        "Lila": {"age": "", "job": "", "connection": ""},
        "Nelly": {"age": 22, "job": "Student", "connection": ""},
        "Zara": {"age": 22, "job": "Student", "connection": {"friend": "Lila"}},
    }

    def forget(my_group, person1, person2):
        # Step 1: check person1's connections
        for relation, name in list(my_group[person1]["connection"].items()):
            if name == person2:
                del my_group[person1]["connection"][relation]
        
        # Step 2: check person2's connections
        for relation, name in list(my_group[person2]["connection"].items()):
            if name == person1:
                del my_group[person2]["connection"][relation]
        # Print information for person 1 and 2
        print(f"{person1}: {my_group[person1]}")
        print(f"{person2}: {my_group[person2]}")

    def add_person(group, name, age, job, relations):
        group[name] = {
            "age": age,
            "job": job,
            "connection": relations
    }
        print(f"Added {name}: {group[name]}")
        
    def average_age(group):
        ages = []
        for person, info in group.items():
            age = info.get("age")
            if isinstance(age, (int, float)):  # only count numbers
                ages.append(age)
        if ages:
            return sum(ages) / len(ages)
        else:
            return 0

    main()