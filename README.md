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

### ADAM COLLINS - Developer
I was in charge of implementing the extra chat topic. As well as the miscellaneous chatbot responses.

Both of these features exist exclusively within the Doctor class.

The extra chat topic is based around dentistry, this means that there is now a second symptom list.
With all new symptoms as well as new severity ratings.

In the doctor class when the chatbot is ran it will prompt the user on whether or not they need a dentist or doctor for advice, when one is selected only it's respective symptom list is acknowledged
while the user is inputting symptoms.

For the miscellaneous chatbot responses these take shape in two ways.

The first being a list of responses for when a symptom that does not exist is written
by the user
The second way is by asking a random question to the user while their diagnosis is being generated.


Features added 
===
### Porter Stemmer
The Porter Stemmer algorithm is an NLP algorithm designed by Martin Stemmer. In essence, it reduces a word down to its "stem", which is the base from which all verb tenses are created. This allows the chat bot to interperet multiple different verb tenses provided by the user, as well as misspelings. This algorithm is imported from the NLTK Python library.
`code here`
### Extra chat topic
The new topic is all dentristry related opposed to the original doctor topic we had.

This is all included in the doctor class.

There is a new symptom list with dentistry related issues. Along with their corresponding severity ratings.

While the patient is being asked basic infromation they are also asked what sort of medical professional they require, such as doctor or dentist.
There is error handling for if they do not choose one of these options.

Once a proper choice is made the program runs as normal.
But the symptom list being referenced and compared with the user inputs depends on what physician the user chose prior.

### Misc. Responses 
This consists of a set of new responses to unrecognised symptoms input by the user.
As well as a set of questions randomly chosen to be asked to the user before their final diagnosis.

These two lists of questions and responses are saved within the Docotr class.

A random number is generated when the user inputs a unrecognised symptom, which then selects one of the responses asking for them to retry.

Then during the diagnosis another random number is generated to chose from a list of questions to simulate small talk with the user.