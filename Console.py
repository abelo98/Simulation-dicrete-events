from fractions import Fraction

class Show:
    def start(self):
        simulations = workers=0
        la = []
        lr = []
        while 1:
            while 1:
                simulations = 1000 
                workers  = 1
            
                print('')
                try:
                    v = input("Enter how many simulations to run: ")
                    if v == '':
                        print(f'By default = 1000')
                        break
                    simulations = int(v)
                    if simulations < 1: 
                        raise Exception()
                except:
                    print('waiting a number >= 1')
                    continue
                break
            while 1:
                try:
                    v = input("Enter how many extra workers for rush hour: ")
                    if v == '':
                        print(f'By default = 1')
                        break
                    workers = int(v)
                    if workers < 1: 
                        raise Exception()
                except:
                    print('waiting a number >= 1')
                    continue
                break
            while 1:
                la = [1/5,1/9,1/13]
                try:
                    v = input("Values of lambda for the arrival of clients, separeted by ',', or press enter(ex:1/5,1/9): ")
                    if v == '':
                        print(f'By default = 1/5,1/9,1/13')
                        break
                    la = list(map(lambda x:Fraction(x),str.split(v,',')))
                
                except ValueError:
                    print('waiting list of fractions')
                    continue
                break

            while 1:
                lr = [1/2,1/2,1/2]
                try:
                    v = input("Values of lambda for the arrival of clients in rush hour, separeted by ',', or press enter(ex:1/2,1/2): ")
                    if v == '':
                        print(f'By default = 1/2,1/2,1/2')
                        break
                    lr = list(map(lambda x:Fraction(x),str.split(v,',')))
                    if len(lr) != len(la): 
                        raise IndexError()
                except IndexError:
                    print('the length of the list of lambdas must match')
                    continue
                except ValueError:
                    print('waiting list of fractions')
                    continue
                break
            print('')
            break
        return simulations,workers,la,lr
