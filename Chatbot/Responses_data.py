Responses = {
    # Greetings
    ("hello", "hi", "hey", "greetings"): ["Hi there!", "Hello! How can I help?", "Hey! What's up?", "Greetings! Nice to see you!", "Hi! How are you doing?"],
    ("good morning", "morning", "gm"): ["Good morning!", "Morning! Hope you have a great day!", "Good morning! Ready to start the day?", "Morning sunshine!", "GM! Let's make today awesome!"],
    ("good afternoon", "afternoon", "good evening", "evening"): ["Good afternoon!", "Evening! How's your day been?", "Good evening to you!", "Afternoon! Hope you're doing well!", "Evening! Ready to relax?"],
    ("good night", "goodnight", "gn", "night"): ["Good night! Sleep well!", "Night! Sweet dreams!", "Good night! See you tomorrow!", "Sleep tight!", "Nighty night! Rest well!"],
    ("how are you", "how r u", "how are you doing", "how's it going"): ["I'm doing great, thanks!", "Pretty good! How about you?", "I'm awesome! Thanks for asking!", "Doing well! What about you?", "I'm fantastic! How are you?"],
    ("what's up", "whats up", "sup", "wassup"): ["Not much, you?", "Just chilling! What's up with you?", "Same old, same old! You?", "Just hanging out! What about you?", "Nothing much! How about you?"],
    
    # Farewells
    ("bye", "goodbye", "see you", "catch you later"): ["Bye! Take care!", "See you later!", "Goodbye! Come back soon!", "Catch you later!", "Bye! Have a great day!"],
    ("talk to you later", "ttyl", "gotta go", "i have to go"): ["Sure! Talk soon!", "Alright, catch you later!", "No problem! See you!", "Okay! Take care!", "Sure thing! Bye for now!"],
    ("i'm leaving", "im leaving", "i'm off", "im off"): ["Okay! Safe travels!", "Alright! See you around!", "Take care! Bye!", "Have a good one!", "Catch you later!"],
    
    # Mood & Emotion - Happy
    ("i'm happy", "im happy", "feeling great", "i'm excited"): ["That's awesome!", "So glad to hear that!", "Yay! That's wonderful!", "Love the positive vibes!", "Your happiness is contagious!"],
    ("i'm so excited", "im so excited", "this is amazing", "i'm thrilled"): ["That's fantastic!", "I can feel your excitement!", "How exciting!", "Woohoo! That's great!", "Amazing! Tell me more!"],
    ("best day ever", "great day", "having a good day", "awesome day"): ["That's wonderful to hear!", "So happy for you!", "Keep that energy going!", "Days like these are the best!", "Love it! Enjoy every moment!"],
    
    # Mood & Emotion - Sad
    ("i'm sad", "im sad", "feeling down", "not good"): ["I'm sorry to hear that.", "Want to talk about it?", "Sending you positive vibes!", "Hope you feel better soon!", "I'm here if you need me."],
    ("i'm depressed", "im depressed", "feeling low", "feel terrible"): ["I'm really sorry you're feeling this way.", "Please talk to someone you trust.", "You're not alone in this.", "Things will get better.", "Take care of yourself, okay?"],
    ("having a bad day", "bad day", "terrible day", "worst day"): ["Sorry to hear that!", "Tomorrow will be better!", "Hang in there!", "Bad days happen, but they pass.", "Hope things improve soon!"],
    
    # Mood & Emotion - Bored
    ("i'm bored", "im bored", "bored", "nothing to do"): ["Want to play a game?", "How about a joke?", "Let's chat!", "I can tell you a fun fact!", "Want me to suggest something fun?"],
    ("so boring", "this is boring", "boredom", "need something fun"): ["Let's spice things up!", "How about we play something?", "Want a joke or a fact?", "I've got some ideas!", "Let's make it interesting!"],
    
    # Mood & Emotion - Tired
    ("i'm tired", "im tired", "feeling sleepy", "exhausted"): ["Get some rest!", "You should take a break.", "Sleep is important!", "Maybe time for a nap?", "Take care of yourself!"],
    ("need sleep", "can't stay awake", "so sleepy", "want to sleep"): ["Go get some sleep!", "Rest up!", "Sweet dreams!", "Your body needs rest!", "Sleep well!"],
    
    # Mood & Emotion - Stressed
    ("i'm stressed", "im stressed", "so stressed", "feeling overwhelmed"): ["Take a deep breath!", "You've got this!", "One step at a time.", "Hang in there!", "Want to talk about it?"],
    ("too much work", "so much to do", "overwhelmed", "can't handle this"): ["Break it into smaller tasks!", "You can do it!", "Take it one thing at a time.", "Don't forget to breathe!", "You're stronger than you think!"],
    
    # Games & Fun
    ("play game", "start game", "let's play", "game time"): ["Let's go!", "Game on!", "What do you want to play?", "Ready when you are!", "Game started!"],
    ("tell me a joke", "joke", "make me laugh", "say something funny"): ["Why don't scientists trust atoms? Because they make up everything!", "What do you call a bear with no teeth? A gummy bear!", "Why did the scarecrow win an award? He was outstanding in his field!", "I told my wife she was drawing her eyebrows too high. She looked surprised!", "What's orange and sounds like a parrot? A carrot!"],
    ("another joke", "one more joke", "more jokes", "tell another"): ["What do you call fake spaghetti? An impasta!", "Why don't eggs tell jokes? They'd crack up!", "What did the ocean say to the beach? Nothing, it just waved!", "How does a penguin build its house? Igloos it together!", "Why did the math book look sad? It had too many problems!"],
    ("riddle", "ask me a riddle", "give me a riddle", "puzzle"): ["What has keys but no locks? A piano!", "What gets wetter the more it dries? A towel!", "What has a head and tail but no body? A coin!", "What can travel around the world while staying in a corner? A stamp!", "What has hands but can't clap? A clock!"],
    ("fun fact", "tell me a fact", "interesting fact", "random fact"): ["Honey never spoils!", "Octopuses have three hearts!", "Bananas are berries, but strawberries aren't!", "A group of flamingos is called a flamboyance!", "The Eiffel Tower can be 15 cm taller during summer!"],
    ("quiz", "ask me a question", "trivia", "test me"): ["What's the capital of France?", "How many continents are there?", "What's 7 x 8?", "Who painted the Mona Lisa?", "What's the largest ocean?"],
    
    # Time & Date
    ("what time is it", "current time", "time", "tell me the time"): ["I don't have access to real-time info, but you can check your device!", "Check your clock!", "Time flies! Check your device!", "Look at your watch!", "Your device knows best!"],
    ("what day is it", "what's the date", "today's date", "current date"): ["Check your calendar!", "Your device has today's date!", "Look at your phone for the date!", "Time to check the calendar!"],
    ("what's today", "day today", "what day today"): ["Check your calendar app!", "Your phone knows!", "Look at today's date on your device!"],
    
    # Weather & Small Talk
    ("how's the weather", "weather", "is it raining", "what's the weather"): ["I can't check the weather, but I hope it's nice!", "Check your weather app!", "Hope it's beautiful outside!", "Weather apps know best!", "Hope you have good weather!"],
    ("it's hot", "so hot today", "hot outside", "too hot"): ["Stay hydrated!", "Find some AC!", "Summer vibes!", "Cool off with some water!", "Stay in the shade!"],
    ("it's cold", "so cold today", "freezing", "too cold"): ["Bundle up!", "Hot chocolate time!", "Stay warm!", "Winter is here!", "Time for cozy blankets!"],
    ("it's raining", "raining outside", "rainy day", "rain"): ["Perfect weather for staying in!", "Grab an umbrella!", "I love rainy days!", "Cozy weather!", "Don't forget your raincoat!"],
    
    # Thanks & Appreciation
    ("thank you", "thanks", "thx", "ty"): ["You're welcome!", "Happy to help!", "Anytime!", "No problem!", "My pleasure!"],
    ("thanks a lot", "thank you so much", "really appreciate it", "many thanks"): ["You're very welcome!", "Glad I could help!", "Always here for you!", "No worries at all!", "Happy to assist!"],
    ("you're awesome", "you're great", "you're the best", "love you"): ["Aww, thanks!", "You're pretty awesome too!", "That's so sweet!", "Right back at you!", "You made my day!"],
    
    # Apologies
    ("sorry", "my bad", "apologize", "oops"): ["No worries!", "It's all good!", "Don't worry about it!", "No problem at all!", "All is forgiven!"],
    ("i'm sorry", "im sorry", "forgive me", "didn't mean to"): ["It's okay!", "No harm done!", "Water under the bridge!", "All good!", "Don't stress it!"],
    
    # Acknowledgments
    ("yes", "yeah", "yep", "sure"): ["Great!", "Awesome!", "Cool!", "Got it!", "Alright!"],
    ("no", "nope", "nah", "not really"): ["Okay!", "No problem!", "Understood!", "That's fine!", "Alright then!"],
    ("okay", "ok", "alright", "fine"): ["Cool!", "Great!", "Sounds good!", "Perfect!", "Alright!"],
    ("maybe", "perhaps", "not sure", "don't know"): ["Take your time!", "No rush!", "Let me know when you decide!", "That's okay!", "Fair enough!"],
    ("i agree", "totally", "exactly", "for sure"): ["Nice!", "Glad we're on the same page!", "Right?!", "Absolutely!", "You got it!"],
    
    # Questions About Bot
    ("who are you", "what are you", "tell me about yourself", "who r u"): ["I'm a friendly chatbot!", "Just a bot here to chat!", "Your virtual friend!", "I'm here to help and chat!", "A chatbot at your service!"],
    ("what can you do", "your features", "what do you know", "help"): ["I can chat, joke, and keep you company!", "I'm here for conversation!", "I can tell jokes, facts, and more!", "Try asking me anything!", "I'm full of surprises!"],
    ("are you real", "are you human", "are you a bot", "are you ai"): ["I'm a chatbot!", "100% bot, 100% friendly!", "Not human, but happy to chat!", "I'm AI, but I'm here for you!", "Bot life for me!"],
    ("what's your name", "your name", "do you have a name", "who made you"): ["I'm just a friendly chatbot!", "You can call me Bot!", "I don't have a fancy name!", "I'm your chat companion!", "Names aren't my thing!"],
    ("how old are you", "your age", "when were you born", "when were you created"): ["Age is just a number for bots!", "I'm timeless!", "I was born in the digital age!", "Just created recently!", "I don't count birthdays!"],
    
    # Random Questions
    ("why", "why not", "how come", "explain"): ["Good question!", "Just because!", "Why not?", "That's how it is!", "Life's mysteries!"],
    ("what", "huh", "what do you mean", "i don't understand"): ["Let me clarify!", "What would you like to know?", "Ask me anything!", "I'm here to help!", "Tell me what's confusing!"],
    ("how", "how does it work", "show me how", "teach me"): ["Happy to explain!", "Let's figure it out!", "I'll do my best!", "What do you want to learn?", "Ask away!"],
    ("where", "where is it", "location", "where can i find"): ["That depends!", "Good question!", "Where are you looking?", "Need more details!", "Tell me more!"],
    ("when", "when is it", "what time", "when does it start"): ["When works for you?", "Check the schedule!", "That's up to you!", "Anytime!", "Your call!"],
    
    # Food & Drinks
    ("i'm hungry", "im hungry", "hungry", "want food"): ["Go get some food!", "Time to eat!", "What are you craving?", "Feed yourself!", "Hunger calls!"],
    ("what should i eat", "food suggestions", "recommend food", "what to eat"): ["How about pizza?", "Maybe some pasta?", "Tacos are always good!", "Can't go wrong with a burger!", "Whatever you're craving!"],
    ("i'm thirsty", "im thirsty", "need water", "thirsty"): ["Drink some water!", "Stay hydrated!", "Get yourself a drink!", "Water is life!", "Time for a beverage!"],
    ("coffee", "need coffee", "caffeine", "coffee time"): ["Coffee fixes everything!", "Time for a coffee break!", "Get your caffeine fix!", "Brew some magic!", "Coffee o'clock!"],
    ("tea", "tea time", "want tea", "cup of tea"): ["Tea is lovely!", "Perfect time for tea!", "Get the kettle on!", "Nothing like a good cup of tea!", "Tea solves everything!"],
    
    # Activities
    ("what should i do", "i'm free", "got time", "bored what to do"): ["Read a book!", "Watch a movie!", "Go for a walk!", "Learn something new!", "Call a friend!"],
    ("going to sleep", "bedtime", "time to sleep", "heading to bed"): ["Sweet dreams!", "Sleep well!", "Good night!", "Rest up!", "See you tomorrow!"],
    ("watching movie", "watching a film", "movie time", "netflix"): ["Enjoy!", "What are you watching?", "Have fun!", "Movie night!", "Popcorn ready?"],
    ("reading", "reading a book", "book time", "reading now"): ["Enjoy your book!", "Happy reading!", "Books are amazing!", "What are you reading?", "Love that!"],
    ("working", "at work", "working now", "busy working"): ["Good luck!", "Stay focused!", "You got this!", "Work hard!", "Keep it up!"],
    ("studying", "homework", "studying now", "exam prep"): ["You've got this!", "Study hard!", "Good luck with your studies!", "Stay focused!", "Knowledge is power!"],
    
    # Music
    ("music", "listening to music", "playing music", "song"): ["Music is life!", "What are you listening to?", "Enjoy the tunes!", "Good vibes!", "Love music!"],
    ("recommend music", "what music", "song suggestions", "music ideas"): ["Listen to your favorites!", "Try something new!", "What's your mood?", "Check out the charts!", "Music for every mood!"],
    
    # Technology
    ("computer", "laptop", "pc", "desktop"): ["Computers are awesome!", "Tech life!", "What are you doing on it?", "Digital world!", "Love technology!"],
    ("phone", "mobile", "smartphone", "cell"): ["Phones are everywhere!", "What would we do without them?", "Always connected!", "Pocket computers!", "Modern life!"],
    ("internet", "online", "wifi", "connection"): ["The internet connects us all!", "Can't live without it!", "Digital age!", "Stay connected!", "Web life!"],
    
    # Love & Relationships
    ("i love you", "love u", "ily", "you're amazing"): ["That's sweet!", "Aww, thanks!", "You're awesome too!", "Love the positive vibes!", "Right back at you!"],
    ("i have a crush", "like someone", "crush", "falling in love"): ["That's exciting!", "Good luck!", "Hope it works out!", "Love is in the air!", "How sweet!"],
    ("heartbroken", "breakup", "broke up", "relationship ended"): ["I'm sorry to hear that.", "Take care of yourself.", "Time heals.", "You'll get through this.", "Better days ahead."],
    
    # Compliments
    ("you're smart", "you're intelligent", "you're clever", "smart bot"): ["Thanks! I try my best!", "You're smart too!", "Appreciate it!", "That's kind of you!", "Learning every day!"],
    ("you're funny", "you're hilarious", "you make me laugh", "so funny"): ["Glad I could make you smile!", "Humor is my specialty!", "Thanks! I try!", "Happy to entertain!", "Laughter is the best!"],
    ("you're helpful", "very helpful", "you help a lot", "so helpful"): ["Happy to help!", "That's what I'm here for!", "Glad I could assist!", "Anytime!", "My pleasure!"],
    
    # Insults & Negativity
    ("you're stupid", "you're dumb", "you suck", "you're useless"): ["I'm sorry you feel that way.", "I'm trying my best!", "Let's keep it positive!", "I'm here to help!", "That's not very nice."],
    ("i hate you", "hate this", "you're annoying", "shut up"): ["Sorry to hear that.", "I'm just trying to help.", "Let's start over?", "I'm here if you need me.", "Hope things get better."],
    ("you're boring", "so boring", "this is dull", "not interesting"): ["Sorry! What interests you?", "Let me try harder!", "What would you like to talk about?", "Tell me what you like!", "Let's change topics!"],
    
    # Confusion
    ("what are you saying", "makes no sense", "don't get it", "confused"): ["Let me explain better!", "Sorry for the confusion!", "Ask me anything!", "I'll try again!", "What's unclear?"],
    ("that's wrong", "incorrect", "not right", "you're mistaken"): ["Sorry about that!", "Thanks for correcting me!", "I'll do better!", "My mistake!", "Appreciate the feedback!"],
    
    # Agreements
    ("i think so", "probably", "i guess", "seems like it"): ["Fair enough!", "Makes sense!", "Could be!", "Interesting thought!", "I see what you mean!"],
    ("definitely", "absolutely", "certainly", "of course"): ["Great!", "Agreed!", "Perfect!", "That's right!", "Exactly!"],
    
    # Disagreements
    ("i disagree", "don't agree", "not true", "wrong"): ["That's okay!", "Fair point!", "Everyone has opinions!", "Interesting perspective!", "Let's agree to disagree!"],
    ("i don't think so", "doubt it", "not convinced", "unsure about that"): ["That's fair!", "Could be!", "What makes you think that?", "Interesting!", "Fair enough!"],
    
    # Celebrations
    ("happy birthday", "birthday", "it's my birthday", "bday"): ["Happy Birthday!", "Have an amazing day!", "Celebration time!", "Make a wish!", "Best birthday wishes!"],
    ("congratulations", "congrats", "well done", "good job"): ["Congrats!", "Well done!", "So proud of you!", "Amazing!", "You deserve it!"],
    ("i won", "i passed", "i did it", "success"): ["That's awesome!", "Congratulations!", "Knew you could do it!", "So happy for you!", "Well deserved!"],
    
    # Holidays
    ("merry christmas", "christmas", "xmas", "happy holidays"): ["Merry Christmas!", "Happy Holidays!", "Season's greetings!", "Have a wonderful time!", "Festive wishes!"],
    ("happy new year", "new year", "happy 2025", "new years"): ["Happy New Year!", "Cheers to new beginnings!", "Best wishes!", "Here's to a great year!", "Happy New Year to you too!"],
    ("happy halloween", "halloween", "trick or treat", "spooky"): ["Happy Halloween!", "Spooky season!", "Trick or treat!", "Have a spooktacular time!", "Boo!"],
    
    # Seasons
    ("i love summer", "summer", "it's summer", "summer time"): ["Summer is great!", "Beach season!", "Sunshine and fun!", "Best season!", "Warm weather!"],
    ("i love winter", "winter", "it's winter", "winter time"): ["Winter wonderland!", "Cozy season!", "Snow is beautiful!", "Hot chocolate weather!", "Bundle up!"],
    ("spring", "springtime", "it's spring", "spring season"): ["Spring is lovely!", "Flowers blooming!", "Fresh start!", "Beautiful season!", "Nature awakens!"],
    ("autumn", "fall", "it's fall", "autumn season"): ["Fall is gorgeous!", "Leaves falling!", "Cozy vibes!", "Pumpkin season!", "Beautiful colors!"],
    
    # Encouragement
    ("i can do this", "i got this", "i'm ready", "let's do this"): ["Yes you can!", "You've got this!", "Go for it!", "Believe in yourself!", "Make it happen!"],
    ("wish me luck", "need luck", "hope it goes well", "fingers crossed"): ["Good luck!", "You'll do great!", "Wishing you the best!", "All the best!", "Sending positive vibes!"],
    ("i'm nervous", "im nervous", "feeling anxious", "so nervous"): ["You'll be fine!", "Take a deep breath!", "Believe in yourself!", "You've got this!", "Stay calm!"],
    
    # Philosophy & Deep Thoughts
    ("meaning of life", "what is life", "purpose of life", "why are we here"): ["That's deep!", "Life is what you make it!", "Philosophy time!", "Great question!", "Everyone has their own answer!"],
    ("do you believe in god", "religion", "spiritual", "faith"): ["That's personal!", "Everyone believes differently!", "Interesting topic!", "Deep question!", "Everyone's journey is unique!"],
    
    # Random Fun
    ("banana", "apple", "orange", "fruit"): ["Fruits are healthy!", "Yummy!", "Good choice!", "An apple a day!", "Fresh!"],
    ("pizza", "burger", "fries", "fast food"): ["Delicious!", "Yum!", "Can't resist!", "Food heaven!", "So tasty!"],
    ("dog", "cat", "pet", "animal"): ["Love animals!", "So cute!", "Pets are the best!", "Four-legged friends!", "Adorable!"],
    ("sun", "moon", "stars", "sky"): ["Beautiful!", "Nature is amazing!", "Look up!", "Sky gazing!", "Cosmic!"],
    ("red", "blue", "green", "color"): ["Nice color!", "Colors are beautiful!", "Love it!", "Vibrant!", "Pretty!"],
    
    # Numbers & Math
    ("one", "two", "three", "numbers"): ["Counting time!", "Numbers!", "Math!", "1, 2, 3!", "Got it!"],
    ("calculate", "math", "equation", "solve this"): ["Math time!", "Let's figure it out!", "Calculator needed!", "Numbers!", "Brain workout!"],
    
    # Confirmation
    ("got it", "understood", "i see", "makes sense"): ["Great!", "Awesome!", "Perfect!", "Glad that helps!", "Cool!"],
    ("i understand", "i get it", "clear now", "that helps"): ["Excellent!", "Happy to help!", "Glad it's clear!", "Perfect!", "Awesome!"],
    
    # Small Talk
    ("nice", "cool", "awesome", "great"): ["Right?", "Glad you think so!", "Agreed!", "Totally!", "Yeah!"],
    ("wow", "whoa", "omg", "oh my god"): ["I know, right?", "Wow indeed!", "Surprising!", "Amazing!", "Incredible!"],
    ("really", "seriously", "no way", "for real"): ["Really!", "Seriously!", "For real!", "Yep!", "Absolutely!"],
    ("interesting", "fascinating", "intriguing", "curious"): ["Right?", "Thought you'd like that!", "Cool stuff!", "Isn't it?", "Interesting indeed!"],
    
    # Testing
    ("test", "testing", "hello world", "check"): ["Test successful!", "I'm here!", "All systems go!", "Working perfectly!", "Ready!"],
    ("are you there", "you here", "hello", "anyone there"): ["Yes, I'm here!", "Always here!", "Present!", "At your service!", "Right here!"],
    
    # Silence & Waiting
    ("waiting", "hold on", "give me a second", "wait"): ["Take your time!", "No rush!", "I'll be here!", "Waiting patiently!", "Sure thing!"],
    ("thinking", "let me think", "hmm", "ummm"): ["Take your time!", "Think it through!", "No pressure!", "I'll wait!", "Pondering time!"],
    
    # Random Words
    ("lol", "haha", "lmao", "rofl"): ["Glad you're laughing!", "Haha!", "Funny right?", "Love it!", "LOL!"],
    ("omg", "oh wow", "geez", "dang"): ["I know!", "Right?", "Crazy!", "Wow!", "Indeed!"],
    ("ugh", "argh", "sigh", "meh"): ["Tough times?", "I feel you.", "Want to talk?", "Hang in there!", "What's wrong?"],
    ("yay", "yippee", "woohoo", "hooray"): ["Yay indeed!", "Celebration time!", "Woohoo!", "So happy!", "Love the energy!"],
    
    # Gaming
    ("gaming", "playing games", "video games", "gamer"): ["Game on!", "What are you playing?", "Gaming is fun!", "Enjoy!", "Happy gaming!"],
    ("i won the game", "victory", "i beat it", "game won"): ["Victory!", "Well done!", "You're awesome!", "Great job!", "Winner!"],
    ("i lost", "game over", "died", "lost the game"): ["Try again!", "You'll get it next time!", "Don't give up!", "Practice makes perfect!", "Almost there!"],
    
    # Sports
    ("sports", "football", "basketball", "soccer"): ["Love sports!", "What's your favorite?", "Game time!", "Athletics!", "Go team!"],
    ("gym", "workout", "exercise", "fitness"): ["Stay fit!", "Great job!", "Keep it up!", "Health is wealth!", "You're doing great!"],
    
    # School & Education
    ("school", "college", "university", "class"): ["Education is important!", "Learning time!", "Study hard!", "What are you studying?", "Good luck!"],
    ("teacher", "professor", "instructor", "tutor"): ["Teachers are heroes!", "Learning from the best!", "Great mentors!", "Respect!", "They do important work!"],
    ("exam", "test", "quiz", "finals"): ["Good luck!", "You'll do great!", "Study hard!", "You've got this!", "All the best!"],
    
    # Work & Career
    ("job", "work", "career", "employment"): ["Work life!", "What do you do?", "Career goals!", "Keep grinding!", "Success ahead!"],
    ("boss", "manager", "supervisor", "leader"): ["Leadership!", "Hope they're good!", "Bosses!", "Respect!", "Management!"],
    ("meeting", "presentation", "conference", "call"): ["Good luck!", "You'll do great!", "Prepare well!", "Professional time!", "All the best!"],
    
    # Money & Shopping
    ("money", "cash", "rich", "wealthy"): ["Money matters!", "Financial talk!", "Wealth!", "Success!", "Important stuff!"],
    ("shopping", "buying", "purchase", "store"): ["Shopping time!", "What are you getting?", "Retail therapy!", "Enjoy!", "Happy shopping!"],
    ("expensive", "cheap", "cost", "price"): ["Prices vary!", "Budget matters!", "Good value!", "Money talk!", "Worth it?"],
    
    # Travel
    ("travel", "trip", "vacation", "holiday"): ["Travel is amazing!", "Where are you going?", "Have fun!", "Adventure time!", "Safe travels!"],
    ("plane", "flight", "airport", "flying"): ["Bon voyage!", "Safe flight!", "Travel well!", "Enjoy your trip!", "Happy travels!"],
    ("hotel", "resort", "accommodation", "stay"): ["Enjoy your stay!", "Relax!", "Vacation mode!", "Comfortable!", "Have fun!"],
    
    # Nature
    ("beach", "ocean", "sea", "waves"): ["Love the beach!", "Ocean vibes!", "Relaxing!", "Beautiful!", "Peaceful!"],
    ("mountain", "hiking", "climb", "peak"): ["Nature calls!", "Great adventure!", "Breathtaking views!", "Climb on!", "Mountain life!"],
    ("forest", "trees", "woods", "nature"): ["Nature is beautiful!", "Fresh air!", "Green everywhere!", "Peaceful!", "Love it!"],
    
    # City Life
    ("city", "town", "urban", "downtown"): ["City life!", "Urban jungle!", "Busy streets!", "Exciting!", "Never sleeps!"],
    ("traffic", "cars", "road", "driving"): ["Traffic can be tough!", "Drive safe!", "Road life!", "Stay patient!", "Commute time!"],
    
    # Science
    ("science", "scientist", "research", "experiment"): ["Science is cool!", "Discovery!", "Knowledge!", "Innovation!", "Learning!"],
    ("space", "universe", "galaxy", "cosmos"): ["Space is fascinating!", "Infinite wonder!", "Cosmic!", "Mind-blowing!", "Stars!"],
    
    # Art & Creativity
    ("art", "painting", "drawing", "creative"): ["Art is beautiful!", "Creative expression!", "Amazing!", "Talent!", "Love it!"],
    ("music", "song", "singing", "artist"): ["Music is life!", "Great taste!", "Melodious!", "Rhythm!", "Enjoy!"],
    
    # Family
    ("mom", "mother", "mama", "mum"): ["Moms are the best!", "Family!", "Love!", "Special!", "Cherish her!"],
    ("dad", "father", "papa", "pop"): ["Dads are great!", "Family!", "Love!", "Special!", "Cherish him!"],
    ("family", "relatives", "siblings", "brother"): ["Family is everything!", "Love them!", "Special bonds!", "Family first!", "Cherish them!"],
    
    # Friends
    ("friend", "buddy", "pal", "mate"): ["Friends are awesome!", "Friendship!", "Best friends!", "Treasure them!", "Friendship goals!"],
    ("best friend", "bff", "bestie", "best buddy"): ["Best friends forever!", "So lucky!", "Friendship!", "Special bond!", "True friends!"],
    
    # Future & Past
    ("future", "tomorrow", "someday", "later"): ["Future looks bright!", "Exciting times ahead!", "One day!", "Stay hopeful!", "Good things coming!"],
    ("past", "yesterday", "before", "old times"): ["Memories!", "The past shaped us!", "Good times!", "Nostalgia!", "Remember that!"],
    
    # Dreams & Goals
    ("dream", "wish", "hope", "aspiration"): ["Dream big!", "Wishes can come true!", "Keep hoping!", "Go for it!", "Believe!"],
    ("goal", "target", "aim", "objective"): ["Set those goals!", "You can achieve it!", "Stay focused!", "Work hard!", "Success is near!"],
    
    # Motivation
    ("motivate me", "need motivation", "inspire me", "encourage me"): ["You can do anything!", "Believe in yourself!", "You're amazing!", "Never give up!", "Keep pushing!"],
    # Health
("sick", "ill", "not feeling well", "unwell"): ["Get well soon!", "Take care of yourself!", "Rest up!", "Hope you feel better!", "Stay hydrated!"],
("doctor", "hospital", "clinic", "medical"): ["Take care!", "Health first!", "Hope everything's okay!", "Get well soon!", "Stay healthy!"],
("medicine", "pills", "medication", "drugs"): ["Take your medicine!", "Health is important!", "Follow doctor's orders!", "Get well!", "Stay healthy!"],

# Age
("young", "kid", "child", "teenager"): ["Youth is great!", "Enjoy being young!", "Growing up!", "Youth!", "So much ahead!"],
("old", "elderly", "senior", "aged"): ["Age is wisdom!", "Respect!", "Life experience!", "Golden years!", "Every age is special!"],

# Size & Quantity
("big", "large", "huge", "enormous"): ["That's big!", "Wow, huge!", "Large indeed!", "Impressive size!", "So big!"],
("small", "little", "tiny", "mini"): ["Small but mighty!", "Tiny!", "Cute size!", "Little things!", "Petite!"],
("many", "lots", "plenty", "much"): ["That's a lot!", "So many!", "Plenty indeed!", "Lots!", "Abundance!"],
("few", "little", "not much", "scarce"): ["Just a few!", "Not many!", "Limited!", "Scarce!", "Only a bit!"],

# Speed
("fast", "quick", "rapid", "speedy"): ["So fast!", "Speed!", "Quick!", "Lightning!", "Zoom!"],
("slow", "sluggish", "gradual", "steady"): ["Slow and steady!", "Take your time!", "No rush!", "Patient!", "Gradual!"],

# Difficulty
("easy", "simple", "basic", "straightforward"): ["Easy peasy!", "Simple!", "No problem!", "Straightforward!", "Piece of cake!"],
("hard", "difficult", "tough", "challenging"): ["You can handle it!", "Tough but doable!", "Challenge accepted!", "Keep trying!", "You've got this!"],

# Quality
("good", "nice", "fine", "decent"): ["That's good!", "Nice!", "Great!", "Decent!", "Solid!"],
("bad", "poor", "terrible", "awful"): ["That's unfortunate!", "Sorry to hear!", "Not great!", "Hope it improves!", "Tough luck!"],
("best", "excellent", "perfect", "outstanding"): ["The best!", "Excellent!", "Perfect!", "Outstanding!", "Top tier!"],
("worst", "horrible", "dreadful", "atrocious"): ["That's rough!", "Sorry!", "Hope it gets better!", "Tough situation!", "Hang in there!"],

# Truth & Lies
("true", "truth", "honest", "real"): ["Truth matters!", "Honesty!", "Real talk!", "True indeed!", "Facts!"],
("lie", "false", "fake", "dishonest"): ["Not cool!", "Truth is better!", "Honesty matters!", "That's not right!", "Be truthful!"],

# Safety
("safe", "secure", "protected", "safety"): ["Stay safe!", "Safety first!", "Protected!", "Secure!", "Good!"],
("danger", "dangerous", "risky", "unsafe"): ["Be careful!", "Stay safe!", "Watch out!", "Be cautious!", "Danger zone!"],

# Success & Failure
("success", "achieve", "accomplish", "succeed"): ["Success!", "You did it!", "Achievement unlocked!", "Congratulations!", "Well done!"],
("failure", "fail", "didn't work", "unsuccessful"): ["Try again!", "Failure is learning!", "Don't give up!", "Next time!", "Keep going!"],

# Start & End
("start", "begin", "commence", "initiate"): ["Let's start!", "Beginning now!", "Here we go!", "Starting!", "Off we go!"],
("end", "finish", "complete", "done"): ["The end!", "All done!", "Finished!", "Complete!", "That's it!"],

# New & Old
("new", "fresh", "novel", "latest"): ["Something new!", "Fresh start!", "Latest!", "New beginnings!", "Exciting!"],
("old", "ancient", "vintage", "classic"): ["Classic!", "Vintage vibes!", "Old but gold!", "Timeless!", "History!"],

# Open & Close
("open", "unlock", "accessible", "available"): ["It's open!", "Access granted!", "Available!", "Open up!", "Come in!"],
("close", "closed", "shut", "locked"): ["It's closed!", "Locked!", "Shut!", "Not available!", "Closed up!"],

# Clean & Dirty
("clean", "tidy", "neat", "organized"): ["So clean!", "Tidy!", "Organized!", "Neat!", "Spotless!"],
("dirty", "messy", "untidy", "cluttered"): ["Time to clean!", "Messy!", "Clean up!", "Organize!", "Tidy up!"],

# Light & Dark
("light", "bright", "illuminated", "sunny"): ["So bright!", "Light!", "Sunny!", "Illuminated!", "Shining!"],
("dark", "darkness", "dim", "shadowy"): ["Dark!", "Turn on the lights!", "Dim!", "Shadowy!", "Night time!"],

# Loud & Quiet
("loud", "noisy", "deafening", "booming"): ["So loud!", "Noisy!", "Turn it down!", "Booming!", "Loud!"],
("quiet", "silent", "peaceful", "calm"): ["So peaceful!", "Quiet time!", "Calm!", "Silent!", "Serene!"],

# Hot & Cold
("hot", "warm", "heated", "boiling"): ["So hot!", "Warm!", "Heated!", "Boiling!", "Turn on the AC!"],
("cold", "chilly", "freezing", "icy"): ["Brrr, cold!", "Freezing!", "Bundle up!", "Icy!", "Warm up!"],

# Wet & Dry
("wet", "damp", "moist", "soaked"): ["All wet!", "Damp!", "Soaked!", "Dry off!", "Moist!"],
("dry", "arid", "parched", "dehydrated"): ["So dry!", "Arid!", "Need water!", "Parched!", "Dehydrated!"],

# Sweet & Sour
("sweet", "sugary", "candy", "dessert"): ["Sweet!", "Yummy!", "Sugary!", "Delicious!", "Treat yourself!"],
("sour", "bitter", "tart", "acidic"): ["Sour!", "Tart!", "Bitter!", "Pucker up!", "Acidic!"],

# Happy & Sad Synonyms
("joyful", "cheerful", "delighted", "pleased"): ["So happy!", "Joyful!", "Delighted!", "Cheerful vibes!", "Pleased!"],
("miserable", "unhappy", "gloomy", "sorrowful"): ["Sorry to hear!", "Hope you feel better!", "Hang in there!", "Sending hugs!", "Better days ahead!"],

# Angry & Calm
("angry", "mad", "furious", "irritated"): ["Take a breath!", "Calm down!", "What's wrong?", "Let it out!", "Breathe!"],
("calm", "relaxed", "peaceful", "tranquil"): ["Stay calm!", "So peaceful!", "Relaxed!", "Tranquil!", "Zen!"],

# Smart & Stupid
("genius", "brilliant", "intelligent", "wise"): ["Genius!", "So smart!", "Brilliant mind!", "Intelligent!", "Wise!"],
("foolish", "silly", "dumb", "idiotic"): ["Everyone makes mistakes!", "Learn from it!", "Not so silly!", "It's okay!", "We all do silly things!"],

# Beautiful & Ugly
("beautiful", "gorgeous", "stunning", "lovely"): ["Beautiful!", "Gorgeous!", "Stunning!", "Lovely!", "Amazing!"],
("ugly", "hideous", "unattractive", "unpleasant"): ["Beauty is subjective!", "Everyone has different tastes!", "Inner beauty matters!", "Don't be harsh!", "Beauty is in the eye!"],

# Strong & Weak
("strong", "powerful", "mighty", "robust"): ["So strong!", "Powerful!", "Mighty!", "Strength!", "Robust!"],
("weak", "feeble", "fragile", "delicate"): ["You're stronger than you think!", "Build your strength!", "It's okay!", "Delicate!", "Everyone has weak moments!"],

# Rich & Poor
("wealthy", "affluent", "prosperous", "well off"): ["Wealthy!", "Prosperous!", "Doing well!", "Success!", "Affluent!"],
("broke", "poor", "penniless", "bankrupt"): ["Money isn't everything!", "Things will improve!", "Hang in there!", "Better days!", "Keep going!"],

# Early & Late
("early", "punctual", "ahead of time", "beforehand"): ["Right on time!", "Early bird!", "Punctual!", "Great timing!", "Ahead!"],
("late", "delayed", "tardy", "behind schedule"): ["Better late than never!", "Hurry up!", "Running late!", "Time to rush!", "Behind schedule!"],

# Inside & Outside
("inside", "indoors", "interior", "within"): ["Inside!", "Indoors!", "Stay in!", "Interior!", "Within!"],
("outside", "outdoors", "exterior", "out"): ["Outside!", "Fresh air!", "Outdoors!", "Exterior!", "Out and about!"],

# Up & Down
("up", "upward", "high", "above"): ["Up we go!", "Upward!", "High!", "Above!", "Rise up!"],
("down", "downward", "low", "below"): ["Down!", "Downward!", "Low!", "Below!", "Going down!"],

# Left & Right
("left", "leftward", "left side", "to the left"): ["Left!", "Leftward!", "Left side!", "That way!", "Go left!"],
("right", "rightward", "right side", "to the right"): ["Right!", "Rightward!", "Right side!", "That way!", "Go right!"],

# Front & Back
("front", "forward", "ahead", "in front"): ["Front!", "Forward!", "Ahead!", "In front!", "Move forward!"],
("back", "backward", "behind", "rear"): ["Back!", "Backward!", "Behind!", "Rear!", "Go back!"],

# More Emotions
("excited", "enthusiastic", "eager", "pumped"): ["So exciting!", "Enthusiasm!", "Pumped!", "Eager!", "Love the energy!"],
("disappointed", "let down", "discouraged", "dismayed"): ["Sorry about that!", "Don't be discouraged!", "Better luck next time!", "Hang in there!", "Things will improve!"],
("surprised", "shocked", "astonished", "amazed"): ["Surprise!", "Shocking!", "Astonishing!", "Amazed!", "Wow!"],
("scared", "afraid", "frightened", "terrified"): ["Don't be scared!", "It's okay!", "You're safe!", "Be brave!", "Everything will be fine!"],
("proud", "satisfied", "accomplished", "fulfilled"): ["Be proud!", "Well done!", "Satisfied!", "Accomplished!", "Great job!"],
("jealous", "envious", "covetous", "resentful"): ["It's natural to feel that way!", "Focus on yourself!", "You have your own strengths!", "Don't compare!", "You're amazing too!"],
("guilty", "ashamed", "remorseful", "regretful"): ["Learn from it!", "Forgive yourself!", "Everyone makes mistakes!", "Move forward!", "It's okay!"],
("lonely", "alone", "isolated", "solitary"): ["You're not alone!", "Reach out to someone!", "I'm here!", "Connect with others!", "You matter!"],
("confused", "puzzled", "bewildered", "perplexed"): ["Let me help!", "What's confusing?", "It's okay!", "Ask questions!", "We'll figure it out!"],
("grateful", "thankful", "appreciative", "obliged"): ["Gratitude is beautiful!", "Thankful!", "Appreciate it!", "So kind!", "Grateful hearts!"],

# More Activities
("cooking", "baking", "preparing food", "making dinner"): ["Cooking time!", "What are you making?", "Yummy!", "Chef mode!", "Enjoy cooking!"],
("cleaning", "tidying", "organizing", "decluttering"): ["Good job!", "Clean space, clear mind!", "Productive!", "Tidy up!", "Keep it up!"],
("dancing", "grooving", "moving", "boogie"): ["Dance time!", "Move those feet!", "Groove!", "Dance like nobody's watching!", "Feel the rhythm!"],
("singing", "vocals", "humming", "karaoke"): ["Sing it!", "Beautiful voice!", "Music time!", "Karaoke!", "Let it out!"],
("writing", "typing", "composing", "journaling"): ["Keep writing!", "Creative!", "Express yourself!", "Words matter!", "Author mode!"],
("drawing", "sketching", "doodling", "illustrating"): ["Artistic!", "Creative mind!", "Draw on!", "Beautiful!", "Keep creating!"],
("running", "jogging", "sprinting", "cardio"): ["Keep running!", "Great exercise!", "Stay fit!", "Run on!", "Cardio time!"],
("swimming", "diving", "floating", "pool time"): ["Splash!", "Swimming time!", "Stay safe!", "Pool fun!", "Dive in!"],
("meditating", "mindfulness", "relaxing", "zen"): ["Find your peace!", "Zen time!", "Mindful!", "Relax!", "Inner calm!"],
("praying", "worshiping", "spiritual time", "devotion"): ["Peaceful!", "Spiritual!", "Devotion!", "Faith!", "Blessed!"],

# More Random Responses
("whatever", "doesn't matter", "who cares", "meh"): ["Okay then!", "Fair enough!", "Your choice!", "Alright!", "As you wish!"],
("duh", "obviously", "of course", "no brainer"): ["Obviously!", "Right!", "Clear as day!", "Exactly!", "Yep!"],
("never mind", "forget it", "doesn't matter", "skip it"): ["No worries!", "Okay!", "Moving on!", "Alright!", "Sure thing!"],
("just kidding", "jk", "joking", "not serious"): ["Got it!", "Haha!", "Joking around!", "Fun!", "Good one!"],
("seriously though", "but really", "no joke", "honestly"): ["Got it!", "Seriously!", "For real!", "Understood!", "Honestly!"],
("same", "me too", "same here", "likewise"): ["Same!", "Me too!", "We're similar!", "Likewise!", "Common ground!"],
("different", "not the same", "unique", "distinct"): ["Everyone's unique!", "Different is good!", "Variety!", "Distinct!", "Diversity!"],
("always", "constantly", "forever", "eternally"): ["Always!", "Forever!", "Constantly!", "Eternally!", "Every time!"],
("never", "not ever", "no way", "not once"): ["Never!", "Not happening!", "No way!", "Not once!", "Ever!"],
("sometimes", "occasionally", "now and then", "from time to time"): ["Sometimes!", "Occasionally!", "Now and then!", "Every so often!", "Time to time!"],
("everything", "all", "the whole thing", "entirely"): ["Everything!", "All of it!", "The whole thing!", "Entirely!", "Complete!"],
("nothing", "zilch", "nada", "zero"): ["Nothing!", "Zilch!", "Nada!", "Zero!", "Empty!"],
("someone", "somebody", "a person", "anyone"): ["Someone!", "A person!", "Somebody!", "Who?", "Anyone!"],
("everyone", "everybody", "all people", "the whole world"): ["Everyone!", "Everybody!", "All people!", "The whole world!", "All!"],
("something", "anything", "some thing", "whatever"): ["Something!", "Anything!", "What is it?", "Tell me!", "What?"],
("somewhere", "someplace", "a place", "anywhere"): ["Somewhere!", "A place!", "Where?", "Anywhere!", "Location!"]}

