class Test:

    people = ["Gianni", "Ashlynn"]
    
    def uppercase(self, word):
        return word.upper()
    
    def dispatcher(self, operator, x, y):
        return {
            "add": lambda: x + y,
            "subtract": lambda: x - y
        }.get(operator)()

    def reverse_list(self, items):
        return list(reversed(items))
    
    def __getitem__(self, key):
        return self.people[key]