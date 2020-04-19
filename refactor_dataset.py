#!/usr/bin/env python3
import pandas as pd

def main():
    dataset = pd.read_csv('./dataset/crime.csv')

    # displaying a few information on the dataset
    print("DATASET INFORMATIONS:")
    print(dataset.info())
    print("SHAPE:", dataset.shape)

    # removing  HOUR,MINUTE,DAY,HUNDRED_BLOCK,X,Y,NEIGHBOURHOOD fields that are useless for our clustering in order reduce weight
    #dataset = dataset.drop("TYPE", axis=1)
    #dataset = dataset.drop("DAY", axis=1)
    #dataset = dataset.drop("HOUR", axis=1)
    #dataset = dataset.drop("MINUTE", axis=1)
    dataset = dataset.drop("X", axis=1)
    dataset = dataset.drop("Y", axis=1)
    dataset = dataset.drop("HUNDRED_BLOCK", axis=1)
    dataset = dataset.drop("NEIGHBOURHOOD", axis=1)

    dataset.to_csv('./dataset/crime_small.csv', index=False)
    return 0


if __name__ == "__main__":
    main()
