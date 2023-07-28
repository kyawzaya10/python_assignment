print("Hello, welcome to Letter Counter!")
full_sentence = input("Enter your context:")
count_letter = input("Enter the letter you want to count:")
print("Your letter count is", full_sentence.count(count_letter))
total = len(full_sentence)
obtain = full_sentence.count(count_letter)
percentage = (obtain*100)/total
print("Your letter percentage is", percentage, "%")
