# Pick one question from timed_challenge.txt
# Paste the question as a comment below
'''3. Remove Duplicates (Keep Order)
Return the values in the order they first appeared, without duplicates.
Input: ["apple", "banana", "apple", "kiwi", "banana"]
Output: ["apple", "banana", "kiwi"]'''
# Set a timer for 30 minutes and complete the question!

def unique_inventory(inventory):
    unique_items = list()
    for product in inventory:
        if product not in unique_items:
            product = str(product).lower().strip()
            unique_items.append(product)
    print (unique_items)
    return

unique_inventory(["apple", "banana", "apple", "kiwi", "banana"])
unique_inventory(["apple", "banana", "grapes", "kiwi", "pear"])
unique_inventory(["apple", "apple", "apple", "apple", "apple"])
unique_inventory(["apple", "banana", "grApes", "kiwi", "pEar"])
unique_inventory(["Apple", "apple", "apple", "apple", "apple"])
unique_inventory([1, 2, 3, 4, 5])
unique_inventory([])
'''For this problem I chose to use a list as a my structure for my program because while a set would remove any duplicates easily,
it would struggle to maintain the order in which the items appear. With a list, it's still easy to iterate through items in the list
and it would help to preserve the order that is being looked for. The only issue from there was just figuring out how I could get the list
to act like a set without having to convert my list to set. Also when you add items into a set, they get added to the beginning, while
in a list the order the items appear are preserved. I also made sure to convert all the items in the list to the same format so that the same items
in different formats aren't tracked as two different products. The time limit made me think about what format I could implement correctly in 
the shortest amount of time that would also still give the desired output. Because where I probably could have implemented a stack or linked list, 
those would take me a bit more time just to set up which would leave me only a little time to check and correct errors. Essentially I had to get 
a healthy balance of effienciency and program effectiveness. In terms of trade-offs, I had to give up any way of inputting separate products to create 
the list through the program, so in order for the function to work, the list needs to be pre-entered when the function is called for it to work.'''
