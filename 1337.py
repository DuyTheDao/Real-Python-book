# Real-Python-book (page 45)
# Leet Speak Script Python v3.6
# This was created for the Real Python course
# Duy Dao

print (" D40'5 Python L33t 5p34k")
word = input("Please enter a message: ")
leetmsg = word
leetwords = "aeiots"
for letter in word:
    if letter in leetwords:
        leetmsg = leetmsg.replace('a', str(4))
        leetmsg = leetmsg.replace('e', str(3))
        leetmsg = leetmsg.replace('i', str(1))
        leetmsg = leetmsg.replace('o', str(0))
        leetmsg = leetmsg.replace('t', str(7))
        leetmsg = leetmsg.replace('s', str(5))
print (leetmsg)
