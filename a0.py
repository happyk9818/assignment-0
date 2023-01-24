# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Taekyung Kang
# taekyk1@uci.edu
# 44996270

n = int(input())

print("+-+")

for i in range(n-1):
    firstLine = ""
    for j in range(i):
        firstLine = firstLine + "  "
    firstLine = firstLine + "| |\n"
    for j in range(i):
        firstLine = firstLine + "  "
    firstLine = firstLine + "+-+-+"
    print(firstLine)

lastLine = ""

for i in range(n-1):
    lastLine = lastLine + "  "
lastLine = lastLine + "| |\n"

for i in range(n-1):
    lastLine = lastLine + "  "
lastLine = lastLine + "+-+"
print(lastLine)