height = float(input('enter the height'))
weight = float(input("enter the weight"))
bmi =18
if bmi<=18.5:
    print(f"your bmi is {bmi}under weight")
elif bmi>18.5 & bmi<25:
    print(f"your bmi is {bmi}normal weight")
elif bmi>25 & bmi<30:
    print(f"your bmi is {bmi}over weight")
elif bmi>35:
    print(f"your bmi is {bmi}clinically obese")