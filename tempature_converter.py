print("welcome to tempature converter, a lightweight utility for converting tempatures")

unit = input("please specify the tempature you want converted: ").upper()
Value = float(input("please specify the input you want converted: "))
#function that converts C to F
def c_2_f(temp_C);
    converted_C = temp_C * (9/5) + 32
    return converted_temp
#function that F to C
def f_2_C(temp_F);
    converted_F = (temp_F -32) * 5/9
    return converted_F

#main function that uses conditionals to decide which convert function to select
def main():
    if (unit == "C");
        Celsius_to_Farenheit = C_to_F(Value)
        return Celsius_to_Farenheit
    elif (unit == "F"):
        Farenheit_to_Celsisus = F_to_C(Value)
        return Farenheit_to_Celsisus
    else:
        Warning = "please enter C or F to specify the unit"
        Return Warning
#print result
result = main()
print("Your value is: " +str(result))