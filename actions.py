# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Text, List, Dict, Any
import datetime
from rasa_sdk.events import ReminderScheduled, ReminderCancelled

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa.core.events import SlotSet
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import pymysql
import mysql.connector
import pandas as pd
import json 



class ActionCustomSentiment(Action):

    def name(self) -> Text:
        return "action_customsentiment"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn=pymysql.connect(host='localhost',port=int(3306),user='root',passwd='IPmanValley',db='rasa')
        df=pd.read_sql_query("SELECT * FROM yip.events ",conn, index_col = 'id')
        l = len(df[df.intent_name == 'pitch'].index)
        m = ''
        for i in range(0,l):
            text = df[df['intent_name']== 'pitch']['data'].iloc[i]
            res = json.loads(text) 
            k = res['text']
            m = m +' '+ k

        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(m)

        if ss['neg'] >= 0.1:
            #tracker.trigger_followup_action(action_utter_getout)
            dispatcher.utter_message(template = 'utter_getout')
        elif ss['pos'] >= 0.4:
            #tracker.trigger_followup_action(action_utter_ilike)
            dispatcher.utter_message(template = 'utter_ilike')
        else:
            #tracker.trigger_followup_action(action_utter_allfine)
            dispatcher.utter_message(template = 'utter_followup')
            
            
        return []

class ActionBargainDiscount(Action):
    def name(self) -> Text:
        return "action_bargaindiscount"

    @staticmethod
    def required_slots(tracker):
        return ["campaignprice",
                "personname"]
       
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ):
        name = tracker.get_slot("personname")
        price = tracker.get_slot("campaignprice")
        closingprice = 0.6*price
        
        bargainprice = tracker.get_slot("bargainprice")
        
        # RNN to utter bargain messages
        if bargainprice <= closingprice:
            dispatcher.utter_message("All right i can work at {}".format(closingprice))
            tracker.trigger_followup_action(self.utter_priceagreedfollowup)
            return events
        else:             
            dispatcher.utter_message("No {}".format(name))
            dispatcher.utter_message("Like I said earlier, we are low on funds and that price point would not be affordable at this point of time")
        return []

class Info_Form(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "info_form"


#@staticmethod
    def required_slots(tracker):
        return [
        "job_function",
        "products",
        "budget",
        "business_email",
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Thanks for the info")
        return []

class TrainForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "train_form"


#@staticmethod
    def required_slots(tracker):
        return [
        "performance",
        "admissioninfo",
        "branding",
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Okay")
        return []



