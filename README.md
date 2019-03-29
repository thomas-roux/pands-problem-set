# pands-problem-set
Solutions to the 2019 problem set for 52445 "Programming and Scripting" module, Higher Diploma in Data Analytics, Galway-Mayo Institute of Technology. 

## Getting Started

### Installing Python 
In order to run the problem sets, you will need to install Python. Python is freely available, and details on how to install and run Python on your native OS are available [here](https://docs.python.org/3/using/index.html). In addition, some of the problems require additional packages in order to execute. These are mentioned within problem descriptions below. 

Alternatively, you can download the free open-source [Anaconda Distribution](https://www.anaconda.com/distribution/) package that includes over 1,500 packages in addition to the latest version of Python. This would preclude the need to download additional packages as mentioned above. 

### Downloading the problem set code
Once you have installed Python, download a zip compressed copy of the problem set code by clicking on the download link in the relevant [github repository](https://github.com/thomas-roux/pands-problem-set). Make sure to unzip the file before proceeding. 

### Executing the problem sets
Open the command line interface. Instructions on how to access the command line interface for your operating system (Windows, Mac or Linux) can be found [here](https://www.ionos.com/help/email-office/troubleshooting-11-11-mail-basicmail-business/opening-a-command-prompt-or-terminal/#c59606). Change file directory to the directory containing the downloaded and unzipped problem set code. Instructions on how to do this in Windows are [here](https://www.computerhope.com/issues/chusedos.htm), and in Mac and Linux [here](https://www.youtube.com/watch?v=j6vKLJxAKfw).

Once in the correct directory, you can run the individual problem sets by typing the following after the command prompt: 'python *problemsetfilename.py*'. Replace *problemsetfilename.py* with the relevant filename as listed below, e.g. sumupto.py. 

Some of the problem sets require a user input to proceed - enter your option when prompted to do so. Other problems merely execute a predefined code and output a result without user input. This is explained under each problem below.

## Problem set descriptions

#### Problem 1: [sumupto.py](https://github.com/thomas-roux/pands-problem-set/blob/master/sumupto.py)
Takes a user entered integer and outputs the sum of all numbers from 1 up to and including the entered number. Contains a `try/except` clause that will continue to execute until the user enters a valid integer. Program will exit if the user enters zero. Program automatically converts a negative integer to a positive before calculating the sum.

#### Problem 2: [begins-with-t.py](https://github.com/thomas-roux/pands-problem-set/blob/master/begins-with-t.py)
Before executing, this program needs to import the **datetime** module from Python. This module is part of the standard Python library and does not need to be downloaded before executing the program. The program determines whether today's day of the week starts with a T, i.e. if today is Tuesday or Thursday. It does not take user input, and will end after outputting the answer.

#### Problem 3: [divisors.py](https://github.com/thomas-roux/pands-problem-set/blob/master/divisors.py)
This program does not take user input. It prints all values between 1000 and 10,000 that are divisible by 6, but not by 12. It will print these sequentially underneath each other on the output. Other values that are divisible by 6 but not by 12 can be calculated by replacing the numbers in the following code on line 9 with a range of your choosing: 
```python
for i in range(1000, 10001):
```

#### Problem 4: [collatz.py](https://github.com/thomas-roux/pands-problem-set/blob/master/collatz.py)
Takes a user entered integer and performs the following calculation: at each step, the next value is determined by taking current value, and if even, divides the value by two; if odd, multiplies by 3 and adds one. Program ends when value equals 1. Outputs each value of calculation on same line. Contains a `try/except` clause that will continue to execute until the user enters a valid integer. Program will exit if the user enters zero. Program automatically converts a negative integer to a positive before performing the calculation.

#### Problem 5: [primes.py](https://github.com/thomas-roux/pands-problem-set/blob/master/primes.py)
Takes a user entered integer and outputs whether integer is a prime number or not. Contains a `try/except` clause that will continue to execute until the user enters a valid integer. Program will exit if the user enters zero. Program automatically converts a negative integer to a positive before performing the calculation. Makes use of `len(list)` to evaluate whether number prime. 

#### Problem 6: [secondstring.py](https://github.com/thomas-roux/pands-problem-set/blob/master/secondstring.py)
Before executing, this program needs to import the **string** module from Python. This module is part of the standard library and does not need to be downloaded before executing the program. Takes a user input string and outputs every second word in the string next to each other on the same line. Contains a `string.punctuation` clause that will not consider standard punctuation as a word if placed on its own, e.g. 'Hello , how are you?' will ignore the ',' and output the following as every second word 'how you?'. The code can be changed to output every odd word by replacing the value in the following line (line 15) of code with zero:
```python
index = 1
```

#### Problem 7: [squareroot.py](https://github.com/thomas-roux/pands-problem-set/blob/master/squareroot.py)
Before executing, this program needs to import the **math** module from Python. This module is part of the standard library and does not need to be downloaded before executing the program. Takes a user input floating number and outputs the square root of the number to the nearest 2 decimal spaces. Contains a `try/except` clause that will continue to execute until the user enters a valid floating number. Program will exit if the user enters zero. Program automatically converts a negative floating number to a positive before performing the calculation.

#### Problem 8: [todays-date.py](https://github.com/thomas-roux/pands-problem-set/blob/master/todays-date.py)
Before executing, this program needs to import the **datetime** module from Python. This module is part of the standard library and does not need to be downloaded before executing the program. This program does not take any user input. Once executed, it outputs today's date in the format Weekday, Month Day Year at Time. The program ends after output.

#### Problem 9: [second.py](https://github.com/thomas-roux/pands-problem-set/blob/master/second.py)
Before executing, this program needs to import the **sys** module from Python. This module is part of the standard library and does not need to be downloaded before executing the program. The program takes a user defined text article argument from the command line and outputs every second line in the text document. To execute this program, type the following at the command prompt: `python second.py *filename.txt*` where `*filename.txt*` is the name of the text file you wish to analyse. The program will end if more than one argument is entered at the command line. The program also contains a `try\except` clause that will raise a `FileNotFoundError` exception if the filename or path variable is incorrect.

#### Problem 10: [plot.py](https://github.com/thomas-roux/pands-problem-set/blob/master/plot.py)
Before executing this program, you will need to download the [Numpy](http://www.numpy.org/) and [Matplotlib](https://matplotlib.org/) packages - click on the links for instructions on how to do this. Once installed, execute the progam. This program does not take user input. It will output a plot of *x, 2x and x\*\*2* in the range 0 to 4 when executed; the program will then end. You can increase the range of the plot by changing the value in the following line of code to any preferred value of *x*:
```python
x = np.arange(5)
```

### Author
The **pands-problem-set solutions** were created by Thomas Roux as part of the 52445 "Programming and Scripting" module for the Higher Diploma in Data Analytics, Galway-Mayo Institute of Technology. Where relevant, attributions to contributors and ideas have been made within each problem code with links. In addition to these sources, the [Python Tutorial](https://docs.python.org/3/tutorial/) was also used extensively.

### License
This project is licensed under the [MIT license](https://github.com/thomas-roux/pands-problem-set/blob/master/LICENSE).


