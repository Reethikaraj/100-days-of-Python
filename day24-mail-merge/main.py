# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/Letters/starting_letter.txt", "r") as letter:
    text = letter.read()

with open("input/Names/invited_names.txt", "r") as names:
    invitee_list = names.readlines()
    for list_item in invitee_list:
        invitee = list_item.strip("\n")
        fine_name = "output/ReadyToSend/" + str(invitee) + ".txt"
        with open(fine_name, "w") as new:
            new_invitation = text.replace("[name]", invitee)
            new.write(new_invitation)
