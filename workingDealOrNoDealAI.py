import random
import os
import time


while True:#27
    NeuralNetwork = []
    for i in range(1,27):
        NeuralNetwork.append(i)

    print("Press any key to get a good box number.\nMake sure to select the given box")

    while len(NeuralNetwork) >= 27:
        #print(str(len(NeuralNetwork)))
        sInput = input("Press any key for number...\n")
        os.system('cls')
        print("AI CALCULATES...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("AI DECIDES:")
        randint = random.randint(0,7)
        print(NeuralNetwork
        [randint])
        print(":)\n")
        NeuralNetwork.pop(randint)
		
