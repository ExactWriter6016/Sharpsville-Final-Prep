import random
import os
import sys
import time
import streamlit as st

Timing = 1.5
Timing_2 = 0.5
categories = ["Science", "Writers", "Poets", "Playwrights", "Philosophers", "Social_Scientists", "Composers", "Artists"]
Incorrect = 0
Correct = 0
Chinese_Dynasties = ["Xia Dynasty", "Shang Dynasty", "Zhou Dynasty",]
Chinese_Dynasties_Dict = {"Xia Dynasty": ["2100-1600 BCE", "Part of the Three Dynasties (Zhou, Shang)"],
                          "Shang Dynasty": ["1600-1050 BCE", "Part of the Three Dynasties (Xia, Zhou)"],
                          "Zhou Dynasty": ["1046-256 BCE", "Capitals Hao & Luoyang", "split into Western ___ (1046-771 BCE) and Eastern _____ (771 - 256 BCE)"],
                          }

Topics = {
    "Science": ["Einstein", "Newton", "Decartes", "Kepler", "Boltzmann", "Dalton", "Lavoisier", "Schrodinger", "Bohr", "Rutherford", "Mendeleev", "Liebnizz", "Hawking"],
    "Writers": ["Plath", "Dickens", "Miller", "Tolstoy", "Woolf", "Achube", "Morrison", "Fitzgerald", "Hemmingway", "Scott", "Chopin", "Salinger", "Chaucer", "Hugo", "Faulkner", "Hawthorne", "Vonnegut", "Cather", "Steinback", "Joyce", "Austen", "Zola", "Defoe", "Lewis", "Kafka", "Wharton", "Paton", "Hardy", "Bronte", "Dante",],
    "Poets": ["Owen", "Shelley", "Ginsberg", "William Carlos Williams", "Pope", "Neruda", "Horace", "Coleridge", "Li Po", "Elliot", "Emerson", "Yeates", "Poe", "Frost", "Longfellow", "Blake", "Dickenson", "Wordsworth", "Tennyson", "Byron", "Kipling", "Whittman",],
    "Playwrights": ["ONeill", "Chekov", "Manet", "Marlowe", "Pinter", "Glass", "Sophocles", "Beckett",],
    "Philosophers": ["Locke", "Plato", "Kant", "Hobbes", "Rousseau", "Machiavelli", "Ptolomy", "Mill", "Smith", "Weber", "Mead", "Bacon", "Carnegie"],
    "Social_Scientists": ["Freud", "Milgram"],
    "Composers": ["Elgar", "Prokofiev", "Beethoven", "Mozart", "Debussy", "Ravel", "Tchaikovsky", "Stravinsky", "Handel", "Bizet", "Copland", "Brahms", "Sibelius", "Liszt", "Strauss", "Mussorosky", "Mendelssohn", "Gershwin", "Rachmaninoff",],
    "Artists": ["da Vinci", "Michealangelo", "Picasso", "Rodin", "Turner", "Hals", "Leutze", "Rembrandt", "Manet", "Magritte", "Vemeer", "Cole", "Copely", "Wood"]
}
Calculus_Formulas = ["Cos(x)",]
Calculus_Formula_Dict = {
    "Cos(x)": "d/dx[sin(x)] = ?",
}

Questions_Set = {
    # Science Starts Here#
    "Einstein": ["Special Relativity", "General Relativity", "Photoelectric Effect"],
    "Newton": ["Universal Theory of Gravity", "Calculus", "Laws of Motions"],
    "Kepler": ["Laws of Planetary Motion"],
    "Boltzmann": ["Namesake Constant"],
    "Dalton": ["Modern Atomic Theory"],
    "Lavoisier": ["First Chemist"],
    "Schrodinger": ["Cat"],
    "Bohr": ["Atomic Model"],
    "Rutherford": ["Discovery of Nucleus"],
    "Mendeleev": ["Periodic Table"],
    "Liebnizz": ["Helped create Calculus"],
    "Hawking": ["Brief Answers to the Big Questions"],
    "Decartes": ["Discourse on the Method", ],

    # Writers Start Here#
    "Plath": ["Bell Jar", "Every woman loves a fascist"],
    "Dickens": ["Great Expectations", "Christmas Carol", "A Tale of Two Cities"],
    "Miller": ["Crucible", "Death of a Salesman", "The Man Who Had All the Luck", "After the Fall", "All My Sons",],
    "Tolstoy": ["Anna Karenina", "War and Peace"],
    "Woolf": ["To the Lighthouse", "Orlando", "A Room of One's Own", "Stream-ofconsousness"],
    "Achube": ["Things Fall Apart", "No Longer At Ease"],
    "Morrison": ["Bluest Eyes", "Beloved"],
    "Fitzgerald": ["Great Gatsby"],
    "Hemmingway": ["The Sun Also Rises", "For Whom the Bell Tolls", "The Old Man and the Sea",],
    "Scott": ["Ivanhoe",],
    "Chopin": ["Story of an Hour", "Awakening",],
    "Salinger": ["Catcher in the Rye"],
    "Chaucer": ["Canterbury Tales"],
    "Hugo": ["Les Miserables", "Hunchback of Notre Dame"],
    "Faulkner": ["Absalom Absalom", "Sound and the Fury"],
    "Hawthorne": ["Scarlet Letter", "Dr. Heidegger's Experiment", "The Gray Champion",],
    "Vonnegut": ["Cat's Cradle", "Slaughterhouse 5",],
    "Cather": ["My Antonia",],
    "Steinback": ["Grapes of Wrath", "Of Mice and Men"],
    "Joyce": ["Dubliners", "Ulysses"],
    "Austen": ["Pride and Predjudice"],
    "Zola": ["J'accuse"],
    "Defoe": ["Moll Flanders", "A Journal of the Plague Year", "Robinson Crusoe"],
    "Lewis": ["Elmer Gantry", "Babbit", "Doc Vickerson & bacteriophage against the plague", "Main Street",],
    "Kafka": ["The Metamorphasis", "The Trial"],
    "Wharton": ["The Age of Innocence",],
    "Paton": ["Cry, The Beloved Country",],
    "Hardy": ["Far from the maddening crowd", "Tess D'Ubervilles",],
    "Bronte": ["Jane Eyre",],
    "Dante": ["Divine Comedy", "Inferno", "Vergil hypeman",],


    # Poets start here#
    "Owen": ["Gas, Gas", "WW1 Poet", "Dulce et Decorum Est", "Anthem for the Doomed Youth"],
    "Shelley": ["Ozymandius", "Husband of Mary Shelley"],
    "Ginsberg": ["Howl", '"I saw the best minds of my generation"',],
    "William Carlos Williams": ["Red Wheelbarrow", "This Is Just To Say", '"Plums"', "Icebox",],
    "Pope": ["Rape of the Loch", "An Essay on Man", '"A little learning is a dangerous thing"',],
    "Neruda": ["Song of Despair", "Heights of Machu Pichu"],
    "Horace": ["Carpe Diem", "Carmina",],
    "Coleridge": ["Kubla Kahn", "Rime of an Anchient Mariner", "Frost at Midnight", "Christabel",],
    "Li Po": ["Song of the Forge", "She spins silk", "Falling plum blossums"],
    "Elliot": ["The Hollow Men", "The Wasteland", "Prufrock", "Practical Cats", "Ash Wednesday", "Quartets",],
    "Emerson": ["American Scholar", "Nature", "Representative Men"],
    "Yeates": ["Easter, 1916", "Circus Animals Desertion", "The Second Coming", "Sailing To Byzantium", "The Countess Cathleen", "The Land of Heart's Desire", "The King's Threshold", "Dierde"],
    "Poe": ["The Raven", "Cask of a Monteago", "The Telltale Heart"],
    "Frost": ["The Road Not Taken", "Fire and Ice", "Mending Wall", '"Drink and be whole again beyond confusion"'],
    "Longfellow": ["Paul Revere's Ride", "Song of Hiawatha",],
    "Blake": ["The Tyger", "Poison Tree",],
    "Dickenson": ["Hope is the Thing with Feathers", "I'm Nobody", "Because I Could Not Stop For Death"],
    "Wordsworth": ["I Wandered lonely as a cloud", "My Heart Leaps Up", "Tintern Abbey"],
    "Tennyson": ["Crossing the Bar", "Tithonus", "Charge of the Light Brigade"],
    "Byron": ["She Walks in Beauty",],
    "Kipling": ["White Man's Burden", "If", "Jungle Book"],
    "Whittman": ["Oh Capitan", "Mighty Yawp", "Song of Myself", "Leaves of Grass"],

    # Social Scientists start here#
    "Freud": ["Id, Ego", "The Interpretation of Dreams"],
    "Milgram": ["Stanford Prison Experiment", "Obediance Experiments"],

    # Composers#
    "Elgar": ["Enigma Variations", "Pomp and Circumstance"],
    "Prokofiev": ["Romeo and Juliet"],
    "Beethoven": ["Choral", "Pastoral"],
    "Stravinsky": ["Firebird", "Rite of Spring", "Procession of the Sage", "The Adoration of the Earth", "The Sacrifice", "Petrushka", "Blackmoor", "Ballet Russes", "Liadov", '"Basoon solo rioting"',],
    "Ravel": ["Bolero", "Pavane for a Dead Princess", "Mother goose", "Jeux d'eau",],
    "Tchaikovsky": ["Swan Lake"],
    "Debussy": ["Prelude to a  Fawn"],
    "Mozart": ["Eine Cline Nocht", "Marriage of Figaro", "Magic Flute",],
    "Handel": ["Messiah", "Water music"],
    "Bizet": ["Carmen"],
    "Copland": ["Fanfare for the Common Man", "A Lincholn Portrait", "Appalachian Spring",],
    "Brahms": ["German Requiem", "21 Hungarian Dances", '"Beethovens Tenth"'],
    "Sibelius": ["Finlandia", "Swan of Tuonela", "Lemminkainen Suite"],
    "Liszt": ["Hungarian Rhapsodies", "Dante Symphony", "Las Precludes", "Gypsey",],
    "Strauss": ["Alpine Symphony", "Symphonia Domestica", '"Song of the Night Wanderer"',],
    "Mussorosky": ["Pictures at an Exhibition"],
    "Mendelssohn": ["Midsummer's Nights Dream", "Italian Symphony", "Reformation", "Hebrides Overture", "Canachos Wedding", "First Walpurgis Night",],
    "Gershwin": ["Rhapsody in Blue", "An American in Paris", "Rumba", "Cuban Overture",],
    "Rachmaninoff": ["Symphonic Dances", "Caprice Bohemian", "A Theme of Pagnini"],

    # Philosophers start here#
    "Locke": ["Two Treatices of Government", "Social Contract", "Thoughts on Education", "An Esssay Concerning Human Understanding"],
    "Plato": ["Republic", "Allegory of the Cave", "Apology"],
    "Kant": ["Ground Work of the Metaphysics of Morals", "Transcendental Doctrine of the Elements", "Critique of Pure Reason"],
    "Hobbes": ["Leviathan"],
    "Rousseau": ["Origin of Languages", '"Everywhere in chains"'],
    "Mill": ["On Liberty"],
    "Ptolomy": ["Geography", "Almagist"],
    "Machiavelli": ["The Prince", "Discourse Or Dialogue Concerning Our Language"],
    "Smith": ["Wealth of Nations",],
    "Weber": ["Capitalism",],
    "Mead": ["Coming Of Age In Samoa",],
    "Bacon": ["Novum Organum",],
    "Carnegie": ["Gospel of Wealth",],

    # Playwrights start here#
    "ONeill": ["Ice Man Cometh", "Long Days Journey Into Night"],
    "Chekov": ["Cherry Orchard", "Seagull"],
    "Manet": ["Glengarry Glen Ross",],
    "Marlowe": ["Jew of Malta", "Doctor Faustus", "Tamburlaine the Great", '"Shakespeare contemporary"',],
    "Pinter": ["The Dumb Waiter", "The Homecoming",],
    "Glass": ["Akhnaten", "Satyagraha", "Einstein on the Beach",],
    "Sophocles": ["Oedipus Rex",],
    "Beckett": ["Waiting for Godot",],

    # Artists start here#
    "da Vinci": ["Mona Lisa", "Last Supper",],
    "Michealangelo": ["David", "Sistine Chappel",],
    "Picasso": ["Guernica", "Three Musicians"],
    "Rodin": ["Thinker", "Gates of Hell"],
    "Turner": ["Rain", "Steam and Speed", "The Slave Ship", "Tate Award", "Dido Building Carthage", "Overboard sharks",],
    "Hals": ["Laughing Cavelier", "Officers of the Saint George Militia", "Young man holding skull", "Malle Babbe",],
    "Leutze": [],
    "Rembrandt": ["Night Watch",],
    "Manet": ["Luncheon on the Grass",],
    "Magritte": ["Son of Man", "Empire of Light", "Time Transfixed", "Menaced Assassin",],
    "Vemeer": ["Woman with a Pearl Earing", "View of Delft", "Woman in Blue Reading a Letter",],
    "Cole": ["Oxbow", "Titan's Goblet", "The Savage State"],
    "Copely": ["Watson and the Shark", "Thomas Gage", "Figures of the Revolution",],
    "Wood": ["American Gothic", "Return from Bohemia", "Daughters of the Revolution"],
}

# This is randomly select a category#


def Find_Category(Correct, Ratio, categories):
    if len(categories) != 0:
        Category = random.choice(categories)

        return Category
    else:
        print("You have completed all the flashcards, your final score is", Ratio)
        time.sleep(Timing)
        Highscores_List(Correct, Ratio)
        sys.exit()


# this is going to get the list of possible answers in the category#
def Find_People(Category, Correct, Ratio,  categories):

    People = Topics[Category]
    # If all the people have been removed from the category, remove the category#
    if len(People) == 0:
        del Topics[Category]
        categories.remove(Category)
        Category = Find_Category(Correct, Ratio, categories)
        People = Topics[Category]

        return People
    else:
        return People


# Randomly select a person from the list of people#
def Find_Person(Ratio, People, Category, categories, Correct):
    if len(People) != 0:
        Person = random.choice(People)
        return Person
    else:
        # if the list is empty, than we restart the program#
        Category = Find_Category(Correct, Ratio, categories)
        if Category == False:
            print("You have completed all the flashcards, your final score is", Ratio)
            time.sleep(Timing)
            Highscores_List(Ratio)
            sys.exit()
        else:
            People = Find_People(Category, Correct, Ratio,  categories)
            Person = Find_Person(Ratio, People, Category, categories, Correct)
            return Person

# This plugs in the person into a dictionary with their respective questions as a list value#


def Find_Question(Correct, Ratio, Person, People, Category, categories):
    if Person in Questions_Set:
        Questions = Questions_Set[Person]
    else:  # if the person isn't in the dictionary, delete the person from the list of people in the category, and restart the program#

        People.remove(Person)
        Category = Find_Category(Correct, Ratio, categories)
        People = Find_People(Category, Correct, Ratio,  categories)
        Person = Find_Person(Ratio, People, Category, categories, Correct)
        Answer = Find_Question(Correct, Ratio, Person, People, Category, categories)
        return Answer
    # somehow this makes the program work, I don't question it#
    Answer = str(Person).lower().strip()
    # this evaluates the length of the question list, and if there is only one, it removes the person from the dictionary#
    # if there are more than one questions in the list, it keeps going,#
    # if there are 0 in the list it restarts the program#

    if len(Questions) > 1:
        Question = random.choice(Questions)
        print(f"{Question}\n")
        Questions.remove(Question)
        return Answer

    elif len(Questions) == 1:

        Question = random.choice(Questions)
        Questions.remove(Question)
        del Questions_Set[Person]
        Questions.clear()
        if Category in Topics:  # if the category still exists, remove person from the category, otherwise restart
            Topics[Category].remove(Person)
            print(f"{Question}\n")
            return Answer
        else:
            print(f"{Question}\n")
            return Answer

    else:
        del Questions_Set[Person]
        People = People.remove(Person)
        Category = Find_Category(Correct, Ratio, categories)
        People = Find_People(Category, Correct, Ratio,  categories)
        Person = Find_Person(Ratio, People, Category, categories, Correct)
        Answer = Find_Question(Correct, Ratio, Person, People, Category, categories)
        return Answer

# this asks the user for input and checks it against the answer


def Ask_Question(People, Person, Answer, Category, Incorrect, Correct):

    if len(Category) == 0:
        del Topics[Category]
        People.remove(Person)
    else:
        Response = input("What is the Answer? ").lower().strip()

        if Response == Answer:
            print("Correct! :)")

            return True

        elif Response == "stop":
            return "Stop"
        else:
            Answer = str(Answer).capitalize()
            print(f"Incorrect! :(")
            print(Answer)
            return False
def Read_Highscores():
    with open('Highscores.txt', 'r') as file:
        filedata = file.readlines()
    # Replace the target string
    highScores = {}
    Scores = []
    for line in filedata:
        line_2= line.split(':')

        line_3 = line_2[0]
        line_4= line_2[1].replace("(", "")
        line_5 = (line_3 +":"+ line_4)
        line_6 , line_7 = line_5.split(':')
        highScores[line_6] = line_7
        line_1 = line.split(":")
        Number = line_1[1].strip(":")
        Number = Number.replace(",", "").replace("'", "").replace("", "").replace('(', "")
        Number = int(Number)

    for highScore in highScores:
        Scores.append(highScores[highScore])


    HIGHSCORES = sorted(highScores.items(), key=lambda item: item[1], reverse = True)
    i = 1
    for Key in HIGHSCORES:
        if i == 1:
            print("\N{CROWN}1st|", Key)
        elif i == 2:
            print("🥈2nd|", Key)
        elif i == 3:
            print("🥉3rd|", Key)
        elif i == 4:
            print("4th|", Key)
        elif i == 5:
            print("5th|", Key)
        else:
            print(Key)
        i += 1

    sys.exit()

Spanish_Words = {
"el pajaro": "bird",
"el pez": "fish",
"el cerdo": "pig",
"la arana": "spider",
"el conejo": "rabbit",
"el mono": "monkey",
"el oso": "bear",
"el toro": "bull",
"la abeja": "bee",
"el caballo": "horse",
"el pastel": "cake",
"la carne": "meat",
"el pollo": "chicken",
"la fresa": "strawberry",
"la manzana": "apple",
"el pan": "bread",
"el arroz": "rice",
"el vaso": "glass",
"la taza": "cup",
"el tenedor": "fork",
"la cuchara": "spoon",
"el cuchillo": "knife",
"la servilleta": "napkin",
"el mesero": "waiter",
"la cuenta": "bill",
"la propina": "tip",
"traer": "to bring",
"el tazon": "bowl",
"pedir": "to order",
"el abuelo": "grandfather",
"la tia": "aunt",
"los hermanos": "siblings",
"la hermana": "sister",
"el primo": "male cousin",
"los padres": "parents",
"los parientes": "relatives",
"la falda": "skirt",
"la camisa": "shirt",
"la camiseta": "t-shirt",
"el abrigo": "coat",
"los zapatos": "shoes",
"el vestido": "dress",
"calcetines": "socks",
"la ropa": "clothes",
"grande": "big",
"pequeno": "small",
"largo": "long",
"corto": "short",
"la garganta": "throat",
"el cuerpo": "body",
"los dedos de mano y pie": "fingers and toes",
"la cara": "face",
"la boca": "mouth",
"el cuello": "neck",
"la oreja": "ear",
"el brazo": "arm",
"la mano": "hand",
"el tobillo": "ankle",
"el corazon": "heart",
"el pierna": "leg",
"la rodilla": "knee",
"el pie": "foot",
"el dormitorio": "bedroom",
"la cama": "bed",
"el cuarto de bano": "bathroom",
"la ventana": "window",
"las escaleras": "stairs",
"la sala": "living room",
"el comedor": "dining room",
"la cocina": "kitchen",
"la puerta": "door",
"la silla": "chair",
"yo": "I",
"tu": "you(familiar)",
"el": "he",
"ella": "she",
"usted": "you(formal)",
"nosotros": "we",
"vosotros": "you all(Spain)",
"ellos": "they(m)",
"ellas": "they(f)",
"ustedes": "you all (Latin Am.)",
"el coche": "car",
"el avion": "airplane",
"el camion": "truck",
"el barco": "boat",
"la calle": "street",
"la carretera": "highway",
"el aeropuerto": "airport",
"la ciudad": "city",
"el campo": "countryside",
"la playa": "beach",
"el trabajo": "job",
"sin": "without",
"con": "with",
"a": "to",
"de": "from",
"menos": "less",
"mas": "more",
"la nieta": "granddaughter",
"la comida": "food",
}
Spanish_Words_List= ["el pajaro","el pez","el cerdo","la arana","el conejo","el oso","el toro","el caballo","el pastel","el pollo","la fresa","la manzna","el pan","el arroz","el vaso","la taza","el tenedor","la cuchara","la servilleta","el mesero","la propina","traer","el tazon","pedir","el abuelo","la tia","la hermana","el primo","los parientes","la falda","la camiseta","el abrigo","el vestido","calcetines","la ropa","grande","pequeno","largo","corto","la garganta","el cuerpo","los dedos de mano y pie","la cara","la boca","la oreja","el brazo","el tobillo","el corazon","el pierna","la rodilla","el pie","el dormitorio","la cama","el cuarto de bano","la ventana","las escaleras","la sala","el comedor","la cocina","la puerta","y","tu","el","ella","usted","nosotros","vosotros","ellos","ellas","ustedes","el coche","el camion","el barco","la carretera","el aeropuerto","el campo","la playa","el trabajo","sin","con","a","de","menos","la nieta","la comida",]
def Spanish():
    Missed = {}
    Missed_List = []
    Correct = 0
    Incorrect = 0
    Check = True
    Ratio = (Correct, ":", Incorrect)
    while True:
        if len(Spanish_Words_List) != 0:
            Word = random.choice(Spanish_Words_List)
            Spanish_Words_List.remove(Word)
            if Word in Spanish_Words:

                Answer = Spanish_Words[Word]
                print(Answer)
                Response = input("What is the Answer? ").lower().strip()

                if Response == Word:
                    Correct += 1
                    Ratio = (Correct, ":", Incorrect)
                    print(Ratio)
                    print("Correct! :)")
                    time.sleep(Timing)
                    os.system("clear")


                elif Response == "stop":
                    return "Stop"
                else:
                    Incorrect += 1
                    Ratio = (Correct, ":", Incorrect)

                    Word = str(Word).capitalize()
                    print(f"Incorrect! :(")
                    print(Word)
                    Word = Word.lower()
                    Missed_List.append(Word)
                    Missed[Word] = Spanish_Words[Word]
                    print(Ratio)
                    time.sleep(Timing)
                    os.system("clear")

                if len(Spanish_Words_List) == 0:
                    print("Done!")
                    Correct = 0
                    Incorrect = 0
                    while True:
                        if len(Missed_List) != 0:
                            Word = random.choice(Missed_List)
                            Missed_List.remove(Word)
                            if Word in Missed:

                                Answer = Missed[Word]
                                print(Answer)
                                Response = input("What is the Answer? ").lower().strip()

                                if Response == Word:
                                    Correct += 1
                                    Ratio = (Correct, ":", Incorrect)
                                    print(Ratio)
                                    print("Correct! :)")
                                    time.sleep(Timing)
                                    os.system("clear")


                                elif Response == "stop":
                                    return "Stop"
                                else:
                                    Incorrect += 1
                                    Ratio = (Correct, ":", Incorrect)

                                    Word = str(Word).capitalize()
                                    print(f"Incorrect! :(")
                                    print(Word)
                                    Word = Word.lower()
                                    Missed_List.append(Word)
                                    Missed[Word] = Spanish_Words[Word]
                                    print(Ratio)
                                    time.sleep(Timing)
                                    os.system("clear")
                        else:
                            break
def AutoCorrect():
    Answer = "Bill"
    Response = "Bilb"
    Answer_a =0
    Answer_b =0
    Answer_c =0
    Answer_d =0
    Answer_e =0
    Answer_f =0
    Answer_g =0
    Answer_h =0
    Answer_i =0
    Answer_j =0
    Answer_k =0
    Answer_l =0
    Answer_m =0
    Answer_n =0
    Answer_o =0
    Answer_p =0
    Answer_q =0
    Answer_r =0
    Answer_s =0
    Answer_t =0
    Answer_u =0
    Answer_v =0
    Answer_w =0
    Answer_x =0
    Answer_y =0
    Answer_z =0
    i = 0
    while i in range(len(Answer)):
        Letter = (f"Index: {i}, Letter: {Answer[i]}")
        Letter.lower()
        i+=1
        if Letter == "a":
            Answer_a += 1
        elif Letter == "b":
            Answer_b +=1
        elif Letter == "c":
            Answer_c +=1
        elif Letter == "d":
            Answer_d +=1
        elif Letter == "e":
            Answer_e +=1
        elif Letter == "f":
            Answer_f +=1
        elif Letter == "g":
            Answer_g +=1
        elif Letter == "h":
            Answer_h +=1
        elif Letter == "i":
            Answer_i +=1
        elif Letter == "j":
            Answer_j +=1
        elif Letter == "k":
            Answer_k +=1
        elif Letter == "l":
            Answer_l +=1
        elif Letter == "m":
            Answer_m +=1
        elif Letter == "n":
            Answer_n +=1
        elif Letter == "o":
            Answer_o +=1
        elif Letter == "p":
            Answer_p +=1
        elif Letter == "q":
            Answer_q +=1
        elif Letter == "r":
            Answer_r +=1
        elif Letter == "s":
            Answer_s +=1
        elif Letter == "t":
            Answer_t +=1
        elif Letter == "u":
            Answer_u +=1
        elif Letter == "v":
            Answer_v +=1
        elif Letter == "w":
            Answer_w +=1
        elif Letter == "x":
            Answer_x +=1
        elif Letter == "y":
            Answer_y +=1
        elif Letter == "z":
            Answer_z +=1

    Count = (Answer_a +Answer_b +Answer_c +Answer_d +Answer_e +Answer_f +Answer_g +Answer_h +Answer_i +Answer_j +Answer_k +Answer_l +Answer_m +Answer_n +Answer_o +Answer_p +Answer_q +Answer_r +Answer_s +Answer_t +Answer_u +Answer_v +Answer_w +Answer_x +Answer_y +Answer_z)
    print(Count)
History_Final = {
"1. At the time of World War One, which countries made up Europe's Great Powers?":["a. Germany and France","b. Great Britain, France, Germany, Austria-Hungary, Russia, and Italy","c. Great Britain and Germany","d. Great Britain, Austria-Hungary, Germany, Spain, Russia, Italy, and France", "b"],
"2. Why did Italy refuse to support its ally Germany?":["a. It opposed the Treaty of Brest-Litovsk.", "b. It accused Germany of starting the war.","c. It did not want to fight the United States.","d. It viewed the Schlieffen Plan as a poor strategy.","b"],
"3. What did the policy of unrestricted submarine warfare refer to?": ["a. Britain's policy to sink any ship in German waters without warning", "b. Germany's policy to sink any ship in British waters without warning","c. the U.S. Navy's warning of the type of warfare the Central Powers could expect","d. Germany's decision to focus its resources on the waters surrounding Europe","b"],
"4. Which of the following events occurred after the Americans joined the war?":["a. Russia withdrew from the war.","b. The Bulgarians and the Ottoman Turks surrendered.","c. Britain and France recruited laborers from their colonies.","d. All of the above are true.","d"],
"5. How did the Treaty of Versailles affect postwar Germany?":["a It left a legacy of bitterness and hatred in the hearts of the German people.", "b. It stabilized the German economy and gave monetary aid to the nation.", "c. It left Germany in much the same state as it was before the war.", "d. It gave Germans the drive to rebuild their nation on a stronger foundation.","a"],
"6. What impact did the war have on the economy of Europe?":["a. It drained the treasuries of Europe.","b. It enriched the treasuries of the Allied Powers.","c. It speeded the industrialization of Europe.","d. It gave women an opportunity t become heads of companies.","a"],
"7. What is the most probable link between militarism and imperialism?": ["a. As a country gains colonies, its military grows to protect them.","b. As a country's military expands, the country wants colonies to recruit troops.","c. As a country's colonies grow, the military stages training exercises there.","d. As the military expands, a country seeks colonies to prevent coups at home.","a"],
"8. What key factor led to the formation of the Triple Alliance and the Triple Entente?": ["a. Germany's desire to isolate France and Britain's desire to remain dominant","b. Germany's hostility toward France and Britain's allegiance to France","c. Bismark's fear of France's army and Britain's fear of Germany's empire","d. Germany and France's separate desires to gain control of the Balkans","a"],
"9. What event in Sarajevo ignited the Great War?": ["a. an ultimatum presented to Serbia in response to royal assassinations", "b. the assassination of Archduke Franz Ferdinand and his wife Sophie", "c. Austria's rejection of Serbia's offer and declaration of war on Serbia", "d. Russia's mobilization of troops along the Austrian border","b"],
"10. What was trench warfare intended to accomplish?": ["a. to protect soldiers from enemy gun fire on the front lines","b. to trap enemy soldiers in mud pits on the front lines","c. to force enemy soldiers to pass through a no man's land","d. all of the above","d"],
"11. Which of the following was used to widen the First World War?": ["a. attacks on African colonies","b. the development of poison gas","c. the use of propaganda","d. the start of rationing","a"],
"12. What gamble did Germany make before the United States entered the war?": ["a. that a defeat of Russia would lead to a German victory in the war","b. that the Gallipoli campaign would weaken the forces on the Western Front","c. that unrestricted submarine warfare would defeat the United States","d. that their blockade would defeat Britain before U.S. troops arrived","d"],
"13. What impact did the Treaty of Brest-Litovsk have on Germany?": ["a. It gave Germany the Russian army's aid against the Allies.'","b. It allowed Germany to focus all their efforts on the Western Front.","c. Germany gained lands that were formerly part of Russia.","d. All of the above are true.","b"],
"14. How did the Allies respond to Wilson's vision for peace?": ["a. Britain and France showed little sign of agreeing to Wilson's plan.","b. Britain and France were concerned with strengthening their own security.","c. Britain and France wanted to strip Germany of its war-making power:","d. All of the above are true.","d"],
"15. What actions led to the formation of new nations out of the Central Powers?": ["a. Wilson's idea of self-determination that inspired revolutions in Europe","b. military occupation of the defeated nations and redistribution of peoples","c. provisions of peace treaties signed with the Central Powers","d. a direction by the League of Nations to realign territories after the war", "d"],
"16. What did the pogroms that occurred in the late 19th-century Russia do?": ["a. violently persecute Jews","b. kill all the kulaks","c. enlist the aid of foreigners", "d. establish a Communist council", "a"],
"17. Who were the Bolsheviks?": ["a. soldiers in the White Army","b. radical Russian Marxist revolutionaries","c. members of the Duma, Russia's parliament","d. followers of Rasputin", "b"],
"18. Who did China's peasants align themselves with in the 1920s?": ["a. warlords","b. Qing Dynasty","c. Nationalists","d. Communists","d"],
"19. What were Soviets under Russia's provisional government?": ["a. labor unions","b. local councils","c. revolutionary leaders","d. plans for redistributing land","b"],
"20. What is a totalitarian state?": ["a. a state in which the people have a direct say in their government","b. a state in which the people elect représentatives to the legislature","c. a state in which the government controls every aspect of public and private life","d. a state in which the working class is glorified and has the greatest voice in government.", "c"],
"21. What was the purpose of the Soviet state's Five-Year Plans?": ["a. foreign policy","b. social restructuring","c. political reform","d. economic development","d"],
"22. What did Sun Yixian's Revolutionary Alliance accomplish in China?": ["a. defeating the Kuomintang", "b. overthrowing the last emperor", "c. spreading Communism in China", "d. controlling the rampaging warlords","b"],
"23. Which group was known for taking a 6,000-mile journey known as the 'Long March?' Why did they do it?": ["a. Chinese Communists, fleeing the Nationalists", "b. Chinese Nationalists, fleeing the Communists", "c. Chinese peasants, fleeing the Japanese invaders", "d. the Russian White Army, fleeing the Bolsheviks","a"],
"24. Which territories were lost by Russia under the Treaty of Brest-Litovsk?": ["a. Finland, Estonia, Latvia, Lithuania, Poland","b. Romania, Turkey, China, Mongolia","c. Brest-Litovsk, Ukraine, Russia","d. all of the above","a"],
"25. What was the capital of Russia before the 1917 Revolution?": ["a. Kiev","b. Moscow","c. St. Petersburg","d. Minsk","c"],
"26. How did Russian czars Alexander Ill and Nicholas Il deal with calls for reform?": ["a. They immediately moved to enact reforms.","b. They made a few reforms but not all.","c. They resisted all efforts for reform.","d. They appointed ministers to study reforms.","c"],
"27. How did the Russo-Japanese war show the czar's weakness?": ["a. His insults to the Japanese emperor caused the war:","b. His poor military strategy prevented his generals from gaining territory.","c. News of repeated losses sparked unrest and led to revolt during the war","d. All of the above are true.","c"],
"28. Under the Treaty of Versailles, what country received Chinese territories previously under German control?": ["a. Italy","b. Japan","c. India","d. Russia","b"],
"29. Which event did NOT happen immediately after the Bolshevik Revolution?": ["a. The workers took control of factories.","b. Farmland was distributed among the peasants.","c. A truce was signed with Germany.","d. A totalitarian state was established.","d"],
"30. Who was responsible for the Great Purge in the USSR?": ["a. Lenin and the Mensheviks","b. Jiang the Kuomintang","c. Jiang and members of the Communist Party","d. Stalin and members of the Communist Party'","d"],
"31. What was started under Stalin to improve the Soviet Union's economy?": ["a. industrial and agricultural revolutions","b. Bolshevik and Communist revolutions","c. socialist and totalitarian revolutions","d. all of the above","a"],
"32. What was the result of China having a Nationalist government recognized by the world but a Communist party growing in the countryside?": ["a. A social realist art campaign was created to uplift nationalist ideas.","b. Nationalist troops and armed gangs wiped out the Communists.","c. Civil war broke out between the two groups.","d. Communist leaders were forced to work in labor camps.","c"],
"33. How did the reigns of Alexander IlI and Nicholas Il in Russia help pave the way for revolution?": ["a. They both upheld an autocratic government without reform.","b. They supported rapid industrialization at the expense of the treasury.","c. They instituted pogroms to weed out revolutionary thinkers.","d. They saw to it that the poor were imprisoned for debts.","a"],
"34. What impact did Russia's involvement in World War I have on the Russian government?": ["a. It created a window for the Mensheviks to attempt a takeover.","b. It led to the establishment of the Duma as a voice for moderates.","c. It revealed the weaknesses of czarist rule and military leadership.","d. All of the above are true.","c"],
"35. How did life change for Russians after the success of the Bolshevik revolution?":["a. Education became a public institution based on the Western model.","b. Motherhood was no longer considered a patriotic duty.","c. Russia was organized into several self-governing republics.","d. All of the above are true.","a"],
"36. Which of the following was NOT part of the transformation of the Soviet Union into a totalitarian state?": ["a. Great Purge","b. Five-Year Plans","c. creation of the first soviets","d. establishment of collective farms","c"],
"37. Why did Chinese peasants align themselves with the Communists rather than the Nationalists?": ["a.The Communists divided land among the farmers, while the Nationalists ignored their problems","b. The Nationalists relocated thousands of peasants in the Long March.","c. The Nationalists were forcing China to industrialize through high taxes on farms.","d. The Communists moved peasants to collective farms, where they prospered.","a"],
"38. What event in 1937 halted the Chinese civil war?": ["a. The Nationalists succeeded in wiping out the Communists.", "b. Chinese Communists began a 6,000 mile journey.", "c. The Japanese launched an all-out invasion of China.", "d. Chinese peasants align themselves with the Communists.","c"],
"39. After World War I, most European nations had what type of government, if only temporarily?": ["a. Fascist","b. Communist","c. Socialist","d. democratic","d"],
"40. What event marked the beginning of the Great Depression?":["a. the end of World War I","b. the passage of the Dawes Plan","c. the stock market crash of 1929","d. the election of Franklin Roosevelt","c"],
"41. Il Duce was the title of which leader?":["a. Juan Péron","b. Haile Selassie","c. Adolf Hitler","d. Benito Mussolini","d"],
"42. Which German political party sought to overturn the Treaty of Versailles and combat communism?": ["Leibenstrum", "b. Fascist", "c. Democrat", "d. Republican","b"],
"43. Which of the following was true of Germany, Italy, and Japan during the 1930s?":["a. All three successfully invaded other nations.","b. All three had governments controlled by Fascists.","c. All three signed nonaggression pacts with the Soviet Union.","d. All three pledged to undo the decisions of the Versailles Treaty.","b"],
"44. What term was used to identify the WWII alliance of Germany, Italy, and Japan?": ["a. Fascist Powers","b. Axis Powers","c. Allied Powers","d. Central Powers","b"],
"45. What was the goal of U.S. isolationists after World War I?":["a. that Nazi ties to other countries should be combatted","b. that political ties to other countries should be avoided","c. that foreign aid to other countries should be lessened","d. that industrial ties to other countries should be ended","b"],
"46. Which country did Germany conquer in September 1939?": ["a. Poland","b. East Prussia","c. Austria","d. Czechoslovakia","a"],
"47. What did Germany do to the Rhineland?": ["a. It annexed the Rhineland to Belgium.","b. It surrendered the Rhineland to France.","c. It remilitarized the Rhineland.","d. The Rhineland became industrialized.","c"],
"48. What happened to the Sudetenland?": ["a. Germany invaded it.","b. Germany annexed it.","c. It became independent.","d. Austria annexed it.","b"],
"49. What effect did the Dawes Plan have on the economy of postwar Germany?": ["a. It saved Germany from an inflationary crisis and stabilized the economy.","b. It replaced German marks with the U.S. dollar as the nation's currency.","c. It introduced U.S. businesses into Germany, which provided jobs.","d. All of the above are true.","a"],
"50. What most damaged the U.S. economy in the late 1920s?": ["a. soaring stock prices","b. a shortage of workers","c. an uneven distribution of wealth","d. a drought in the farm states north of Oklahoma.","c"],
"51. What caused Germans to start taking Adolf Hitler and his message seriously?": ["a. the threat of invasion by the Soviet Union","b. his skill at making speeches","c. the example of Mussolini's success in Italy","d. the economic crisis brought on by the Depression","d"],
"52. Which of the following does fascism stress?": ["a. nationalism","b. isolationism","c. individual rights","d. a classless society","a"],
"53. What was the policy of appeasement?": ["a. the British and French decision to give into aggression to keep peace","b. the move that Mussolini made to form an alliance with Germany","c. the U.S. desire to stay out of foreign affairs","d. the treaty between Germany and the Soviet Union to not fight each other","a"],
"54. Why did Japan invade Manchuria?": ["a. to avenge an ancient grudge","5. to gain its iron ore and coal deposits","c. to regain land lost in the Russo-Japanese War","d. to obey the terms of the Kellogg-Briand Pact","b"],
"55. What effect did the nonaggression pact between the Nazis and the Soviets have?": ["a. It brought the United States out of its isolation", "b.It allowed the Axis Powers to continue unchecked.","c. It forced Britain and France to abandon the policy of appeasement.","d. All of the above are true.","b"],
"56. Why did millions of Germans turn against the leaders of the Weimar Republic?": ["a. They had signed the Treaty of Versailles.","b. Their leadership led to the loss of the war.","c. They were members of the Nazi party.","d. The country was not ready for a democratic government.","a"],
"57. What was the major cause of the collapse of the stock market?": ["a. American businesses failed.","b. More people bought stock than sold it.","c. Stocks sold for more than they were worth.","d. More stocks were sold than there were shares in companies.","c"],
"58. What fear added to the appeal of fascism in Italy and Germany?": ["a. a Communist revolution","b. foreign attack","c. a loss of individual rights","d. all of the above","a"],
"59. Why did Hitler blame the Jewish population for all of Germany's troubles?": ["a. The Jewish people had aided Germany's enemies in World War I.", "b, Hatred of Jews, or anti-Semitism, was a key part of Nazi ideology.","c. The Jewish population in Germany outnumbered the Nazi party.","d. Jewish people held most of the prominent roles in the German government.","b"],
"60. The Munich Conference came to symbolize the dangers of what?": ["a. Communism","b. negotiation","c. appeasement","d. militarism","c"],
"61. In what way was Japan different from its allies Germany and Italy?": ["a. It established a successful democracy.","b. It was ruled by a hereditary aristocracy.","c. It kept its economy prosperous throughout the Depression.","d. It was ruled by militarists who kept the emperor in power.","d"],
"62. What prompted Great Britain and France to declare war on Germany?": ["a. Soviet invasion of Finland","b. German invasion of Poland","c. German invasion of Czechoslovakia","d. Soviet invasion of Poland","b"],
"63. The German blitzkrieg was a military strategy that depended on what advantage?": ["a. a system of fortifications","b. 'out-waiting' the opponent","c. surprise and overwhelming force","d. ability to make a long, steady advance","c"],
"64. What crucial lesson was learned in the Battle of Britain?": ["a. that Germany had a powerful airforce", "b. that Hitler's advances could be blocked","c. that the RAF needed more planes","d. that the British were inexperienced","b"],
"65. What event occurred on the day described as 'a date which will live in infamy'?": ["a. attack on Pearl Harbor","b. Battle of Guadal canal","c. bombing of Hiroshima","d. signing of the Atlantic Charter","a"],
"66. What was significant about the Battle of Midway?": ["a. It turned the war in the Pacific against the Japanese.","b. It marked the end of the war for the Japanese.","c. It destroyed the whole of the Japanese navy.","d. all of the above","a"],
"67. Which of the following battles marked the final German offensive in WWII?": ["a. Battle of the Bulge","b. Battle of Stalingrad","c. Battle of Leyte Gulf","d. Battle of El Alamein","a"],
"68. What caused the Japanese emperor to have reduced power after the war?": ["a. the Allies' insistence","b. the anger of the Japanese citizenry","c. the distrust of the Japanese parliament","d. the emperor's decision to reform the government","a"],
"69. Where were atomic bombs dropped?": ["a. Tokyo and Hong Kong","b. Dresden and Berlin","c. Hiroshima and Nagasaki","d. Leyte Island and Midway","c"],
"70. Which of the following was addressed by the Nuremberg Trials?": ["a. the Holocaust","b. the use of nuclear bombs","c. the firebombing of Dresden","d. the internment of Japanese-American citizens","a"],
"71. What was Hitler's prime reason for wanting to take Poland?": ["He knew it would be a bargaining chip with the Soviet Union.","b. He wanted the Polish Corridor and the port city of Danzig.","c. He knew it would cause Great Britain and France to declare war:","d. He wanted to control the ancestral home of the Malovich clan.","b"],
"72. Which of the following factors led to the fall of France to the Nazis?": ["a. the fall of Dunkirk","b. evacuation of the British forces","c. the fall of Paris","d. all of the above","d"],
"73. What was the significance of the Atlantic Charter both during and after the war?": ["a. It was signed on a ship in the Atlantic where the U.S. Navy would soon enter an undeclared naval war with Germany.","b. It established an alliance between Great Britain and the United States to divide the world..","c. It upheld rights of free trade and choice of government, and it became the plan for postwar peace.","d. It cut off trade with Axis Powers and established trade embargoes for the postwar era.","c"],
"74. What did the Allies' strategy of 'island hopping' in the Pacific involve?": ["a. attacks on all Japanese-held islands","b. attacks on all islands within 500 miles of Japan","c. attacks only on islands that were not well-defended","d. attacks only on islands that were Japanese strongholds","c"],
"75. How did the Japanese try to build a Pacific empire?": ["a. by attacking Pearl Harbor in a surprise raid","b. by taking over U.S., British, and French territories","c. by convincing native peoples to save 'Asia for the Asians'","d. by sponsoring Communist overthrow of colonial governments","b"],
"76. How did Kristallnacht demonstrate Nazi persecution of Jews?": ["a. Nazi supporters attacked Jewish homes, businesses, and synagogues.","b. A law passed on that day required Jews to wear yellow stars","c. That was the day the Nazis began large deportations of Jews.","d. all of the above.","a"],
"77. What was the goal of Hitler's 'Final Solution'?": ["a. It was a process to divide up his territories among his generals.","b. It was a system for winning the war before the Americans entered.","c. It was a way to amass more soldiers for the invasion of Russia.","d. It was genocide of people the Nazis considered inferior.","d"],
"78. What combination led to the German defeat in the Battle of Stalingrad?": ["a. Russian and British troops","b. Russian troops and the Russian winter","c. Russian and German fuel shortages","d. Russian ground forces and American air strikes","b"],
"79. Under the postwar constitution of Japan, who was the head of government?": ["a the emperor","b. the leader of the diet","c. a prime minister selected by the diet","d. a prime minister selected by the emperor","b"],
"80. What was the result of Germany's invasion of Poland?": ["a. Soviet forces invaded Germany.","b. Soviet forces came to Poland's defense.","c. Britain and France declared war on Germany.","d. Britain and France sued for peace with Germany.","c"],
"81. How did the Lend-Lease Act benefit the United States?": ["a. It enriched the U.S. economy through selling coal to the Allies.","• It lent the Allies material in exchange for military bases.","c. It allowed the Allies to purchase computers from the United States.","d. all of the above","b"],
"82. Which of the following did NOT motivate japan to build an empire?": ["a. Japan was overcrowded and faced shortages of raw materials.","b. Japan wanted the rich European colonies of Southeast Asia.","c. Japan took over Manchuria and later fought for the heartland of China.","d. The emperor wanted a larger empire to suit his divine status.","d"],
"83. What was the U.S. response to Japanese aggression in Southeast Asia in mid-1941?": ["a. declare war on Japan","b. cut oil supplies to Japan","c. broke off peace talks with Japan","d. began a boycott of Japanese-made products","b"],
"84. How were the Holocaust and Hitler's 'Final Solution' related?": ["a. They were both terms used by the Germans to describe their plan for permanent removal of the Jewish population.","b. The Holocaust is the term for the genocide that resulted from the plan called the 'Final Solution.'","c. The 'Final Solution' was the plan Hitler meant to follow after the Holocaust was complete.","d. The Holocaust and the 'Final Solution' were not related.","b"],
"85. How did civilians join in the war effort in WWII?": ["a. scrap metal drives","b. working in war industries","c. rationing","d. all of the above","d"],
"86. What was the Allies' plan for victory over the Nazis?": ["a. The Allies focused their forces on North Africa to keep control of the oil.","b. The Allies would join forces on the Eastern Front and invade Germany.","c. The Allies would fight Germany on two fronts to weaken it.","d. The Allies instigated Operation Torch to burn key points in Germany.","c"],
"87. Why were thousands of U.S. citizens put in internment camps during the war?": ["a. They were radioing helpful information to the Germans.","b. They were of Japanese descent and falsely labeled as enemies.","c. They were of German descent and falsely labeled as enemies.","d. They had known of the attack on Pearl Harbor in advance.","b"],
"88. Why did President Truman agree to use the atomic bomb?": ["a. to punish Japan for Pearl Harbor","b. to avenge those who died in the Bataan Death March","c. to destroy weapons plants in Japan","d. to bring the war to the quickest possible end","d"],
"89. Which of the following is NOT a reason for the high number of displaced persons after WWII?": ["a. Border changes caused people to find themselves in the wrong country","b. The United States deported thousands of Japanese-Americans to Japan","c. Prisoners of war tried to return to their homelands","d. Holocaust survivors searched desperately for missing loved ones.","b"],
"90. In the 1940s and 1950s, what did the region described as being 'behind the iron curtain' include?": ["a. Soviet Union only","b. Soviet Union and its satellite nations","c. democratic nations of Western Europe","d. German Democratic Republic, or East Germany","b"],
"91. What was the purpose of the Truman Doctrine?": ["a. to raise funds for Communist activities in Europe.","b. to create a Communist party in the United States","c. to judge political parties that favored communism","d. to support countries that rejected communism","d"],
"92. What was the name of the alliance established by European Communist nations in response to NATO?": ["a, Iron Curtain","b. Warsaw Pact","c. Second World","d. Union of Soviet Socialist Republics","b"],
"93. Which two groups fought a civil war in China both before and after World War II?": ["a. the peasants and the middle class","b. the warlords and the emperor","c. the Nationalists and the Communists","d. the socialists and the nationalists","c"],
"94. What idea was the major justification for U.S. foreign policy during the Cold War era?": ["a. Pareto Principle","b. Alliance Theory","c. Domino Theory","d. Grand Axial Theory","c"],
"95. What were Third World countries?": ["a. countries aligned with the United States and its allies","b. countries aligned with the Soviet Union and its allies","c. developing countries not aligned with the United States or Soviet Union","d. countries with a gross national product higher than First and Second World countries","c"],
"96. What was the Strategic Defense Initiative?": ["a. a council created to create defense measures","b. a failed operation to invade the Soviet Union","c. a system to protect the United States against enemy missiles","d. a program to weed out terrorist activity in the United States","c"],
"97. Which European countries could receive aid through the Marshall Plan?": ["a. any European country that needed it", "b. any European country that shared a border with iron curtain countries","c. any European country that politically opposed the Soviet Union","d. any European country that modeled its government after U.S. democracy","a"],
"98. What led the Soviets to blockade West Berlin?": ["a. the formation of NATO","b.a reunification of the three western zones of Germany","c. Marshall Plan aid to West Germany","d. the crash of a U2 spy flight over Soviet territory","b"],
"99. What Cold War event increased U.S. spending on education and technology?": ["a. Cuban missile crisis","b. establishment of the Warsaw Pact","c. Chinese-Soviet treaty of friendship","d. Soviet launching of a space satellite","d"],
"100. What was the primary goal for the Soviet Union's invasion of Afghanistan?": ["a. to fight an indirect war with the United States","b. to gain control of Middle Eastern oil supplies","c. to reestablish the Communist regime in Afghanistan","d. to cause the United States to boycott the 1980 Olympics","c"],
}
History_List = ["1. At the time of World War One, which countries made up Europe's Great Powers?","2. Why did Italy refuse to support its ally Germany?","3. What did the policy of unrestricted submarine warfare refer to?","4. Which of the following events occurred after the Americans joined the war?","5. How did the Treaty of Versailles affect postwar Germany?","6. What impact did the war have on the economy of Europe?","7. What is the most probable link between militarism and imperialism?","8. What key factor led to the formation of the Triple Alliance and the Triple Entente?","9. What event in Sarajevo ignited the Great War?","10. What was trench warfare intended to accomplish?","11. Which of the following was used to widen the First World War?","12. What gamble did Germany make before the United States entered the war?","13. What impact did the Treaty of Brest-Litovsk have on Germany?","14. How did the Allies respond to Wilson's vision for peace?","15. What actions led to the formation of new nations out of the Central Powers?","16. What did the pogroms that occurred in the late 19th-century Russia do?","17. Who were the Bolsheviks?","18. Who did China's peasants align themselves with in the 1920s?","19. What were Soviets under Russia's provisional government?","20. What is a totalitarian state?","21. What was the purpose of the Soviet state's Five-Year Plans?","22. What did Sun Yixian's Revolutionary Alliance accomplish in China?","23. Which group was known for taking a 6,000-mile journey known as the 'Long March?' Why did they do it?","24. Which territories were lost by Russia under the Treaty of Brest-Litovsk?","25. What was the capital of Russia before the 1917 Revolution?","26. How did Russian czars Alexander Ill and Nicholas Il deal with calls for reform?","27. How did the Russo-Japanese war show the czar's weakness?","28. Under the Treaty of Versailles, what country received Chinese territories previously under German control?","29. Which event did NOT happen immediately after the Bolshevik Revolution?","30. Who was responsible for the Great Purge in the USSR?","31. What was started under Stalin to improve the Soviet Union's economy?","32. What was the result of China having a Nationalist government recognized by the world but a Communist party growing in the countryside?","33. How did the reigns of Alexander IlI and Nicholas Il in Russia help pave the way for revolution?","34. What impact did Russia's involvement in World War I have on the Russian government?","35. How did life change for Russians after the success of the Bolshevik revolution?","36. Which of the following was NOT part of the transformation of the Soviet Union into a totalitarian state?","37. Why did Chinese peasants align themselves with the Communists rather than the Nationalists?","38. What event in 1937 halted the Chinese civil war?","39. After World War I, most European nations had what type of government, if only temporarily?","40. What event marked the beginning of the Great Depression?","41. Il Duce was the title of which leader?","42. Which German political party sought to overturn the Treaty of Versailles and combat communism?","43. Which of the following was true of Germany, Italy, and Japan during the 1930s?","44. What term was used to identify the WWII alliance of Germany, Italy, and Japan?","45. What was the goal of U.S. isolationists after World War I?","46. Which country did Germany conquer in September 1939?","47. What did Germany do to the Rhineland?","48. What happened to the Sudetenland?","49. What effect did the Dawes Plan have on the economy of postwar Germany?","50. What most damaged the U.S. economy in the late 1920s?","51. What caused Germans to start taking Adolf Hitler and his message seriously?","52. Which of the following does fascism stress?","53. What was the policy of appeasement?","54. Why did Japan invade Manchuria?","55. What effect did the nonaggression pact between the Nazis and the Soviets have?","56. Why did millions of Germans turn against the leaders of the Weimar Republic?","57. What was the major cause of the collapse of the stock market?","58. What fear added to the appeal of fascism in Italy and Germany?","59. Why did Hitler blame the Jewish population for all of Germany's troubles?","60. The Munich Conference came to symbolize the dangers of what?","61. In what way was Japan different from its allies Germany and Italy?","62. What prompted Great Britain and France to declare war on Germany?","63. The German blitzkrieg was a military strategy that depended on what advantage?","64. What crucial lesson was learned in the Battle of Britain?","65. What event occurred on the day described as 'a date which will live in infamy'?","66. What was significant about the Battle of Midway?","67. Which of the following battles marked the final German offensive in WWII?","68. What caused the Japanese emperor to have reduced power after the war?","69. Where were atomic bombs dropped?","70. Which of the following was addressed by the Nuremberg Trials?","71. What was Hitler's prime reason for wanting to take Poland?","72. Which of the following factors led to the fall of France to the Nazis?","73. What was the significance of the Atlantic Charter both during and after the war?","74. What did the Allies' strategy of 'island hopping' in the Pacific involve?","75. How did the Japanese try to build a Pacific empire?","76. How did Kristallnacht demonstrate Nazi persecution of Jews?","77. What was the goal of Hitler's 'Final Solution'?","78. What combination led to the German defeat in the Battle of Stalingrad?","79. Under the postwar constitution of Japan, who was the head of government?","80. What was the result of Germany's invasion of Poland?","81. How did the Lend-Lease Act benefit the United States?","82. Which of the following did NOT motivate japan to build an empire?","83. What was the U.S. response to Japanese aggression in Southeast Asia in mid-1941?","84. How were the Holocaust and Hitler's 'Final Solution' related?","85. How did civilians join in the war effort in WWII?","86. What was the Allies' plan for victory over the Nazis?","87. Why were thousands of U.S. citizens put in internment camps during the war?","88. Why did President Truman agree to use the atomic bomb?","89. Which of the following is NOT a reason for the high number of displaced persons after WWII?","90. In the 1940s and 1950s, what did the region described as being 'behind the iron curtain' include?","91. What was the purpose of the Truman Doctrine?","92. What was the name of the alliance established by European Communist nations in response to NATO?","93. Which two groups fought a civil war in China both before and after World War II?","94. What idea was the major justification for U.S. foreign policy during the Cold War era?","95. What were Third World countries?","96. What was the Strategic Defense Initiative?","97. Which European countries could receive aid through the Marshall Plan?","98. What led the Soviets to blockade West Berlin?","99. What Cold War event increased U.S. spending on education and technology?","100. What was the primary goal for the Soviet Union's invasion of Afghanistan?",]
def History():
    Correct = 0
    Incorrect = 0
    Ratio = (Correct, ":", Incorrect)
    History_List = ["1. At the time of World War One, which countries made up Europe's Great Powers?","2. Why did Italy refuse to support its ally Germany?","3. What did the policy of unrestricted submarine warfare refer to?","4. Which of the following events occurred after the Americans joined the war?","5. How did the Treaty of Versailles affect postwar Germany?","6. What impact did the war have on the economy of Europe?","7. What is the most probable link between militarism and imperialism?","8. What key factor led to the formation of the Triple Alliance and the Triple Entente?","9. What event in Sarajevo ignited the Great War?","10. What was trench warfare intended to accomplish?","11. Which of the following was used to widen the First World War?","12. What gamble did Germany make before the United States entered the war?","13. What impact did the Treaty of Brest-Litovsk have on Germany?","14. How did the Allies respond to Wilson's vision for peace?","15. What actions led to the formation of new nations out of the Central Powers?","16. What did the pogroms that occurred in the late 19th-century Russia do?","17. Who were the Bolsheviks?","18. Who did China's peasants align themselves with in the 1920s?","19. What were Soviets under Russia's provisional government?","20. What is a totalitarian state?","21. What was the purpose of the Soviet state's Five-Year Plans?","22. What did Sun Yixian's Revolutionary Alliance accomplish in China?","23. Which group was known for taking a 6,000-mile journey known as the 'Long March?' Why did they do it?","24. Which territories were lost by Russia under the Treaty of Brest-Litovsk?","25. What was the capital of Russia before the 1917 Revolution?","26. How did Russian czars Alexander Ill and Nicholas Il deal with calls for reform?","27. How did the Russo-Japanese war show the czar's weakness?","28. Under the Treaty of Versailles, what country received Chinese territories previously under German control?","29. Which event did NOT happen immediately after the Bolshevik Revolution?","30. Who was responsible for the Great Purge in the USSR?","31. What was started under Stalin to improve the Soviet Union's economy?","32. What was the result of China having a Nationalist government recognized by the world but a Communist party growing in the countryside?","33. How did the reigns of Alexander IlI and Nicholas Il in Russia help pave the way for revolution?","34. What impact did Russia's involvement in World War I have on the Russian government?","35. How did life change for Russians after the success of the Bolshevik revolution?","36. Which of the following was NOT part of the transformation of the Soviet Union into a totalitarian state?","37. Why did Chinese peasants align themselves with the Communists rather than the Nationalists?","38. What event in 1937 halted the Chinese civil war?","39. After World War I, most European nations had what type of government, if only temporarily?","40. What event marked the beginning of the Great Depression?","41. Il Duce was the title of which leader?","42. Which German political party sought to overturn the Treaty of Versailles and combat communism?","43. Which of the following was true of Germany, Italy, and Japan during the 1930s?","44. What term was used to identify the WWII alliance of Germany, Italy, and Japan?","45. What was the goal of U.S. isolationists after World War I?","46. Which country did Germany conquer in September 1939?","47. What did Germany do to the Rhineland?","48. What happened to the Sudetenland?","49. What effect did the Dawes Plan have on the economy of postwar Germany?","50. What most damaged the U.S. economy in the late 1920s?","51. What caused Germans to start taking Adolf Hitler and his message seriously?","52. Which of the following does fascism stress?","53. What was the policy of appeasement?","54. Why did Japan invade Manchuria?","55. What effect did the nonaggression pact between the Nazis and the Soviets have?","56. Why did millions of Germans turn against the leaders of the Weimar Republic?","57. What was the major cause of the collapse of the stock market?","58. What fear added to the appeal of fascism in Italy and Germany?","59. Why did Hitler blame the Jewish population for all of Germany's troubles?","60. The Munich Conference came to symbolize the dangers of what?","61. In what way was Japan different from its allies Germany and Italy?","62. What prompted Great Britain and France to declare war on Germany?","63. The German blitzkrieg was a military strategy that depended on what advantage?","64. What crucial lesson was learned in the Battle of Britain?","65. What event occurred on the day described as 'a date which will live in infamy'?","66. What was significant about the Battle of Midway?","67. Which of the following battles marked the final German offensive in WWII?","68. What caused the Japanese emperor to have reduced power after the war?","69. Where were atomic bombs dropped?","70. Which of the following was addressed by the Nuremberg Trials?","71. What was Hitler's prime reason for wanting to take Poland?","72. Which of the following factors led to the fall of France to the Nazis?","73. What was the significance of the Atlantic Charter both during and after the war?","74. What did the Allies' strategy of 'island hopping' in the Pacific involve?","75. How did the Japanese try to build a Pacific empire?","76. How did Kristallnacht demonstrate Nazi persecution of Jews?","77. What was the goal of Hitler's 'Final Solution'?","78. What combination led to the German defeat in the Battle of Stalingrad?","79. Under the postwar constitution of Japan, who was the head of government?","80. What was the result of Germany's invasion of Poland?","81. How did the Lend-Lease Act benefit the United States?","82. Which of the following did NOT motivate japan to build an empire?","83. What was the U.S. response to Japanese aggression in Southeast Asia in mid-1941?","84. How were the Holocaust and Hitler's 'Final Solution' related?","85. How did civilians join in the war effort in WWII?","86. What was the Allies' plan for victory over the Nazis?","87. Why were thousands of U.S. citizens put in internment camps during the war?","88. Why did President Truman agree to use the atomic bomb?","89. Which of the following is NOT a reason for the high number of displaced persons after WWII?","90. In the 1940s and 1950s, what did the region described as being 'behind the iron curtain' include?","91. What was the purpose of the Truman Doctrine?","92. What was the name of the alliance established by European Communist nations in response to NATO?","93. Which two groups fought a civil war in China both before and after World War II?","94. What idea was the major justification for U.S. foreign policy during the Cold War era?","95. What were Third World countries?","96. What was the Strategic Defense Initiative?","97. Which European countries could receive aid through the Marshall Plan?","98. What led the Soviets to blockade West Berlin?","99. What Cold War event increased U.S. spending on education and technology?","100. What was the primary goal for the Soviet Union's invasion of Afghanistan?",]

    while True:
        if len(History_List) != 0:
            Key = random.choice(History_List)
            History_List.remove(Key)
            Questions = History_Final[Key]
            print(Key,"\n")
            i =0
            for Question in Questions:
                if Question != Questions[4]:
                    print(Questions[i])
                    i+=1
                else:
                    Response = input("\nWhat letter? ").lower()
                    if Response == Questions[4]:
                        print("Correct!")
                        Correct += 1
                        Ratio = (Correct, ":", Incorrect)
                        print(Ratio)
                        del History_Final[Key]
                        time.sleep(Timing)
                        os.system('clear')
                    else:
                        print("Incorrect, the answer was", Questions[4])
                        Incorrect += 1
                        del History_Final[Key]
                        Ratio = (Correct, ":", Incorrect)
                        print(Ratio)
                        time.sleep(Timing)
                        os.system('clear')
        else:
            print("All done! Your final score was:", Ratio)
            break
        #for Key, Values in History_Final.items():
            #print(Key)
def Test_Zone():
    History()
    sys.exit()
def Highscores_List(Correct, Ratio):
    while True:
        Name = input("Please type your name to save your score! ").lower().strip().capitalize()
        if Name == "":
            os.system('clear')
            continue
        else:
            break
    with open('Highscores.txt', 'r') as file:
        filedata = file.readlines()
    # Replace the target string
    Scores = []
    Found = False
    for line in filedata:
        if Name in line:
            Found = True
            line_1 = line.split(":")
            Number = line_1[1].strip(":")
            Number = Number.replace(",", "").replace("'", "").replace("", "").replace('(', "")
            Number = int(Number)
            if Number < Correct:
                highscore = (f"{Name}:{Ratio}\n").replace(",", "").replace("'", "").replace("", "").replace('', "").replace("","").replace(" ", "")
                Scores.append(highscore)
                print("New Highscore")
            else:
                Scores.append(line)
        else:
            Scores.append(line)
    if Found == False:
        highscore = (f"{Name}:{Ratio}\n").replace(",", "").replace("'", "").replace(" ", "").replace('', "").replace("", "").replace("","").replace(" ", "")
        Scores.append(highscore)
    # Write the file out again
    with open('Highscores.txt', 'w') as file:
        i = 0
        for Score in Scores:
            file.write(Score)
    sys.exit()
# this is the start of the program, it asks if you want to choose a category#
def Menu():
    os.system("clear")
    Game = input("What would you like to study? \n [Flashcards, Dynasties, Leaderboard, Spanish, History] ").lower().strip().capitalize().title()
    if Game == "Leaderboard":
        Read_Highscores()
    elif Game == "Test":
        Test_Zone()
    elif Game == "Dynasties":
        Chinese_Dynasty()
        sys.exit()
    elif Game == "Spanish":
        Spanish()
    elif Game == "History":
        History()
    elif Game == "Flashcards" or Game == "":
        User_Input = input("If you would you like to choose your categories, type 'Yes', if you want to do all categories, type 'No'. ").lower().strip().capitalize().title()
        if User_Input == "No" or User_Input == "N" or User_Input == "":
            categories = ["Science", "Writers", "Poets", "Playwrights", "Philosophers", "Social_Scientists", "Composers", "Artists"]
            time.sleep(Timing)
            os.system("clear")
            return categories
        else:
            while True:
                Categories_Choosers = input("What Categories Would You Like To Quiz On?\n Please write all the categories you would like to choose and seperate them with commas. \n {Science, Writers, Poets, Playwrights, Philosophers, Social_Scientists, Composers, Artists }").lower().capitalize().strip().split(",")

                if Categories_Choosers[0] == None or Categories_Choosers[0] == "All" or Categories_Choosers[0] == "":
                    categories = ["Science", "Writers", "Poets", "Playwrights","Philosophers", "Social_Scientists", "Composers", "Artists"]
                    Continue = True
                    return categories
                else:
                    all_categories = ["Science", "Writers", "Poets", "Playwrights","Philosophers", "Social Scientists", "Composers", "Artists"]
                    categories = []
                    for Categories_Chooser in Categories_Choosers:
                        if Categories_Chooser.lower().strip().capitalize().title() in all_categories:

                            categories.append(Categories_Chooser.lower().strip().capitalize().title())
                            Continue = True
                        elif Categories_Chooser == "Patel":
                            Name = input("Is your name Om? ").lower().strip().capitalize().title()
                            if Name == "Yes":
                                return "Om"
                        else:
                            print("You have selected a category that does not exist, please try again.")
                            time.sleep(Timing)
                            os.system("clear")
                            Continue = False
                            continue
                if Continue != False:
                    print(categories)
                    time.sleep(Timing)
                    os.system("clear")
                    return categories
                else:
                    continue
    else:
        print("Sorry this is under contruction, please choose a different area of study.")
        time.sleep(Timing)
        os.system("clear")
        categories = Menu()
        return categories


def All(categories, Correct, Incorrect):

    while True:

        Ratio = (Correct, ":", Incorrect)
        Category = Find_Category(Correct, Ratio, categories)

        if Category == False:
            break
        else:
            People = Find_People(Category, Correct, Ratio,  categories)
            Person = Find_Person(Ratio, People, Category, categories, Correct)
            Answer = Find_Question(Correct, Ratio, Person, People, Category, categories)
            time.sleep(Timing_2)
            Status = Ask_Question(People, Person, Answer, Category, Correct, Incorrect)
            time.sleep(Timing)

            if Status == True:
                Correct += 1
                Ratio = (Correct, ":", Incorrect)
                print(Ratio)
                time.sleep(Timing)
                os.system("clear")
            elif Status == False:
                Incorrect += 1
                Ratio = (Correct, ":", Incorrect)
                print(Ratio)
                time.sleep(Timing)
                os.system("clear")
            elif Status == "Stop":
                time.sleep(Timing)
                Highscores_List(Correct, Ratio)
                sys.exit("You have exited the program")
def Chinese_Dynasty():
    print("Nope")
def Om_Zone():
    Formula = random.choice(Calculus_Formulas)
    Question = Calculus_Formula_Dict[Formula]
    print(Question)
    Answer = input("").lower().strip().capitalize().title()
    if Formula == Answer:
        print("Correct!")
    else:
        print("No!")

    sys.exit("The Om Zone is under construction.")
categories = Menu()
if categories == "Om":
    Om_Zone()
else:
    All(categories, Correct, Incorrect)

