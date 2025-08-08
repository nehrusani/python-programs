'''
How to use class:

- 1:  First create one class for example: use_class.py
- 2:  Create some functions for example: def india
      Remember, first initialise it using __init__

- 3:  Once it is created use another file for example:  use_module.py
      
    ```
    from use_class import use_class
    a = input("Enter a word: ")
    b = int(input("Enter a number: "))

    var = use_class(a,b)
    var.india()
    ```

4. Once it is created, then you can run use_class.py it will ask you word and integrer and print that


'''
class use_class :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def india(self):
        print(self.a,self.b)