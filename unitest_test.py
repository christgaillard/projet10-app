import sys
import pytest
import aiounittest
import unittest  
import asyncio
import datetime as dt
from botbuilder.dialogs.prompts import (AttachmentPrompt,
                                        PromptOptions,
                                        PromptValidatorContext)
from botbuilder.core import(TurnContext,
                            ConversationState,
                            MemoryStorage,
                            MessageFactory)

from botbuilder.schema import ActivityTypes,Attachment,Activity
from botbuilder.dialogs import DialogSet, DialogTurnStatus
#from email_prompt import EmailPrompt
from botbuilder.core.adapters import TestAdapter

def check_date(date_str):
    try:
        date_obj=dt.datetime.strptime('%m/%d/%y')
        return date_obj>=dt.datetime.now()
    except Exception as error:
        return False
        

class Bottest(unittest.TestCase):
    def test_date(self):
        d='12/10/2022'  
        self.assertEqual(check_date(d), True) 
        
    def  test_date_bad_format(self):
         d='25/11/2020'
         self.assertEqual(check_date(d), False)
         
    def test_date_old(self):
        d='11/15/2020'     
        self.assertEqual(check_date(d),False)

