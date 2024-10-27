name = input("Enter your name: ")
score = float(input("Enter your score: "))

if score >= 90 and score <=100 :
    print(f"Hi {name}, your grade is A.")
elif score >= 80 and score <90:
    print(f"Hi {name}, your grade is B.")
elif score >= 70 and score <80:
    print(f"Hi {name}, your grade is c.")
elif score >= 60 and score <70:
    print(f"Hi {name}, your grade is D.")
elif score >= 0 and score <60:
    print(f"Hi {name}, your grade is F.")
else:
    print(f"Hi {name}, the marks you entered were invalid, enter marks between 0 and 100.")