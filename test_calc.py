#import our modules
import unittest
import calc

'''
Create Test Cases for the Functions for our Test Cases
Create Test Cases for the Functions We Want to Test
Create a Class that inherits from   unitest.testcase
Create a class method

'''

''' #Section 1
class TestCalc(unittest.TestCase): #Inheriting from unittest.Testcase will give us a lot of testing capabilities in the class
    #write a method that starts with test_
    #First testing our calc function
    #Any method in a class takes self as the first arg
    #We are inheriting our assert methods and this is defined in the documentation
    def test_add(self):
        result = calc.add(10, 5)
        self.assertTrue(result, 15)
#To test this from the command line, run unittest as our main module and pass in the module
#python3 -m unittest test_calc.py
#Lets set it up so we do not need to pass the -m command

#This isn't related to unit testing - it says if we run it directly run the code within our conditional
if __name__ == '__main__':
    unittest.main()

#Now re run with our first method python3 test_calc.py
#Now What happens if our test fails?

'''

'''
#Section 2 - Making our Test Better By adding Edge Cases
#Lets Make Another Test, and this time lets drop our function directly into the assert statement
#This is still one Test, we just iterated and improved it by adding additional assertions

class TestCalc(unittest.TestCase):

    def test_add(self):
        #Lets Test Some Edge Cases
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

if __name__ == '__main__':
    unittest.main()


#It is not our goal to write as many tests as we can its our goal to write good tests!
#To add more tests we just add in more test methods

'''

#Section 3 - Add in more test

class TestCalc(unittest.TestCase):

    def test_add(self):
        #Lets Test Some Edge Cases
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        #Lets Test Some Edge Cases
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)


    def test_multiply(self):
        #Lets Test Some Edge Cases
        self.assertEqual(calc.multiple(10, 5), 50)
        self.assertEqual(calc.multiple(-1, 1), -1)
        self.assertEqual(calc.multiple(-1, -1), 1)

    def test_divide(self):
        #Lets Test Some Edge Cases
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()


'''
#Section 4
#Lets test that dividing by Zero raises the Error
#We first pass in the exception we expect which is a value error, and then the function
#we want the function we want to run, then we pass in each arg we want to pass to the divide function
#This will pass. Indeed the Value Error. Chaange the value to 2
        self.assertRaises(ValueError, calc.divide, 10, 2)
    
'''

#Section 5
#Lets use the context manager and call our function the way we normally would
'''
    with self.assertRaises(ValueError):
    calc.divide(10, 0)
'''




