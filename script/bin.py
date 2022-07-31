
bin = 0
num = []
result = []

try:
    ask = int(input("Deseja converter de binário para decimal [0] ou de decimal para binário [1]? \n "))
    
    if ask == 0: 
        try:
            numb = input("Digite um número em binário: ")
            dec = 0
            size = len(numb) -1
            for x in numb:
                if x == "1":
                    dec+=2**size
                    size-=1
                else:
                    size-=1
            
            print("{} em binário é: {} em decimal.".format(numb, dec))
        except:
            print("Digite apenas números...")
    

    elif ask == 1:
        try:
            user = int(input("Digite um número para ser convertido em Binário: "))
            none = user
                
            if user == 0:
                print("0 em Binário é: 0")
                exit()

            elif user == 1:
                print("1 em Binário é: 1")
                exit()

            for i in range(0, 2**9):
                save = 2**bin
                bin += 1

                num.append(save)

            num.reverse()

            while len(num) > 0 :

                if num[0] > user:
                    del(num[0])
                    result.append(0)
                        
                elif num[0] < user:             
                    user -= num[0]
                    del(num[0])
                    result.append(1)
                
                elif num[0] == user:
                    user -= num[0]
                    del(num[0])
                    result.append(1)
                
            while result[0] == 0:
                del(result[0])    
            
            restring = str(result).strip('[]')
            rest = ''.join(map(str, result))
            print("{} em binário é: {} em decimal".format(none, rest))
                
                 
        except:
            print("Digite apenas números")                                                                    
            exit()

        
        

except:
    print("Digite apenas [0] ou [1]... ")
    exit()
    
#Copyright-@Junior4Carvalho
