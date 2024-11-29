#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = "./Input/Names/invited_names.txt"
template_file = "./Input/Letters/starting_letter.txt"
ready = "./Output/ReadyToSend/example.txt"


with open(names, "r") as file:
    names = file.readlines()

with open(template_file, "r") as file:
    template = file.read()

for name in names:
    name = name.strip()
    personalized_letter = template.replace("[name]", name)

    with open(ready, "a") as file:
        file.write(personalized_letter)
