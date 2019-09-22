import random
def drink_recipes():
    questions = [
        "Do ye like yer drinks strong?",
        "Do ye like it with a salty tang?",
        "Are ye a lubber who likes it bitter?",
        "Would ye like a bit of sweetness with yer poison?",
        "Are ye one for a fruity finish?"
    ]
    incredients = [
        ["glug of rum", "slug of whisky", "splash of gin"],
        ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        ["sugar cube", "spoonful of honey", "spash of cola"],
        ["slice of orange", "dash of cassis", "cherry on top"]
    ]
    print("Please input y (yes) or n (no) :")
    list =[]
    index_incre = 0
    for ask in questions:
        str = input(ask + " [Y/N] ")
        if ( (str == "y") | (str == "Y") ):
            list.append(random.choice(incredients[index_incre]))
            index_incre += 1
    print("Your drink recipes are :")
    print(", ".join(list))
drink_recipes()