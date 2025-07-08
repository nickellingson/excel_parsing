# parse data files
# add logic to find problems in data
# can be used to help with our cleaning pipeline

import pandas as pd

def read_data(file):
    df = pd.read_csv(file)

    # df = df.reset_index()
    df.index += 1

    print(df)

    for index, row in df.iterrows():

        # add whatever logic needed

        # print(index, row['first_appeared'], row['last_appeared'])

        # if row['menus_appeared'] > row['times_appeared']:
        #     print(index, row)

        if row['first_appeared'] > row['last_appeared']:
            print(index, row)


if __name__=="__main__":
    file = "Dish.csv"
    read_data(file)