class getter_setter:
    Brand="Toyota"
    a=10
    def __init__(self,car_name):
        self.car_name=car_name
        self.engine_formula=2*3+98

    @property
    def update_engine_formula(self):
        return 10*self.engine_formula
    @ update_engine_formula.setter
    def update_engine_formula(self,value):
        self.a=value


obj=getter_setter("corola")
obj.update_engine_formula=1000

print(obj.update_engine_formula)
print(obj.engine_formula)


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

p = Person("Alice")
print(p.name)  # Output: Alice
p.name = "Bob"
print(p.name)  # Output: Bob




