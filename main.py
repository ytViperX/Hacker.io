#Imports
import sys, time, os
import random as rd

passwordList = [
  "salmon",
  "dog",
  "duck",
]

#Colors
Blue="\33[0;34m"
Cyan="\033[1;36m"
Purple="\033[0;35m"
Green="\033[0;32m"
Orange ="\033[0;33m"
Pink = "\033[1;31m"
DarkBlue = "\033[1;34m"
White = "\033[1;37m"
Gray = "\033[1;30m"

#Clear page function
def clear():
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')

#Br
def space():
  print("")

#Wait function
def wait(secs):
  time.sleep(secs)

#Typing
def print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.04)

#Main game
print(Cyan + "You will have to login with an authorized account.")
print(Cyan + "Enter username: ")
name = input(Orange)
space()
print(Cyan + "Logging in...")
space()
wait(1)
print(Green + "Access Granted!")
space()
print(Cyan + "Welcome " + Orange + str(name) + Cyan + " to this program!")
space()
input(Orange + "Press ENTER to continue")
space()
print(Cyan + "In this program, you will have to guess the password of someone that works in your school.")
space()
print(Cyan + "We are going to start with the English teacher's password.")
print(Cyan + 'Write down "data.getPassword(english)" to get a hint of the password.')
verification = True
while verification:
  code = input(Orange)
  if code == "data.getPassword(english)":
    space()
    verification = False
  else:
    verification = True
    print(Cyan + "Wrong code!")
    space()
password = rd.choice(passwordList)
if password == "salmon":
  hint = "It's an orange fish used in sushi."
elif password == "dog":
  hint = "Most people has this pet, it is a wolf descendant."
elif password == "duck":
  hint = "It's an animal that makes annoying sounds, it lives in lakes and swamps."
print(Green + "Validating account...")
wait(1)
print(Green + "Accessing database...")
wait(1)
space()
print(Cyan + "It is one of these: " + str(passwordList))
print(Cyan + "Hint: " + Orange + hint)
passwordGuess = input(Cyan + "Enter your guess: " + Orange)
if passwordGuess.lower() == password:
  space()
  print(Green + "You correctly guessed the password!")
  print(Cyan + "I guess the english teacher really likes animals!")
  space()
  input(Orange + "Press ENTER to continue")
  clear()
  print(Cyan + "Ok, now let's try to send fake news to the school principal!")
  print("Make an account by entering an e-mail.")
  print("Enter new e-mail: ")
  input(Orange)
  space()
  print(Cyan + "Creating new e-mail...")
  wait(1)
  print("E-mail Created!")
  space()
  verification = True
  print("Now, you will have to write this code to get your school principal's email: 'document.getPrincipalEmail()'")
  while verification:
    code = input(Orange)
    if code == "document.getPrincipalEmail()":
      verification = False
    else:
      print(Cyan + "Wrong code!")
      space()
  space()
  print(Green + "Getting email...")
  wait(1)
  space()
  print(Cyan + "Now you need to type 'email.send(whatever you want to send to him)'")
  input(Orange)
  space()
  print(Cyan + "Succesfully sent that e-mail!")
  space()
  wait(1)
  print(Orange + "Press ENTER to continue")
  input()
  clear()
  grades = [
    "James 5/10",
    "Bob 3/10",
    name + " 2/10",
  ]
  print(Cyan + "Now, we will change your grades!")
  space()
  print("These are your grades: " + str(grades))
  print("You have pretty bad grades! Type" + Orange + " 'document.SelectMe()'" + Cyan)
  input(Orange)
  print(Cyan + "What grade do you want? (Write in numbers)")
  grade = input(Orange)
  grades[2] = name + " " + str(grade) + "/10"
  space()
  print(Green + "Succesfully changed your grade!")
  print(Cyan + "Here are your grade now: " + str(grades))
  space()
  print("That is all for this program! I will make a part two if this goes trending! So if you would like this to go trending, share it with your friends!")
else:
  space()
  print(Pink + "The database got locked because you didn't get the right password!")