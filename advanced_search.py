import time
import pandas as pd

if __name__ == "__main__":
    while True:
        # keep checking the content in the txt file
        print("advanced_search microservice is running.....")
        time.sleep(3)
        f = open('advanced_search.txt', 'r')
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        f.close()

        # check if the line is empty, if not---> continue to search this item in csv
        if len(line1) != 0 and len(line2) != 0 and len(line3) != 0:
            w = float(line1)
            d = float(line2)
            h = float(line3)
            df = pd.read_csv('home_inventory.csv')
            filtered_df = df.loc[(df['Width'] < w) & (df['Depth'] < d) & (df['Height'] < h)]
            # write the results into advanced_result.csv
            if len(filtered_df) > 0:
                filtered_df.to_csv("advanced_result.csv", index=False)
            # if not found, return not found
            else:
                pd.DataFrame([{"item": 'Not Found'}]).to_csv('advanced_result.csv', mode='a', index=False, header=False)
            # sleep for 5s and delete data in advanced_search text and csv
            time.sleep(5)
            with open('advanced_search.txt', 'r+') as f:
                f.truncate()
            with open("advanced_result.csv", "w") as f_c:
                f_c.write("")
