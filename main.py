PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", mode="r") as name_list:
    list_names = name_list.readlines()
    print(list_names)




with open("./Input/Letters/starting_letter.txt", mode="r") as data_names:
    message = data_names.read()
    for names in list_names:
        striped_name = names.strip("\n")
        new_letter = message.replace(PLACEHOLDER, names.strip("\n"))
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode='w') as new_message:
            new_message.write(new_letter)
