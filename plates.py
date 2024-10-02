def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def check_start(plate):
    if plate[0:2].isalpha():
        return True
    return False

def check_length(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum():
        return True
    return False

def check_first_digit(plate):
    for index, _ in enumerate(plate):
        if plate[index].isdigit():
            if plate[index] == "0" or not plate[index:].isdigit():
               return False
            break
    return True


def is_valid(s):
    if check_length(s) and check_start(s) and check_first_digit(s):
        return True
    return False


main()
