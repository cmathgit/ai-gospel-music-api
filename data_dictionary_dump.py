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
    #("Prestissimo", 200, float('inf'))
    ("Prestissimo", 200, 420)
]

# Writing to file with error handling
tempo_bpm_dump_file = f"{base_file_path}tempo_dict.json"
try:
    with open(tempo_bpm_dump_file, 'w') as tempo_dump_file:
        json.dump(tempos, tempo_dump_file)
except IOError as e:
    print("Error writing to file:", e)

# list of tuples to store name of the key, its tonic note, whether it's major or minor, its musical mode, and Camelot code.
musical_keys = [
    ("C Ionian", "C", "Major", "Ionian", "8B"),
    ("C# Ionian", "C#", "Major", "Ionian", "3B"),
    ("Db Ionian", "Db", "Major", "Ionian", "3B"),
    ("D Ionian", "D", "Major", "Ionian", "10B"),
    ("D# Ionian", "D#", "Major", "Ionian", "5B"),
    ("Eb Ionian", "Eb", "Major", "Ionian", "5B"),
    ("E Ionian", "E", "Major", "Ionian", "12B"),
    ("F Ionian", "F", "Major", "Ionian", "7B"),
    ("F# Ionian", "F#", "Major", "Ionian", "2B"),
    ("Gb Ionian", "Gb", "Major", "Ionian", "2B"),
    ("G Ionian", "G", "Major", "Ionian", "9B"),
    ("G# Ionian", "G#", "Major", "Ionian", "4B"),
    ("Ab Ionian", "Ab", "Major", "Ionian", "4B"),
    ("A Ionian", "A", "Major", "Ionian", "11B"),
    ("A# Ionian", "A#", "Major", "Ionian", "6B"),
    ("Bb Ionian", "Bb", "Major", "Ionian", "6B"),
    ("B Ionian", "B", "Major", "Ionian", "1B"),
    ("C Dorian", "C", "Minor", "Dorian", "8A"),
    ("C# Dorian", "C#", "Minor", "Dorian", "3A"),
    ("Db Dorian", "Db", "Minor", "Dorian", "3A"),
    ("D Dorian", "D", "Minor", "Dorian", "10A"),
    ("D# Dorian", "D#", "Minor", "Dorian", "5A"),
    ("Eb Dorian", "Eb", "Minor", "Dorian", "5A"),
    ("E Dorian", "E", "Minor", "Dorian", "12A"),
    ("F Dorian", "F", "Minor", "Dorian", "7A"),
    ("F# Dorian", "F#", "Minor", "Dorian", "2A"),
    ("Gb Dorian", "Gb", "Minor", "Dorian", "2A"),
    ("G Dorian", "G", "Minor", "Dorian", "9A"),
    ("G# Dorian", "G#", "Minor", "Dorian", "4A"),
    ("Ab Dorian", "Ab", "Minor", "Dorian", "4A"),
    ("A Dorian", "A", "Minor", "Dorian", "11A"),
    ("A# Dorian", "A#", "Minor", "Dorian", "6A"),
    ("Bb Dorian", "Bb", "Minor", "Dorian", "6A"),
    ("B Dorian", "B", "Minor", "Dorian", "1A"),
    ("C Phrygian", "C", "Minor", "Phrygian", "8A"),
    ("C# Phrygian", "C#", "Minor", "Phrygian", "3A"),
    ("Db Phrygian", "Db", "Minor", "Phrygian", "3A"),
    ("D Phrygian", "D", "Minor", "Phrygian", "10A"),
    ("D# Phrygian", "D#", "Minor", "Phrygian", "5A"),
    ("Eb Phrygian", "Eb", "Minor", "Phrygian", "5A"),
    ("E Phrygian", "E", "Minor", "Phrygian", "12A"),
    ("F Phrygian", "F", "Minor", "Phrygian", "7A"),
    ("F# Phrygian", "F#", "Minor", "Phrygian", "2A"),
    ("Gb Phrygian", "Gb", "Minor", "Phrygian", "2A"),
    ("G Phrygian", "G", "Minor", "Phrygian", "9A"),
    ("G# Phrygian", "G#", "Minor", "Phrygian", "4A"),
    ("Ab Phrygian", "Ab", "Minor", "Phrygian", "4A"),
    ("A Phrygian", "A", "Minor", "Phrygian", "11A"),
    ("A# Phrygian", "A#", "Minor", "Phrygian", "6A"),
    ("Bb Phrygian", "Bb", "Minor", "Phrygian", "6A"),
    ("B Phrygian", "B", "Minor", "Phrygian", "1A"),
    ("C Lydian", "C", "Major", "Lydian", "8B"),
    ("C# Lydian", "C#", "Major", "Lydian", "3B"),
    ("Db Lydian", "Db", "Major", "Lydian", "3B"),
    ("D Lydian", "D", "Major", "Lydian", "10B"),
    ("D# Lydian", "D#", "Major", "Lydian", "5B"),
    ("Eb Lydian", "Eb", "Major", "Lydian", "5B"),
    ("E Lydian", "E", "Major", "Lydian", "12B"),
    ("F Lydian", "F", "Major", "Lydian", "7B"),
    ("F# Lydian", "F#", "Major", "Lydian", "2B"),
    ("Gb Lydian", "Gb", "Major", "Lydian", "2B"),
    ("G Lydian", "G", "Major", "Lydian", "9B"),
    ("G# Lydian", "G#", "Major", "Lydian", "4B"),
    ("Ab Lydian", "Ab", "Major", "Lydian", "4B"),
    ("A Lydian", "A", "Major", "Lydian", "11B"),
    ("A# Lydian", "A#", "Major", "Lydian", "6B"),
    ("Bb Lydian", "Bb", "Major", "Lydian", "6B"),
    ("B Lydian", "B", "Major", "Lydian", "1B"),
    ("C Mixolydian", "C", "Major", "Mixolydian", "8B"),
    ("C# Mixolydian", "C#", "Major", "Mixolydian", "3B"),
    ("Db Mixolydian", "Db", "Major", "Mixolydian", "3B"),
    ("D Mixolydian", "D", "Major", "Mixolydian", "10B"),
    ("D# Mixolydian", "D#", "Major", "Mixolydian", "5B"),
    ("Eb Mixolydian", "Eb", "Major", "Mixolydian", "5B"),
    ("E Mixolydian", "E", "Major", "Mixolydian", "12B"),
    ("F Mixolydian", "F", "Major", "Mixolydian", "7B"),
    ("F# Mixolydian", "F#", "Major", "Mixolydian", "2B"),
    ("Gb Mixolydian", "Gb", "Major", "Mixolydian", "2B"),
    ("G Mixolydian", "G", "Major", "Mixolydian", "9B"),
    ("G# Mixolydian", "G#", "Major", "Mixolydian", "4B"),
    ("Ab Mixolydian", "Ab", "Major", "Mixolydian", "4B"),
    ("A Mixolydian", "A", "Major", "Mixolydian", "11B"),
    ("A# Mixolydian", "A#", "Major", "Mixolydian", "6B"),
    ("Bb Mixolydian", "Bb", "Major", "Mixolydian", "6B"),
    ("B Mixolydian", "B", "Major", "Mixolydian", "1B"),
    ("C Aeolian", "C", "Minor", "Aeolian", "8A"),
    ("C# Aeolian", "C#", "Minor", "Aeolian", "3A"),
    ("Db Aeolian", "Db", "Minor", "Aeolian", "3A"),
    ("D Aeolian", "D", "Minor", "Aeolian", "10A"),
    ("D# Aeolian", "D#", "Minor", "Aeolian", "5A"),
    ("Eb Aeolian", "Eb", "Minor", "Aeolian", "5A"),
    ("E Aeolian", "E", "Minor", "Aeolian", "12A"),
    ("F Aeolian", "F", "Minor", "Aeolian", "7A"),
    ("F# Aeolian", "F#", "Minor", "Aeolian", "2A"),
    ("Gb Aeolian", "Gb", "Minor", "Aeolian", "2A"),
    ("G Aeolian", "G", "Minor", "Aeolian", "9A"),
    ("G# Aeolian", "G#", "Minor", "Aeolian", "4A"),
    ("Ab Aeolian", "Ab", "Minor", "Aeolian", "4A"),
    ("A Aeolian", "A", "Minor", "Aeolian", "11A"),
    ("A# Aeolian", "A#", "Minor", "Aeolian", "6A"),
    ("Bb Aeolian", "Bb", "Minor", "Aeolian", "6A"),
    ("B Aeolian", "B", "Minor", "Aeolian", "1A"),
    ("C Locrian", "C", "Minor", "Locrian", "8A"),
    ("C# Locrian", "C#", "Minor", "Locrian", "3A"),
    ("Db Locrian", "Db", "Minor", "Locrian", "3A"),
    ("D Locrian", "D", "Minor", "Locrian", "10A"),
    ("D# Locrian", "D#", "Minor", "Locrian", "5A"),
    ("Eb Locrian", "Eb", "Minor", "Locrian", "5A"),
    ("E Locrian", "E", "Minor", "Locrian", "12A"),
    ("F Locrian", "F", "Minor", "Locrian", "7A"),
    ("F# Locrian", "F#", "Minor", "Locrian", "2A"),
    ("Gb Locrian", "Gb", "Minor", "Locrian", "2A"),
    ("G Locrian", "G", "Minor", "Locrian", "9A"),
    ("G# Locrian", "G#", "Minor", "Locrian", "4A"),
    ("Ab Locrian", "Ab", "Minor", "Locrian", "4A"),
    ("A Locrian", "A", "Minor", "Locrian", "11A"),
    ("A# Locrian", "A#", "Minor", "Locrian", "6A"),
    ("Bb Locrian", "Bb", "Minor", "Locrian", "6A"),
    ("B Locrian", "B", "Minor", "Locrian", "1A")
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
    ("horsehead fiddle"),
    ("plucked bass"),
    ("synth"),
    ("horn"),
    ("beat"),
    ("sub-bass"),
    ("oud"),
    ("kemenche"),
    ("bağlama"),
    ("acoustic guitar"),
    ("Ondes Martenot"), # an early electronic instrument, used extensively by Jonny Greenwood)
    ("Brass"),
    ("Strings"),
    ("Sampler"),
    ("Harmonium"),
    ("Computer-based Effects"),
    ("Handpan")
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
    ("Chylandyk", "", "male"), # bird-like sounds
    
    # rhythmic vocalists
    ("Rapper","MC","Male"),
    ("Rapper","MC","Female"),
    ("MC","Rapper","Male"),
    ("MC","Rapper","Female"),
    ("Emcee","Rapper","Male"),
    ("Emcee","Rapper","Female"),
    ("Rapper","Emcee","Male"),
    ("Rapper","Emcee","Female"),
    ("MC","Master of Ceremonies","Male"),
    ("MC","Master of Ceremonies","Female"),
    ("cryptic lyricism","rapid-fire vocals","Male"),
    ("cryptic lyricism","rapid-fire vocals","Female"),
    ("rapid-fire vocals","cryptic lyricism","Male"),
    ("rapid-fire vocals","cryptic lyricism","Female")
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
    ('Music Theater', False),
    ('zydeco', False),
    ("experimental hip hop", False),
    ("punk rap", False),
    ("noise", False),
    ("industrial", False),
    ("rap rock", False),
    ("electropunk", False),
    ("Avant-garde", False),
    ("death trips", False),
    ("math drums", False),
    ('fast drum and bass', False),
    ('slow ambient drone', False),
    ('progressive metal djent', False),
    ('90s Tech House', False),
    ('fast reggaeton', False),
    ('heavy thrash metal', False),
    ('bolero', False),
    ('heavy industrial', False),
    ('IDM (Intelligent Dance Music)', False),
    ('ranchera', False),
    ('fast breakbeat', False),
    ('Jungle Drum n Bass', False),
    ('lo-fi indie', False),
    ('60s Proto Metal', False),
    ('Electronic Drum n Bass', False),
    ('smooth fusion jazz', False),
    ('Grime 140 BPM', False),
    ('contemporary classical', False),
    ('Avant Garde', False),
    ('heavy sludge metal', False),
    ('Jazz Fusion', False),
    ('Freestyle Electro', False),
    ('Freestyle Dance Music', False),
    ('minimalist techno', False),
    ('Hip Hop 80-115 BPM', False),
    ('lo-fi hip hop', False),
    ('krautrock', False),
    ('progressive metal', False),
    ('fast progressive house', False),
    ('Math Rock', False),
    ('Progressive House', False),
    ('Soundtrack', False),
    ('slow psychedelic rock', False),
    ('Oldskool Latin Freestyle', False),
    ('vaporwave lo-fi hip-hop', False),
    ('corrido', False),
    ('american folk', False),
    ('celtic guitar melody', False),
    ('Math Prog Rock', False),
    ('haunting witch house', False),
    ('symphonic metal', False),
    ('neofolk', False),
    ('Hardstyle', False),
    ('glitch', False),
    ('Neurofunk Drum n Bass', False),
    ('Neurofunk 170-180 BPM', False),
    ('Fusion Freestyle', False),
    ('heavy death metal', False),
    ('American hip hop', False),
    ('Liquid Drum n Bass', False),
    ('Electronic Dance', False),
    ('Heavy Blues', False),
    ('contemporary worship', False),
    ('Early 90s Freestyle Dance', False),
    ('J-Pop', False),
    ('chiptune', False),
    ('shoegaze', False),
    ('heart throb freestyle', False),
    ('Space music ', False),
    ('Acid Rock', False),
    ('mongolian folk metal', False),
    ('slow indie rock', False),
    ('gospel hymn', False),
    ('Triphop', False),
    ('christian worship', False),
    ('Freestyle EDM', False),
    ('fast garage rock', False),
    ('Drum n Bass BPM 160-180', False),
    ('lo-fi hip-hop', False),
    ('middle-eastern', False),
    ('Progressive Trance', False),
    ('fast ska', False),
    ('fast disco', False),
    ('Fusion House', False),
    ('Electronic', False),
    ('fast hardcore punk', False),
    ('fast flamenco', False),
    ('fast techno', False),
    ('slow waltz', False),
    ('fast salsa', False),
    ('80s heart throb freestyle', False),
    ('heavy doom metal', False),
    ('Techstep Drum n Bass', False),
    ('Freestyle Music Mix', False),
    ('Early Metal', False),
    ('Early 2000s Drum n Bass', False),
    ('vaporwave', False),
    ('post-rock', False),
    ('Sambass Drum n Bass', False),
    ('slow tango', False),
    ('Chinese Classical folk', False),
    ('Drum n Bass', False),
    ('ranchera-Mariachi Fusion', False),
    ('noise rock', False),
    ('slow country folk', False),
    ('fast grindcore', False),
    ('Breakcore Drum n Bass', False),
    ('Deep House', False),
    ('slow bossa nova', False),
    ('slow folk ballad', False),
    ('witch house', False),
    ('Trance', False),
    ('fast trap', False),
    ('Dubstep', False),
    ('film score', False),
    ('Drumstep', False),
    ('banda', False),
    ('chicano rap', False),
    ('norteño', False),
    ('classical acoustic guitar', False),
    ('heavy dubstep', False),
    ('mongolian folk', False),
    ('darkwave', False),
    ('kpop', False),
    ('fast house', False),
    ('fast hardstyle', False),
    ('narcocorridos', False),
    ('fast jazz fusion', False),
    ('Jazz-funk', False),
    ('classical celtic guitar', False),
    ('huapango', False),
    ('Christian hip hop', False),
    ('wonky', False),
    ('breakcore', False),
    ('Club/Dance', False),
    ('classical guitar melody', False),
    ('future garage', False),
    ('fast punk rock', False),
    ('metal djent screamo', False),
    ('EDM Techno', False),
    ('Oldskool Freestyle Mix', False),
    ('fast aggressive phonk', False),
    ('Halftime Drum n Bass', False),
    ('chillwave', False),
    ('Hardstyle 150 BPM', False),
    ('mariachi', False),
    ('math rock', False),
    ('Heavy Psyche', False),
    ('EDM', False),
    ('minimalism', False),
    ('fast screamo', False),
    ('slow blues', False),
    ('Jump Up Drum n Bass', False),
    ('Hip Hop', False),
    ('acid jazz', False),
    ('Gospel Rap', False),
    ('70s Proto Metal', False),
    ('Hip Hop/Rap', False),
    ('cumbia', False),
    ('christian worship', False),
    ('American Christian hip hop', False),
    ('ambient Christian worship', False),
    ('powernoise', False),
    ('lo-fi house', False),
    ('aggressive witch house', False),
    ('metalcore djent screamo', False),
    ('UK funky', False),
    ('western', False),
    ('Early 90s  Freestyle', False),
    ('heavy metal', False),
    ('fast bluegrass', False),
    ('fast thrash metal', False),
    ('smooth vaporwave jazz', False),
    ('Concert marches', False),
    ('Oldskool Latin Freestyle', False),
    ('slow soul', False),
    ('Schranz', False),
    ('fast hip-hop', False),
    ('slow R&B', False),
    ('Juke/Footwork', False),
    ('Intelligent Drum n Bass', False),
    ('fast electroswing', False),
    ('bluegrass gospel', False),
    ('New Jersey Hip Hop', False),
    ('Oldschool jungle', False),
    ('slow chamber music', False),
    ('son jarocho', False),
    ('slow reggae', False),
    ('heavy ambient drone', False),
    ('NYC Hip Hop', False),
    ('jungle', False),
    ('Psychedelic ', False),
    ('electronic dance music', False),
    ('Acid Techno', False),
    ('UK garage/2-step', False),
    ('Motown', False),
    ('Mo Town', False),
    ('Soulful Motown', False),
    ('alternative rock', False),
    ('art rock', False),
    ('experimental rock', False),
    ('art pop', False),
    ('Britpop', False),
    ('Progressive Rock', False),
    ('Post-Rock', False),
    ("Motown", False),
    ("Mo Town", False),
    ("Soulful Motown", False),
    ("alternative rock", False),
    ("art rock", False),
    ("experimental rock", False),
    ("art pop", False),
    ("Britpop", False),
    ("Progressive Rock", False),
    ("Post-Rock", False),
    ("gospel soul", False), 
    ("A Capella", False), 
    ("voices", False), 
    ("lo-fi", False), 
    ("jazz-infused beats", False),
    ("warm", False), 
    ("rich basslines", False), 
    ("jazzy guitar riffs", False),
    ("soft keys", False), 
    ("mellow synths", False), 
    ("smooth", False),
    ("emotive vocals", False),
    ("harmonies", False),
    ("reverb", False), 
    ("echo", False),
    ("dreamy", False),
    ("atmospheric", False),
    ("Upbeat Jazz", False),
    ("Burning Jazz", False),
    ("Burning Jazz, Liquid Drum and Bass", False),
    ("Video Game OST", False),
    ("Video Game Original Sound Track", False),
    ("Cinematic Score", False),
    ("Orchestral, Ambient, atmospheric", False),
    ("Fantasy RPG Game OST", False),
    ("Fantasy RPG Video Game OST", False),
    ("RPG Video Game Original Sound Track", False),
    ("Fantasy RPG Original Sound Track", False),
    ("Suite bergamasque", False),
    ("Baroque", False),
    ("Baroque, Complex polyphony, ornate melodies", False),
    ("Classical", False),
    ("Romantic", False),
    ("Impressionist", False),
    ("Expressionist", False),
    ("Modernism", False),
    ("Neoclassicism", False),
    ("Serialism", False),
    ("Avant-Garde", False),
    ("Renaissance", False),
    ("Chamber Music", True),
    ("Opera", False),
    ("Choral Music", False),
    ("Programmatic Music", False),
    ("Minimalism", False),
    ("Baroque, Complex polyphony, ornate melodies", False),
    ("Classical, structured forms, sonata, symphony, homophony.", False),
    ("Classical, structured forms, sonata, homophony.", False),
    ("Classical, structured forms, symphony, homophony.", False),
    ("Romantic, Emotional expression, expanded orchestra, programmatic music, lyrical melodies", False),
    ("Romantic, Emotional expression, expanded orchestra", False),
    ("Romantic, programmatic music, lyrical melodies", False),
    ("Impressionist, atmospheric, ambiguous harmonies, tone color", False),
    ("Expressionist, Intense emotion, dissonance, atonal, fragmented melodies", False),
    ("Modernism, dissonant, abstract.", False),
    ("Serialism, twelve-tone technique, mathematical", False),
    ("Minimalism, simple motifs, meditative quality", False),
    ("Avant-Garde, unconventional, Experimental", False),
    ("Renaissance, Polyphonic, modal, vocal", False),
    ("Choral Music, choir, religious, ceremonial", False),
    ("Programmatic Music", False),
    ("binaural beats", False),
    ("binaural beats, theta wave", False),
    ("binaural beats, beta wave", False),
    ("binaural beats, alpha wave", False),
    ("binaural beats, gamma wave", False),
    ("Minimalist Soundscapes", False),
    ("Minimalist Soundscapes", False),
    ("Minimalist Soundscapes", False),
    ("Corporate or Upbeat Instrumental", False),
    ("Corporate Instrumental", False),
    ("Upbeat Instrumental", False),
    ("Corporate Upbeat", False),
    ("Corporate or Upbeat Instrumental", False),
    ("Chillhop", False),
    ("Futuristic Sound Design", False),
    ("Percussive Solos", False),
    ("Drum Solos", False),
    ("Bass Solos", False),
    ("Guitar Solos", False),
    ("Keyboard Solos", False),
    ("Synth Solos", False),
    ("String Solos", False),
    ("Brass Solos", False),
    ("Woodwind Solos", False),
    ("Hip Hop Drum Solos", False),
    ("Rock Drum Solos", False),
    ("Pop Drum Solos", False),
    ("Country Drum Solos", False),
    ("Blues Drum Solos", False),
    ("Jazz Drum Solos", False),
    ("Reggae Drum Solos", False),
    ("Soul Drum Solos", False),
    ("Hip Hop Drum Loop", False),
    ("Rock Drum Loop", False),
    ("Pop Drum Loop", False),
    ("Country Drum Loop", False),
    ("Blues Drum Loop", False),
    ("Jazz Drum Loop", False),
    ("Reggae Drum Loop", False),
    ("Drum Loop", False)
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
    ("experimental hip hop", True),
    ("punk rap", True),
    ("noise", True),
    ("industrial", True),
    ("rap rock", True),
    ("electropunk", True),
    ("Avant-garde", True),
    ("death trips", True),
    ("math drums", True),
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
    ("Grime 140 BPM", True),
    ("American Christian hip hop", True),
    ("NYC Hip Hop", True),
    ("J-Pop", True),
    ("Hip Hop/Rap", True),
    ("Gospel Rap", True),
    ("American hip hop", True),
    ("New Jersey Hip Hop", True),
    ("Freestyle Dance Music", True),
    ("Freestyle Electro", True),
    ("Freestyle EDM", True),
    ("Early 90s Freestyle Dance Music Mix", True),
    ("Early 90s Heart Throb Freestyle", True),
    ("Motown", True),
    ("Mo Town", True),
    ("Soulful Motown", True),
    ("alternative rock", True),
    ("art rock", True),
    ("experimental rock", True),
    ("art pop", True),
    ("Britpop", True),
    ("Progressive Rock", True),
    ("Post-Rock", True),
    ("Upbeat Jazz", True),
    ("Burning Jazz", True),
    ("Burning Jazz, Liquid Drum and Bass", True),
    ("gospel soul", True), 
    ("A Capella", True), 
    ("voices", True), 
    ("lo-fi", True), 
    ("jazz-infused beats", True),
    ("warm", True), 
    ("rich basslines", True), 
    ("jazzy guitar riffs", True),
    ("soft keys", True), 
    ("mellow synths", True), 
    ("smooth", True),
    ("emotive vocals", True),
    ("harmonies", True),
    ("reverb", True), 
    ("echo", True),
    ("dreamy", True),
    ("atmospheric", True),
    ("Video Game OST", True),
    ("Video Game Original Sound Track", True),
    ("Cinematic Score", True),
    ("Orchestral, Ambient, atmospheric", True),
    ("Fantasy RPG Game OST", True),
    ("Fantasy RPG Video Game OST", True),
    ("RPG Video Game Original Sound Track", True),
    ("Fantasy RPG Original Sound Track", True),
    ("Suite bergamasque", True),
    ("Baroque", True),
    ("Baroque, Complex polyphony, ornate melodies", True),
    ("Classical", True),
    ("Romantic", True),
    ("Impressionist", True),
    ("Expressionist", True),
    ("Modernism", True),
    ("Neoclassicism", True),
    ("Serialism", True),
    ("Avant-Garde", True),
    ("Renaissance", True),
    ("Chamber Music", True),
    ("Opera", True),
    ("Choral Music", True),
    ("Programmatic Music", True),
    ("Minimalism", True),
    ("Baroque, Complex polyphony, ornate melodies", True),
    ("Classical, structured forms, sonata, symphony, homophony.", True),
    ("Classical, structured forms, sonata, homophony.", True),
    ("Classical, structured forms, symphony, homophony.", True),
    ("Romantic, Emotional expression, expanded orchestra, programmatic music, lyrical melodies", True),
    ("Romantic, Emotional expression, expanded orchestra", True),
    ("Romantic, programmatic music, lyrical melodies", True),
    ("Impressionist, atmospheric, ambiguous harmonies, tone color", True),
    ("Expressionist, Intense emotion, dissonance, atonal, fragmented melodies", True),
    ("Modernism, dissonant, abstract.", True),
    ("Serialism, twelve-tone technique, mathematical", True),
    ("Minimalism, simple motifs, meditative quality", True),
    ("Avant-Garde, unconventional, Experimental", True),
    ("Renaissance, Polyphonic, modal, vocal", True),
    ("Choral Music, choir, religious, ceremonial", True),
    ("Programmatic Music", True),
    ("binaural beats", True),
    ("binaural beats, theta wave", True),
    ("binaural beats, beta wave", True),
    ("binaural beats, alpha wave", True),
    ("binaural beats, gamma wave", True),
    ("Minimalist Soundscapes", True),
    ("Minimalist Soundscapes", True),
    ("Minimalist Soundscapes", True),
    ("Corporate or Upbeat Instrumental", True),
    ("Corporate Instrumental", True),
    ("Upbeat Instrumental", True),
    ("Corporate Upbeat", True),
    ("Corporate or Upbeat Instrumental", True),
    ("Chillhop", True),
    ("Futuristic Sound Design", True),
    ("Percussive Solos", True),
    ("Drum Solos", True),
    ("Bass Solos", True),
    ("Guitar Solos", True),
    ("Keyboard Solos", True),
    ("Synth Solos", True),
    ("String Solos", True),
    ("Brass Solos", True),
    ("Woodwind Solos", True),
    ("Hip Hop Drum Solos", True),
    ("Rock Drum Solos", True),
    ("Pop Drum Solos", True),
    ("Country Drum Solos", True),
    ("Blues Drum Solos", True),
    ("Jazz Drum Solos", True),
    ("Reggae Drum Solos", True),
    ("Soul Drum Solos", True),
    ("Hip Hop Drum Loop", True),
    ("Rock Drum Loop", True),
    ("Pop Drum Loop", True),
    ("Country Drum Loop", True),
    ("Blues Drum Loop", True),
    ("Jazz Drum Loop", True),
    ("Reggae Drum Loop", True),
    ("Drum Loop", True)
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
    ('Music Theater', False),
    ("classical acoustic guitar", False),
    ("experimental hip hop", False),
    ("punk rap", False),
    ("noise", False),
    ("industrial", False),
    ("rap rock", False),
    ("electropunk", False),
    ("Avant-garde", False),
    ("death trips", False),
    ("math drums", False),
    ("progressive metal djent", False),
    ("classical acoustic guitar melody", False),
    ("classical celtic guitar melody", False),
    ("bluegrass gospel", False),
    ("classical celtic guitar", False),
    ("gospel hymn", False),
    ("christian worship", False),
    ("contemporary worship", False),
    ("fast aggressive phonk", False),
    ("slow ambient drone", False),
    ("slow ambient drone christian worship", False),
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
    ("Grime 140 BPM", False),
    ("American Christian hip hop", False),
    ("Christian hip hop", False),
    ("NYC Hip Hop", False),
    ("J-Pop", False),
    ("Hip Hop/Rap", False),
    ("Gospel Rap", False),
    ("American hip hop", False),
    ("New Jersey Hip Hop", False),
    ("Freestyle Dance Music", False),
    ("Freestyle Electro", False),
    ("Freestyle EDM", False),
    ("Early 90s Freestyle Dance Music Mix", False),
    ("Early 90s Heart Throb Freestyle", False),
    #("Too Cool Chris, Early 90s Heart Throb Freestyle Dance Underground DJ Mix, female falsetto singer flat", False),
    ("Freestyle Music Mix", False),
    ("Oldskool Latin Freestyle Mix", False),
    ("Oldskool Freestyle Mix", False),
    ("Motown", False),
    ("Mo Town", False),
    ("Soulful Motown", False),
    ("alternative rock", False),
    ("art rock", False),
    ("experimental rock", False),
    ("art pop", False),
    ("Britpop", False),
    ("Progressive Rock", False),
    ("Upbeat Jazz", False),
    ("Burning Jazz", False),
    ("Burning Jazz, Liquid Drum and Bass", False),
    ("Post-Rock", False),
    ("gospel soul", False), 
    ("A Capella", False), 
    ("voices", False), 
    ("lo-fi", False), 
    ("jazz-infused beats", False),
    ("warm", False), 
    ("rich basslines", False), 
    ("jazzy guitar riffs", False),
    ("soft keys", False), 
    ("mellow synths", False), 
    ("smooth", False),
    ("emotive vocals", False),
    ("harmonies", False),
    ("reverb", False), 
    ("echo", False),
    ("dreamy", False),
    ("atmospheric", False),
    ("Video Game OST", False),
    ("Video Game Original Sound Track", False),
    ("Cinematic Score", False),
    ("Orchestral, Ambient, atmospheric", False),
    ("Fantasy RPG Game OST", False),
    ("Fantasy RPG Video Game OST", False),
    ("RPG Video Game Original Sound Track", False),
    ("Fantasy RPG Original Sound Track", False),
    ("Suite bergamasque", False),
    ("Baroque", False),
    ("Baroque, Complex polyphony, ornate melodies", False),
    ("Classical", False),
    ("Romantic", False),
    ("Impressionist", False),
    ("Expressionist", False),
    ("Modernism", False),
    ("Neoclassicism", False),
    ("Serialism", False),
    ("Avant-Garde", False),
    ("Renaissance", False),
    ("Chamber Music", True),
    ("Opera", False),
    ("Choral Music", False),
    ("Programmatic Music", False),
    ("Minimalism", False),
    ("Baroque, Complex polyphony, ornate melodies", False),
    ("Classical, structured forms, sonata, symphony, homophony.", False),
    ("Classical, structured forms, sonata, homophony.", False),
    ("Classical, structured forms, symphony, homophony.", False),
    ("Romantic, Emotional expression, expanded orchestra, programmatic music, lyrical melodies", False),
    ("Romantic, Emotional expression, expanded orchestra", False),
    ("Romantic, programmatic music, lyrical melodies", False),
    ("Impressionist, atmospheric, ambiguous harmonies, tone color", False),
    ("Expressionist, Intense emotion, dissonance, atonal, fragmented melodies", False),
    ("Modernism, dissonant, abstract.", False),
    ("Serialism, twelve-tone technique, mathematical", False),
    ("Minimalism, simple motifs, meditative quality", False),
    ("Avant-Garde, unconventional, Experimental", False),
    ("Renaissance, Polyphonic, modal, vocal", False),
    ("Choral Music, choir, religious, ceremonial", False),
    ("Programmatic Music", False),
    ("binaural beats", False),
    ("binaural beats, theta wave", False),
    ("binaural beats, beta wave", False),
    ("binaural beats, alpha wave", False),
    ("binaural beats, gamma wave", False),
    ("Minimalist Soundscapes", False),
    ("Minimalist Soundscapes", False),
    ("Minimalist Soundscapes", False),
    ("Corporate or Upbeat Instrumental", False),
    ("Corporate Instrumental", False),
    ("Upbeat Instrumental", False),
    ("Corporate Upbeat", False),
    ("Corporate or Upbeat Instrumental", False),
    ("Chillhop", False),
    ("Futuristic Sound Design", False),
    ("Percussive Solos", False),
    ("Drum Solos", False),
    ("Bass Solos", False),
    ("Guitar Solos", False),
    ("Keyboard Solos", False),
    ("Synth Solos", False),
    ("String Solos", False),
    ("Brass Solos", False),
    ("Woodwind Solos", False),
    ("Hip Hop Drum Solos", False),
    ("Rock Drum Solos", False),
    ("Pop Drum Solos", False),
    ("Country Drum Solos", False),
    ("Blues Drum Solos", False),
    ("Jazz Drum Solos", False),
    ("Reggae Drum Solos", False),
    ("Soul Drum Solos", False),
    ("Hip Hop Drum Loop", False),
    ("Rock Drum Loop", False),
    ("Pop Drum Loop", False),
    ("Country Drum Loop", False),
    ("Blues Drum Loop", False),
    ("Jazz Drum Loop", False),
    ("Reggae Drum Loop", False),
    ("Drum Loop", False)
]

# Writing to file with error handling
song_genre_dump_file = f"{base_file_path}song_genre_dict.json"
try:
    with open(song_genre_dump_file, 'w') as song_genre_data_dump_file:
        json.dump(song_genre, song_genre_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
    # [Narrator .Reflective and engaging.]
    # [Clips of uplifting hymns and soulful vocals play.]
    # [Shift to darker, bass-heavy beats.]
    # [Acoustic guitar and live audience sounds play.]
    # [Trumpets and heavenly hosts sounds play.]
    # [Studio sounds with energetic drums and loops.]
    # [Narrator excitedly.]
    # [Fade out with music crescendoing.]
simple_bible_prompts = [
    ("mellow synths, Handpan, Choir, mandolin, trumpet, plucked bass, Triple Concerto, Andante 100 bpm, F Lydian, music plays in the background, gradually building in intensity as the narrator speaks, Fade out with music crescendoing"),
    ("[Narrator Reflective and engaging.][Clips of uplifting hymns and soulful vocals play.][Shift to darker, bass-heavy beats.][Acoustic guitar and live audience sounds play.][Trumpets and heavenly hosts sounds play.][Studio sounds with energetic drums and loops.][Narrator excitedly.][Fade out with music crescendoing.]"),
    ("Upbeat music plays in the background, gradually building in intensity as the narrator speaks, Fade out with album covers on screen and music crescendoing"),
    ("slow bossa nova, Tenor (Leggero), saxophone, Psalms 72, Largo 45, C Lydian"),
    ("kpop, Soprano (Dramatic), guitar, Genesis 12, Allegro 145, G# Ionian"),
    ("darkwave, Contralto (Alto), drums, Exodus 22, Presto 190, F# Aeolian"),
    ("EDM Techno, Countertenor (Countertenor), piano, Ruth 3, Moderato 115, A# Dorian"),
    ("smooth fusion jazz, Baritone (Dramatic), violin, Isaiah 48, Andante 85, D# Mixolydian"),
    ("fast reggae, Khoomei (Tuvan Style), trumpet, Matthew 14, Allegro 130, B Locrian"),
    ("acid jazz, MC (Rapper), clarinet, Revelation 6, Larghetto 64, Eb Phrygian"),
    ("fast disco, Soprano (Lyric), electric guitar, Job 22, Presto 180, G# Lydian"),
    ("heavy industrial, Mezzo-Soprano (Lyric), accordion, Nehemiah 7, Moderato 110, C# Ionian"),
    ("fast hip-hop, Tenor (Lyric), cello, Acts 18, Allegro 160, Bb Aeolian"),
    ("lo-fi house, Bass (Lyric), bass guitar, Daniel 4, Andante 100, E Mixolydian"),
    ("smooth vaporwave jazz, Rapper (MC), flute, 1 Samuel 11, Largo 55, Ab Ionian"),
    ("slow tango, Khoomei (Kharkhiraa Khoomei), harmonica, Romans 8, Larghetto 63, A# Locrian"),
    ("lo-fi hip hop, Bass (Dramatic), drums, Deuteronomy 25, Presto 175, G# Aeolian"),
    ("fast salsa, Soprano (Coloratura), harp, Judges 9, Allegro 155, D Lydian"),
    ("fast drum and bass, Rapper (Emcee), ukulele, Ezekiel 22, Moderato 115, F# Phrygian"),
    ("minimalist techno, Mezzo-Soprano (Dramatic), mandolin, James 3, Larghetto 61, Bb Ionian"),
    ("heavy dubstep, Bass (Basso Profondo), guitar, Haggai 1, Presto 195, Eb Lydian"),
    ("haunting atmospheric witch house, Soprano (Dramatic), violin, Amos 5, Allegro 140, C# Phrygian"),
    ("fast breakbeat, Tenor (Dramatic), oboe, Lamentations 4, Andante 95, E Aeolian"),
    ("fast flamenco, Baritone (Lyric), bagpipes, Proverbs 15, Presto 185, G# Mixolydian"),
    ("slow country folk, Soprano (Dramatic), synthesizer, Leviticus 18, Larghetto 55, F# Dorian"),
    ("fast bluegrass, Mezzo-Soprano (Coloratura), accordion, Exodus 15, Allegro 150, D Mixolydian"),
    ("fast screamo, Countertenor (Countertenor), violin, Numbers 28, Presto 195, Bb Locrian"),
    ("slow indie rock, Contralto (Alto), electric guitar, Joshua 9, Larghetto 62, A Aeolian"),
    ("fast reggaeton, Soprano (Lyric), drums, Job 40, Allegro 155, C Dorian"),
    ("fast progressive house, Tenor (Leggero), saxophone, Jeremiah 14, Presto 180, G Lydian"),
    ("fast trap, Mezzo-Soprano (Dramatic), trombone, Nehemiah 3, Allegro 165, A Mixolydian"),
    ("slow psychedelic rock, Baritone (Lyric), bass guitar, Ecclesiastes 10, Larghetto 60, F Phrygian"),
    ("fast techno, Bass (Basso Profondo), synthesizer, Judges 5, Allegro 170, B Mixolydian"),
    ("slow blues, Contralto (Alto), harmonica, Psalms 119, Larghetto 56, E Aeolian"),
    ("slow R&B, Tenor (Lyric), electric guitar, Ezekiel 40, Larghetto 58, D Mixolydian"),
    ("fast punk rock, Soprano (Coloratura), drums, Deuteronomy 7, Allegro 155, G Mixolydian"),
    ("heavy dubstep, Mezzo-Soprano (Lyric), synthesizer, Genesis 29, Presto 190, Eb Phrygian"),
    ("fast thrash metal, Countertenor (Countertenor), electric guitar, 1 Chronicles 22, Allegro 175, Bb Dorian"),
    ("slow bossa nova, Baritone (Lyric), piano, Ruth 2, Larghetto 58, C Phrygian"),
    ("fast salsa, Soprano (Dramatic), trumpet, Job 4, Allegro 160, E Phrygian"),
    ("slow tango, Contralto (Alto), violin, Zechariah 5, Larghetto 59, F Lydian"),
    ("fast flamenco, Tenor (Leggero), flamenco guitar, Psalms 110, Allegro 165, G Mixolydian"),
    ("heavy metal, Mezzo-Soprano (Dramatic), drums, Jeremiah 48, Presto 185, D Phrygian"),
    ("fast jazz fusion, Soprano (Lyric), saxophone, Ecclesiastes 7, Allegro 160, A Mixolydian"),
    ("slow reggae, Countertenor (Countertenor), bass guitar, Exodus 2, Larghetto 54, C Dorian"),
    ("heavy ambient drone, Baritone (Lyric), synthesizer, Leviticus 1, Presto 200, F# Locrian"),
    ("slow country folk, Contralto (Alto), banjo, Esther 1, Larghetto 57, G Mixolydian"),
    ("fast hip-hop, Soprano (Dramatic), electric guitar, Judges 16, Allegro 155, E Dorian"),
    ("fast bluegrass, Mezzo-Soprano (Coloratura), mandolin, Isaiah 50, Allegro 155, A Mixolydian"),
    ("fast punk rock, Countertenor (Countertenor), drums, Hosea 3, Allegro 170, G Dorian"),
    ("slow bossa nova, Baritone (Lyric), accordion, Haggai 2, Larghetto 57, Bb Ionian"),
    ("fast disco, Tenor (Leggero), synthesizer, Song of Solomon 2, Allegro 175, E Mixolydian"),
    ("slow tango, Contralto (Alto), bandoneon, Psalms 25, Larghetto 61, Ab Mixolydian"),
    ("fast flamenco, Mezzo-Soprano (Dramatic), guitar, 1 Samuel 31, Allegro 160, F Phrygian"),
    ("heavy metal, Soprano (Lyric), drums, Jeremiah 44, Presto 190, D Phrygian"),
    ("fast jazz fusion, Countertenor (Countertenor), saxophone, Ezekiel 33, Allegro 165, Bb Dorian"),
    ("slow reggae, Baritone (Lyric), bass guitar, Job 1, Larghetto 56, G# Aeolian"),
    ("heavy ambient drone, Tenor (Leggero), synthesizer, Numbers 6, Presto 200, C Phrygian"),
    ("fast hip-hop, Contralto (Alto), electric guitar, Judges 19, Allegro 155, D Dorian"),
    ("fast bluegrass, Soprano (Dramatic), banjo, Isaiah 2, Allegro 160, E Mixolydian"),
    ("fast punk rock, Mezzo-Soprano (Coloratura), drums, Hosea 6, Allegro 170, A Mixolydian"),
    ("slow bossa nova, Countertenor (Countertenor), piano, Haggai 1, Larghetto 58, F# Locrian"),
    ("fast disco, Baritone (Lyric), synthesizer, Song of Solomon 7, Allegro 175, G Mixolydian"),
    ("slow tango, Tenor (Leggero), bandoneon, Psalms 2, Larghetto 62, A Mixolydian"),
    ("fast flamenco, Contralto (Alto), guitar, 1 Samuel 20, Allegro 160, F# Phrygian"),
    ("heavy metal, Soprano (Lyric), drums, Jeremiah 1, Presto 195, C# Phrygian"),
    ("fast jazz fusion, Mezzo-Soprano (Dramatic), saxophone, Ezekiel 18, Allegro 165, Bb Dorian"),
    ("slow reggae, Countertenor (Countertenor), bass guitar, Job 3, Larghetto 56, G Aeolian"),
    ("heavy ambient drone, Baritone (Lyric), synthesizer, Numbers 10, Presto 200, C# Locrian"),
    ("experimental hip hop, punk rap, noise, industrial, rap rock, electropunk, Avant-garde, death trips, synth, math drums, cryptic lyricism, MC Ryde shouting, rapid-fire vocals, biblically inspired lyrics"),
    ("gospel soul, A Capella, voices, church choir, Baritone (male), Soprano (female), lo-fi, jazz-infused beats, drums, warm, rich basslines, jazzy guitar riffs, soft keys, mellow synths, 70-90 BPM, smooth, emotive vocals, harmonies, reverb, echo, dreamy, atmospheric"),
    ("lo-fi, jazz-infused beats, drums, warm, rich basslines, jazzy guitar riffs, soft keys, mellow synths, 70-90 BPM, smooth, emotive vocals, harmonies, reverb, echo, dreamy, atmospheric"),
    ("rich basslines, jazzy guitar riffs, soft keys, mellow synths, 70-90 BPM, smooth, emotive vocals, harmonies, reverb, echo, dreamy, atmospheric"),
    ("slow ambient drone, binaural beats, theta wave, E Dorian, Larghetto 66 bpm")
]

# Writing to file with error handling
simple_bible_prompts_dump_file = f"{base_file_path}simple_bible_prompts_dict.json"
try:
    with open(simple_bible_prompts_dump_file, 'w') as simple_bible_prompts_data_dump_file:
        json.dump(simple_bible_prompts, simple_bible_prompts_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
    
drum_loop_genres = [
    ("Drum Loop House", True),
    ("Drum Loop Techno", True),
    ("Drum Loop Trance", True),
    ("Drum Loop Dubstep", True),
    ("Drum Loop Drum & Bass", True),
    ("Drum Loop Jungle", True),
    ("Drum Loop Trap", True),
    ("Drum Loop Future Bass", True),
    ("Drum Loop Lo-fi", True),
    ("Drum Loop Chillhop", True),
    ("Drum Loop Boom Bap", True),
    ("Drum Loop Modern Trap", True),
    ("Drum Loop R&B", True),
    ("Drum Loop Afrobeats", True),
    ("Drum Loop Dancehall", True),
    ("Drum Loop Reggaeton", True),
    ("Drum Loop Classic Rock", True),
    ("Drum Loop Hard Rock", True),
    ("Drum Loop Grunge", True),
    ("Drum Loop Punk Rock", True),
    ("Drum Loop Pop Punk", True),
    ("Drum Loop Metal", True),
    ("Drum Loop Swing", True),
    ("Drum Loop Big Band", True),
    ("Drum Loop Bebop", True),
    ("Drum Loop Bossa Nova", True),
    ("Drum Loop Jazz-Fusion", True),
    ("Drum Loop Blues Shuffle", True),
    ("Drum Loop Funk", True),
    ("Drum Loop Neo-Soul", True),
    ("Drum Loop Motown", True),
    ("Drum Loop Disco", True),
    ("Drum Loop Samba", True),
    ("Drum Loop Reggae", True),
    ("Drum Loop Afro-Cuban", True),
    ("Drum Loop Middle Eastern", True),
    ("Drum Loop Indie Rock", True),
    ("Drum Loop Indie Pop", True),
    ("Drum Loop Synthpop", True),
    ("Drum Loop Electropop", True),
    ("Drum Loop Alternative", True),
    ("Drum Loop Shoegaze", True),
    ("Drum Loop Pop Ballad", True),
    ("Drum Loop IDM", True),
    ("Drum Loop Glitch Hop", True),
    ("Drum Loop Downtempo", True),
    ("Drum Loop Ambient", True),
    ("Drum Loop Minimalism", True),
    ("Drum Loop House", True),
    ("Drum Loop Techno", True),
    ("Drum Loop Trance", True),
    ("Drum Loop Dubstep", True),
    ("Drum & Bass", True),
    ("Drum Loop Jungle", True),
    ("Drum Loop Trap", True),
    ("Drum Loop Future Bass", True),
    ("Drum Loop Lo-fi", True),
    ("Drum Loop Chillhop", True),
    ("Drum Loop Boom Bap", True),
    ("Drum Loop Modern Trap", True),
    ("Drum Loop R&B", True),
    ("Drum Loop Afrobeats", True),
    ("Drum Loop Dancehall", True),
    ("Drum Loop Reggaeton", True),
    ("Drum Loop Classic Rock", True),
    ("Drum Loop Hard Rock", True),
    ("Drum Loop Grunge", True),
    ("Drum Loop Punk Rock", True),
    ("Drum Loop Pop Punk", True),
    ("Drum Loop Metal", True),
    ("Drum Loop Swing", True),
    ("Drum Loop Big Band", True),
    ("Drum Loop Bebop", True),
    ("Drum Loop Bossa Nova", True),
    ("Drum Loop Jazz-Fusion", True),
    ("Drum Loop Blues Shuffle", True),
    ("Drum Loop Funk", True),
    ("Drum Loop Neo-Soul", True),
    ("Drum Loop Motown", True),
    ("Drum Loop Disco", True),
    ("Drum Loop Samba", True),
    ("Drum Loop Reggae", True),
    ("Drum Loop Afro-Cuban", True),
    ("Drum Loop Middle Eastern", True),
    ("Drum Loop Indie Rock", True),
    ("Indie Pop Drum Loop", True),
    ("Drum Loop Synthpop", True),
    ("Drum Loop Electropop", True),
    ("Drum Loop Alternative", True),
    ("Drum Loop Shoegaze", True),
    ("Drum Loop Pop Ballad", True),
    ("Drum Loop IDM", True),
    ("Drum Loop Glitch Hop", True),
    ("Drum Loop Downtempo", True),
    ("Drum Loop Ambient", True),
    ("Drum Loop Minimalism", True),
    ("Drum Loop Experimental Hip Hop", True),
    ("Drum Loop Punk Rap", True),
    ("Drum Loop Noise", True),
    ("Drum Loop Industrial", True),
    ("Drum Loop Rap Rock", True),
    ("Drum Loop Electropunk", True),
    ("Drum Loop Avant-garde", True),
    ("Drum Loop Death Trips", True),
    ("Drum Loop Math Drums", True),
    ("Drum Loop Progressive Metal", True),
    ("Drum Loop Progressive Metal Djent", True),
    ("Drum Loop Progressive Metal Djent Screamo", True),
    ("Drum Loop Metalcore Djent Screamo", True),
    ("Drum Loop Fast Aggressive Phonk", True),
    ("Drum Loop Slow Ambient Drone", True),
    ("Drum Loop Heavy Metal", True),
    ("Drum Loop Fast Jazz Fusion", True),
    ("Drum Loop Slow Reggae", True),
    ("Drum Loop Heavy Ambient Drone", True),
    ("Drum Loop Fast Salsa", True),
    ("Drum Loop Fast Bluegrass", True),
    ("Drum Loop Fast Screamo", True),
    ("Drum Loop Fast Reggaeton", True),
    ("Drum Loop Slow Psychedelic Rock", True),
    ("Drum Loop Fast Techno", True),
    ("Drum Loop Slow R&B", True),
    ("Drum Loop Fast Thrash Metal", True),
    ("Drum Loop Heavy Dubstep", True),
    ("Drum Loop Heavy Industrial", True),
    ("Drum Loop Heavy Doom Metal", True),
    ("Drum Loop Fast Flamenco", True),
    ("Drum Loop Fast Drum and Bass", True),
    ("Drum Loop Heavy Sludge Metal", True),
    ("Drum Loop Slow Tango", True),
    ("Drum Loop Fast Garage Rock", True),
    ("Drum Loop Heavy Death Metal", True),
    ("Drum Loop Fast Punk Rock", True),
    ("Drum Loop Fast House", True),
    ("Drum Loop Minimalist Techno", True),
    ("Drum Loop Darkwave", True),
    ("Drum Loop Chiptune", True),
    ("Drum Loop Kpop", True),
    ("Drum Loop Math Rock", True),
    ("Drum Loop Vaporwave", True),
    ("Drum Loop Shoegaze", True),
    ("Drum Loop Lo-fi Hip Hop", True),
    ("Drum Loop Haunting Atmospheric Witch House", True),
    ("Drum Loop Fast Progressive House", True),
    ("Drum Loop Fantasy RPG OST", True),
    ("Drum Loop Baroque", True),
    ("Drum Loop Binaural Beats", True),
    ("Drum Loop Heavy Psyche", True),
    ("Drum Loop Upbeat Jazz", True),
    ("Drum Loop Burning Jazz", True),
    ("Drum Loop Video Game OST", True),
    ("Drum Loop Smooth Vaporwave Jazz Lo-fi Hip Hop", True),
    ("Drum Loop American Folk", True),
    ("Drum Loop Hip Hop 80-115 BPM", True),
    ("Drum Loop Juke/Footwork", True)
]


# Writing to file with error handling
drum_loop_genres_dump_file = f"{base_file_path}drum_loop_genres_dict.json"
try:
    with open(drum_loop_genres_dump_file, 'w') as drum_loop_genres_data_dump_file:
        json.dump(drum_loop_genres, drum_loop_genres_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    

drum_kits = [
    ("Standard Acoustic Kit", "Snare", "Bass Drum", "Toms", "Cymbals"),
    ("Jazz Drum Kit", "Smaller Bass Drum", "Ride Cymbal", "Snare", "Hi-Hats"),
    ("Rock Drum Kit", "Large Bass Drum", "Loud Snare", "Toms", "Crash Cymbals"),
    ("Metal Drum Kit", "Double Bass Pedals", "Multiple Toms", "China Cymbals", "Splash Cymbals"),
    ("Funk Drum Kit", "Tight Snare", "Quick Hi-Hats", "Smaller Toms", "Ride Cymbal"),
    ("Blues Drum Kit", "Warm Snare", "Minimal Cymbals", "Bass Drum", "Toms"),
    ("Orchestral Drum Kit", "Timpani", "Bass Drum", "Snare", "Cymbals"),
    ("Country Drum Kit", "Crisp Snare", "Brushes", "Bass Drum", "Hi-Hats"),
    ("Electronic Drum Set", "Roland", "Alesis", "Yamaha", "Pads/Triggers"),
    ("Hybrid Drum Kit", "Acoustic Drums", "Electronic Pads", "Triggers", "Sound Module"),
    ("Sampling Pad Drum Kit", "Akai", "Roland SPD", "Pads", "Sample Triggers"),
    ("Trigger-based Drum Kit", "Triggers", "Acoustic Drums", "Sound Module", "Electronic Sounds"),
    ("Synth Drum Kit", "Analog", "Digital", "Modular Synth", "Drum Synth"),
    ("Analog Drum Machine", "Roland TR-808", "TR-909", "Bass Drum Synth", "Hi-Hats"),
    ("Digital Drum Machine", "Akai MPC", "Elektron Digitakt", "Samples", "Sequences"),
    ("World Percussion Kit", "Congas", "Bongos", "Djembes", "Cajón"),
    ("Latin Percussion Kit", "Timbales", "Cowbells", "Claves", "Bongos"),
    ("Brazilian Samba Kit", "Surdo", "Tamborim", "Pandeiro", "Agogô"),
    ("Afro-Cuban Kit", "Congas", "Claves", "Cowbells", "Bongos"),
    ("Reggae Drum Kit", "Rim Clicks", "Off-beat Hi-Hats", "Snare", "Bass Drum"),
    ("Recording Studio Drum Kit", "Balanced Sound", "Dampened Heads", "Snare", "Bass Drum"),
    ("Compact/Cocktail Drum Kit", "Small Bass Drum", "Snare", "Hi-Hats", "Crash Cymbal"),
    ("Travel Drum Kit", "Collapsible", "Lightweight", "Snare", "Bass Drum"),
    ("Quiet Practice Kit", "Mesh Heads", "Rubber Pads", "Silent Cymbals", "Bass Pedal"),
    ("Brushes Kit", "Snare with Brushes", "Hi-Hats", "Bass Drum", "Ride Cymbal"),
    ("Minimal Drum Kit", "Bass Drum", "Snare", "Hi-Hat", "Crash Cymbal"),
    ("Custom Drum Kit", "Exotic Wood", "Hand-built", "Custom Finish", "Unique Hardware"),
    ("Vintage Drum Kit", "Old Shells", "Vintage Tone", "Snare", "Bass Drum"),
    ("Double Bass Drum Kit", "Two Bass Drums", "Toms", "Snare", "Cymbals"),
    ("Open Tuning Drum Kit", "Higher-tuned Toms", "Bass Drum", "Snare", "Cymbals")
]

# Writing to file with error handling
drum_kits_dump_file = f"{base_file_path}drum_kits_dict.json"
try:
    with open(drum_kits_dump_file, 'w') as drum_kits_data_dump_file:
        json.dump(drum_kits, drum_kits_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)


percussion_instruments = [
    ("Snare Drum", "Traditional", "Drums", "Membranophones"),
    ("Bass Drum", "Traditional", "Drums", "Membranophones"),
    ("Rack Tom", "Traditional", "Drums", "Membranophones"),
    ("Floor Tom", "Traditional", "Drums", "Membranophones"),
    ("Concert Bass Drum", "Concert", "Drums", "Membranophones"),
    ("Djembe", "West African Drum", "Drums", "Membranophones"),
    ("Cajón", "Box Drum", "Drums", "Membranophones"),
    ("Bongos", "Latin Percussion", "Drums", "Membranophones"),
    ("Congas", "Cuban Drum", "Drums", "Membranophones"),
    ("Tabla", "Indian Percussion", "Drums", "Membranophones"),
    ("Doumbek", "Middle Eastern Drum", "Drums", "Membranophones"),
    ("Handpan", "Hang Drum", "Drums", "Membranophones"),
    ("Frame Drum", "Traditional", "Drums", "Membranophones"),
    ("Timpani", "Orchestral Drum", "Drums", "Membranophones"),
    ("Taiko Drums", "Japanese Drum", "Drums", "Membranophones"),
    ("Talking Drum", "Dundun", "Drums", "Membranophones"),
    ("Octobans", "Extended Tom Drums", "Drums", "Membranophones"),
    ("Rototoms", "Tunable Drum", "Drums", "Membranophones"),
    ("Surdo", "Brazilian Bass Drum", "Drums", "Membranophones"),
    ("Pandeiro", "Brazilian Tambourine", "Drums", "Membranophones"),
    ("Timbales", "Cuban Drums", "Drums", "Membranophones"),
    ("Kanjira", "South Indian Frame Drum", "Drums", "Membranophones"),
    ("Bodhrán", "Irish Frame Drum", "Drums", "Membranophones"),
    ("Hi-Hats", "Traditional", "Cymbals", "Idiophones"),
    ("Crash Cymbal", "Traditional", "Cymbals", "Idiophones"),
    ("Ride Cymbal", "Traditional", "Cymbals", "Idiophones"),
    ("Splash Cymbal", "Small Cymbal", "Cymbals", "Idiophones"),
    ("China Cymbal", "Trashy Sounding", "Cymbals", "Idiophones"),
    ("Bell Cymbal", "Focused Sound", "Cymbals", "Idiophones"),
    ("Swish Cymbal", "Wide Sound", "Cymbals", "Idiophones"),
    ("Finger Cymbals", "Zills", "Cymbals", "Idiophones"),
    ("Gong", "Traditional", "Gongs and Bells", "Idiophones"),
    ("Tam-tam", "Flat Gong", "Gongs and Bells", "Idiophones"),
    ("Agogô Bells", "West African", "Gongs and Bells", "Idiophones"),
    ("Bell Tree", "Chime Tree", "Gongs and Bells", "Idiophones"),
    ("Cowbell", "Traditional", "Gongs and Bells", "Idiophones"),
    ("Almglocken", "Tuned Cowbells", "Gongs and Bells", "Idiophones"),
    ("Hand Bells", "Orchestral", "Gongs and Bells", "Idiophones"),
    ("Temple Blocks", "Orchestral", "Gongs and Bells", "Idiophones"),
    ("Crotales", "Antique Cymbals", "Gongs and Bells", "Idiophones"),
    ("Triangle", "Traditional", "Small Percussive", "Idiophones"),
    ("Woodblock", "Traditional", "Small Percussive", "Idiophones"),
    ("Claves", "Traditional", "Small Percussive", "Idiophones"),
    ("Castanets", "Spanish", "Small Percussive", "Idiophones"),
    ("Maracas", "Latin Percussion", "Small Percussive", "Idiophones"),
    ("Guiro", "Latin Percussion", "Small Percussive", "Idiophones"),
    ("Vibraslap", "Percussive Sound", "Small Percussive", "Idiophones"),
    ("Cabasa", "Latin Percussion", "Small Percussive", "Idiophones"),
    ("Shakers", "Traditional", "Small Percussive", "Idiophones"),
    ("Rainstick", "Ambient", "Small Percussive", "Idiophones"),
    ("Flexatone", "Unique Sound", "Small Percussive", "Idiophones"),
    ("Slapstick", "Whip", "Small Percussive", "Idiophones"),
    ("Chimes", "Tubular Bells", "Chimes and Resonant", "Idiophones"),
    ("Mark Tree", "Wind Chimes", "Chimes and Resonant", "Idiophones"),
    ("Glockenspiel", "Orchestral", "Chimes and Resonant", "Idiophones"),
    ("Xylophone", "Orchestral", "Chimes and Resonant", "Idiophones"),
    ("Marimba", "Orchestral", "Chimes and Resonant", "Idiophones"),
    ("Vibraphone", "Jazz", "Chimes and Resonant", "Idiophones"),
    ("Steelpan", "Caribbean", "Chimes and Resonant", "Idiophones"),
    ("Electronic Drum Pads", "Roland SPD-SX", "Electronic Percussion", "Pads"),
    ("Trigger Pads", "Electronic", "Electronic Percussion", "Triggers"),
    ("Drum Machines", "TR-808", "Electronic Percussion", "Akai MPC"),
    ("Hybrid Kits", "Acoustic and Electronic", "Electronic Percussion", "Modules"),
    ("Synth Drums", "Analog and Digital", "Electronic Percussion", "Synthesizers"),
    ("Tambourine", "Traditional", "Miscellaneous", "Idiophones"),
    ("Ocean Drum", "Ambient", "Miscellaneous", "Membranophones"),
    ("Log Drum", "Wooden", "Miscellaneous", "Idiophones"),
    ("Thunder Sheet", "Special Effect", "Miscellaneous", "Idiophones"),
    ("Spring Drum", "Special Effect", "Miscellaneous", "Membranophones"),
    ("Bamboo Wind Chimes", "Traditional", "Miscellaneous", "Idiophones"),
    ("Anklung", "Indonesian", "Miscellaneous", "Idiophones"),
    ("Slit Drum", "African", "Miscellaneous", "Idiophones"),
    ("Bullroarer", "Indigenous", "Miscellaneous", "Aerophones")
]

# Writing to file with error handling
percussion_instruments_dump_file = f"{base_file_path}percussion_instruments_dict.json"
try:
    with open(percussion_instruments_dump_file, 'w') as percussion_instruments_data_dump_file:
        json.dump(percussion_instruments, percussion_instruments_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

#exclude non percussion instruments
anti_percussion_instruments = [
    "guitar",
    "piano",
    "bass guitar",
    "horns",
    "winds",
    "vocals",
    "strings",
    "pads",
    "synths",
    "woodwinds",
    "brass",
    "organ",
    "accordion",
    "harp"
]

# Writing to file with error handling
anti_percussion_instruments_dump_file = f"{base_file_path}anti_percussion_instruments_dict.json"
try:
    with open(anti_percussion_instruments_dump_file, 'w') as anti_percussion_instruments_data_dump_file:
        json.dump(anti_percussion_instruments, anti_percussion_instruments_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

#exclude pop genres
# Pop, Electropop, Synthpop, Indie Pop, K-pop, J-pop, Dance-pop, Art Pop, Teen Pop, Hyperpop, Bubblegum Pop, Dream Pop, Power Pop, Pop Rock, Alternative Pop, Soft Pop, Pop Punk, Country Pop, Chamber Pop, Jazz Pop
#exclude_pop_genres_prompt = ["pop", "electropop", "synthpop", "indie pop", "K-pop", "J-pop", "dance-pop", "art pop", "teen pop", "hyperpop"]
exclude_pop_genres_prompt = ["pop", "electropop", "synthpop", "indie pop", "K-pop", "J-pop", "dance-pop", "art pop", "teen pop", "hyperpop", "bubblegum pop", "dream pop", "power pop", "pop rock", "alternative pop", "soft pop", "pop punk", "country pop", "chamber pop", "jazz pop"]


# Writing to file with error handling
exclude_pop_genres_dump_file = f"{base_file_path}exclude_pop_genres_dict.json"
try:
    with open(exclude_pop_genres_dump_file, 'w') as exclude_pop_genres_data_dump_file:
        json.dump(exclude_pop_genres_prompt, exclude_pop_genres_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

#concerto variants
concerto_variants = [
  {
    "name": "Solo Concerto",
    "soloists": 1,
    "ensemble": "Orchestral",
    "description": "A single instrument with orchestral accompaniment"
  },
  {
    "name": "Double Concerto",
    "soloists": 2,
    "ensemble": "Orchestral",
    "description": "Two solo instruments with orchestra"
  },
  {
    "name": "Triple Concerto",
    "soloists": 3,
    "ensemble": "Orchestral",
    "description": "Three solo instruments with orchestra"
  },
  {
    "name": "Concerto Grosso",
    "soloists": 5,
    "ensemble": "Baroque Ensemble",
    "description": "A Baroque form with a group of solo instruments (the concertino) contrasted with the full ensemble (the ripieno)"
  },
  {
    "name": "Sinfonia Concertante",
    "soloists": 5,
    "ensemble": "Symphony",
    "description": "A hybrid between symphony and concerto with multiple soloists (often wind instruments)"
  },
  {
    "name": "Chamber Concerto",
    "soloists": 5,
    "ensemble": "Chamber Ensemble",
    "description": "A smaller ensemble replaces the full orchestra, with one or more solo instruments highlighted"
  },
  {
    "name": "Baroque Concerto",
    "soloists": 5,
    "ensemble": "Baroque Orchestra",
    "description": "Features polyphonic textures and ornamentation, typical of the Baroque era"
  },
  {
    "name": "Classical Concerto",
    "soloists": 5,
    "ensemble": "Classical Orchestra",
    "description": "Emphasizes clear forms such as sonata form within movements"
  },
  {
    "name": "Romantic Concerto",
    "soloists": 5,
    "ensemble": "Romantic Orchestra",
    "description": "Highly virtuosic with emotional expressiveness, characteristic of the Romantic period"
  },
  {
    "name": "20th-Century & Contemporary Concerto",
    "soloists": 5,
    "ensemble": "Orchestral or Experimental",
    "description": "Experiments with harmony, timbre, and non-traditional forms"
  },
  {
    "name": "Concertino",
    "soloists": 1,
    "ensemble": "Orchestral or Piano Accompaniment",
    "description": "A shorter and simpler form of concerto, often written for students"
  },
  {
    "name": "Concertante Works",
    "soloists": 5,
    "ensemble": "Variable",
    "description": "Works that emphasize the interaction of multiple instruments with the orchestra"
  }
]

# Writing to file with error handling
concerto_variants_dump_file = f"{base_file_path}concerto_variants_dict.json"
try:
    with open(concerto_variants_dump_file, 'w') as concerto_variants_data_dump_file:
        json.dump(concerto_variants, concerto_variants_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)


concerto_instruments_by_family = [
  {
    "family": "String Instruments",
    "instruments": [
      {
        "name": "Violin",
        "example": "Tchaikovsky, Mendelssohn"
      },
      {
        "name": "Viola",
        "example": "Bartók, Walton"
      },
      {
        "name": "Cello",
        "example": "Dvořák, Elgar"
      },
      {
        "name": "Double Bass",
        "example": "Bottesini"
      }
    ]
  },
  {
    "family": "Keyboard Instruments",
    "instruments": [
      {
        "name": "Piano",
        "example": "Mozart, Rachmaninoff"
      },
      {
        "name": "Harpsichord",
        "example": "J.S. Bach"
      },
      {
        "name": "Organ",
        "example": "Handel, Poulenc"
      }
    ]
  },
  {
    "family": "Woodwind Instruments",
    "instruments": [
      {
        "name": "Flute",
        "example": "Mozart, Ibert"
      },
      {
        "name": "Oboe",
        "example": "Marcello, Strauss"
      },
      {
        "name": "Clarinet",
        "example": "Mozart, Nielsen"
      },
      {
        "name": "Bassoon",
        "example": "Vivaldi, Mozart"
      },
      {
        "name": "Saxophone",
        "example": "Glazunov, Villa-Lobos"
      }
    ]
  },
  {
    "family": "Brass Instruments",
    "instruments": [
      {
        "name": "Trumpet",
        "example": "Haydn, Hummel"
      },
      {
        "name": "Horn",
        "example": "Mozart, Strauss"
      },
      {
        "name": "Trombone",
        "example": "Alto Trombone Concerto by Albrechtsberger"
      },
      {
        "name": "Tuba",
        "example": "Vaughan Williams"
      }
    ]
  },
  {
    "family": "Percussion Instruments",
    "instruments": [
      {
        "name": "Marimba",
        "example": "Ney Rosauro, Séjourné"
      },
      {
        "name": "Vibraphone",
        "example": ""
      },
      {
        "name": "Timpani",
        "example": "Werner Thärichen’s Timpani Concerto"
      }
    ]
  }
]

    
instrument_families_by_ensemble = [
  {
    "ensemble": "Orchestral",
    "families": [
      "Strings",
      "Woodwinds",
      "Brass",
      "Percussion",
      "Keyboard"
    ]
  },
  {
    "ensemble": "Baroque Ensemble",
    "families": [
      "Strings",
      "Woodwinds",
      "Harpsichord (Keyboard)",
      "Occasional Percussion"
    ]
  },
  {
    "ensemble": "Symphony",
    "families": [
      "Strings",
      "Woodwinds",
      "Brass",
      "Percussion",
      "Keyboard (Piano, Celesta, or Organ)"
    ]
  },
  {
    "ensemble": "Chamber Ensemble",
    "families": [
      "Strings",
      "Woodwinds",
      "Occasional Brass",
      "Percussion (Optional)",
      "Keyboard (Piano, Harpsichord, or Organ)"
    ]
  },
  {
    "ensemble": "Baroque Orchestra",
    "families": [
      "Strings",
      "Woodwinds",
      "Harpsichord or Organ (Keyboard)",
      "Occasional Brass (Natural Trumpet, Horn)",
      "Occasional Percussion"
    ]
  },
  {
    "ensemble": "Classical Orchestra",
    "families": [
      "Strings",
      "Woodwinds",
      "Brass",
      "Percussion",
      "Keyboard (Fortepiano or Harpsichord)"
    ]
  },
  {
    "ensemble": "Romantic Orchestra",
    "families": [
      "Strings",
      "Woodwinds",
      "Brass",
      "Percussion",
      "Keyboard (Piano or Organ)"
    ]
  }
]


instrument_family_string = [
      {
        "name": "Violin",
        "example": "Tchaikovsky, Mendelssohn"
      },
      {
        "name": "Viola",
        "example": "Bartók, Walton"
      },
      {
        "name": "Cello",
        "example": "Dvořák, Elgar"
      },
      {
        "name": "Double Bass",
        "example": "Bottesini"
      }
    ]
    
 # Writing to file with error handling
concerto_instrument_family_string_dump_file = f"{base_file_path}concerto_instrument_family_string_dict.json"
try:
    with open(concerto_instrument_family_string_dump_file, 'w') as concerto_instrument_family_string_data_dump_file:
        json.dump(instrument_family_string, concerto_instrument_family_string_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

instrument_family_keys = [
      {
        "name": "Piano",
        "example": "Mozart, Rachmaninoff"
      },
      {
        "name": "Harpsichord",
        "example": "J.S. Bach"
      },
      {
        "name": "Organ",
        "example": "Handel, Poulenc"
      }
    ]
    
 # Writing to file with error handling
concerto_instrument_family_keys_dump_file = f"{base_file_path}concerto_instrument_family_keys_dict.json"
try:
    with open(concerto_instrument_family_keys_dump_file, 'w') as concerto_instrument_family_keys_data_dump_file:
        json.dump(instrument_family_keys, concerto_instrument_family_keys_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

instrument_family_keys = [
      {
        "name": "Piano",
        "example": "Mozart, Rachmaninoff"
      },
      {
        "name": "Harpsichord",
        "example": "J.S. Bach"
      },
      {
        "name": "Organ",
        "example": "Handel, Poulenc"
      }
    ]
    
 # Writing to file with error handling
concerto_instrument_family_keys_dump_file = f"{base_file_path}concerto_instrument_family_keys_dict.json"
try:
    with open(concerto_instrument_family_keys_dump_file, 'w') as concerto_instrument_family_keys_data_dump_file:
        json.dump(instrument_family_keys, concerto_instrument_family_keys_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

instrument_family_woodwinds = [
      {
        "name": "Flute",
        "example": "Mozart, Ibert"
      },
      {
        "name": "Oboe",
        "example": "Marcello, Strauss"
      },
      {
        "name": "Clarinet",
        "example": "Mozart, Nielsen"
      },
      {
        "name": "Bassoon",
        "example": "Vivaldi, Mozart"
      },
      {
        "name": "Saxophone",
        "example": "Glazunov, Villa-Lobos"
      }
    ]
    
 # Writing to file with error handling
concerto_instrument_family_woodwinds_dump_file = f"{base_file_path}concerto_instrument_family_woodwinds_dict.json"
try:
    with open(concerto_instrument_family_woodwinds_dump_file, 'w') as concerto_instrument_family_woodwinds_data_dump_file:
        json.dump(instrument_family_woodwinds, concerto_instrument_family_woodwinds_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

instrument_family_brass = [
      {
        "name": "Trumpet",
        "example": "Haydn, Hummel"
      },
      {
        "name": "Horn",
        "example": "Mozart, Strauss"
      },
      {
        "name": "Trombone",
        "example": "Alto Trombone Concerto by Albrechtsberger"
      },
      {
        "name": "Tuba",
        "example": "Vaughan Williams"
      }
]

concerto_instrument_family_brass_dump_file = f"{base_file_path}concerto_instrument_family_brass_dict.json"
try:
    with open(concerto_instrument_family_brass_dump_file, 'w') as concerto_instrument_family_brass_data_dump_file:
        json.dump(instrument_family_brass, concerto_instrument_family_brass_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

instrument_family_percussion = [
      {
        "name": "Marimba",
        "example": "Ney Rosauro, Séjourné"
      },
      {
        "name": "Vibraphone",
        "example": ""
      },
      {
        "name": "Timpani",
        "example": "Werner Thärichen’s Timpani Concerto"
      }
]

concerto_instrument_family_percussion_dump_file = f"{base_file_path}concerto_instrument_family_percussion_dict.json"
try:
    with open(concerto_instrument_family_percussion_dump_file, 'w') as concerto_instrument_family_percussion_data_dump_file:
        json.dump(instrument_family_percussion, concerto_instrument_family_percussion_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
