Favourite_letters=["a","b","m","n","c","e","k","p","h","q"]
response=input("Do you want to play/start the game, type yes if you want to? Don't type a letter more than once:")
if response=="yes":
    count = 0
    for i in range(10):
        GuessLetter = input("There are letters I like to type, can you guess?")
        for j in Favourite_letters:
            if GuessLetter==j:
                count+=5
    print("congratulations!","you have scored",count,"thank you so much for playing my game!")
else:
    print("That is totally okay!")




