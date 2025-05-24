def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    year = int(input(""))
    if 1900 <= year <= 10**5:
        result = is_leap_year(year)
        print(result)
    else:
        print("Error!")