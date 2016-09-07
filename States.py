"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Zestern Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Z"}
width = len(max(STATE_NAMES.values()))
for state, value in STATE_NAMES.items():
    print("{:{width}} is {:}".format(state, value, width = width))

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()


