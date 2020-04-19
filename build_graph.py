#!/usr/bin/env python3
import pandas as pd


def main(MONTH=1, YEAR=2017):
    # load the dataset
    dataset = pd.read_csv('./dataset/crime_small.csv')

    #displaying a few information
    print("DATASET INFORMATIONS:")
    print(dataset.info())
    print("Building graph for date: " + str(MONTH) + '/' + str(YEAR) + "...")
    Y = []

    # Select the data we want + ignore dataset errors
    for i in dataset.values:
        if i[0] == YEAR and i[1] == MONTH and i[2] > 0.0 and i[3] < 0.0:
            Y.append([i[3], i[2]]) #adding latitude / longitude to our list

    # Transform data to csv
    df = pd.DataFrame(Y)
    df.to_csv('./graphs/' + str(MONTH) + '-' + str(YEAR) + '.csv', index=False)
    print("Wrote graph into " + './graphs/' + str(MONTH) + '-' + str(YEAR) + '.csv')
    return 0


if __name__ == "__main__":
    #MIN DATE (MM/YY): 01/2003
    #MAX DATE (MM/YY): 06/2017
    YEAR = 2003
    MONTH = 1
    main(MONTH, YEAR)
