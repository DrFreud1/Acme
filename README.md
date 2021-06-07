# Acme Exercise
The following repository contains a set of scripts to calculate the payments for an employee accordingly to the compensation policies from ACME company.

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday

00:01 - 09:00 25 USD

09:01 - 18:00 15 USD

18:01 - 00:00 20 USD

Saturday and Sunday

00:01 - 09:00 30 USD

09:01 - 18:00 20 USD

18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday

TU: Tuesday

WE: Wednesday

TH: Thursday

FR: Friday

SA: Saturday

SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

## Requirements
There are no requirements besides having python 3 for the main script as no external libraries were allowed for the present exercise. The only requirement for the test script is pytest library which can be installed as follows: 
```console
pip install pytest
```

## Solution
There are three main functions within the main script, those are designed to carry out three main tasks:
1. To clean the input and to make it readable for the program
2. To check the day of the week and to calculate the payments accordingly
3. To actually calculate the payments corresponding to each employee

The program can calculate payments for different work shifts on the same day, having inputs as follows: MATEO=SA14:00-18:00,SA20:00-21:00 which calculates payments for different shifts on Saturday.

## Testing
Testing was carried out for the following inputs:
1. SANTIAGO=MO09:00-12:00,MO23:00-24:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
2. RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
3. ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
4. GENESIS=WE09:00-11:00,FR18:00-20:00,SA00:00-02:00
5. MATEO=SA14:00-18:00,SA20:00-21:00

Their correspoding outputs are 250,215,85,130 and 105.

## Running

Run program
```console
python3 acme.py
```
Run unit tests
```console
python3 acme_test.py
```
