#!/usr/bin/python
import sys,random,os, string
sys.dont_write_bytecode=True
__author__ = 'Ankur Kataria'

class Employee:
    'Employee Class'

    def __init__(self, name, age):
        self.name=name
        self.age= int(age)

    def __repr__(self):
        return 'Name: %s; Age: %i' %(self.name, self.age)

    def __lt__(self, other):
       return self.age < other.age

if __name__ == "__main__":
    emp1 = Employee("Ankur", 26)
    emp2 = Employee("Sneha", 25)
    emp3 = Employee("Shalini", 29)

    emp_lst = [emp1,emp2,emp3]
    print("Unsorted")
    for e in emp_lst:
        print (e)

    print("Sorted list")
    for e in sorted(emp_lst):
        print (e)