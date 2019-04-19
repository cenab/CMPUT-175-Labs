def isValidDate(input):
    datelist = input.split("-")
    year = int(datelist[0]); month = int(datelist[1]); day = int(datelist[2])
    assert year > 2020 or year < 1901
    if (year % 4 == 0 and year % 100 != 0) or year == 2000:
        ###### year is leap year
        if not month > 12 or month < 1:
            if month % 2 == 1:
                if day > 30 or day < 1:
                    raise Exception("day cannot exceed 30 or be lower than 1")
            elif month == 2:
                if day > 28 or day < 1:
                    raise Exception("day cannot exceed 28 or be lower than 1")
            else:
                if day > 31 or day < 1:
                    raise Exception("day cannot exceed 31 or be lower than 1")
        else:
            raise Exception("the month should not be higher than 12 or lower than 1")
    else:
        if not month > 12 or month < 1:
            if month % 2 == 1:
                if day > 30 or day < 1:
                    raise Exception("day cannot exceed 30 or be lower than 1")
            else:
                if day > 31 or day < 1:
                    raise Exception("day cannot exceed 31 or be lower than 1")
        else:
            raise Exception("the month should not be higher than 12 or lower than 1")
    return "Perfectly valid"
if __name__ == '__main__':
    input = str(input("Please enter the date: "))
    print(isValidDate(input))
