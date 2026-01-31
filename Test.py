prenom = input("Quel est ton prénom ? ")
age = int(input("Quel est ton âge ? "))

if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")

print("Bienvenue", prenom, "!")