init:
    transform right_half_center:
        xalign 0.75  # Moves the image toward the right half
        yalign 0.5   # Centers it vertically

    transform the_center:
        xalign 0.5 
        yalign 0.5

define Isles = Character('Dr. Isles', color = "#c8ffc8")
image ph7 = "ph7.png"
image ph4 = "ph4.png"
image ph11 = "ph11.png"
image phtube = "phtube.png"


label start:
    play music "illurock.opus"
    scene lab with fade

    # to randomly choose a liquid each time
    python:
        import random
    
        # Define different liquid types and their properties
        liquids = {
            "Water": {"color": "Clear", "smell": "Odorless", "pH": 7, "flammable": False, "reaction": "No reaction"},
            "Alcohol": {"color": "Clear", "smell": "Sharp", "pH": 4, "flammable": True, "reaction": "No reaction"},
            "Bleach": {"color": "Yellowish", "smell": "Strong chemical", "pH": 11, "flammable": False, "reaction": "Turns cloudy"},
            "Cyanide": {"color": "Clear", "smell": "Bitter Almond", "pH": 11, "flammable": False, "reaction": "Bubbles/ Fizziling"},
        }

        # Randomly select a liquid
        # the liquid
        selected_liquid = random.choice(list(liquids.keys()))
        # the liquid properties
        liquid_properties = liquids[selected_liquid]


    "Dr. Isles places a test tube on the table."
    Isles "We found an unknown liquid at the scene. Let's analyze it."

    # Show randomly chosen liquid
    "The liquid appears to be {b}[liquid_properties['color']]{/b} and has a {b}[liquid_properties['smell']]{/b} smell."

label menustart:
menu:
        "Perform pH test":
            jump ph_test
        "Check flammability":
            jump flammability_test
        "Perform chemical reaction test":
            jump chemical_test
        "Restart":
            jump start

label ph_test:
    show phtube at the_center
    "You dip a pH strip into the liquid."
    hide phtube
    "The strip indicates a pH level of {b}[liquid_properties['pH']]{/b}."

    if liquid_properties['pH'] < 7:
        show ph4 at right_half_center
        Isles "What conclusion can you make? "
        hide ph4
        # Isles "This is quite acidic. It could be a toxic substance."
    elif liquid_properties['pH'] > 7:
        show ph11 at right_half_center
        Isles "What conclusion can you make? "
        hide ph11
        # Isles "This is highly alkaline. Possibly a cleaning agent."
    else:
        show ph7 at right_half_center
        Isles "What conclusion can you make? "
        hide ph7
        # Isles "This is neutral. It might just be water or alcohol."


    
    
    # can add interactive option for "acidic, alkaline, neutral"


    

    jump next_step

label flammability_test:
    "You carefully expose a small sample to an open flame."

    if liquid_properties['flammable']:
        "The liquid {b}ignites instantly{/b}!"
        Isles "This is highly flammable. "
        # "It could be alcohol or another accelerant."
    else:
        "{b}Nothing happens{/b}."
        Isles "It doesn't burn."
        # "Likely not an accelerant."

    jump next_step

label chemical_test:
    "You mix the liquid with a kind of acid."

    "The reaction: {b}[liquid_properties['reaction']]{/b}."

    Isles "What does this suggest?"

    # if liquid_properties['reaction'] == "Bubbles/ Fizziling":
    #     Isles "Interesting! This indicates a possible toxic substance."
    # elif liquid_properties['reaction'] == "Turns cloudy":
    #     Isles "This suggests it's a strong cleaning agent, possibly bleach."
    # else:
    #     Isles "No reaction. This liquid might not be dangerous."

    jump next_step

label next_step:
    menu:
        "Make a conclusion":
            jump conclusion
        "Perform another test":
            # Goes back to menu and allow additional tests
            jump menustart

label conclusion:
    menu:
        "This is Water":
            if selected_liquid == "Water":
                Isles "Correct! This liquid is harmless."
                jump again
            else:
                Isles "Not quite. Let's analyze it again."
                jump conclusion
        "This is Alcohol":
            if selected_liquid == "Alcohol":
                Isles "Correct! This could be an accelerant in arson."
                jump again
            else:
                Isles "That doesn't seem right. Try again!"
                jump conclusion
        "This is Bleach":
            if selected_liquid == "Bleach":
                Isles "Correct! This could have been used to destroy evidence."
                jump again
            else:
                Isles "Not quite. Maybe you wanna review the test?"
                jump conclusion
        "This is a Cyanide":
            if selected_liquid == "Cyanide":
                Isles "Correct! This could be key evidence in Cyanideing."
                jump again
            else:
                Isles "That's incorrect. Give it another shot! "
                jump conclusion
        "I want to perform another test":
            jump menustart

label again:
    Isles "Do you wanna play another round?"
    menu:
            "yes":
                jump start
            "no":
                return

    return
