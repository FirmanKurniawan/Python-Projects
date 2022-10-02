def required_input(text):
    result = input(text)
    return result if (result != '') else required_input(text)


name = required_input("Masukkan nama kamu: ")
print(f"Halo {name}")
