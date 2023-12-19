class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.gold_card_points = 0
        self.is_rewards_member = False
        
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
        print(self.is_rewards_member)
        return self
        
    def enroll(self):
        if self.is_rewards_member == False:
            self.gold_card_points = 200
            self.is_rewards_member = True
        else:
            print("Already a member")
        return self
        
    def spend_points(self, amount):
        if self.gold_card_points > 0:
            self.gold_card_points -= amount
        else:
            print("No points left")
        return self
        
me = User("Matt", "Baldwin", "matt@test.com", 39)
me.display_info()

him = User("Noah", "Baldwin", "noah@test.com", 6)
her = User("Molly", "Baldwin", "molly@test.com", 35)

me.enroll()
me.spend_points(50)

him.enroll()
him.spend_points(80)

me.display_info()
him.display_info()

me.enroll()

her.spend_points(40)

me.enroll().spend_points(50).display_info()

him.enroll().spend_points(80).display_info()