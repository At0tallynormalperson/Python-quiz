#PythonTest.py
Name = input("Type your name: ").strip()
#Score
Score = 0
#No Looking!
print(f"{Name}, This is a test to see if you know Python")
print(f"{Name}, I will ask you questions about python!")
#Ok fr no looking!
print(f"{Name}, What is the output of the following code?")
print("print(Hi there!)")

print("A) Nothing")
print("B) Hi there!")
print("C) An error")
print("D) The word print")

Answer1 = input("Choose A, B, C, or D: ").strip().upper()
print(f"Your answer is: {Answer1}")
#IfElse
if Answer1 == "C":
    print("Correct!")
    Score += 1
else:
    print("Not quite—the answer is C, an error.")

#Test2
print(f"{Name}, What is the output of the following code?")
print('Name1 = "Frankie"')
print('print(f"{Name1}, hello!")')
print("A) Frankie, hello!")
print("B) Name1, hello!")
print("C) An error")
print('D) f"{Name1}, hello!"')
Answer2 = input("Choose A, B, C, or D: ").strip().upper()
print(f"Your answer is: {Answer2}")
#IfElse
if Answer2 == "A":
    print(f"{Name}, You are correct!") 
    print(f'{Name}, the reason is that the code uses an f-string to include the value of Name1 in the printed message')
    print("+1 Score was added")
    Score += 1
else:
    print(f"{Name}, You are incorrect, the answer is A (Frankie, hello!)")
    print(f"{Name}, the reason is that the code uses an f-string to include the value of Name1 in the printed message")
#Test3
print(f"{Name}, What is the output of the following code?")
print("#Hello")
print('A) Hello')
print('B) #Hello')
print('C) Nothing')
print('D) The word #Hello')
Answer3 = input("Choose A, B, C, or D: ").strip().upper()
print(f"Your answer is: {Answer3}")
#IfElse
if Answer3 == "C":
    print(f"{Name}, You are correct!")
    print(f'{Name}, the reason is that the code is a comment and will not produce any output')
    Score += 1
    print("+1 Score was added")
else: 
    print(f"{Name}, You are incorrect, the answer is C (Nothing)")
    print(f"{Name}, the reason is that the code is a comment and will not produce any output")
#Showscore
print(f"Your final score is: {Score}")
#End of test, run the code to see your score!
