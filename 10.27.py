""" class Person :
	name = "python"
	age = 23
	number = "01012345678"
 
 
p = Person()
print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)
 """


""" 
class Person :
	name = "python"
	age = 23
	number = "01012345678"
	def getIntroduce(self):
		return f"My name is {self.name}"
 
 
p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number)
print(p1.getIntroduce)

 """
 
 
"""  
class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  
  
p = Person("apple", "22", "0111")
p1 = Person("bee", "4", "0137")
p2 = Person("sam", "46", "01005")

print(p.name,p.age,p.number)
print(p1.name,p1.age,p1.number)
print(p2.name,p2.age,p2.number)

 """
"""  
class Person :
	count = 0

	def __init__(self, name, age, number) :
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

p = Person("apple", "22", "0111")
print(p.name)
print(p.count)
p1 = Person("bee", "4", "0137")
print(p1.name)
print(p1.count)
p2 = Person("sam", "46", "01005")
print(p2.name)
print(p2.count)

print(p.count)
print(p1.count)
print(p2.count)

 """



class Person :
	count = 0

	def __init__(self, name, age, number) :
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count

p = Person("apple", "22", "0111")
print(p.name)
print(p.getCount())
p1 = Person("bee", "4", "0137")
print(p1.name)
print(p1.getCount())
p2 = Person("sam", "46", "01005")
print(p2.name)
print(p2.getCount())

