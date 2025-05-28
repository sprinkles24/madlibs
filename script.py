
authors = ["Shyla", "Name"]

#procedures

def noun(end):
    return (input("Noun:" + end)) #end can be " " or "ing " etc
def verb(end)
    return (input("Verb:" + end))
def adjective(end):
    return (input("Adjective:" + end))
def adverb(end):
    return (input("Adverb:" + end))

#stories
def story1():
    global authors

    print(f"story story story\n\nStory written by {authors[0]}\nProgram written by Shyla")
    input("Blanks filled in by ")


###############

#printing stuff
print("Type in a word that fits the criteria, and read your story!")
print("""Definitions:

Noun: Person, place, thing, idea (ex. 'cat')
Proper Noun: Name of a noun (ex. 'Shyla')
Pronoun: Replaces noun (ex. 'I', 'she')
Adjective: Describes noun (ex. 'cool)
Verb: Describes action (ex. 'run')
Adverb: Describes adjective, verb, or other adverb (ex. very [as in 'very tall'])
Preposition: Describes relation or position (ex. 'after)
Onomatopoeia: Directly imitates sound (ex. 'zap')""")

print("""Which story would you like to complete?

1 - Name of story............written by {author[0]}
2 - Name of story 2 .........written by Name
""")

storyChoice = input("Type the number of your chosen story. ")
while storyChoice not in range(1,2):
    storyChoice = input("> ")

if storyChoice == 1:
    print(story1())
elif storyChoice == 2:
    pass
