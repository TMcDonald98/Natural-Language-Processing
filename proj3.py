'''
Class: CPSC 475-01
Team Member 1: Thomas McDonald
Team Member 2: Diego Valdez
Pgm Name: proj3.py 
Pgm Desc: pickle & de-pickle a Corpus and then word prossesing
			The program traverses inaugural speeches and graphs the amount of time a specific word was said/year
Usage: 1) python pro3.py 
'''
import matplotlib.pyplot as plt
import pickle
def main():

    fin = open('proj3.pkl', 'rb')
    lsts_in = pickle.load(fin)
	
    word = raw_input('What word would you like to search for? ')
    frequency = []#int[]
    years = []
    counter = 0
    year = 1789 #Start Year
    for speech in lsts_in:#for each list in the list[][]
        frequency.append(0)
        years.append(year)
        for string in speech: #For each word in the speach[]
            if string == word:
                frequency[counter] = frequency[counter] + 1
        counter = counter + 1
        year = year + 4
    fin.close()
    y = [i for i in years]
    x = [h for h in frequency]
    plt.title('Frequency of Words in Speeches')
    plt.ylabel('Year of Speech')
    plt.xlabel('Frequency')
    plt.barh(y,x)
    plt.show()
    
main()