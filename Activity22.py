#2d list
#mcu
#LEVEL 1: 
iron_man = ["Genius billionaire philanthropist", "Powered armor suit"]
captain_america = ["Super soldier from World War II", "Enhanced strength and Vibranium shield"]
thor = ["God of Thunder from Asgard", "Lightning manipulation and Mjolnir"]
star_lord = ["Leader of the Guardians of the Galaxy", "Expert marksman and Element Guns"]
groot = ["Flora colossus from Planet X", "Body regeneration and branch manipulation"]
rocket = ["Genetically engineered raccoon", "Master tactician and heavy weaponry"]
doctor_strange = ["Master of the Mystic Arts", "Eldritch magic and Eye of Agamotto"]
wong = ["Sorcerer Supreme of Earth", "Mystic portals and spells"]
spider_man = ["High school hero from Queens", "Wall-crawling, spider-sense, and web-shooters"]
ned = ["Peter Parker's best friend", "Tech support and Sling Ring magic"]
mj = ["Observant classmate and friend", "Sharp intellect and deduction"]
shang_chi = ["Master of martial arts", "Ten Rings energy manipulation"]
katy = ["Valet driver and best friend", "Expert archery and driving skills"]
dr_doom =["Genius Scientist and Sorcerer", "Monarch of the nation Latveria"]
#level 2
avengers_movie = {"Iron Man": iron_man, "Captain America": captain_america, "Thor": thor, "Doctor DOOM": dr_doom}
guardians_series = {"Star-Lord": star_lord, "Groot": groot, "Rocket": rocket}
doctor_strange_movie = {"Doctor Strange": doctor_strange, "Wong": wong}
no_way_home = {"Spider-Man": spider_man, "Ned": ned, "MJ": mj}
shang_chi_movie = {"Shang-Chi": shang_chi, "Katy": katy}
avengers_doomsday = {"Doctor Doom": dr_doom, "Thor:": thor}
#level 3:
infinity_saga = {"The Avengers": avengers_movie, "Guardians of the Galaxy": guardians_series, "Doctor Strange": doctor_strange_movie}
multiverse_saga = {"Spider-Man: No Way Home": no_way_home, "Shang-Chi and the Legend of the Ten Rings": shang_chi_movie, "AVENGERS DOOMSDAY": dr_doom}

#level 4:
mcu = {"Infinity Saga": infinity_saga, "Multiverse Saga": multiverse_saga}

print("=== 1. Going down one level at a time ===")
print(mcu["Infinity Saga"]["The Avengers"]["Iron Man"][1])

print()
print("=== 2. Loop level 1: categories ===")
for category in mcu:
    print(category)

print()
print("=== 3. Loop levels 1-2: categories and titles ===")
for category, titles in mcu.items():
    print(category)
    for title in titles:
        print(" -", title)

print()
print("=== 4. Loop ALL levels ===")
for category, titles in mcu.items():
    print(category)
    for title, characters in titles.items():
        print("  " + title)
        for name, info in characters.items():
            print("    " + name)
            print("      Description:", info[0])
            print("      Power:", info[1])

print()
print("=== 5. Count every character ===")
count = 0
for titles in mcu.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1
print("Total characters:", count)