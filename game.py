paths = {
    "mirrors": ["priestess","professor"],
    "priestress" : ["professor", "giant"],
    "professor" : ["mirror_rooms","giant","siamese"],
    "giant" : ["professor", "siamese"],
    "siamese" : ["giant", "mirrors", "giant_world"]
}


#print(", ".join(paths["mirrors"]))

#if target in paths[room]:
#    ...



#STARTING POINT
room = "mirrors"

wait = False
talk_priestress = False
grumpy_professor = False
turned_giant = False

import time


print(                  #THE STORY STARTS
    """       
    \x1B[3mTHE LIMBO\x1B[0m
    
    You are in a empty rooms full of mirrors. Neons are filling the space with bright light. 
    The room seems endless and you captivated by the shape of infinity unfolding in from on you. 
    Amazed by the vision of such space, you can't stop looking at the only thing that can be started at, 
    yourself.
    Soon, you notice that the longer and the closer you look at yoursel, the room changes. As the mirrors 
    are moving and distorting the reflection of your body, the light tunrs into violent flashlights.
    Your body is now unrecognizable and you cannot bare looking at your reflection anymore. 
    \nSuddenly... 
    The lights turns off.
    """)

node_mirrors = {        #NODE AT THE MIRROR ROOM
   "text": """
   \n\x1B[3mWhat do you do?
    - You panic and try to find a door (type : panic)
    - You wait until the light comes back (type : wait) : \x1B[0m""", 
   "panic":              #you wake up the grumpy professor. Nothing happens. Come back to the mirrors.
    """
    The room trembles again.
    It seems like you are back in the osbure and hostile environment. You're again very scared.""",
   "wait":               #now you entered another room and the talk_priestress appear.
   """
   Another woman appears instead of your reflections in the mirror.
   She has no arm and a big roll of steal instead of her legs. You try to find yourself in any 
   other mirror but no, she is in every corner and reflection of this room...
   "Oh hi! You waited for me?\" """              
}

node_grumpy_prof = {    #INTERACTION WITH GRUMPY PROF. DEAD END. RETURN TO MIRROR ROOM.
    "text": """
    You can't find the door and the space becomes more and more stressful. You here a loud noise 
    followed by a long and heavy silence in complete darkness.
    Eventually, lhe light turns on and you see a man standing in front of you.
    He looks like a mad and grumpy old man.
    "HEY! It was just time to sleep dude. Why making so much tourment around here. 
    Urrr... thank you for waking me up! Really... how kind!"
    \n\x1B[3m- You answer : 
    - Who are you? (type : who) 
    - I'm sorry (type : sorry)\x1B[0m""",
    "sorry": """
    Well... Try to relax, you're gonna be fine!""",
    "who": """
    I'm professor Kanye and I was sleeping. Would you mind leaving me in peace?!
    As the professor is more and more annoyed by your attitude, you see the space 
    collapse around you...
    """
}


talk_priestress = {     #INTERACTION PRIESTRESS. MOVE FORWARD
   "text": """\n\x1B[3m
   - You answer :
   I'm stuck! (type : stuck)
   Where am I? (type: where)
   Who are you? (type : who)\x1B[0m""", 
   "stuck":"""\n
   She answers: \"You are not stuck. You've been patient, waiting for the door to open. 
   You are most certainly about to enter a secret and wonderful world.\"
   """, 
   "who": """
   I'm Marta. I used to be a none in the human world, but I couldn't find my true purpose there.
   It felt so limiting, frustrating! But I still had faith... 
   One day, I was on my way to church and fell into a hole! 
   And here I am, living with a giant!
   \nYou answer : 
   - A giant?! (type : giant)
    """,
    "where": """
    - Ah, the limbo space… it is a realm of endless twilight, where darkness and light dance 
   in an eternal struggle. The mirrors on the walls reflect the fractured images of reality. 
   They distort the perceptions of unsettled minds. Time flows differently here and those who 
   find themselves here are caught in an endless cycle of uncertainty. It is a place where 
   your deepest fears and desires are laid bare — a test of resilience and inner strength.
   Even a giant lives here. Well... he's been captured!
   \n\x1B[3m- You answer : 
   - A giant?! 
   (type : giant)\x1B[0m"""
}

talk_priestress_2 = {       #WHEN SHE ASKS TO GO SEE PROFESSOR, OR STRAIGHT TO THE GIANT

    "giant" : """
    - Yes indeed... He's been captured, ensnared by the professor who conducts all sorts 
    of experiments within these shadowy confines. It's said that this limbo serves as a portal 
    to a world of giants, a realm of wonder and magic beyond imagination. The professor, driven 
    by his insatiable curiosity, may even seek to turn you into a giant yourself, should you venture 
    further into his domain. 
    \n\x1B[3mYou answer :
    - That sounds like a crazy idea... Can I meet the professor? (type : prof)
    - What an horrible story! Can we do something about this poor giant? (type : help)\x1B[0m
    """,
    "prof" : """
    - Sure, I'll call him for you!""",
    "help" : """\n
    I agree... The Siamese sisters hold the giant captive. It's been impossible for me 
    o gain their favor; they abhor any form of religion. But they'll take a liking to you, and 
    I'm confident you'll be able to distract them. 
    Good luck...
    """
}


talk_professor = {
    "text_0" : """
    It is dark again but you learned to be patient. 
    The light turns on. You see a man standing in front of you.
    He looks like a mad and grumpy old man.""",
    "text_1" : """
    It is dark again but you learned to be patient. 
    The light turns on. Here he is...
    "- You again?! You never give up do you?\" """,
    "text" : """
    You're coming from the prietress I can see.
    \n\x1B[3mYou answer : 
    - Yes, she told me I could become a giant 
    (press enter)\x1B[0m""",                                                                         #input from that : ()
    "text_giant" : """
    \n- Ah! She speaks too much. It is true  you coulf turn yoursel 
    into a giant if you'd like.
    I'm not sure you're truely ready for it. But today, I don't really care!
    \nWould you like to become a giant? 
    \n\x1B[3m(type : "yes" or "no")\x1B[0m""",                              #input for that : yes or no 
    "giant_giant" : """
    I guess you'll be two giants stuck in here right now...
    As he leaves the room. Your body enters an altered dimension. You feel like you're
    loosing control over it. The mirrors break and see the terrifying body of the siamese sisters.
    They are laughing. Are holding a big doll in their hand. You panic but can't move any 
    of your giant body.
    You are stuck in this and there is nothing you can do. You realize you are the doll in their 
    hands and are prisoner
    with who you finally can see next to you, the other gentle giant. 
    \n\nTHE END. """,
    "human_giant" : """
    - Oh wow, I'm surprised! Good for you! I guess it wouldn't have been nice 
    to be in the hands of the siamese. They can be quite mean sometimes. But who know, you might get along with them. 
    \n \x1B[3m(press enter to see the end...)\x1B[0m
    """
}


#


while not wait:         #WHILE LOOP, MIRROR ROOM
    print(node_mirrors['text'])
    reaction_priestress = input()
    if reaction_priestress.lower() in ['panic', 'p']:
        print(node_grumpy_prof["text"])
        reaction_grumpy = input()
        if reaction_grumpy.lower() in ["who", "who are you"]:
            print(node_grumpy_prof["who"])
            print(node_mirrors['panic'])
        elif reaction_grumpy.lower() in ["sorry"]:
            print(node_grumpy_prof["sorry"])
            print(node_mirrors['panic'])
        else: 
            print("try again")
        grumpy_professor = True
    else:
        print(node_mirrors ["wait"])
        wait = True
room = "priestress"



#reaction

#grumpy professor amy be True or False.

talked_priestress = False

while not talked_priestress and room == "priestress":         #INTERACTION WITH PRIETRESS
    print(talk_priestress['text'])
    reaction_priestress = input("")
    if reaction_priestress.lower() in ['stuck']:            #if I'm stuck, I go back to the loop and ask who or where
        print(talk_priestress["stuck"])
    elif reaction_priestress.lower() in ["where"]:
        print(talk_priestress["where"])
        talked_priestress = True
    else:
        print(talk_priestress["who"])                       #if i ask who, I move forward with another input "giant?"
        talked_priestress = True

while talked_priestress and room =="priestress":
    reaction_priestress_2 = input()
    print(talk_priestress_2["giant"])                       #if i ask where, I also move forward, arrive at the same point : "giant?"
    reaction_priestress_2 = input()
    if reaction_priestress_2.lower() in ["prof"]:           #another if arrives, to go to the professor, or the go straight to the siamese.
        print(talk_priestress_2["prof"])
        room = "professor"                                  #to professor
    else:
        print(talk_priestress_2["help"])
        time.sleep(3)
        room = "siamese"                                    #to siamese




### ERROR WITH STUCK 
#Doesn't go again up to enter again where, or who but after asking for an input goes straight to the else 


if room == "professor":
    
    if grumpy_professor == True:                            #if I met the professor already, he'll recognize me
        print (talk_professor["text_1"])
    else:                                                   #if not, I discover him.
        print(talk_professor["text_0"])
    print(talk_professor["text"])
    reaction_professor = input()
    print (talk_professor["text_giant"])
    reaction_professor = input()
    if reaction_professor.lower() in ["yes"]:
        print(talk_professor["giant_giant"])
        #dark end of the game
    else:
        print(talk_professor["human_giant"])
        reaction_prietress = input()
        time.sleep(3) 
        room = "siamese"
        #happy ending of the game

    




room = "siamese"

print ("""
\nAs you approach the Siamese sisters, their initially skeptical expressions soften as you greet 
them warmly. Surprised by your friendliness, they cautiously engage in conversation, gradually 
opening up about their desires and fears. Through your genuine empathy and understanding, you quickly 
earn their trust. Meanwhile, you remember the gentle giant you left behind in the limbo room. 
With newfound determination, you return to release him from his imprisonment. As the barriers shatter, 
you both step into a radiant light, escaping the nightmare once and for all. 
\nEmerging into a world beyond imagination, you find yourselves in a vast wonderland of towering trees, 
shimmering lakes, and endless skies. This realm is inhabited by gentle giants like yourselves, 
living in harmony with nature and magic.
\nFilled with gratitude for your kindness, the giant offers you a choice. You can stay in this enchanting 
paradise, joining the community of magical giants, or return to your own world. Whatever you decide,
the giant assures you that you will always be welcomed with open arms.
\nWith a heart full of joy and wonder, you choose to embark on this new adventure, embracing the magic and 
beauty of the giant wonderland. As you journey alongside your newfound friends, you know that no matter 
where life may lead, you will always cherish the bonds forged in this extraordinary realm of dreams.
\n\nTHE END.
       """)

