Have a conversation with Doctor Notadoctar, a real PHD!

Hopefully you only have symptoms he is programed to deal with...

Get your expert diagnoses today!

Just run Chatbot.py, talk with the doctor, and let our state of the art symptom analysis
system recommend action!


Features added 
===
### Porter Stemmer
The Porter Stemmer algorithm is an NLP algorithm designed by Martin Stemmer. In essence, it reduces a word down to its "stem", which is the base from which all verb tenses are created. This allows the chat bot to interperet multiple different verb tenses provided by the user. This algorithm is imported from the NLTK Python library.

`What is a symptom you are experiencing? (say none for no more) I'm sneezing a lot too`

The bot understands this to be the same as "I sneezed today"

### Extra chat topic
The new topic is all dentristry related opposed to the original doctor topic we had.

This is all included in the doctor class.

There is a new symptom list with dentistry related issues. Along with their corresponding severity ratings.

While the patient is being asked basic infromation they are also asked what sort of medical professional they require, such as doctor or dentist.
There is error handling for if they do not choose one of these options.

Once a proper choice is made the program runs as normal.
But the symptom list being referenced and compared with the user inputs depends on what physician the user chose prior.

`Are you looking for a general doctor. Or, a dentist? dentist`

`What is a symptom you are experiencing? (say none for no more) My jaw is very sore`

### Misc. Responses 
This consists of a set of new responses to unrecognised symptoms input by the user.
As well as a set of questions randomly chosen to be asked to the user before their final diagnosis.

These two lists of questions and responses are saved within the Doctor class.

A random number is generated when the user inputs a unrecognised symptom, which then selects one of the responses asking for them to retry.

`Are you sure that's a real thing try something else`

`This is a little embarassing. But what is that?`

`Sorry I do not know that symptom`

Then during the diagnosis another random number is generated to chose from a list of questions to simulate small talk with the user.

`This may take a while. Any plans for the weekend?`

`While my diagnosis is being calculated. How's your week been?`

### Synonym Recognition
The bot is able to recognize some synonyms, and as such can provide support for many more user inputs. For example: 

` What is your gender? Male, Female or other. man`

`man is invalid`

`Did you mean: male?`

or

`What is a symptom you are experiencing? (say none for no more) my tummy hurts`

The bot will understand this as "stomach" instead of "tummy"

Limitations
===
The bot still has some issues with misspellings

`What is a symptom you are experiencing? (say none for no more) coug`

`Are you sure that's a real thing try something else`

The bot cannot understand tone or emotion

The bot doesn't recognize named entities

Resources used
=== 

NLTK - Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.