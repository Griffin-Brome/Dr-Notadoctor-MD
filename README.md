Have a conversation with Doctor Notadoctar, a real PHD!

Hopefully you only have symptoms he is programed to deal with...

Get your expert diagnoses today!

Just run Chatbot.py, talk with the doctor, and let our state of the art symptom analysis
system recommend action!

Installation
===
This application requires Python 3

`# apt install python3`

`$ pip3 install -r requirements.txt`

To run it, simply execute Chatbot.py

`$ python3 -m Chatbot.py`

Then follow the provided prompts

Team
===

### NATE WICKENHEISER - Developer
I created a patient and symptom classes

A patient object will be created during conversation with the doctor
A Symptom object will be created during during conversation aswell

Symptoms will be added to the patient object, since they are all stored
in the end you can retrieve them and give a final diagnoses

My test.py class just gives examples how to use

### GRIFFIN BROME - Project Manager
I wrote the project documentation and oversaw the design and implementation of the application.

I created the Project Charter, WBS, and Gantt Chart. I also created the DFD's 

I provided support to the team in successfully setting up thier workflows and development environments. I also set up the Github repository and help team members learn git. Finally I merged changes into master and resolved merge conflicts in order to setup the final product 


Features added 
===
### Porter Stemmer
The Porter Stemmer algorithm is an NLP algorithm designed by Martin Stemmer. In essence, it reduces a word down to its "stem", which is the base from which all verb tenses are created. This allows the chat bot to interperet multiple different verb tenses provided by the user, as well as misspelings. This algorithm is imported from the NLTK Python library.
`code here`
### Extra chat topic
For the extra topic, the chatbot's diagnostic functionality was extended to include dentistry. As such it can now recognise queries meant for a dental professional and diagnose them.
`code here`
### Misc. Responses 
Several random phrases were added to the chatbot's repertoire. These are implemented as two lists, from which random responses are chosen. This occurs when a user queries the bot with an unknown symptom, as well as prior to calculating the final diagnosis.
`code here`
