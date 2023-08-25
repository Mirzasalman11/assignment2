
from lec_3 import dic_up

def display_menu():
    print("Menu:")
    print("1. Dictionary Update")
    print("2. Prime Number Check")
    print("3. Change List of Dictionaries")
    print("4. Find Primes in a Range")
    print("5. Pass and Continue Demo")
    print("6. Split String Values")
    print("7. Common Elements in Lists")
    print("8. Change Values in Dictionary")
    print("9. Convert Two Lists to Dictionary")
    print("10. order list")
    print("11. card_sort")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            dic_up_obj = dic_up()
            dic_up_obj.dic_change()
        elif choice == '2':
            prime_obj = dic_up()
            prime_obj.prime()
        elif choice == '3':
            change_list_obj = dic_up()
            change_list_obj.change_list_di()
        elif choice == '4':
            prime_in_range_obj = dic_up()
            prime_in_range_obj.find_prime_in_range()
        elif choice == '5':
            pass_cont_obj = dic_up()
            pass_cont_obj.pas_con()
        elif choice == '6':
            sp_val_obj = dic_up()
            sp_val_obj.split_val()
        elif choice == '7':
            com_in_list_obj = dic_up()
            com_in_list_obj.coman_in_list()
        elif choice == '8':
            change_in_d_obj = dic_up()
            change_in_d_obj.change_in_dic()
        elif choice == '9':
            con2_list_dic_obj = dic_up()
            con2_list_dic_obj.con_to_dic()
        elif choice == '10':
            o=dic_up()
            o.oder_list()

        elif choice == '11':
            o=dic_up()
            o.cards_sort()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

