"""An example of how to represent a group of acquaintances in Python."""
import json

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


json_string = json.dumps(my_group, indent=4, sort_keys=True)
#print(json_string)

# Write .json file
with open('my_file.json', 'w') as f:
    json.dump(my_group, f, indent=4, sort_keys=True)

# Read .json file
with open('my_file.json', 'r') as f:
     loaded_data = json.load(f)
print(f"loaded_data = {loaded_data}")