class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, age, name, work):
        super(Employee, self).__init__(name, age)
        self.work = work

    def age(self):
        print("%s his/her age" % self.name)


class Programmer(Employee):
    def __init__(self, computer, age, name, work):
        super(Programmer, self).__init__(age, name, work)
        self.computer = computer

    def name(self):
        print("%s his/her name" % self.name)