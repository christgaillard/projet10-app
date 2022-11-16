import sys
import pytest
import unittest  
import asyncio
import datetime as dt


def check_date(date_str):
    try:
        date_obj=dt.datetime.strptime(date_str,'%m/%d/%y')
        return date_obj >= dt.datetime.now()
    except Exception as error:
        return False
        

#class Bottest(unittest.TestCase):
    #def test_date_ok(self):
        #d='12/20/2022'  
       #self.assertEqual(check_date(d), True) 
        
    def  test_date_bad_format(self):
         d='25/11/2020'
         self.assertEqual(check_date(d), False)
         
    def test_date_old(self):
        d='10/15/2023'     
        self.assertEqual(check_date(d),False)

