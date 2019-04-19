def main():
    try:
        filename = input("Enter filename> ")
        openfile = open(filename, "r")
    except IOError:
        openfile = ""
        print("IOError. %s does not exist"%(filename))
    return openfile
def readAccount(openfile):
    account = dict()
    try:
        line= openfile.readline()
        list = line.split(';')
        account[list[0]] = int(list[1][:-1])
    except ValueError:
        print("ValueError. Account for %s not added: illegal value for balance" %(list[0]))
    while line != '':
        try:
            line= openfile.readline()
            list = line.split(';')
            account[list[0]] = int(list[1][:-1])
        except ValueError:
            print("ValueError. Account for %s not added: illegal value for balance" %(list[0]))
            continue
        except IndexError:
            continue
    return account
def processAccounts(account):
    try:
        name = str(input("Enter account name, or 'Stop' to exit: "))
        if name == "Stop":
            return name
        balance = account[name]
        addedmoney = float(input("Please enter the amount of money that will be deposited: "))
        balance = balance + addedmoney
        print("New balance for account %s: %f" %(name, balance))
    except KeyError:
        print("KeyError. Account for %s does not Exist. Transaction cancelled."%(name))
        processAccounts(account)
    except ValueError:
        print("Value Error. Incorrect Amount. Transaction cancelled.")
        processAccounts(account)
    return
if __name__ == '__main__':
    openfile = main()
    if not openfile == "":
        account = readAccount(openfile)
        process = processAccounts(account)
        while process != "Stop":
            process = processAccounts(account)
