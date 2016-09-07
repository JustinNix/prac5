COLOURS_HEXADECIMAL = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
                       "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378"}
width = len(max(COLOURS_HEXADECIMAL.keys()))
for colour, hexadecimal in COLOURS_HEXADECIMAL.items():
    print("{:{width}} is {:{width}}".format(colour, hexadecimal, width=width))

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in COLOURS_HEXADECIMAL:
        print(colour, "is", COLOURS_HEXADECIMAL[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").lower()
