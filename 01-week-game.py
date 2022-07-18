country = {
    "airport": [
        "China", "Japan",
        "This is Gabiland airport and you will always have two destinations per turn to test your knowledge of the world's seven wonders,\ntake pictures of what you'll see along the way and complete your album."
    ],
    "china": [
        "Mexico", "USA",
        "Congratulations, you took your first photo on the Great Wall of China.\nIt has been considered a wonder of the world since 1987."
    ],
    "mexico": [
        "Jordan", "Israel",
        "Congratulations, you took your second photo in Chichen Itza.\nIt has been considered a wonder of the world since 1988."
    ],
    "jordan": [
        "Peru", "Chile",
        "Congratulations, you took your third photo in Petra.\nIt has been considered a wonder of the world since 1985."
    ],
    "peru": [
        "Brazil", "Argentina",
        "Congratulations, you took your fourth photo in Machu Picchu.\nIt has been considered a wonder of the world since 1983. You are almost there"
    ],
    "brazil": [
        "India", "Germany",
        "Congratulations, you took your fifth photo in Christ the Redeemer.\nIt has always been considered a wonder of the world in my heart LOL."
    ],
    "india": [
        "Congrats, you completed your trip.\nLet's take the last photo together at the Taj Mahal.\nLook how beautiful this place is."
    ]
}

location = 'airport'
destination = ''

while destination != 'exit':
    destination = input(
        f'\nYou arrived at {location}.\n{country[location][2]}\nPlease choose your next destination, you would like to go to {country[location][0]} or {country[location][1]}?'
    ).lower()
    print("\n")
    if destination != country[location][0].lower() and destination != 'exit':
        location = 'airport'
        print(
            'the destination you choose is not one of the 7 wonders, you will be redirect to the airport'
        )
    elif destination == 'india':
        print(country[destination][0])
        destination = 'exit'
    else:
        location = destination