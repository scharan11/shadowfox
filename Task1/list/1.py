justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# 1. Calculate number of members
print("1. Number of members:", len(justice_league))
print("List:", justice_league)
print()

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("2. After adding Batgirl and Nightwing:")
print(justice_league)
print()

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("3. After moving Wonder Woman to the beginning:")
print(justice_league)
print()

# 4. Put Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")

aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")

print("4. After moving Green Lantern:")
print(justice_league)
print()

# 5. Replace list with new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("5. New Justice League:")
print(justice_league)
print()

# 6. Sort alphabetically
justice_league.sort()

print("6. Alphabetically sorted Justice League:")
print(justice_league)

print()
print("New leader:", justice_league[0])
