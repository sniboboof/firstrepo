myfizzbuzz release version 1.0

1 file: myfizzbuzz.py

contains two functions: fizzbuzz and fizzbuzzetc

fizzbuzz(int n)
accepts an integer, checks if the integer is divisible by 15, 5, 3, or none of the above and returns the appropriate string (fizzbuzz for 15, buzz for 5, fizz for 3, and a string of the integer if none of the above)

fizzbuzzetc(int n, list noises)
accepts an integer and a LIST of TUPLES, each of the tuples should contain an integer at index 0 and a string at index 1. fizzbuzzetc checks if n is divisible by the integer at index 0 in each tuple, and if so, adds the appropriate string to the return value.
if the user does not specify the list, the function uses the default values for fizz and buzz, functioning exactly like fizzbuzz, but if the user does not include fizz and buzz in their list, there will be no fizzing or buzzing.