class User:
    gold_card_points = 0
    
    is_rewards_member = False

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Status: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        # print(f"Member status set to: {self.is_rewards_member} Gold Card Balance: {self.gold_card_points}")
        return self
        
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self

user1= User('Tad', 'Deck', 'Tdeck@gmail.com', '56')
user2= User('Connor', 'West', 'ConWest@gmail.com', '27')
user3= User('Taylor', 'Dimelio', 'TaylorD@gmail.com', '19')

user1.enroll().spend_points(50).display_info()

user2.enroll().spend_points(80).display_info()

user3.display_info()