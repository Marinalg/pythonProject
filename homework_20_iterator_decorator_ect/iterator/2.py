
class MyWorkingDay:
    days = [1, 2, 3, 4, 5, 6]
    def __iter__(self):
      self.start_index = 1
      return self

    def __next__(self):
      start_index = self.start_index
      self.start_index += 1
      return start_index

myclass = MyWorkingDay()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))