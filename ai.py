import random

def compliment_generator(name, age, gender):
    m_compliments = ["You are the most handsome person in the world", "You are very attractive","You are very handsome!", "You have a great smile!"]
    w_compliments = ["You are the most beautiful person in the world", "You are very pretty!", "You are very cute!"]
    b_compliments = ["You are handsome young man", "You look smart!", "You are very handsome!"]
    g_compliments = ["Cute Girl!", "You are pretty!", "Strong girl!"]
    bad_m_response = ["You are very ugly!", "You are not handsome"] 
    bad_f_responses = ["You are not beautiful", "You are ugly", "You aren't cute at all!"]
    # List variables to store strings of compliments and insults
    # Modify text inside a string to change the output
    
    good_response_probability = 0.7  # Adjust the number to change the good response probability
    bad_response_probability = 1 - good_response_probability

    if gender.capitalize() == "Male":
        if age == 16 and name.upper() == "SY SOPHANETH" or name.upper() == "NETH" or name.upper() == "SOPHANETH":
            response = "You are my CREATOR I cannot rate you sir!"
        elif random.random() < good_response_probability:
            if age >= 18:
                response = random.choice(m_compliments)
            else:
                response = random.choice(b_compliments)
        else:
            response = random.choice(bad_m_response)
        return f"{name}, {response}"
    elif gender.capitalize() == "Female":
        if random.random() < good_response_probability:
            if age >= 18:
                response = random.choice(w_compliments)
            else:
                response = random.choice(g_compliments)
        else:
            response = random.choice(bad_f_responses)
        return f"{name}, {response}"

def main():
    while True:
        print("\nHello! I am an AI that can judge based on how you look!\n")
        name = input("What is your name?: ")
        age = int(input("\nWhat is your age?: "))
        gender = input("\nWhat is your gender? Male or Female?: ")
        print("==========================")
        print("          Result")
        print("==========================")
        print("Your name is",name)
        print("Your age is",age)
        print("and you are a",gender)
        print(compliment_generator(name, age, gender))
        if age == 16 and name.upper() == "SY SOPHANETH" or name.upper() == "NETH" or name.upper() == "SOPHANETH":
            repeat = input("\nCreator! Would you let me to try again? (yes/no): ")
        else:
            repeat = input("\nHello! Would you like to try again? (yes/no): ")
        if repeat.lower() != "yes":
            print("Goodbye! See you later!")
            break

if __name__ == "__main__":
    main()