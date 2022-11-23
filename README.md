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
You need to install pytest to run the unit tests, besides that, there are no further requirements. Install it using
```console
pip install pytest
```
or
```console
pip install -r requirements.txt
```

## Solution
There are two main classes which contain the logic to calculate the payments to ACME employees, they are located in the *app* folder. 

Basically, what has been done is to create an Employee class that contains the name of the employee and the salary received by that employee could be updated according to the input data. The Employee class also contains the method to load and clean input data according to what is required.

The PaymentManager class contains the logic necessary to update salaries of employees from Employee class, according to input data.

In the *utils* folder you'll find some constants that establish the bussiness rules for the present application.

For testing, the *pytest* library is used. Besides, you can notice that Github Actions have been also used.
## Running

Run program
```console
python3 main.py
```
Run unit tests
```console
python3 -m pytest .
```
