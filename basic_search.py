import time
import pandas as pd

if __name__ == "__main__":
    while True:
        # keep checking the content in the txt file
        print("search microservice is running.....")
        time.sleep(3)
        file = open('search_item.txt', 'r')
        item = file.readline()
        file.close()

        # check if the line is empty, if not---> continue to search this item in csv
        if len(item) != 0:
            df = pd.read_csv('home_inventory.csv')
            res = df[df["Name"] == item]
            if res.shape[0] > 0:
                # write the res row into result.csv
                res.to_csv('result.csv', mode='a', index=False, header=False)
                # open search_item.txt and delete contents (so that the text file will be empty and this program will
                # not keep writing results to csv)
                with open('search_item.txt', 'r+') as f:
                    f.truncate()
            # if not found, return not found
            else:
                pd.DataFrame([{"item": 'Not Found'}]).to_csv('result.csv', mode='a', index=False, header=False)
                with open('search_item.txt', 'r+') as f:
                    f.truncate()















