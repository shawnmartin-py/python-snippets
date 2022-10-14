# Single Responsibility Principle

# A class should only have one reason to change
# Separation of concerns - different classes handling different, independent
# tasks/problems
# Prevents God Objects

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]
 
    def __str__(self):
        return "\n".join(self.entries)


# seperated from Journal class
def save_to_file(journal, filename):
    with open(filename, "w") as file:
        file.write(str(journal)) 

#-----------------------------------------------------------------------------#

j = Journal()
j.add_entry("I looked after baby")
j.add_entry("I took a shower")
print(j)