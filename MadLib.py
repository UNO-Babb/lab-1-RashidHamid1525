#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  adjective1 = input("Enter an adjective: ")
  verb1 = input("Enter a verb: ")
  noun2 = input("Enter a noun: ")
  place1 = input("Enter a place: ")
  adjective2 = input("Enter an adjective: ")
  verb2 = input("Enter a verb: ")

  #Print the story with the user supplied words.
  print("One day, I found a", noun1 + ".")
  print("The", noun1, "was surprisingly", adjective1 + ".")
  print("Suddenly, it began to", verb1 + ".")
  print("I quickly grabbed my", noun2, "for help.")
  print("Together, we ran to", place1 + ".")
  print("Everyone there was shocked that it was", adjective2 + "!")
  print("In the end, I decided to", verb2 + ".")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
