user_score = int(input("Enter your score\n"))

if user_score > 100 or user_score < 0:
    print("Invalid Score")
elif 90 <= user_score <= 100:
    print("A")
elif 80 <= user_score <= 89:
    print("B")
elif 70 <= user_score <= 79:
    print("C")
elif 60 <= user_score <= 69:
    print("D")
else:
    print("F")
