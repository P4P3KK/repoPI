def kat(bmi):
    W = []
    W.append(str(round(bmi, 2)))
    if bmi < 16:
        W.append("Wygłodzenie")
    elif 16 <= bmi <= 16.99:
        W.append("Wychudzenie")
    elif 17 <= bmi <= 18.49:
        W.append("Niedowaga")
    elif 18.5 <= bmi <= 24.99:
        W.append("Pożądana masa ciala")
    elif 25 <= bmi <= 29.99:
        W.append("Nadwaga")
    elif 30 <= bmi <= 34.99:
        W.append("Otylosc I stopnia")
    elif 35 <= bmi <= 39.99:
        W.append("Otylosc II stopnia")
    elif bmi >= 40:
        W.append("Otylosc III stopnia")
    W[1] += "\n"
    return W


w = 0
h = 0
output = open("wyniki.txt", "w")
print("Podaj w jakich jednostkach bedziesz wprowadzal dane [metryczne] lub [imperialne]:")
j = input()

print("Podaj ile chcesz wpisać obserwacji:")
c = int(input())

for i in range(c):
    if j == "metryczne":
        print(f"Podaj wzrost [cm] {i + 1}:")
        h = float(input()) / 100
        print(f"Podaj wage [kg] {i + 1}:")
        w = float(input())
    elif j == "imperialne":
        print(f"Podaj wzrost [ft] {i + 1}:")
        h = 0.3048 * float(input())
        print(f"Podaj wage [lb] {i + 1}:")
        w = 0.45359237 * float(input())
    else:
        print("Błąd, nieobslugiwany system jednostek.")

    bmi = w / (h ** 2)
    print(" ".join(kat(bmi)))
    output.write(" ".join(kat(bmi)))
