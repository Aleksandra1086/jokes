'''Create a new Python file in this folder called jokes.py
● You are going to create a random joke generator using Python’s random
module. This will require a bit of research on your part. For more
information on the random module look here.
● Create a list of jokes.
● Use the random module to display a random joke each time the code
runs.

'''

import random

list_of_jokes = ['Flash the big wads of tens and twenties you created with your color laser printer and top-notch graphics program.',
'Spend an evening playing floppy disks backward, listening for the secret messages about Satan.',
'Invite her back to your place to show her the etchings on your Newton MessagePad.',
'Let the lady go first when you reach the virtual reality escalator.', 'Serenade her with your MIDI-compatible drum pads.',
'Have your dinner illuminated by the soft glow of an active-matrix LCD panel.',
'If you\'re getting serious, consider a set of \'his \'n\' her\' system unit keys.',
'Drive her crazy by murmuring tender love words with the help of a French-speaking voice-synthesizer.',
'Never type on your date\'s laptop computer without permission, particularly if the system is on her lap.']

random_joke = random.choice(list_of_jokes)

print(' How can a computer guy impress his date ;) : '+ random_joke + ' :)')




