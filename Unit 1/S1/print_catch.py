def print_catchphrase(character):

    phrases = {
        "Pooh": "Oh bother.",
        "Tigger": "TTFN: Ta-ta for now!",
        "Eeyore": "Thanks for noticin' me.",
        "Christopher Robin": "Silly old bear."
    }


    if character in phrases:
        print(phrases[character])
    else:
        print("I don't know" + character + "'s catchphrase.")


character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)