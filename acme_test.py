from acme import *
import unittest

class TestPicoyPlacaPredictor(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        inputs = ['SANTIAGO=MO09:00-12:00,MO23:00-24:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 
        'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
        'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'GENESIS=WE09:00-11:00,FR18:00-20:00,SA00:00-02:00', 
        'MATEO=SA14:00-18:00,SA20:00-21:00']
        expected_outputs = [250,215,85,130,105]
        
        for input,output in zip(inputs,expected_outputs):
            employee_name, working_hours = clean_input(input)
            result = calculate_payment(working_hours)
            print(input)
            self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()