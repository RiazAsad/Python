# This program shows how to create lottery numbers at random
import random # In python import random, which means there is a random library and it will
# generate random numbers

def main():
    # Initialize list of numbers.
    number_list = [0, 0, 0, 0, 0, 0, 0]

    # Assign random numbers to list.
    for i in range(7):
        number_list[i] = random.randint(2, 12) # Randomly the list is going to be flooded with the lotterry numbers between 0 and 9.

    # Display numbers in a single line.
    for i in range(7):
        print (number_list[i], end='') # Organizing the numbers in horizontal line and displaying
        
        # Separate current number from next number.
        if i < 6:
            print(', ', end='') # Creating a comma between the numbers, this is just formatting code
            

# Call the main function.
main()
