waga = float(input("podaj swoja wagę: "))
wzrost = float(input("podaj swój wzrost: "))

def kalk_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    bmi = round(bmi, 2)
    print(f"twoje bmi wynosi: {bmi}")
    if bmi < 16:
        print("wygłodzenie")
    elif 16.0 <= bmi < 16.99:
        print("wychudzenie")
    elif 17.0 <= bmi < 18.49:
        print("niedowaga")
    elif 18.5 <= bmi < 24.99:
        print("pożądana masa ciała")
    elif 25.0 <= bmi < 29.99:
        print("nadwaga")
    elif 30.0 <= bmi < 34.99:
        print("otyłość I stopnia")
    elif 35.0 <= bmi < 39.99:
        print("otyłość II stopnia")
    else:
        print("otyłość III stopnia")
    return bmi

kalk_bmi(waga, wzrost)