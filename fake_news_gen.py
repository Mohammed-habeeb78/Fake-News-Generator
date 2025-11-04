import random 

#Subject names
subjects =["Virat Kohli","PM Modi","Speed","Group of Donkeys"]

#action list
actions = ["dances","showers","does a backflip","does garba","screams"]

#place list
places = ["at rooftop","in Dubai","in Bihar","infront of White House"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = ("BREAKING NEWS: " + subject +" "+ action +" "+ place + "!")
    print(headline) 

    user_choice = input("Do you want to generate a new headline (yes/no)?")
    if user_choice.lower() == 'no':
        break

print("Shoutout to all news channels")