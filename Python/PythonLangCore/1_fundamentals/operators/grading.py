# >= 90 :: A
# >= 75 AND < 90 :: B
# >= 60 AND < 75 :: C
# >= 50 AND < 60 :: D
# < 50 :: F



score = int(input("Enter the score: "))
# score = 85
grade = ''

if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")