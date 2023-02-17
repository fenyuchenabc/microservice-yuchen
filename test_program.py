import time
import pandas as pd

if __name__ == "__main__":
    while True:
        try:
            user_input = int(
                input("Enter '1' to send search request or '2' for advanced search"))
        except ValueError:
            print("Please enter a valid number\n")
            continue
        else:
            if user_input == 1:
                search_item = str(
                    input("Enter the item you want to search"))
                print("searching for ", search_item)
                f = open('search_item.txt', 'w')
                f.write(search_item)
                f.close()
                time.sleep(3)

                # read the last row in csv file and display
                df = pd.read_csv('result.csv', header=None,
                                 names=["Name", "Brand", "Category", "Color", "Location", "Width",
                                        "Depth", "Height", "Price", "Link"])
                print(df.iloc[-1:])
            elif user_input == 2:
                width = str(
                    input("Enter the maximum width you want"))
                depth = str(
                    input("Enter the maximum depth you want"))
                height = str(
                    input("Enter the maximum height you want")
                )
                f = open('advanced_search.txt', 'w')
                f.write(width + '\n' + depth + '\n' + height)
                f.close()
                time.sleep(5)
                # output the result
                df = pd.read_csv('advanced_result.csv', header=None,
                                 names=["Name", "Brand", "Category", "Color", "Location", "Width",
                                        "Depth", "Height", "Price", "Link"])
                print(df)



