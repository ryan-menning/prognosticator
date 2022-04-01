# Prognosticator
For some reason I feel the need to explain the name of the project. The original vision for this program was to digest a specific type of data and make a prediction for how to proceed based on an established model. The program does not make any predictions. There, that's out of the way.

Now, a brief explanation of "color numbers" before I get to what the program does do. "Color numbers" is a generic term for what is specifically known as "Lab" or CIELab values. Essentially, CIELab values are a way to plot colors on a 3-dimensional plane.  The "L" value represents a position on the vertical axis, the "a" value represents a position on a horizontal axis and the "b" value represents a position on another horizontal axis that is perpendicular to the "a" axis. For more information on CIELab values you can check out this short [article](https://www.xrite.com/blog/lab-color-space). 

Paint is an easy example to use to describe color. You've likely looked over color swatches at home improvement stores as you searched to find that perfect color to paint a room or wall in your house. All of those different swatches have a specific formula to make that color or shade that is on display. Each formula could consist of a number of different color combinations so it's important for the paint manufacturer to consistently provide the home improvement stores paint that is similar in color from batch to batch. A common way to ensure that color remains consistent between batches is to evaluate color by use of CIELab values against a master standard for a given color. There is typically an allowance for a certain amount of variation from that master standard. The data that is used for this program is that difference between a production batch of "paint" and a master standard.

## What my program is about
The program asks the user to select a csv file from a displayed list. Each file represents a different color/product code and within the files are color deltas for various production batches that represent the color deviation  compared to a master standard of that color/product. Once a valid csv file has been selected by the user the program reads the data into a Pandas dataframe. The program identifies the product code from the file name and then obtains  customer specifications for that product from a separate specifications file. The color variation (color deltas) for each batch is compared to the product specifications and the program displays how many batches are within the lower and upper specification limits. To be considered "good" a batch must have all color values within the specification limits as well as any additional tests that may be required by the customer. The user then has the option to create a histogram for a specific test key for further visual analysis.

## Relevant Packages
There is a requirements.yml file that lists all packages in my Conda Environment. However, the packages required for the python program to operate are:
-  pandas
-  numpy
-  matplotlib
-  seaborn

## How the project meets the Feature List requirements
### Category 1: Python Programming Basics
1. Implement a “master loop” - the program continually loops to allow the user to look at more files or create additional graphs until they choose to exit the program.

2. 	Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program. - Dictionaries and lists are used in a number of places throughout the code. One example is the opening function call to create a dictionary of the available CSV files and display them to the user.

3. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. - There are eleven functions that are called in the program. Many of them return a value that is then used in the code.

### Category 2: Utilize External Data
1. Read data from an external file, such as CSV and use that data in your application. - Data is read from CSV files.

### Category 3: Data Display
1. Visualize data in a graph, chart, or other visual representation of data. - The user has the option to create a histogram for individual test keys of a given product.

### Category 4: Best Practices
1. Utilize a virtual environment and document library dependencies in a requirements.txt file. - Conda was used for my virtual environment. A re
2. Check for invalid inputs - Though it may not be the most elegant input validation the user's input is checked to confirm that it's a valid choice. If it is not valid then a message is displayed to the user that it's invalid.

### “STRETCH” FEATURE LIST
1. The program uses pandas, matplotlib, and numpy for data analysis. 


## How to run the program
The program should be executed with the command: python main.py  
Any histograms that the user creates are saved to the graph_output folder

