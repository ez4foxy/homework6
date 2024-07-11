my_dict = {"Флэм": 22, "Ханна": 12, "Ванилла": 11}
print(my_dict)
print(my_dict["Флэм"])
my_dict["Мускат"] = 28
print(my_dict["Мускат"])
my_dict.update({"Чика": 7,
                "Ваппа": 9})
Name = my_dict.pop("Ванилла")
print(Name)
print(my_dict)

my_set = {4,7,9,11,22,22,9}
print(my_set)
my_set.add (28)
my_set.add(12)
my_set.discard(4)
print(my_set)

