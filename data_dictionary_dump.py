import json

base_file_path = 'lib/'

# list of tuples to store name and BPM of a song tempo
# In this list, each tuple contains the name of the tempo, the minimum BPM, and the maximum BPM. For "Prestissimo", since the BPM is 200+, the maximum BPM is represented as infinity (float('inf')). 
tempos = [
    ("Largo", 40, 60),
    ("Larghetto", 60, 66),
    ("Adagio", 66, 76),
    ("Andante", 76, 108),
    ("Moderato", 108, 120),
    ("Allegro", 120, 168),
    ("Presto", 168, 200),
    ("Prestissimo", 200, float('inf'))
]

# Writing to file with error handling
tempo_bpm_dump_file = f"{base_file_path}tempo_dict.json"
try:
    with open(tempo_bpm_dump_file, 'w') as tempo_dump_file:
        json.dump(tempos, tempo_dump_file)
except IOError as e:
    print("Error writing to file:", e)

#list of tuples to store name of the key, its tonic note, whether it's major or minor, and its musical mode.
musical_keys = [
    ("C Ionian", "C", "Major", "Ionian"),
    ("C# Ionian", "C#", "Major", "Ionian"),
    ("Db Ionian", "Db", "Major", "Ionian"),
    ("D Ionian", "D", "Major", "Ionian"),
    ("D# Ionian", "D#", "Major", "Ionian"),
    ("Eb Ionian", "Eb", "Major", "Ionian"),
    ("E Ionian", "E", "Major", "Ionian"),
    ("F Ionian", "F", "Major", "Ionian"),
    ("F# Ionian", "F#", "Major", "Ionian"),
    ("Gb Ionian", "Gb", "Major", "Ionian"),
    ("G Ionian", "G", "Major", "Ionian"),
    ("G# Ionian", "G#", "Major", "Ionian"),
    ("Ab Ionian", "Ab", "Major", "Ionian"),
    ("A Ionian", "A", "Major", "Ionian"),
    ("A# Ionian", "A#", "Major", "Ionian"),
    ("Bb Ionian", "Bb", "Major", "Ionian"),
    ("B Ionian", "B", "Major", "Ionian"),
    ("C Dorian", "C", "Minor", "Dorian"),
    ("C# Dorian", "C#", "Minor", "Dorian"),
    ("Db Dorian", "Db", "Minor", "Dorian"),
    ("D Dorian", "D", "Minor", "Dorian"),
    ("D# Dorian", "D#", "Minor", "Dorian"),
    ("Eb Dorian", "Eb", "Minor", "Dorian"),
    ("E Dorian", "E", "Minor", "Dorian"),
    ("F Dorian", "F", "Minor", "Dorian"),
    ("F# Dorian", "F#", "Minor", "Dorian"),
    ("Gb Dorian", "Gb", "Minor", "Dorian"),
    ("G Dorian", "G", "Minor", "Dorian"),
    ("G# Dorian", "G#", "Minor", "Dorian"),
    ("Ab Dorian", "Ab", "Minor", "Dorian"),
    ("A Dorian", "A", "Minor", "Dorian"),
    ("A# Dorian", "A#", "Minor", "Dorian"),
    ("Bb Dorian", "Bb", "Minor", "Dorian"),
    ("B Dorian", "B", "Minor", "Dorian"),
    ("C Phrygian", "C", "Minor", "Phrygian"),
    ("C# Phrygian", "C#", "Minor", "Phrygian"),
    ("Db Phrygian", "Db", "Minor", "Phrygian"),
    ("D Phrygian", "D", "Minor", "Phrygian"),
    ("D# Phrygian", "D#", "Minor", "Phrygian"),
    ("Eb Phrygian", "Eb", "Minor", "Phrygian"),
    ("E Phrygian", "E", "Minor", "Phrygian"),
    ("F Phrygian", "F", "Minor", "Phrygian"),
    ("F# Phrygian", "F#", "Minor", "Phrygian"),
    ("Gb Phrygian", "Gb", "Minor", "Phrygian"),
    ("G Phrygian", "G", "Minor", "Phrygian"),
    ("G# Phrygian", "G#", "Minor", "Phrygian"),
    ("Ab Phrygian", "Ab", "Minor", "Phrygian"),
    ("A Phrygian", "A", "Minor", "Phrygian"),
    ("A# Phrygian", "A#", "Minor", "Phrygian"),
    ("Bb Phrygian", "Bb", "Minor", "Phrygian"),
    ("B Phrygian", "B", "Minor", "Phrygian"),
    ("C Lydian", "C", "Major", "Lydian"),
    ("C# Lydian", "C#", "Major", "Lydian"),
    ("Db Lydian", "Db", "Major", "Lydian"),
    ("D Lydian", "D", "Major", "Lydian"),
    ("D# Lydian", "D#", "Major", "Lydian"),
    ("Eb Lydian", "Eb", "Major", "Lydian"),
    ("E Lydian", "E", "Major", "Lydian"),
    ("F Lydian", "F", "Major", "Lydian"),
    ("F# Lydian", "F#", "Major", "Lydian"),
    ("Gb Lydian", "Gb", "Major", "Lydian"),
    ("G Lydian", "G", "Major", "Lydian"),
    ("G# Lydian", "G#", "Major", "Lydian"),
    ("Ab Lydian", "Ab", "Major", "Lydian"),
    ("A Lydian", "A", "Major", "Lydian"),
    ("A# Lydian", "A#", "Major", "Lydian"),
    ("Bb Lydian", "Bb", "Major", "Lydian"),
    ("B Lydian", "B", "Major", "Lydian"),
    ("C Mixolydian", "C", "Major", "Mixolydian"),
    ("C# Mixolydian", "C#", "Major", "Mixolydian"),
    ("Db Mixolydian", "Db", "Major", "Mixolydian"),
    ("D Mixolydian", "D", "Major", "Mixolydian"),
    ("D# Mixolydian", "D#", "Major", "Mixolydian"),
    ("Eb Mixolydian", "Eb", "Major", "Mixolydian"),
    ("E Mixolydian", "E", "Major", "Mixolydian"),
    ("F Mixolydian", "F", "Major", "Mixolydian"),
    ("F# Mixolydian", "F#", "Major", "Mixolydian"),
    ("Gb Mixolydian", "Gb", "Major", "Mixolydian"),
    ("G Mixolydian", "G", "Major", "Mixolydian"),
    ("G# Mixolydian", "G#", "Major", "Mixolydian"),
    ("Ab Mixolydian", "Ab", "Major", "Mixolydian"),
    ("A Mixolydian", "A", "Major", "Mixolydian"),
    ("A# Mixolydian", "A#", "Major", "Mixolydian"),
    ("Bb Mixolydian", "Bb", "Major", "Mixolydian"),
    ("B Mixolydian", "B", "Major", "Mixolydian"),
    ("C Aeolian", "C", "Minor", "Aeolian"),
    ("C# Aeolian", "C#", "Minor", "Aeolian"),
    ("Db Aeolian", "Db", "Minor", "Aeolian"),
    ("D Aeolian", "D", "Minor", "Aeolian"),
    ("D# Aeolian", "D#", "Minor", "Aeolian"),
    ("Eb Aeolian", "Eb", "Minor", "Aeolian"),
    ("E Aeolian", "E", "Minor", "Aeolian"),
    ("F Aeolian", "F", "Minor", "Aeolian"),
    ("F# Aeolian", "F#", "Minor", "Aeolian"),
    ("Gb Aeolian", "Gb", "Minor", "Aeolian"),
    ("G Aeolian", "G", "Minor", "Aeolian"),
    ("G# Aeolian", "G#", "Minor", "Aeolian"),
    ("Ab Aeolian", "Ab", "Minor", "Aeolian"),
    ("A Aeolian", "A", "Minor", "Aeolian"),
    ("A# Aeolian", "A#", "Minor", "Aeolian"),
    ("Bb Aeolian", "Bb", "Minor", "Aeolian"),
    ("B Aeolian", "B", "Minor", "Aeolian"),
    ("C Locrian", "C", "Minor", "Locrian"),
    ("C# Locrian", "C#", "Minor", "Locrian"),
    ("Db Locrian", "Db", "Minor", "Locrian"),
    ("D Locrian", "D", "Minor", "Locrian"),
    ("D# Locrian", "D#", "Minor", "Locrian"),
    ("Eb Locrian", "Eb", "Minor", "Locrian"),
    ("E Locrian", "E", "Minor", "Locrian"),
    ("F Locrian", "F", "Minor", "Locrian"),
    ("F# Locrian", "F#", "Minor", "Locrian"),
    ("Gb Locrian", "Gb", "Minor", "Locrian"),
    ("G Locrian", "G", "Minor", "Locrian"),
    ("G# Locrian", "G#", "Minor", "Locrian"),
    ("Ab Locrian", "Ab", "Minor", "Locrian"),
    ("A Locrian", "A", "Minor", "Locrian"),
    ("A# Locrian", "A#", "Minor", "Locrian"),
    ("Bb Locrian", "Bb", "Minor", "Locrian"),
    ("B Locrian", "B", "Minor", "Locrian")
]

# Writing to file with error handling
music_key_dump_file = f"{base_file_path}music_key_dict.json"
try:
    with open(music_key_dump_file, 'w') as music_dump_file:
        json.dump(musical_keys, music_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
    
# List of tuples to store every Bible Book and total number of Chapters
bible_chapters = [
    ("Genesis", 50),
    ("Exodus", 40),
    ("Leviticus", 27),
    ("Numbers", 36),
    ("Deuteronomy", 34),
    ("Joshua", 24),
    ("Judges", 21),
    ("Ruth", 4),
    ("1 Samuel", 31),
    ("2 Samuel", 24),
    ("1 Kings", 22),
    ("2 Kings", 25),
    ("1 Chronicles", 29),
    ("2 Chronicles", 36),
    ("Ezra", 10),
    ("Nehemiah", 13),
    ("Esther", 10),
    ("Job", 42),
    ("Psalms", 150),
    ("Proverbs", 31),
    ("Ecclesiastes", 12),
    ("Song of Solomon", 8),
    ("Isaiah", 66),
    ("Jeremiah", 52),
    ("Lamentations", 5),
    ("Ezekiel", 48),
    ("Daniel", 12),
    ("Hosea", 14),
    ("Joel", 3),
    ("Amos", 9),
    ("Obadiah", 1),
    ("Jonah", 4),
    ("Micah", 7),
    ("Nahum", 3),
    ("Habakkuk", 3),
    ("Zephaniah", 3),
    ("Haggai", 2),
    ("Zechariah", 14),
    ("Malachi", 4),
    ("Matthew", 28),
    ("Mark", 16),
    ("Luke", 24),
    ("John", 21),
    ("Acts", 28),
    ("Romans", 16),
    ("1 Corinthians", 16),
    ("2 Corinthians", 13),
    ("Galatians", 6),
    ("Ephesians", 6),
    ("Philippians", 4),
    ("Colossians", 4),
    ("1 Thessalonians", 5),
    ("2 Thessalonians", 3),
    ("1 Timothy", 6),
    ("2 Timothy", 4),
    ("Titus", 3),
    ("Philemon", 1),
    ("Hebrews", 13),
    ("James", 5),
    ("1 Peter", 5),
    ("2 Peter", 3),
    ("1 John", 5),
    ("2 John", 1),
    ("3 John", 1),
    ("Jude", 1),
    ("Revelation", 22)
]

# Writing to file with error handling
bible_book_dump_file = f"{base_file_path}bible_book_dict.json"
try:
    with open(bible_book_dump_file, 'w') as bible_dump_file:
        json.dump(bible_chapters, bible_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
    
# This tuple contains the names of various musical instruments.
instruments = [
    ("piano"),
    ("guitar"),
    ("violin"),
    ("flute"),
    ("trumpet"),
    ("drums"),
    ("saxophone"),
    ("cello"),
    ("clarinet"),
    ("bass guitar"),
    ("accordion"),
    ("harp"),
    ("trombone"),
    ("ukulele"),
    ("banjo"),
    ("double bass"),
    ("harmonica"),
    ("mandolin"),
    ("xylophone"),
    ("oboe"),
    ("electric guitar"),
    ("bassoon"),
    ("french horn"),
    ("synthesizer"),
    ("accordion"),
    ("bagpipes"),
    ("conga"),
    ("djembe"),
    ("marimba"),
    ("organ"),
    ("steel drum"),
    ("tabla"),
    ("tambourine"),
    ("triangle"),
    ("vibraphone"),
    ("zither"),
    ("cello"),
    ("bongo"),
    ("castanets"),
    ("cowbell"),
    ("didgeridoo"),
    ("kazoo"),
    ("tuba"),
    ("fiddle"),
    ("harp"),
    ("drums"),
    ("guttural throat singing"),
    ("mongolian guitar"),
    ("bajo sexto"),
    ("vihuela"),
    ("jarana"),
    ("horsehead fiddle")
]

# Writing to file with error handling
instrument_dump_file = f"{base_file_path}instrument_dict.json"
try:
    with open(instrument_dump_file, 'w') as instrument_data_dump_file:
        json.dump(instruments, instrument_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
    # This tuple contains lead various vocalists.
vocalists = [
    # Female Vocal Types
    ("Soprano", "Coloratura", "female"),
    ("Soprano", "Lyric", "female"),
    ("Soprano", "Dramatic", "female"),
    ("Mezzo-Soprano", "Coloratura", "female"),
    ("Mezzo-Soprano", "Lyric", "female"),
    ("Mezzo-Soprano", "Dramatic", "female"),
    ("Contralto", "Alto", "female"),
    
    # Male Vocal Types
    ("Countertenor", "Countertenor", "male"),
    ("Tenor", "Leggero", "male"),
    ("Tenor", "Lyric", "male"),
    ("Tenor", "Spinto", "male"),
    ("Tenor", "Dramatic", "male"),
    ("Baritone", "Lyric", "male"),
    ("Baritone", "Dramatic", "male"),
    ("Bass", "Bass-Baritone", "male"),
    ("Bass", "Basso Profondo", "male"),
    ("Bass", "Lyric", "male"),
    ("Bass", "Dramatic", "male"),
        
    # Mongolian Throat Singing Styles
    ("Khoomei", "Kharkhiraa Khoomei", "male"), # producing multiple pitches simultaneously
    ("Khoomei", "Tuvan Style", "male"), # Originating from the Tuva region of Russia
    ("Sygyt", "", "male"), # flute-like sound with harmonics
    ("Kargyraa", "", "male"), # deep, growling sound
    ("Borbangnadyr", "", "male"), # pulsating rhythm 
    ("Ezengileer", "", "male"), # emphasizes nasal resonance
    ("Chylandyk", "", "male") # bird-like sounds
]

# Writing to file with error handling
vocalists_dump_file = f"{base_file_path}vocalists_dict.json"
try:
    with open(vocalists_dump_file, 'w') as vocalists_data_dump_file:
        json.dump(vocalists, vocalists_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
# A list of tuples representing song genre and whether it is instrumental or not
bible_song_genre = [
    ("progressive metal djent", False),
    ("progressive metal", False),
    ("progressive metal djent screamo", False),
    ("metalcore djent screamo", False),
    ("bluegrass gospel", False),
    ("classical celtic guitar", False),
    ("gospel hymn", False),
    ("christian worship", False),
    ("contemporary worship", False),
    ("slow ambient drone christian worship", False),
    ("mongolian folk", False),
    ("mongolian folk metal", False),
    ("western", False),
    ("ranchera-Mariachi Fusion", False),
    ("bolero", False),
    ("huapango", False),
    ("son jarocho", False),
    ("corrido", False),
    ("banda", False),
    ("cumbia", False),
    ("norteño", False),
    ("mariachi", False),
    ("ranchera", False),
    ("chicano rap", False),
    ("american folk", False),
    ("middle-eastern", False),
    ("classic 80s heart throb freestyle", False),
    ("Electronic", False),
    ("heart throb freestyle", False),
    ("Fusion Freestyle", False),
    ("Fusion House", False),
    ("Progressive House", False),
    ("Deep House", False),
    ("EDM Techno", False),
    ("90s Tech House", False),
    ("Club/Dance", False),
    ("EDM", False),
    ("Trance", False),
    ("Progressive Trance", False),
    ("Jazz Fusion", False),
    ("Jazz-funk", False),
    ("Psychedelic ", False),
    ("Space music ", False),
    ("Hardstyle", False),
    ("Drum n Bass", False),
    ("Electronic Drum n Bass", False),
    ("Early 2000s Drum n Bass", False),
    ("Techstep Drum n Bass", False),
    ("Neurofunk Drum n Bass", False),
    ("Liquid Drum n Bass", False),
    ("Jungle Drum n Bass", False),
    ("Jump Up Drum n Bass", False),
    ("Intelligent Drum n Bass", False),
    ("Halftime Drum n Bass", False),
    ("Breakcore Drum n Bass", False),
    ("Sambass Drum n Bass", False),
    ("Electronic Dance", False),
    ("Dubstep", False),
    ("60s Proto Metal", False),
    ("70s Proto Metal", False),
    ("Acid Rock", False),
    ("Early Metal", False),
    ("Math Rock", False),
    ("Math Prog Rock", False),
    ("Avant Garde", False),
    ("Heavy Blues", False),
    ("Heavy Psyche", False),
    ("Soundtrack", False),
    ("film score", False),
    ("contemporary classical", False),
    ("minimalism", False),
    ("Hip Hop 80-115 BPM", False),
    ("Triphop", False),
    ("Concert marches", False),
    ("UK garage/2-step", False),
    ("UK funky", False),
    ("Acid Techno", False),
    ("Schranz", False),
    ("Hardstyle 150 BPM", False),
    ("Juke/Footwork", False),
    ("Drum n Bass BPM 160-180", False),
    ("Oldschool jungle", False),
    ("Drumstep", False),
    ("Neurofunk 170-180 BPM", False),
    ("Grime 140 BPM", False),
]

# Writing to file with error handling
bible_song_genre_dump_file = f"{base_file_path}bible_song_genre_dict.json"
try:
    with open(bible_song_genre_dump_file, 'w') as bible_song_genre_data_dump_file:
        json.dump(bible_song_genre, bible_song_genre_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
# A list of tuples representing song genre
instrumental_song_genre = [
    ("classical acoustic guitar", True),
    ("progressive metal djent", True),
    ("progressive metal", True),
    ("progressive metal djent screamo", True),
    ("metalcore djent screamo", True),
    ("classical acoustic guitar melody", True),
    ("classical celtic guitar melody", True),
    ("fast aggressive phonk", True),
    ("slow ambient drone", True),
    ("heavy metal", True),
    ("fast jazz fusion", True),
    ("heavy electronic dance music", True),
    ("slow reggae", True),
    ("heavy ambient drone", True),
    ("slow country folk", True),
    ("fast hip-hop", True),
    ("fast salsa", True),
    ("fast bluegrass", True),
    ("fast screamo", True),
    ("slow indie rock", True),
    ("fast reggaeton", True),
    ("fast progressive house", True),
    ("fast trap", True),
    ("slow psychedelic rock", True),
    ("fast techno", True),
    ("slow blues", True),
    ("slow R&B", True),
    ("fast punk rock", True),
    ("heavy dubstep", True),
    ("fast thrash metal", True),
    ("slow bossa nova", True),
    ("fast disco", True),
    ("heavy industrial", True),
    ("fast garage rock", True),
    ("slow folk ballad", True),
    ("fast drum and bass", True),
    ("heavy doom metal", True),
    ("fast grindcore", True),
    ("slow tango", True),
    ("fast flamenco", True),
    ("heavy death metal", True),
    ("fast breakbeat", True),
    ("slow waltz", True),
    ("fast hardcore punk", True),
    ("heavy sludge metal", True),
    ("slow soul", True),
    ("fast electroswing", True),
    ("heavy thrash metal", True),
    ("fast ska", True),
    ("slow chamber music", True),
    ("fast house", True),
    ("fast hardstyle", True),
    ("kpop", True),
    ("minimalist techno", True),
    ("darkwave", True),
    ("acid jazz", True),
    ("neofolk", True),
    ("chiptune", True),
    ("witch house", True),
    ("noise rock", True),
    ("IDM (Intelligent Dance Music)", True),
    ("shoegaze", True),
    ("vaporwave", True),
    ("zydeco", True),
    ("krautrock", True),
    ("powernoise", True),
    ("glitch", True),
    ("wonky", True),
    ("chillwave", True),
    ("future garage", True),
    ("post-rock", True),
    ("math rock", True),
    ("jungle", True),
    ("breakcore", True),
    ("lo-fi hip hop", True),
    ("lo-fi indie", True),
    ("lo-fi house", True),
    ("haunting atmospheric witch house", True),
    ("fast aggressive witch house", True),
    ("lo-fi hip-hop", True),
    ("smooth vaporwave jazz", True),
    ("smooth fusion jazz", True),
    ("smooth vaporwave jazz lo-fi hip-hop", True),
    ("mongolian folk", True),
    ("mongolian folk metal", True),
    ("Chinese Classical folk", True),
    ("classical celtic guitar", True),
    ("symphonic metal", True),
    ("narcocorridos", True),
    ("ranchera-Mariachi Fusion", True),
    ("bolero", True),
    ("huapango", True),
    ("son jarocho", True),
    ("corrido", True),
    ("banda", True),
    ("cumbia", True),
    ("norteño", True),
    ("mariachi", True),
    ("ranchera", True),
    ("chicano rap", True),
    ("american folk", True),
    ("middle-eastern", True),
    ("classic 80s heart throb freestyle", True),
    ("Electronic", True),
    ("heart throb freestyle", True),
    ("Fusion Freestyle", True),
    ("Fusion House", True),
    ("Progressive House", True),
    ("Deep House", True),
    ("EDM Techno", True),
    ("90s Tech House", True),
    ("Club/Dance", True),
    ("EDM", True),
    ("Trance", True),
    ("Progressive Trance", True),
    ("Jazz Fusion", True),
    ("Jazz-funk", True),
    ("Psychedelic ", True),
    ("Space music ", True),
    ("Hardstyle", True),
    ("Drum n Bass", True),
    ("Electronic Drum n Bass", True),
    ("Early 2000s Drum n Bass", True),
    ("Techstep Drum n Bass", True),
    ("Neurofunk Drum n Bass", True),
    ("Liquid Drum n Bass", True),
    ("Jungle Drum n Bass", True),
    ("Jump Up Drum n Bass", True),
    ("Intelligent Drum n Bass", True),
    ("Halftime Drum n Bass", True),
    ("Breakcore Drum n Bass", True),
    ("Sambass Drum n Bass", True),
    ("Electronic Dance", True),
    ("Dubstep", True),
    ("60s Proto Metal", True),
    ("70s Proto Metal", True),
    ("Acid Rock", True),
    ("Early Metal", True),
    ("Math Rock", True),
    ("Math Prog Rock", True),
    ("Avant Garde", True),
    ("Heavy Blues", True),
    ("Heavy Psyche", True),
    ("Soundtrack", True),
    ("film score", True),
    ("contemporary classical", True),
    ("minimalism", True),
    ("Hip Hop 80-115 BPM", True),
    ("Triphop", True),
    ("Concert marches", True),
    ("UK garage/2-step", True),
    ("UK funky", True),
    ("Acid Techno", True),
    ("Schranz", True),
    ("Hardstyle 150 BPM", True),
    ("Juke/Footwork", True),
    ("Drum n Bass BPM 160-180", True),
    ("Oldschool jungle", True),
    ("Drumstep", True),
    ("Neurofunk 170-180 BPM", True),
    ("Grime 140 BPM", True)
]

# Writing to file with error handling
instrumental_song_genre_dump_file = f"{base_file_path}instrumental_song_genre_dict.json"
try:
    with open(instrumental_song_genre_dump_file, 'w') as instrumental_song_genre_data_dump_file:
        json.dump(instrumental_song_genre, instrumental_song_genre_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
# A list of tuples representing song genre
song_genre = [
    ("classical acoustic guitar", False),
    ("progressive metal djent", False),
    ("classical acoustic guitar melody", False),
    ("classical celtic guitar melody", False),
    ("fast aggressive phonk", False),
    ("slow ambient drone", False),
    ("heavy metal", False),
    ("fast jazz fusion", False),
    ("heavy electronic dance music", False),
    ("slow reggae", False),
    ("heavy ambient drone", False),
    ("slow country folk", False),
    ("fast hip-hop", False),
    ("fast salsa", False),
    ("fast bluegrass", False),
    ("fast screamo", False),
    ("slow indie rock", False),
    ("fast reggaeton", False),
    ("fast progressive house", False),
    ("fast trap", False),
    ("slow psychedelic rock", False),
    ("fast techno", False),
    ("slow blues", False),
    ("slow R&B", False),
    ("fast punk rock", False),
    ("heavy dubstep", False),
    ("fast thrash metal", False),
    ("slow bossa nova", False),
    ("fast disco", False),
    ("heavy industrial", False),
    ("fast garage rock", False),
    ("slow folk ballad", False),
    ("fast drum and bass", False),
    ("heavy doom metal", False),
    ("fast grindcore", False),
    ("slow tango", False),
    ("fast flamenco", False),
    ("heavy death metal", False),
    ("fast breakbeat", False),
    ("slow waltz", False),
    ("fast hardcore punk", False),
    ("heavy sludge metal", False),
    ("slow soul", False),
    ("fast electroswing", False),
    ("heavy thrash metal", False),
    ("fast ska", False),
    ("slow chamber music", False),
    ("fast house", False),
    ("fast hardstyle", False),
    ("kpop", False),
    ("minimalist techno", False),
    ("darkwave", False),
    ("acid jazz", False),
    ("neofolk", False),
    ("chiptune", False),
    ("witch house", False),
    ("noise rock", False),
    ("IDM (Intelligent Dance Music)", False),
    ("shoegaze", False),
    ("vaporwave", False),
    ("zydeco", False),
    ("krautrock", False),
    ("powernoise", False),
    ("glitch", False),
    ("wonky", False),
    ("chillwave", False),
    ("future garage", False),
    ("post-rock", False),
    ("math rock", False),
    ("jungle", False),
    ("breakcore", False),
    ("lo-fi hip hop", False),
    ("lo-fi indie", False),
    ("lo-fi house", False),
    ("haunting atmospheric witch house", False),
    ("fast aggressive witch house", False),
    ("lo-fi hip-hop", False),
    ("smooth vaporwave jazz", False),
    ("smooth fusion jazz", False),
    ("smooth vaporwave jazz lo-fi hip-hop", False),
    ("mongolian folk", False),
    ("mongolian folk metal", False),
    ("Chinese Classical folk", False),
    ("classical celtic guitar", False),
    ("symphonic metal", False),
    ("western", False),
    ("narcocorridos", False),
    ("ranchera-Mariachi Fusion", False),
    ("bolero", False),
    ("huapango", False),
    ("son jarocho", False),
    ("corrido", False),
    ("banda", False),
    ("cumbia", False),
    ("norteño", False),
    ("mariachi", False),
    ("ranchera", False),
    ("chicano rap", False),
    ("american folk", False),
    ("middle-eastern", False),
    ("classic 80s heart throb freestyle", False),
    ("Electronic", False),
    ("heart throb freestyle", False),
    ("Fusion Freestyle", False),
    ("Fusion House", False),
    ("Progressive House", False),
    ("Deep House", False),
    ("EDM Techno", False),
    ("90s Tech House", False),
    ("Club/Dance", False),
    ("EDM", False),
    ("Trance", False),
    ("Progressive Trance", False),
    ("Jazz Fusion", False),
    ("Jazz-funk", False),
    ("Psychedelic ", False),
    ("Space music ", False),
    ("Hardstyle", False),
    ("Drum n Bass", False),
    ("Electronic Drum n Bass", False),
    ("Early 2000s Drum n Bass", False),
    ("Techstep Drum n Bass", False),
    ("Neurofunk Drum n Bass", False),
    ("Liquid Drum n Bass", False),
    ("Jungle Drum n Bass", False),
    ("Jump Up Drum n Bass", False),
    ("Intelligent Drum n Bass", False),
    ("Halftime Drum n Bass", False),
    ("Breakcore Drum n Bass", False),
    ("Sambass Drum n Bass", False),
    ("Electronic Dance", False),
    ("Dubstep", False),
    ("60s Proto Metal", False),
    ("70s Proto Metal", False),
    ("Acid Rock", False),
    ("Early Metal", False),
    ("Math Rock", False),
    ("Math Prog Rock", False),
    ("Avant Garde", False),
    ("Heavy Blues", False),
    ("Heavy Psyche", False),
    ("Soundtrack", False),
    ("film score", False),
    ("contemporary classical", False),
    ("minimalism", False),
    ("Hip Hop 80-115 BPM", False),
    ("Triphop", False),
    ("Concert marches", False),
    ("UK garage/2-step", False),
    ("UK funky", False),
    ("Acid Techno", False),
    ("Schranz", False),
    ("Hardstyle 150 BPM", False),
    ("Juke/Footwork", False),
    ("Drum n Bass BPM 160-180", False),
    ("Oldschool jungle", False),
    ("Drumstep", False),
    ("Neurofunk 170-180 BPM", False),
    ("Grime 140 BPM", False)
]

# Writing to file with error handling
song_genre_dump_file = f"{base_file_path}song_genre_dict.json"
try:
    with open(song_genre_dump_file, 'w') as song_genre_data_dump_file:
        json.dump(song_genre, song_genre_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)