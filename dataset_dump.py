import json

base_file_path = 'datasets/'

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
tempo_bpm_dump_file = f"{base_file_path}tempos.json"
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
music_key_dump_file = f"{base_file_path}music_keys.json"
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
bible_book_dump_file = f"{base_file_path}bible_books.json"
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
    ("Handpan"),
    ("low-pass sweep"),
    ("high-pass sweep"),
    ("band-pass sweep"),
    ("low-pass filter"),
    ("high-pass filter"),
    ("band-pass filter")
]

# Writing to file with error handling
instrument_dump_file = f"{base_file_path}instruments.json"
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
vocalists_dump_file = f"{base_file_path}vocalists.json"
try:
    with open(vocalists_dump_file, 'w') as vocalists_data_dump_file:
        json.dump(vocalists, vocalists_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)
    
# Your list of genres (each item is a string)
song_genres = [
    "Music Theater",
    "zydeco",
    "experimental hip hop",
    "punk rap",
    "noise",
    "industrial",
    "rap rock",
    "electropunk",
    "Avant-garde",
    "death trips",
    "math drums",
    "drum and bass",
    "ambient drone",
    "progressive metal djent",
    "Tech House",
    "reggaeton",
    "heavy thrash metal",
    "bolero",
    "heavy industrial",
    "IDM (Intelligent Dance Music)",
    "ranchera",
    "breakbeat",
    "Jungle Drum n Bass",
    "lo-fi indie",
    "60s Proto Metal",
    "Electronic Drum n Bass",
    "smooth fusion jazz",
    "Grime 140 BPM",
    "contemporary classical",
    "Avant Garde",
    "heavy sludge metal",
    "Jazz Fusion",
    "Freestyle Electro",
    "Freestyle Dance Music",
    "minimalist techno",
    "Hip Hop 80-115 BPM",
    "lo-fi hip hop",
    "krautrock",
    "progressive metal",
    "progressive house",
    "Math Rock",
    "Progressive House",
    "Soundtrack",
    "psychedelic rock",
    "Oldskool Latin Freestyle",
    "vaporwave lo-fi hip-hop",
    "corrido",
    "american folk",
    "celtic guitar melody",
    "Math Prog Rock",
    "haunting witch house",
    "symphonic metal",
    "neofolk",
    "Hardstyle",
    "glitch",
    "Neurofunk Drum n Bass",
    "Neurofunk 170-180 BPM",
    "Fusion Freestyle",
    "heavy death metal",
    "American hip hop",
    "Liquid Drum n Bass",
    "Electronic Dance",
    "Heavy Blues",
    "contemporary worship",
    "Early 90s Freestyle Dance",
    "J-Pop",
    "chiptune",
    "shoegaze",
    "heart throb freestyle",
    "Space music",
    "Acid Rock",
    "mongolian folk metal",
    "slow indie rock",
    "gospel hymn",
    "Triphop",
    "christian worship",
    "Freestyle EDM",
    "garage rock",
    "Drum n Bass BPM 160-180",
    "lo-fi hip-hop",
    "middle-eastern",
    "Progressive Trance",
    "ska",
    "disco",
    "Fusion House",
    "Electronic",
    "hardcore punk",
    " flamenco",
    "techno",
    "waltz",
    "salsa",
    "80s heart throb freestyle",
    "heavy doom metal",
    "Techstep Drum n Bass",
    "Freestyle Music Mix",
    "Early Metal",
    "Early 2000s Drum n Bass",
    "vaporwave",
    "post-rock",
    "Sambass Drum n Bass",
    "slow tango",
    "Chinese Classical folk",
    "Drum n Bass",
    "ranchera-Mariachi Fusion",
    "noise rock",
    "country folk",
    "grindcore",
    "Breakcore Drum n Bass",
    "Deep House",
    "bossa nova",
    "folk ballad",
    "witch house",
    "Trance",
    "trap",
    "Dubstep",
    "film score",
    "Drumstep",
    "banda",
    "chicano rap",
    "norteño",
    "classical acoustic guitar",
    "heavy dubstep",
    "mongolian folk",
    "darkwave",
    "kpop",
    "house",
    "hardstyle",
    "narcocorridos",
    "jazz fusion",
    "Jazz-funk",
    "classical celtic guitar",
    "huapango",
    "Christian hip hop",
    "wonky",
    "breakcore",
    "Club/Dance",
    "classical guitar melody",
    "future garage",
    "punk rock",
    "metal djent screamo",
    "EDM Techno",
    "Oldskool Freestyle Mix",
    "fast aggressive phonk",
    "Halftime Drum n Bass",
    "chillwave",
    "Hardstyle 150 BPM",
    "mariachi",
    "math rock",
    "Heavy Psyche",
    "EDM",
    "minimalism",
    "screamo",
    "slow blues",
    "Jump Up Drum n Bass",
    "Hip Hop",
    "acid jazz",
    "Gospel Rap",
    "70s Proto Metal",
    "Hip Hop/Rap",
    "cumbia",
    "christian worship",
    "American Christian hip hop",
    "ambient Christian worship",
    "powernoise",
    "lo-fi house",
    "witch house",
    "metalcore djent screamo",
    "UK funky",
    "western",
    "Early 90s  Freestyle",
    "heavy metal",
    "bluegrass",
    "smooth vaporwave jazz",
    "Concert marches",
    "Oldskool Latin Freestyle",
    "soul",
    "Schranz",
    "hip-hop",
    "R&B",
    "Juke/Footwork",
    "Intelligent Drum n Bass",
    "electroswing",
    "bluegrass gospel",
    "New Jersey Hip Hop",
    "Oldschool jungle",
    "chamber music",
    "son jarocho",
    "reggae",
    "ambient drone",
    "NYC Hip Hop",
    "jungle",
    "Psychedelic",
    "electronic dance music",
    "Acid Techno",
    "UK garage/2-step",
    "Motown",
    "Mo Town",
    "Soulful Motown",
    "alternative rock",
    "art rock",
    "experimental rock",
    "art pop",
    "Britpop",
    "Progressive Rock",
    "Post-Rock",
    "gospel soul",
    "A Capella",
    "Upbeat Jazz",
    "Burning Jazz",
    "Burning Jazz, Liquid Drum and Bass",
    "Video Game OST",
    "Video Game Original Sound Track",
    "Cinematic Score",
    "Orchestral, Ambient, atmospheric",
    "Fantasy RPG Game OST",
    "Fantasy RPG Video Game OST",
    "RPG Video Game Original Sound Track",
    "Fantasy RPG Original Sound Track",
    "Suite bergamasque",
    "Baroque",
    "Baroque, Complex polyphony, ornate melodies",
    "Classical",
    "Romantic",
    "Impressionist",
    "Expressionist",
    "Modernism",
    "Neoclassicism",
    "Serialism",
    "Avant-Garde",
    "Renaissance",
    "Chamber Music",
    "Opera",
    "Choral Music",
    "Programmatic Music",
    "Minimalism",
    "Baroque, Complex polyphony, ornate melodies",
    "Classical, structured forms, sonata, symphony, homophony.",
    "Classical, structured forms, sonata, homophony.",
    "Classical, structured forms, symphony, homophony.",
    "Romantic, Emotional expression, expanded orchestra, programmatic music, lyrical melodies",
    "Romantic, Emotional expression, expanded orchestra",
    "Romantic, programmatic music, lyrical melodies",
    "Impressionist, atmospheric, ambiguous harmonies, tone color",
    "Expressionist, Intense emotion, dissonance, atonal, fragmented melodies",
    "Modernism, dissonant, abstract.",
    "Serialism, twelve-tone technique, mathematical",
    "Minimalism, simple motifs, meditative quality",
    "Avant-Garde, unconventional, Experimental",
    "Renaissance, Polyphonic, modal, vocal",
    "Choral Music, choir, religious, ceremonial",
    "Programmatic Music",
    "binaural beats",
    "binaural beats, theta wave",
    "binaural beats, beta wave",
    "binaural beats, alpha wave",
    "binaural beats, gamma wave",
    "Minimalist Soundscapes",
    "Minimalist Soundscapes",
    "Minimalist Soundscapes",
    "Corporate or Upbeat Instrumental",
    "Corporate Instrumental",
    "Upbeat Instrumental",
    "Corporate Upbeat",
    "Corporate or Upbeat Instrumental",
    "Chillhop",
    "Futuristic Sound Design",
    "Percussive Solos",
    "Drum Solos",
    "Bass Solos",
    "Guitar Solos",
    "Keyboard Solos",
    "Synth Solos",
    "String Solos",
    "Brass Solos",
    "Woodwind Solos",
    "Hip Hop Drum Solos",
    "Rock Drum Solos",
    "Pop Drum Solos",
    "Country Drum Solos",
    "Blues Drum Solos",
    "Jazz Drum Solos",
    "Reggae Drum Solos",
    "Soul Drum Solos",
    "Hip Hop Drum Loop",
    "Rock Drum Loop",
    "Pop Drum Loop",
    "Country Drum Loop",
    "Blues Drum Loop",
    "Jazz Drum Loop",
    "Reggae Drum Loop",
    "Drum Loop",
    "Music Theater",
    "classical acoustic guitar",
    "experimental hip hop",
    "punk rap",
    "noise"
]

# Writing to file with error handling
song_genres_dump_file = f"{base_file_path}song_genres.json"
try:
    with open(song_genres_dump_file, 'w') as song_genres_data_dump_file:
        json.dump(song_genres, song_genres_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

  
# list of adjectives
adjectives = [
    "fast",
    "slow",
    "aggressive",
    "reflective",
    "engaging",
    "uplifting",
    "soulful",
    "vibrant",
    "voices",
    "lo-fi",
    "jazz-infused beats",
    "warm",
    "rich basslines",
    "jazzy guitar riffs",
    "soft keys",
    "mellow synths",
    "smooth",
    "emotive vocals",
    "harmonies",
    "reverb",
    "echo",
    "dreamy",
    "atmospheric",
    "deep brass fanfares",
    "excited",
    "crescendoing",
    "upbeat",
    "lush strings",
    "soft piano motifs",
    "flowing woodwind lines",
    "minimalist film score",
    "ambient orchestral soundscape",
    "90s",
    "80s",
    "70s",
    "60s",
    "50s",
    "40s",
    "30s",
    "20s",
    "2000s",
    "pulsating",
    "throbbing",
    "resonant",
    "booming",
    "whispering",
    "staccato",
    "legato",
    "syncopated",
    "percussive",
    "soaring",
    "ethereal",
    "gritty",
    "simmering",
    "vibrating",
    "rushing",
    "crisp",
    "dynamic",
    "explosive",
    "smoky",
    "wailing",
    "murmuring",
    "chiming",
    "tingling",
    "bouncing",
    "rumbling",
    "undulating",
    "sizzling",
    "sparkling",
    "jarring",
    "subdued",
    "low-pass sweep",
    "high-pass sweep",
    "band-pass sweep",
    "low-pass filter",
    "high-pass filter",
    "band-pass filter"
]

# Writing to file with error handling
adjectives_dump_file = f"{base_file_path}adjectives.json"
try:
    with open(adjectives_dump_file, 'w') as adjectives_data_dump_file:
        json.dump(adjectives, adjectives_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)

lyrical_adjectives = [
    "uplifting hymns",
    "darker, bass-heavy beats",
    "acoustic guitar and live audience sounds",
    "trumpets and heavenly hosts sounds",
    "studio sounds with energetic drums and loops",  
    "music crescendoing",
    "energetic drums and loops",
    "upbeat music plays in the background",
    "gradually building in intensity as the narrator speaks",
    "Fade out with music crescendoing",
    "upbeat music plays in the background",
    "gradually building in intensity as the narrator speaks",
    "Fade out with music crescendoing",
    "soulful vocals play"
  ]




# Writing to file with error handling
lyrical_adjectives_dump_file = f"{base_file_path}lyrical_adjectives.json"
try:
    with open(lyrical_adjectives_dump_file, 'w') as lyrical_adjectives_data_dump_file:
        json.dump(lyrical_adjectives, lyrical_adjectives_data_dump_file)
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

random_mnemonic_topics = [
    "Gödel's incompleteness theorems",
    "Fibonacci sequence",
    "Turing Machines",
    "Boyce-Codd Normal Form (BCNF)",
    "Relational Algebra",
    "Quantum Entanglement",
    "Eigenvalues and Eigenvectors",
    "Thermodynamic Entropy",
    "Bayesian Inference",
    "Heisenberg Uncertainty Principle",
    "Graph Isomorphism",
    "Markov Chains",
    "Euler's Formula",
    "Maxwell's Equations",
    "Schrödinger Equation",
    "Neural Networks",
    "Boolean Algebra",
    "Monty Hall Problem",
    "Chaos Theory",
    "General Relativity",
    "P vs NP Problem",
    "Dijkstra's Algorithm",
    "Fourier Transform",
    "Lagrangian Mechanics",
    "Cryptographic Hash Functions",
    "Cantor's Diagonal Argument",
    "Zermelo-Fraenkel Set Theory",
    "Combinatorial Optimization",
    "Newton's Laws of Motion",
    "Laplace Transform",
    "Poisson Distribution",
    "Game Theory",
    "Mandelbrot Set",
    "Fermat's Last Theorem",
    "Cellular Automata",
    "Ramanujan's Summation",
    "Gaussian Elimination",
    "Noether's Theorem",
    "Quantum Superposition",
    "DNA Transcription",
    "Molecular Orbital Theory",
    "Kepler's Laws of Planetary Motion",
    "Topological Sorting",
    "Big-O Notation",
    "Bose-Einstein Condensate",
    "Shannon Entropy",
    "Kolmogorov Complexity",
    "Huffman Coding",
    "Lorenz Attractor",
    "Poincaré Conjecture",
    "Symplectic Geometry",
    "Feynman Path Integral",
    "Navier-Stokes Equations",
    "Mersenne Primes",
    "Tarski's Fixed Point Theorem",
    "Electromagnetic Induction",
    "Lindemann-Weierstrass Theorem",
    "Quantum Field Theory",
    "Catalan Numbers",
    "Möbius Transformation",
    "Cauchy-Schwarz Inequality",
    "Pell's Equation",
    "Quantum Chromodynamics",
    "Central Limit Theorem",
    "Self-Avoiding Walk",
    "Graph Coloring Problem",
    "Maximum Flow Algorithm",
    "Planck's Constant",
    "Helmholtz Free Energy",
    "Legendre Polynomials",
    "Boltzmann Distribution",
    "Ricci Tensor",
    "Radon Transform",
    "Viterbi Algorithm",
    "Bessel Functions",
    "Fractals",
    "Curry-Howard Correspondence",
    "Erdős Number",
    "Homotopy Theory",
    "Cauchy Integral Formula",
    "Quantum Tunneling",
    "Information Gain",
    "Van der Waals Equation",
    "Curie Temperature",
    "Tautology in Propositional Logic",
    "Zeno's Paradoxes",
    "Adaptive Signal Processing",
    "Singular Value Decomposition (SVD)",
    "Dynamic Programming",
    "Bayesian Networks",
    "Kolmogorov-Smirnov Test",
    "Lattice-Based Cryptography",
    "Inverse Kinematics",
    "Riemann Hypothesis",
    "Hyperbolic Geometry",
    "Gödel Numbering",
    "Coxeter Groups",
    "Neutrino Oscillation",
    "Ergodic Theory",
    "Spin-Statistics Theorem",
    "Quantum Error Correction",
    "Generalized Stokes' Theorem",
    "Prehistoric Archaeology",
    "Historical Archaeology",
    "Classical Archaeology",
    "Underwater Archaeology",
    "Ethnoarchaeology",
    "Environmental Archaeology",
    "Bioarchaeology",
    "Zooarchaeology",
    "Geoarchaeology",
    "Experimental Archaeology",
    "Industrial Archaeology",
    "Cognitive Archaeology",
    "Paleoanthropology",
    "Primatology",
    "Human Genetics",
    "Forensic Anthropology",
    "Human Biology",
    "Dental Anthropology",
    "Anthropological Epidemiology",
    "Evolutionary Medicine",
    "Growth and Development Anthropology",
    "Descriptive Linguistics",
    "Historical Linguistics",
    "Sociolinguistics",
    "Ethnolinguistics",
    "Psycholinguistics",
    "Language Documentation",
    "Cognitive Linguistics",
    "Paleolinguistics",
    "Ethnography",
    "Ethnology",
    "Medical Anthropology",
    "Economic Anthropology",
    "Political Anthropology",
    "Religious Anthropology",
    "Urban Anthropology",
    "Environmental Anthropology",
    "Cognitive Anthropology",
    "Applied Anthropology",
    "Visual Anthropology",
    "Gender and Sexuality Anthropology",
    "Ontology",
    "Cosmology",
    "Philosophy of Time and Space",
    "Modality",
    "Philosophy of Mind",
    "Theories of Knowledge",
    "Skepticism",
    "Justification and Belief",
    "Social Epistemology",
    "Philosophy of Perception",
    "Normative Ethics",
    "Meta-Ethics",
    "Applied Ethics",
    "Moral Psychology",
    "Symbolic Logic",
    "Informal Logic",
    "Modal Logic",
    "Mathematical Logic",
    "Theories of Justice",
    "Rights and Liberty",
    "Democracy",
    "Marxism",
    "Liberalism",
    "Libertarianism",
    "Theories of Beauty",
    "Art Criticism",
    "Aesthetic Experience",
    "Scientific Methodology",
    "Realism vs. Anti-Realism",
    "Philosophy of Physics",
    "Philosophy of Biology",
    "Philosophy of Mathematics",
    "Arguments for and Against God's Existence",
    "Nature of Faith and Reason",
    "Religious Language",
    "Problem of Evil",
    "Meaning and Reference",
    "Speech Act Theory",
    "Linguistic Determinism",
    "Mind-Body Problem",
    "Theories of Consciousness",
    "Artificial Intelligence",
    "Existential Themes",
    "Phenomenological Method",
    "Bioethics",
    "Environmental Philosophy",
    "Philosophy of Education",
    "Philosophy of Law",
    "Ancient History",
    "Medieval History",
    "Early Modern History",
    "Modern History",
    "Contemporary History",
    "World History",
    "European History",
    "American History",
    "Asian History",
    "African History",
    "Middle Eastern History",
    "Latin American History",
    "Political History",
    "Military History",
    "Economic History",
    "Social History",
    "Cultural History",
    "Religious History",
    "Intellectual History",
    "Legal History",
    "Diplomatic History",
    "Historiography",
    "Environmental History",
    "History of Science and Technology",
    "Gender and Women's History",
    "Labor History",
    "Urban History",
    "Colonial and Postcolonial History",
    "Transnational History"
]

# Writing to file with error handling
random_mnemonic_topics_dump_file = f"{base_file_path}random_mnemonic_topics_dict.json"
try:
    with open(random_mnemonic_topics_dump_file, 'w') as random_mnemonic_topics_data_dump_file:
        json.dump(random_mnemonic_topics, random_mnemonic_topics_data_dump_file)
except IOError as e:
    print("Error writing to file:", e)