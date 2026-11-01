#PythonTest.py
#Edit this line ONLY
Name = "[Your Name Here]" #Keep quotation marks around your name
#Score
Score = 0
#No Looking!
print(f"{Name}, This is a test to see if you know Python")
print(f"{Name}, I will ask you questions about python!")
#Ok fr no looking!
print(f"{Name}, What is the output of the following code?")
print("print(Hi there!)")
#Edit this line (keep quotes)
Answer1 = "[Answer]" #Caps lock the first word of your answer, and keep quotation marks around your answer
print(f"Your answer is: {Answer1}")
#Dont peek at the line below!
if Answer1 == "Nothing":
    print(f"{Name}, You are correct!")
    print("+1 score was added")
    Score += 1
else:
    print(f"{Name}, You are incorrect, the answer is Nothing")
#Test2
print(f"{Name}, What is the output of the following code?")
print('Name1 = "Frankie"')
print('print(f"{Name1}, hello!")')
Answer2 = "[Answer]" #Caps lock the first word of your answer, and keep quotation marks around your answer
print(f"Your answer is: {Answer2}")
#dont look at this line
if Answer2 == "Frankie, hello!":
    print(f"{Name}, You are correct!") 
    print("+1 Score was added")
    Score += 1
else:
    print(f"{Name}, You are incorrect, the answer is Frankie, hello!")
#Test3
print(f"{Name}, What is the output of the following code?")
print("#Hello")
Answer3 = "[Answer]" #Caps lock the first word of your answer, and keep quotation marks around your answer
print(f"Your answer is: {Answer3}")
#Dont look at this line
if Answer3 == "Nothing":
    print(f"{Name}, You are correct!")
    Score += 1
    print("+1 Score was added")
else: 
    print(f"{Name}, You are incorrect, the answer is Nothing")
#Showscore
print(f"Your final score is: {Score}")
#End of test, run the code to see your score!
