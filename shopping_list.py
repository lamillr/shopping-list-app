#make a list to hold our items
shopping_list []
#print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter DONE when list is complete.")
#ask for new items
while True
    new_item=input(">")
#be able to quit the program
    if new_item=="DONE":
    break

# add new items to our list
shopping_list.append(new_item)
# print out list
print ("Here's your list:")
for item in shopping_list:
    print(item)
