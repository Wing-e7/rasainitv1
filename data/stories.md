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
