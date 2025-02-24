import encryption

def main():
    text = input("Unesite tekst: ")
    key = int(input("Unesite broj: "))

    option = input("Izaberite opciju (0 - sifrovati, 1 - desifrovati): ")

    if option == '0':
        encrypted_text = encryption.encrypt_text(text, key)
        print("Sifrovani tekst:", encrypted_text)
    elif option == '1':
        decrypted_text = encryption.decrypt_text(text, key)
        print("Desifrovan tekst:", decrypted_text)
    else:
        print("Mozete koristiti samo 0 i 1!")

if __name__ == "__main__":
    main()
