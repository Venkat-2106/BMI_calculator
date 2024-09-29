'''
BMI - BODY MASS INDEX
Body Mass Index is the measure of body fat based on height and weight

BMI             CLASSIFICATION                  HEALTH RISK
Under 18.5      Underweight                     Minimal
18.5-24.9       Normal Weight                   Minimal
25-29.5         Overweight                      Increased
30 and above    Obese                          High

Formula:
BMI = (KG / CM**2)*10,000
BMI = (Weight in pound * 703)/height in inches ** 2
'''

weight = int(input("Enter your Weight: "))
height = int(input("Enter your Height: "))
bmi=(weight/height**2)*10000
print(f"Your BMI is: {round(bmi,2)}")

if bmi<=18:
    print("You are underweighted and Your health risk is minimal")
elif bmi>18 and bmi<=24.9:
    print("You are normal weight and your health risk is minimal")
elif bmi>=25 and bmi<=29.5:
    print("You are Overweighted and your health risk is increased")
else:
    print("You are obese and your health risk is high")