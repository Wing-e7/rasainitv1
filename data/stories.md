## interactive_story_1
* greet
    - utter_greet
* pitch{"person_name": "Beenu", "company": "Collegedunia"}
    - slot{"company": "Collegedunia"}
    - slot{"person_name": "Beenu"}
    - utter_nod
* pitch{"admission": "admissions"}
    - slot{"admission": "admissions"}
    - utter_nod
* pitch{"products": "applications"}
    - slot{"products": "applications"}
    - action_customsentiment
    - utter_followup
* get_contact
    - utter_contact
* get_bye
    - utter_bye

## interactive_story_1
    - utter_greet
* pitch{"hurray": {"neg": 0.0, "neu": 1.0, "pos": 0.0, "compound": 0.0}, "company": "Collegedunia", "products": "review"}
    - slot{"company": "Collegedunia"}
    - slot{"products": "review"}
* pitch{"hurray": "{'neg': 0.0, 'neu': 0.769, 'pos': 0.231, 'compound': 0.7184}"}
    - action_customsentiment
* get_contact{"hurray": {"neg": 0.0, "neu": 0.859, "pos": 0.141, "compound": 0.3182}}
    - utter_contact
* get_bye{"hurray": {"neg": 0.0, "neu": 0.612, "pos": 0.388, "compound": 0.4215}}
    - utter_bye

