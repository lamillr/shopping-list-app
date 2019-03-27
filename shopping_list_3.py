#have a help command
#have a show command
#clean up code generally


#make a list to hold our items
shopping_list=[]
#print out instructions on how to use the app
def show_help():
    print("What should we pick up at the store?")
    print(""""
Enter 'DONE' when list is complete.
Enter 'HELP for this help.
Enter 'SHOW' to see your current list.
""")
def show_list():
    print ("Here's your list:")
    for item in shopping_list:
        print(item)
# add new items to our list
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()
#ask for new items
while True:
    new_item=input(">")
#be able to quit the program
    if new_item=='DONE':
        break
    elif new_item=='HELP':
        show_help()
        continue
    elif new_item=='SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
