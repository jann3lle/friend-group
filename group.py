"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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
