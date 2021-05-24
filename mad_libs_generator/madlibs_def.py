def madlib_family():
    name = input("what is your name? ")
    age = int(input("How old are you? "))
    city = input("what is your city? ")
    country = input("what is your country? ")
    prof = input("What do you do in your live? ")
    num_member = int(input("How many people in your family? "))
    num_sibling = int(input("How many sister/brother? "))
    return "Let me talk about my family and myself.\nMy name is " + name + ". I'm " + str(age) + "year old. I am " \
            "living in " + city + ", " + country + ". I'm a(an) " + prof + "."+ "My family have " + str(num_member) + \
            " people. My parents and my " + str(num_sibling) + "sibling in all. "


def madlib_color():
    color = input("what is your favorite color? ")
    people = input("Who make your thing about the color")
    thing = input("Input the thing concerns about the color? ")
    pos = input("where did you keep the thing? ")

    return "My lucky color is " + color + ". It makes me things about " + people + ". When I was a kid, almost my " \
            "clothes is " + color + ". My mother gave me a(an) " + thing + " in my birthday" + ". It is my first " + \
            color + " " + thing + " I have." + "I have kept it in " + pos + " in my room. I love it so much. "


def madlib_dream():
    adjective = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person = input('enter a person name : ')
    adjective1 = input('enter a adjective : ')
    insect = input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    return 'Last night I dreamed I was a ' + adjective + ' butterfly with ' + color + \
           ' splotches that looked like ' + thing + ' .I flew to ' + place + ' with my best friend and ' \
           + person + ' who was a ' + adjective1 + ' ' + insect + ' .We ate some ' + food + 'when we got there and ' \
           'then decided to ' + verb + ' and the dream ended when I said-- lets ' + verb + '. '
