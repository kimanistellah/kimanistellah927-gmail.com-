# ACTIVITY 1: Design Your Own Class (Smartphone with Inheritance)
class Smartphone:
    """Base class representing a smartphone"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now on"
    
    def power_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now off"
    
    def use_app(self, app_name):
        if self.is_on:
            return f"Using {app_name} on {self.brand} {self.model}"
        return "Phone is off. Cannot use apps."
    
    def __str__(self):
        return f"{self.brand} {self.model}"


class GamingPhone(Smartphone):
    """Specialized smartphone for gaming with enhanced features"""
    
    def __init__(self, brand, model, gpu):
        super().__init__(brand, model)
        self.gpu = gpu
        self.game_mode = False
    
    def toggle_game_mode(self):
        self.game_mode = not self.game_mode
        status = "enabled" if self.game_mode else "disabled"
        return f"Game mode {status}"
    
    def use_app(self, app_name):
        base_result = super().use_app(app_name)
        if self.game_mode and "game" in app_name.lower():
            return base_result + " with enhanced performance"
        return base_result
    
    def __str__(self):
        return f"{super().__str__()} (Gaming Edition)"

# ACTIVITY 2: Polymorphism Challenge (Animals with move() method)
class Animal:
    """Base class representing an animal"""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} moves"
    
    def __str__(self):
        return self.name


class Bird(Animal):
    """Bird class that overrides move method"""
    
    def move(self):
        return f"{self.name} flies 🕊️"


class Fish(Animal):
    """Fish class that overrides move method"""
    
    def move(self):
        return f"{self.name} swims 🐠"


class Dog(Animal):
    """Dog class that overrides move method"""
    
    def move(self):
        return f"{self.name} runs 🐕"

# DEMONSTRATION CODE
if __name__ == "__main__":
    print("=" * 50)
    print("OOP ASSIGNMENT DEMONSTRATION")
    print("=" * 50)
    
    # Activity 1: Smartphone Demonstration
    print("\nACTIVITY 1: SMARTPHONE WITH INHERITANCE")
    print("-" * 40)
    
    # Create smartphone instances
    regular_phone = Smartphone("Apple", "iPhone 14")
    gaming_phone = GamingPhone("ASUS", "ROG Phone 6", "Adreno 730")
    
    # Demonstrate smartphone functionality
    print(regular_phone.power_on())
    print(regular_phone.use_app("Safari"))
    print(regular_phone.power_off())
    print()
    
    print(gaming_phone.power_on())
    print(gaming_phone.toggle_game_mode())
    print(gaming_phone.use_app("Genshin Impact"))
    print(gaming_phone.use_app("Calendar"))
    
    # Activity 2: Polymorphism Demonstration
    print("\nACTIVITY 2: POLYMORPHISM CHALLENGE")
    print("-" * 40)
    
    # Create animal instances
    animals = [
        Bird("Robin"),
        Fish("Nemo"), 
        Dog("Buddy")
    ]
    
    # Demonstrate polymorphism - each animal moves differently
    for animal in animals:
        print(animal.move())
    
    print("\n" + "=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("=" * 50)
