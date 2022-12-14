# Inheritance
class Phone: #base class / parent class
    def __init__(self, brand, model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling{number}...."

class Smartphone(Phone): #derived/child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand, model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera = rear_camera

phone=Phone('Nokia','1100',1000)
smartphone=Smartphone('Oneplus','5',30000,'6 GB','64GB','20MP')
print(phone.full_name())
print(smartphone.full_name()+f" and price is {smartphone.price}")

