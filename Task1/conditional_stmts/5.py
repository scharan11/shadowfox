total_jumping_jacks = 100
completed = 0

for i in range(10):
    completed += 10

    print()
    print("You completed", completed, "jumping jacks.")

    if completed == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break

    remaining = total_jumping_jacks - completed
    print("Jumping jacks remaining:", remaining)
