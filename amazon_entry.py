#import cloths.men_clothing  # import packagename.modulename
from cloths.men_clothing import *
from cloths.women_clothing import *
from electronics.cameras import *

def start_searching(category):
    if category == 1:
        men_party_wear()
        men_ethnic_wear()
        men_jeans_tshirts()

    elif category == 2:
        women_ethnic_wear()
        women_party_wear()
        women_jeans_tshirts()

    elif category == 3:
        digital_camera()



if __name__ == "__main__":
    print("1.Men Cloths")
    print("2.Women Cloths")
    print("3.Electronic Cameras")
    category = input("What do you want to purchase:")
    start_searching(int(category))
