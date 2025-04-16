import art
import game_data
import random

continue_if = True
current_score = 0
compare_a = random.choice(game_data.data)
#check the answer
while continue_if:
    print(art.logo)

    # choose a library randomly in the list
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")

    # Questions, is all the people they can only occur once? yes

    print(art.vs)
    game_data.data.remove(compare_a)
    compare_b = random.choice(game_data.data)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

    # make compare a == compare b last round
    # make a loop

    user_answer = input("Who has more followers? Type 'A' or 'B':").upper()

    if compare_a['follower_count'] > compare_b['follower_count'] and user_answer == "A":
        current_score +=1
        print("\n" * 20)
        print(f" You are right! Current score: {current_score}.")
        compare_a = compare_b
    elif compare_a['follower_count'] < compare_b['follower_count'] and user_answer == "B":
        current_score += 1
        print("\n" *20 )
        print("You are right! Current score: {current_score}.")
        compare_a = compare_b
    elif compare_a['follower_count'] > compare_b['follower_count'] and user_answer == "B":
        print(f"Sorry,that's wrong. Final score: {current_score}")
        continue_if = False
    elif compare_a['follower_count'] < compare_b['follower_count'] and user_answer == "A":
        print(f"Sorry,that's wrong. Final score: {current_score}")
        continue_if = False
    else:
        print("You put sth can't be defined.")
