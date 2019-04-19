from random import randint


class  Secret_Number:
    def __init__(self):
#        self.continue_game=True
        return

    def get(self):
        a = randint(1, 9)
        b = randint(0, 9)
        c = randint(0, 9)
        while not(a != b and c != a and b != c):
            a = randint(1, 9)
            b = randint(0, 9)
            c = randint(0, 9)
        self.number = str(a) + str(b) + str(c)
#        generate=True
#            num=str(randint(102,987))
#            if num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
#                generate==True
#            else:
#                generate==False
    def getClues(self):
        printing = []
        if self.guess[0] not in self.number and self.guess[1] not in self.number and self.guess[2] not in self.number:
            printing= ['Wrong']
        elif self.guess[0]==self.number[0] and self.guess[1]==self.number[1] and self.guess[2]==self.number[2]:
            printing= ['Correct']
        else:
            self.ding_count=0
            self.dong_count=0
            for i in range(0,3):
                if self.guess[i]==self.number[i]:
#                    self.ding_count+=1
                    printing.append('DING')
                elif self.guess[i] in self.number and self.guess[i]!=self.number[i]:
#                    self.dong_count+=1
                    printing.append('DONG')
        self.printclue = ' '.join(printing)
#            printing='DING'*self.ding_count+'DONG'*self.dong_count

    def readNumber(self):
        ask=True
        while ask:
            self.guess = input('Enter a three digit number with non-repeating digits')
            if len(self.guess)==3 and self.guess.isdigit() and self.guess[0]!=self.guess[1] and self.guess[0]!=self.guess[2] and self.guess[1]!=self.guess[2]:
                ask=False
    def run(self):
        i= 1
        self.get()
        while i<=10 or i == 1:
            self.repetition=i
            self.readNumber()
            self.getClues()
            if self.printclue =='Correct':
                print("CORRECT")
                break
            print(self.printclue)
            i+=1
def main():
    game = Secret_Number()
    game.run()
main()
