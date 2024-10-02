def main():
    time = input("What time is it? ").strip()
    result = convert(time)

    if 7.0 <= result <= 8.0:
        print("breakfast time")
    elif 12.0 <= result <= 13.0 :
        print("lunch time")
    elif 18.0 <= result <= 19.0:
        print("dinner time")


def convert(time):

    hours, minutes = time.split(":")

    hours_int, minutes_int = int(hours), int(minutes)

    time_float = hours_int + minutes_int/60
    return time_float





if __name__ == "__main__":
    main()
