
def create_list(task_to_do):
    to_do_list.append(task_to_do)
    return to_do_list

to_do_list = []
done = []
done_dict = {}
name = input("\nPlease enter your name:  ").title()

print("\nHello {}, glad you're with us!:D.\nLet's get started and organize the day properly. Consistency and discipline are your way to freedome!\n".format(name))

# infinite loop!
while True:
    answer = input("Do you want to add or remove a task on your to do list?(add or remove): ").lower()
    if answer == 'add':
        tasks = input("Enter your task: ").lower()
        if tasks in to_do_list:
            to_do_list.remove(tasks)
            print("\nBe careful to not write the same task twice!!!!")
        create_list(tasks)
        print("\nTasks left to do: {}".format(to_do_list))
        print("\nTasks done: {}".format(done_dict))
    elif answer == 'remove':
        answer_one = input("\nPlease type the name of the task you have finsihed: ").lower()
        try:                                                                                                    #could use for the whole while loop. Assume it would apply except ValueError to every action in the loop---ask Senesi Abi
            done.append(to_do_list.pop(to_do_list.index(answer_one)))
            for task in done:
                done_dict[task] = done_dict.get(task, 0) + 1
            done.clear()
                                                                                                                #could use remove--done.append(to_do_list.remove(anser_one)), doesnt show empty list, shows None.
        except ValueError:
            print("\nThe task you wanted to remove doesn't exist or you spelt it wrong. Please try again!")     #how to make it ask for the task again instead of going all the way up to the beginning of the while loop
        print("\nTasks left to do: {}".format(to_do_list))
        print("\nTasks done: {}".format(done_dict))
        if not len(to_do_list):
            print("\nCongrats top G! You finished all of the tasks!:D\n")
    else:
        print("\nYOU SHALL NOT BREAK MY CODE MUGGLE!!!\n")
        print("\nPlease make sure you only type 'add' or 'remove'. Also check if your spelling is correct and try again! :D\n")
