import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''Two, of course there are two.
It seems perfectly natural now——
The one who never looks up, whose eyes are lidded
And balled¸ like Blake's.
Who exhibits

The birthmarks that are his trademark——
The scald scar of water,
The nude
Verdigris of the condor.
I am red meat. His beak

Claps sidewise: I am not his yet.
He tells me how badly I photograph.
He tells me how sweet
The babies look in their hospital
Icebox, a simple

Frill at the neck
Then the flutings of their Ionian
Death-gowns.
Then two little feet.
He does not smile or smoke.

The other does that
His hair long and plausive
Bastard
Masturbating a glitter
He wants to be loved.

I do not stir.
The frost makes a flower,
The dew makes a star,
The dead bell,
The dead bell.

Somebody's done for.
           Sylvia ploth''')

engine.runAndWait()