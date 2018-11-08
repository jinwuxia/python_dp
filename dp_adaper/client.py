from dog import Dog 
from cat import Cat 
from adapter import Adapter 

def main():
    objects = []
    
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))

main()
