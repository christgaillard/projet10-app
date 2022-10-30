import sys
import pytest
import aiounittest
import asyncio
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

class EmailPromptTest(aiounittest.AsyncTestCase):
        async def test_email_prompt(self):
            async def exec_test(turn_context : TurnContext):
                dialog_context = await dialogs.create_context(turn_context)
            
            adapter = TestAdapter()
    
            conv_state = ConversationState(MemoryStorage())
            dialogs_states = conv_state.create_property("dialog-state")
            dialogs = DialogSet(dialogs_states)
            #dialogs.add(email_prompt("email_prompt"))
         
            #step1 = await adapter.test('hello', 'what is your email adress?')
            #step2 = await step1.send('My email id is toto@titi.com')
            #await step2.assert_reply("toto@titi.com")
        


