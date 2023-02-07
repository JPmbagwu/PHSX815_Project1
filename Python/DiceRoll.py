#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number] [-Ndice number] [-Nexp number] [-prob1 number] [-prob2 number] [-prob3 number] [-prob4 number] [-prob5 number] [-prob6 number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default single dice roll probability for "1"
    prob1 = 0.166667
    
    # default single dice roll probability for "2"
    prob2 = 0.166667    
    
    # default single dice roll probability for "3"
    prob3 = 0.166667    
    
    # default single dice roll probability for "4"
    prob4 = 0.166667
    
    # default single dice roll probability for "5"
    prob5 = 0.166667

    # default single dice roll probability for "6"
    prob6 = 0.166667        

    # default number of dice rolls per experiment
    Ndice = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob1' in sys.argv:
        p1 = sys.argv.index('-prob1')
        ptemp1 = float(sys.argv[p1+1])
        if ptemp1 >= 0 and ptemp1 <= 1:
            prob1 = ptemp1
    if '-prob2' in sys.argv:
        p2 = sys.argv.index('-prob2')
        ptemp2 = float(sys.argv[p2+1])
        if ptemp2 >= 0 and ptemp2 <= 1:
            prob2 = ptemp2            
    if '-prob3' in sys.argv:
        p3 = sys.argv.index('-prob3')
        ptemp3 = float(sys.argv[p3+1])
        if ptemp3 >= 0 and ptemp3 <= 1:
            prob3 = ptemp3
    if '-prob4' in sys.argv:
        p4 = sys.argv.index('-prob4')
        ptemp4 = float(sys.argv[p4+1])
        if ptemp4 >= 0 and ptemp4 <= 1:
            prob4 = ptemp4
    if '-prob5' in sys.argv:
        p5 = sys.argv.index('-prob5')
        ptemp5 = float(sys.argv[p5+1])
        if ptemp5 >= 0 and ptemp5 <= 1:
            prob5 = ptemp5 
    if '-prob6' in sys.argv:
        p6 = sys.argv.index('-prob6')
        ptemp6 = float(sys.argv[p6+1])
        if ptemp6 >= 0 and ptemp6 <= 1:
            prob6 = ptemp6                                       
    if '-Ndice' in sys.argv:
        p = sys.argv.index('-Ndice')
        Nd = int(sys.argv[p+1])
        if Nd > 0:
            Ndice = Nd
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = rng.Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Ndice):
                outfile.write(str(random.Categorical(prob1,prob2,prob3,prob4,prob5,prob6))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Ndice):
                print(random.Categorical(prob1,prob2,prob3,prob4,prob5,prob6), end=' ')
            print(" ")
