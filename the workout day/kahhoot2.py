from kahhoot import Kahhoot
obj = Kahhoot(
    name=str(input("name : ")),
    age=int(input("age : ")),
    job=str(input("job : "))
)
print("you are in kahhoot accepted ")

print(obj.name, obj.age, obj.job)

