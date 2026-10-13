from colorama import Fore, init

init(autoreset=True)

name=input("Enter student's name:")
marks=int(input("Enter student's marks:"))

print(Fore.CYAN + "Student Name: " + name)

if marks >= 40:
    print(Fore.GREEN + "Result: PASS")
else:
    print(Fore.RED + "Result: FAIL")
