# Global Warming Facts Quiz
# Author - Immanuel Kolapo

"""This application administers a five-question multiple-
choice quiz on global warming, calculates the number
of correct answers, and returns a message to the user"""

questions = \
{
    "What is the global warming controversy about?": {
        "A": "the public debate over whether global warming is occuring",
        "B": "how much global warming has occured in modern times",
        "C": "what global warming has caused",
        "D": "all of the above"
    },
    "What movie was used to publicize the controversial issue of global warming?": {
        "A": "the bitter truth",
        "B": "destruction of mankind",
        "C": "the inconvenient truth",
        "D": "the depletion"
    },
    "In what year did former Vice President Al Gore and a U.N. network of scientists share the Nobel Peace Prize?": {
        "A": "1996",
        "B": "1998",
        "C": "2003",
        "D": "2007"
    },
    "Many European countries took action to reduce greenhouse gas before what year?": {
        "A": "1985",
        "B": "1990",
        "C": "1759",
        "D": "2000"
    },
    "Who first proposed the theory that increases in greenhouse gas would lead to an increase in temperature?": {
        "A": "Svante Arrhenius",
        "B": "Niccolo Machiavelli",
        "C": "Jared Bayless",
        "D": "Jacob Thornton"
    }
}

print("\nGlobal Warming Facts Quiz")
prompt = ">>> "
correct_options = ['D', 'C', 'D', 'B', 'A']
score = 0

for correct_option, (question, options) in zip(correct_options, questions.items()):
    print("\n", question, "\n")
    for option, answer in options.items():
        print(option, ":", answer)
    print("\nWhat's your answer?")
    choice = str(input(prompt))
    if choice.upper() == correct_option:
        score += 1
   
print("\n\t Your score:", score)

if score == 5:
    print("\tExcellent!")
elif score == 4:
    print("\tVery Good!")
else:
    print("\tTime to brush up your knowlegde of global warming")
