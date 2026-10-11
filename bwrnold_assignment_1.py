"""
ASSIGNMENT 1
POKEMON TOURNAMENT

ASSIGNMENT REQUIREMENTS (100 points)
Correctness: import_data 12.5, attack_multiplier 12.5, fight 22.5, tournament 22.5.
Required methods: 5 points per function (20 total; reviewed by the instructor).
Supervised understanding check: 10 points. See the assignment post for details.
Correct output earns correctness credit even if a required method is missing.

AI POLICY AND PERMITTED HELP
Do not use generative AI for any part of this assignment, including generating,
rewriting, debugging, explaining assignment-specific code, or AI autocomplete.
Disable AI coding assistants. Ordinary non-AI editor completion, syntax
highlighting, running Python, and its debugger are allowed. You may use course
materials, official Python documentation, and help from the instructor or TA.
Write your own code; do not copy solutions from classmates, websites, or prior
semesters. Ask the instructor before using a resource not listed here.

SUBMISSION AND EXECUTION
Keep all five function names and parameter lists unchanged. Return results;
do not replace returns with print statements. Do not use input() or run tests
at module level. Put any local test calls under if __name__ == "__main__":.
No imports are needed or permitted in the submitted file for this exercise.
Enter your name and HawkID below. Save as hawkid_assignment_1.py, upload that
file to ICON, and commit and push the identical file to your GitHub repository.
ICON is the graded submission. Identity mistakes will be flagged for correction,
not assigned an automatic zero. The GitHub copy will be checked.

VALID INPUTS AND EDGE CASES
CSV input has no header, no blank lines, and exactly four comma-separated fields
per row. Fields contain no embedded commas or quotes and no surrounding spaces.
The last line may or may not have a newline. An empty file is valid.
Names are nonempty strings. Types are exactly Water, Fire, Electric, Grass, or
Ground. Health and base damage are positive finite numbers. Convert both to
float. No malformed-input handling is required. first2attack is always 1 or 2.
Never change input participant lists, including their health. Every match starts
at the original full health. One attack counts as one round; stop immediately
when either health becomes <= 0 (including exactly zero). Do not round damage
or health. tournament([]) returns []; a one-participant tournament returns [0].
For n participants there are n*(n-1) matches and that many total wins.

Pokemon, also known as Pocket Monsters in Japan, is a Japanese media franchise managed by
The Pokemon Company, a company founded by Nintendo, Game Freak, and Creatures. The franchise
was created by Satoshi Tajiri in 1995, and is centered on fictional creatures called "Pokemon",
which humans, known as Pokemon Trainers, catch and train to battle each other for sport.
Works within the franchise are set in the Pokemon universe. The English slogan for the franchise
is "Gotta Catch 'Em All".

For more information: https://en.wikipedia.org/wiki/Pok%C3%A9mon

In this assignment, we will simulate a Pokemon tournament. Each pokemon will be a
participant in the tournament. In order to simulate, we have 4 main tasks to complete.
Since later tasks are dependent on the prior ones, you have to complete tasks in order.
Explanation of tasks and a pseudocode is provided to you within each function. However,
tasks can be summarized as:
    1. Importing Participant data from a CSV file: Name of the file will be given to you
       as a parameter. This CSV file does not have any header row. It has 4 fields.
            - 1st Field: Name of the Pokemon
            - 2nd Field: Type of the Pokemon ({Water, Fire, Electric, Grass or Ground})
            - 3rd Field: Health (HP) of the Pokemon
            - 4th Field: Base Attack Damage of the Pokemon
    2. Calculating the Attack Multiplier: Since some type of pokemons are more powerful
       against some specific types, their power can be enhanced up to some multiplier value.
       This Attack Multiplier is provided as a chart in the function description below.
    3. Fight Simulation: This task will ask you to implement a fight simulation between two
       given participants/pokemons. You have to use the attack multipliers and find out
       which participant wins the fight after how many rounds.
    4. Tournament Simulation: Since we already implemented the fight simulation between two
       participants, we can easily run a tournament. Each participant will play two games against
       the participants which appears after them in the participants list. We will keep
       track of how many games each participant won in a list, then return this list.
"""

######################################################################
#                           IMPORTANT
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid. If you do not
# change it, the grader will flag your identification for correction.
#
# Note: Your hawkid is the login name you use to access ICON, and NOT
# your firstname-lastname@uiowa.edu email address.
#
# def hawkid():
#     return(["YOUR NAME", "YOUR HAWKID"])
######################################################################
def hawkid():
    return(["Ben Arnold", "bwrnold"])

def import_data(filename):
    participants = []
    testCSV = open(filename)
    for row in testCSV:
        row = row.strip().split(",")
        for i in row:
            POKEMON = []
            POKEMON.append(row[0])
            POKEMON.append(row[1])
            POKEMON.append(float(row[2]))
            POKEMON.append(float(row[3]))
        participants.append(POKEMON)
    return participants


def attack_multiplier(attacker_type, defender_type):
    if attacker_type == "Water" and defender_type == "Fire":
        return 2.5
    elif attacker_type == "Electric" and defender_type == "Water":
        return 1.3
    elif attacker_type == "Ground" and defender_type == "Electric":
        return 2.0
    elif attacker_type == "Fire" and defender_type == "Grass":
        return 3.0
    elif attacker_type == "Grass" and defender_type == "Water":
        return 1.5
    else:
        return 1.0

def fight(participant1, participant2, first2attack):
    rounds = 0
    winner = 1
    variable1 = participant1[2]
    variable2 = participant2[2]
    while variable1 > 0 and variable2 > 0:
        if first2attack == 1:
            mult = attack_multiplier(participant1[1], participant2[1])
            dmg = participant1[3] * mult
            variable2 -= dmg
        elif first2attack == 2:
            mult = attack_multiplier(participant2[1], participant1[1])
            dmg = participant2[3] * mult
            variable1 -= dmg
        rounds += 1
        if first2attack == 1:
            first2attack = 2
        else:
            first2attack = 1
    if variable2 > variable1:
        winner = 2
    return [winner, rounds]


def tournament(participants):
    wins = []
    for p in participants:
        wins.append(0)
    for i in participants:
        for j in participants[participants.index(i) + 1:]:
            home = fight(i, j, 1)
            away = fight(i, j, 2)
            if home[0] == 1:
                wins[participants.index(i)] += 1
            else:
                wins[participants.index(j)] += 1
            if away[0] == 1:
                wins[participants.index(i)] += 1
            else:
                wins[participants.index(j)] += 1
    return wins