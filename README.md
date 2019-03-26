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

### Problem set descriptions

#### Problem 1: sumupto.py
Takes a user entered integer and outputs the sum of all numbers from 1 up to and including the entered number. Contains a `try/except` clause that will continue to execute until the user enters a valid integer. Program will exit if the user enters zero. Program automatically converts a negative integer to a positive before calculating the sum.

#### Problem 2: begins-with-t.py
Before executing, this program needs to import the datetime module from Python. This module is part of the standar Python library and does not need to be downloaded before executing the program. The program determines whether today's day of the week starts with a T, i.e. if today is Tuesday or Thursday. It does not take user input, and will end after outputting the answer.

#### Problem 3: divisors.py
This program does not take user input. It prints all values between 1000 and 10,000 that are divisible by 6, but not by 12. It will print these sequentially underneath each other on the output. Other values that are divisible by 6 but not by 12 can be calculated by replacing the numbers in the following code on line 9 with a range of your choosing: ```for i in range(1000, 10001):```

