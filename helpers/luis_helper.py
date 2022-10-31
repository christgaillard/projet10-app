# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from enum import Enum
from typing import Dict
from botbuilder.ai.luis import LuisRecognizer
from botbuilder.core import IntentScore, TopIntent, TurnContext
from booking_details import BookingDetails
from datetime import date

class Intent(Enum):
    BOOK_FLIGHT = "book"
    CANCEL = "Cancel"
    GET_WEATHER = "GetWeather"
    NONE_INTENT = "NoneIntent"


def top_intent(intents: Dict[Intent, dict]) -> TopIntent:
    max_intent = Intent.NONE_INTENT
    max_value = 0.0

    for intent, value in intents:
        intent_score = IntentScore(value)
        if intent_score.score > max_value:
            max_intent, max_value = intent, intent_score.score

    return TopIntent(max_intent, max_value)


class LuisHelper:
    @staticmethod
    async def execute_luis_query(
        luis_recognizer: LuisRecognizer, turn_context: TurnContext
    ) -> (Intent, object):
        """
        Returns an object with preformatted LUIS results for the bot's dialogs to consume.
        """
        result = None
        intent = None
        recognizer_result = await luis_recognizer.recognize(turn_context)

        try:
            recognizer_result = await luis_recognizer.recognize(turn_context)

            intent = (
                sorted(
                    recognizer_result.intents,
                    key=recognizer_result.intents.get,
                    reverse=True,
                )[:1][0]
                if recognizer_result.intents
                else None
            )

            if intent == Intent.BOOK_FLIGHT.value:
                result = BookingDetails()
                #print(recognizer_result)
                # We need to get the result from the LUIS JSON which at every level returns an array.
                to_entities = recognizer_result.entities.get("$instance", {}).get(
                    "dst_city", []
                )
                if len(to_entities) > 0 :
                    result.destination = to_entities[0]["text"].capitalize()
                else:
                    result.destination = None
                # if len(to_entities) > 0:
                #     if recognizer_result.entities.get("dst_city", [{"$instance": {}}])[0][
                #         "$instance"
                #     ]:
                #         result.destination = to_entities[0]["text"].capitalize()
                #     else:
                #         result.unsupported_airports.append(
                #             to_entities[0]["text"].capitalize()
                #         )

                from_entities = recognizer_result.entities.get("$instance", {}).get(
                    "or_city", []
                )
                if len(from_entities) > 0 :
                    result.origin = from_entities[0]["text"].capitalize()
                else:
                    result.origin =None
                # if len(from_entities) > 0:
                #     if recognizer_result.entities.get("or_city", [{"$instance": {}}])[0][
                #         "$instance"
                #     ]:
                #         result.origin = from_entities[0]["text"].capitalize()
                #     else:
                #         result.unsupported_airports.append(
                #             from_entities[0]["text"].capitalize()
                #         )

                buge_entities = recognizer_result.entities.get("$instance", {}).get(
                    "budget", []
                )
                if len(buge_entities) > 0 :
                    result.travel_budget = buge_entities[0]["text"].capitalize()
                else:
                    result.travel_budget = None


                date_start=recognizer_result.entities.get("str_date", [])
                date_end=recognizer_result.entities.get("end_date", [])
               # print(type(date_start))
               # print(date_end)
     
                # This value will be a TIMEX. And we are only interested in a Date so grab the first result and drop
                # the Time part. TIMEX is a format that represents DateTime expressions that include some ambiguity.
                # e.g. missing a Year.
                date_entities = recognizer_result.entities.get("datetime", [])
                
                print("--------------------")
                date_voyage=[]
                if date_entities:
                    for dates in date_entities:
                        if dates['type']=='date':
                            data=dates['timex'][0]
                            #si la date renvoyé ne contient pas l'année
                            data=data.replace('XXXX', str(date.today().year))
                        elif dates['type']=='daterange':
                            data = dates['timex'][0]
                            data = data.replace('(','')
                            data = data.replace(')','')
                            data = data.split(',')
                            if len(date_entities)>1:
                                date_voyage.append(data[0].replace('XXXX', str(date.today().year)))
                                date_voyage.append(data[1].replace('XXXX', str(date.today().year))) 
                            else:
                                 data = data[0].replace('XXXX', str(date.today().year))  
                        date_voyage.append(data)        
                
                    if len(date_voyage) > 1:
                        if date_voyage[0]<date_voyage[1]:
                            result.travel_date = date_voyage[0]
                            result.return_date = date_voyage[1]
                        else:
                            result.travel_date = date_voyage[1]
                            result.return_date = date_voyage[0]
                    else:
                        result.travel_date=date_voyage[0]
                              
                else:
                    result.travel_date = None
                    result.return_date = None    
                         
                print("--------------------")
                print(date_start)
                print(date_end)
                print(f"date_allée : {result.travel_date}")
                print(f"date_retour : {result.return_date}")   
                      
                #si l'entities date existe:
               
                    # timex == date allèe
                #timex =     date_entities[0]["timex"]
                    # si 
                #if len(date_entities)>=2 :
                #        timex_ret = date_entities[1]["timex"]
                #else:
                #        timex_ret = None   
                         
                #if timex:
                #        datetime = timex[0].split("T")[0]
                        #print(datetime)
                #        result.travel_date = datetime
                #if timex_ret :
                #        datetime_ret = timex_ret[0].split("T")[0]
                #        result.return_date = datetime_ret
                

        except Exception as exception:
            print(exception)

        return intent, result
