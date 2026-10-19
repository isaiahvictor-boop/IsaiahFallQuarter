prompt = input("do you want to print the list? Y/N ")
geniuses = ["jayden", "dayyon", "jahlil", "caden", "jeremy"]

while (prompt == "Y"):
  for genius in geniuses:
    print(genius)
  prompt = input("do you want me to print the list again? Y/N ")