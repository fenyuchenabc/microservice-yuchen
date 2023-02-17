# Microservice-yuchen
# file description:
There are 1 text file, 2 python files and 2 csv files in the microservice package.

basic_search.py: This is the microservice program. Run it first and it will keep running at the background.
                 It will receive requests from the test program and perform the task required.

test_program.py: This is a test program to simulate the main program sending requests to the microservice and  
                 receive data.

home_inventory.csv: This is the csv file of database. It stores all the infomation of the items.

search_item.txt: This is the data pipeline to store the name of searched item. Test program will write info in this
                 file and the microservice will read from this file.

result.csv: This is the csv file to store the result of search. The test program will read the info from this file.

# How to request data from the microservice:
In the microserive python file, it keeps checking if there is a string in the search_item.txt:

        file = open('search_item.txt', 'r')
        item = file.readline()
        file.close()
        # check if the line is empty, if not---> continue to search this item in csv
        if len(item) != 0:
        
Therefore, to request data from microservice, the main program needs to open search_item.txt and write the string of item name in it. So that the microservice will continue to search this name in csv.
For example:

        search_item = str(input("Enter the item you want to search"))
        f = open('search_item.txt', 'w')
        f.write(search_item)
        f.close()

# How to receive data from the microservice:
To receive data from the microservice, simply read the last row from result.csv, For example:

        df = pd.read_csv('result.csv', header=None, names=["Name","Brand","Category","Color","Location","Width","Depth","Height","Price","Link"])
        print(df.iloc[-1:])

This code will read the last row of data in result.csv file, which is the item detail just searched.


# UML Sequence Diagram
<img width="897" alt="image" src="https://user-images.githubusercontent.com/56098703/218611000-d79ae150-2d22-4c94-bf16-5f8852960346.png">

# For more details, check out the test_program.py





    
