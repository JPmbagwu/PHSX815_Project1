# PHSX815_Project1

# Dice roller

These programs are available in this repository:

* DiceAnalysis.py [Python]
* DiceRoll.py [Python]

# Utilization

The -h or —help flag can be used to print the options when calling any of the executables from the command line. This code creates and displays two histograms using the NumPy and Matplotlib libraries in a straightforward Python script. The first histogram displays the likelihood that each face value (1, 2, 3, 4, 5, 6) will appear after a predetermined number of rolls. When rolling numerous dice at simultaneously, the second histogram displays the frequency of the sum of face values for each experiment. The code initially looks for the "-input" flag or the "—help" flag in the command line arguments (sys.argv), and if either is present, it displays a usage message. The function reads the supplied file name, which is believed to contain the data for the histograms, and saves it to the 'dat' variable if the "-input" flag is present. The sum of the face numbers for each experiment is then calculated once the data has been flattened. Using the Matplotlib function "hist," which accepts the flattened data as input and bins the data into six ranges, the first histogram is produced (1 to 2, 2 to 3, etc.). There are labels, a title, and gridlines in the plot's formatting. The frequency of the sum of face values for each trial is shown in the second histogram, which is produced in a similar fashion but with 20 bins. Finally, the Matplotlib'show' function is used to display both histograms. Once the histograms have been closed, the application will only terminate.
