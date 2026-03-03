linking_words = [
    "a", "an", "the",

    "about", "above", "across", "after", "against", "along", "among", "around",
    "at", "before", "behind", "below", "beneath", "beside", "between", "beyond",
    "by", "down", "during", "for", "from", "in", "inside", "into", "near", "of",
    "off", "on", "out", "outside", "over", "through", "throughout", "to",
    "toward", "under", "underneath", "until", "up", "upon", "with", "within",
    "without",

    "and", "but", "or", "nor", "for", "yet", "so", "although", "because",
    "since", "unless", "while",

    "he", "she", "it", "they", "we", "you", "I", "them", "us", "me", "him",
    "her", "our", "their", "its",

    "is", "are", "was", "were", "am", "be", "been", "being", "have", "has",
    "had", "do", "does", "did", "can", "could", "shall", "should", "will",
    "would", "may", "might", "must",

    "if", "then", "therefore", "thus", "hence", "however", "nevertheless",
    "moreover", "furthermore", "likewise", "similarly", "additionally"
]

books_by_authors = {
    "George Orwell": """
    In the year 1984, the world has been transformed into a dystopian society under the watchful eye 
    of a totalitarian regime led by the Party and its leader, Big Brother. The novel follows Winston 
    Smith, a low-ranking member of the Party who works at the Ministry of Truth, where he alters historical 
    records to fit the Party's propaganda. Despite the pervasive surveillance and oppression, Winston 
    harbors rebellious thoughts and dreams of rebellion. The book explores themes of control, manipulation, 
    and the erosion of personal freedom in a society where every aspect of life is regulated and individuality 
    is suppressed.
    """,

    "Gabriel Garcia Marquez": """
    "One Hundred Years of Solitude" is a seminal work by Gabriel Garcia Marquez that tells the multi-generational 
    story of the Buendia family in the fictional town of Macondo. The novel blends magical realism with historical 
    and social commentary, following the rise and fall of the Buendia family over the course of a century. The 
    narrative delves into themes of solitude, fate, and the cyclical nature of history, as the characters experience 
    a series of fantastical and tragic events. The book is renowned for its rich, lyrical prose and its innovative 
    approach to storytelling.
    """,

    "Ursula K. Le Guin": """
    "The Left Hand of Darkness" by Ursula K. Le Guin is a landmark science fiction novel set on the planet Gethen, 
    where the inhabitants possess the unique ability to change gender. The story follows Genly Ai, an envoy from 
    Earth sent to Gethen to persuade its leaders to join an interplanetary alliance. As Genly navigates the complex 
    political and cultural landscape of Gethen, he grapples with issues of gender and identity, forming deep bonds 
    with the people he meets. The novel explores themes of human nature, society, and the ways in which gender 
    influences relationships and social structures.
    """,

    "J.K. Rowling": """
    "Harry Potter and the Philosopher's Stone" introduces readers to Harry Potter, a young boy who discovers 
    on his eleventh birthday that he is a wizard. He attends Hogwarts School of Witchcraft and Wizardry, where 
    he learns about magic, makes friends, and uncovers the truth about his parents' mysterious deaths. The book 
    follows Harry's first year at Hogwarts as he faces challenges and uncovers a dark secret about the magical 
    world, setting the stage for a larger epic of good versus evil.
    """,

    "J.R.R. Tolkien": """
    "The Hobbit" by J.R.R. Tolkien tells the story of Bilbo Baggins, a hobbit who is reluctantly drawn into an epic 
    quest to reclaim the lost Kingdom of Erebor from the dragon Smaug. Along the way, Bilbo encounters trolls, elves, 
    goblins, and a mysterious creature named Gollum. The adventure reveals Bilbo's hidden courage and resourcefulness, 
    and the journey becomes a prelude to the larger saga of "The Lord of the Rings."
    """,

    "Jane Austen": """
    "Pride and Prejudice" by Jane Austen is a classic novel that explores the themes of love, reputation, and class 
    through the story of Elizabeth Bennet and her interactions with the wealthy and aloof Mr. Darcy. The novel examines 
    the social structures of early 19th century England and the personal growth of its characters as they navigate 
    romantic and societal challenges.
    """,

    "Mark Twain": """
    "Adventures of Huckleberry Finn" follows the journey of Huck Finn, a young boy who escapes from his abusive 
    father and travels down the Mississippi River on a raft with Jim, an escaped slave. The novel explores themes 
    of friendship, freedom, and moral dilemmas as Huck and Jim encounter various characters and situations that 
    challenge their views on society and humanity.
    """,

    "F. Scott Fitzgerald": """
    "The Great Gatsby" is set in the Jazz Age of the 1920s and tells the story of Jay Gatsby, a wealthy and enigmatic 
    man who throws extravagant parties in hopes of rekindling a past romance with Daisy Buchanan. Narrated by Nick 
    Carraway, the novel explores themes of wealth, class, and the American Dream, revealing the moral decay and 
    disillusionment beneath the glittering surface of society.
    """,

    "Herman Melville": """
    "Moby-Dick" is a classic American novel that follows the obsessive quest of Captain Ahab to seek revenge on 
    Moby Dick, a giant white whale that had previously maimed him. Narrated by Ishmael, the novel delves into themes 
    of fate, vengeance, and the struggle between man and nature, exploring the depths of human obsession and 
    the unknown.
    """,

    "Leo Tolstoy": """
    "War and Peace" is an epic novel set against the backdrop of the Napoleonic Wars in Russia. It weaves together 
    the lives of several aristocratic families, including Pierre Bezukhov, Andrei Bolkonsky, and Natasha Rostov. 
    The novel explores themes of war, peace, love, and personal transformation, capturing the complexities of 
    human experience and historical change.
    """,

    "Charles Dickens": """
    "A Tale of Two Cities" is set during the turbulent times of the French Revolution and follows the lives of 
    Charles Darnay, a French aristocrat, and Sydney Carton, a dissolute English lawyer. The novel examines themes 
    of resurrection, sacrifice, and social justice, highlighting the stark contrasts between the privileged and the 
    oppressed during a period of profound societal upheaval.
    """,

    "H.P. Lovecraft": """
    "The Call of Cthulhu" is a seminal work in the genre of cosmic horror. The story unfolds through a series of 
    accounts that reveal the existence of ancient, malevolent entities that lurk beyond the comprehension of human 
    understanding. The novel explores themes of forbidden knowledge, madness, and the insignificance of humanity 
    in the face of an indifferent universe.
    """,

    "Aldous Huxley": """
    "Brave New World" envisions a future society driven by technological advancements and social engineering, 
    where humans are conditioned from birth to fulfill predetermined roles. The novel critiques the loss of individuality 
    and personal freedom in a world obsessed with stability, consumerism, and superficial pleasure.
    """,

    "J.D. Salinger": """
    "The Catcher in the Rye" follows Holden Caulfield, a disaffected teenager who is expelled from his prep school 
    and wanders through New York City in search of meaning and authenticity. The novel captures Holden's deep sense 
    of alienation and his quest for personal connection in a world he views as phony and superficial.
    """
}

books_by_authors_1 = {
    "John Steinbeck": """
    "The Grapes of Wrath" is a novel by John Steinbeck that tells the story of the Joad family, who are displaced 
    from their Oklahoma farm by the Dust Bowl and migrate to California in search of a better life. The novel 
    explores themes of poverty, injustice, and the struggle for dignity as the Joads face harsh realities and 
    social inequality. Steinbeck's depiction of the American working class and the impact of economic hardship 
    on human lives is both poignant and powerful.
    """,

    "Ray Bradbury": """
    "Fahrenheit 451" is a dystopian novel by Ray Bradbury set in a future society where books are banned and "firemen" 
    burn any that are found. The story follows Guy Montag, a fireman who begins to question the purpose of his work 
    and the oppressive society he lives in. As Montag becomes disillusioned, he seeks knowledge and rebellion, 
    challenging the norms of a world that suppresses intellectual freedom and critical thought.
    """,

    "Margaret Atwood": """
    "The Handmaid's Tale" is a dystopian novel by Margaret Atwood set in a theocratic society known as the Republic 
    of Gilead. The story follows Offred, a handmaid who is forced into reproductive servitude in a world where 
    women have lost all rights. The novel explores themes of power, control, and resistance, reflecting on the 
    consequences of extreme ideological control and the loss of individual autonomy.
    """,

    "Isaac Asimov": """
    "Foundation" is a seminal science fiction novel by Isaac Asimov that follows the efforts of the Foundation, a 
    group of scientists dedicated to preserving knowledge and guiding the future of a galaxy-spanning empire. The 
    novel explores themes of history, sociology, and the role of knowledge in shaping civilization, set against 
    the backdrop of a declining empire and the rise of a new order.
    """,

    "Arthur C. Clarke": """
    "2001: A Space Odyssey" is a science fiction novel by Arthur C. Clarke that explores themes of artificial intelligence, 
    extraterrestrial life, and the evolution of humanity. The story follows the journey of the spaceship Discovery One 
    as it travels to Jupiter, guided by the enigmatic monoliths and the increasingly sentient computer HAL 9000. 
    Clarke's novel raises questions about the future of human evolution and the nature of intelligence.
    """,

    "Toni Morrison": """
    "Beloved" is a novel by Toni Morrison that tells the haunting story of Sethe, an escaped enslaved woman who is 
    haunted by the ghost of her deceased daughter. The book explores themes of memory, trauma, and the legacy of 
    slavery, examining the emotional and psychological scars left on individuals and communities by the institution 
    of slavery.
    """,

    "Kurt Vonnegut": """
    "Slaughterhouse-Five" is a novel by Kurt Vonnegut that blends science fiction with historical fiction to tell 
    the story of Billy Pilgrim, a soldier who becomes "unstuck in time" and experiences events from his life, including 
    his time as a soldier in World War II and his abduction by aliens. The novel explores themes of fatalism, free will, 
    and the effects of war on the human psyche.
    """,

    "Chimamanda Ngozi Adichie": """
    "Half of a Yellow Sun" is a novel by Chimamanda Ngozi Adichie set during the Nigerian Civil War. The story follows 
    the lives of three characters—Ugwu, a houseboy; Olanna, a professor; and Richard, a writer—as their lives are 
    impacted by the conflict. The novel explores themes of identity, love, and the effects of war on personal and 
    political levels.
    """,

    "Harlan Ellison": """
    "I Have No Mouth, and I Must Scream" is a dystopian science fiction novella by Harlan Ellison that tells the story 
    of a group of survivors trapped in a post-apocalyptic world controlled by a supercomputer named AM. The novella 
    explores themes of suffering, consciousness, and the nature of evil as the characters endure psychological and 
    physical torment.
    """,

    "Philip K. Dick": """
    "Do Androids Dream of Electric Sheep?" is a science fiction novel by Philip K. Dick set in a post-apocalyptic 
    future where Earth is devastated by nuclear war. The story follows Rick Deckard, a bounty hunter tasked with 
    "retiring" rogue androids that have escaped to Earth. The novel explores themes of humanity, identity, and the 
    ethical implications of artificial intelligence.
    """,

    "J.D. Salinger": """
    "Franny and Zooey" by J.D. Salinger is a novel divided into two parts, focusing on the Glass siblings, Franny 
    and Zooey. The story delves into their intellectual and spiritual struggles as they grapple with their family 
    dynamics and personal crises. The novel explores themes of self-discovery, existential angst, and the search for 
    authenticity in a superficial world.
    """,

    "Ernest Hemingway": """
    "The Old Man and the Sea" is a novel by Ernest Hemingway that tells the story of Santiago, an aging Cuban fisherman 
    who struggles to catch a giant marlin after an extended period of bad luck. The novel explores themes of perseverance, 
    dignity, and the human spirit's capacity to endure hardship, reflecting Hemingway's minimalist writing style and 
    philosophical insights.
    """,

    "Leo Tolstoy": """
    "Anna Karenina" is a novel by Leo Tolstoy that explores the life of Anna Karenina, a woman trapped in a loveless 
    marriage who engages in a passionate affair with Count Vronsky. The novel delves into themes of love, society, and 
    morality, offering a panoramic view of Russian society and the conflicts between personal desires and social 
    expectations.
    """,

    "Mary Shelley": """
    "Frankenstein" is a classic novel by Mary Shelley that tells the story of Victor Frankenstein, a scientist who 
    creates a sentient creature in an unorthodox experiment. The novel explores themes of ambition, responsibility, 
    and the consequences of playing God, as well as the ethical implications of scientific experimentation.
    """,

    "H.G. Wells": """
    "The War of the Worlds" is a science fiction novel by H.G. Wells that recounts an alien invasion of Earth by Martians. 
    The story follows the narrator's experiences as humanity faces the existential threat posed by the technologically 
    advanced invaders. The novel explores themes of survival, human resilience, and the impact of technology on society.
    """
}
books_by_authors_2 = {
    "Agatha Christie": """
    "Murder on the Orient Express" is a classic detective novel by Agatha Christie featuring Hercule Poirot, a famous 
    Belgian detective. The story unfolds on the luxurious Orient Express train, where a passenger is murdered. Poirot 
    must solve the case, interviewing the other passengers and uncovering a web of deceit. The novel explores themes 
    of justice, morality, and the intricacies of human behavior.
    """,

    "Dan Brown": """
    "The Da Vinci Code" is a thriller by Dan Brown that follows Robert Langdon, a Harvard professor of symbology, as he 
    investigates a murder in the Louvre Museum. The novel weaves together historical and religious themes, involving a 
    secret society and hidden messages within famous works of art. The story explores themes of faith, secrecy, and the 
    search for truth.
    """,

    "William Faulkner": """
    "The Sound and the Fury" is a novel by William Faulkner that uses stream-of-consciousness narration to depict 
    the decline of the Compson family in the American South. The novel explores themes of time, memory, and the impact 
    of social change, presenting the story from multiple perspectives and highlighting the family's struggles with 
    loss and disintegration.
    """,

    "Ayn Rand": """
    "Atlas Shrugged" is a novel by Ayn Rand that presents her philosophy of Objectivism through a story set in a dystopian 
    future where the world's leading innovators and creators go on strike to protest against a collectivist government. 
    The novel explores themes of individualism, capitalism, and the role of government in society.
    """,

    "John Green": """
    "The Fault in Our Stars" is a contemporary young adult novel by John Green that follows Hazel Grace Lancaster, a 
    teenage cancer patient, and her relationship with Augustus Waters, a fellow cancer survivor. The novel explores 
    themes of love, loss, and the search for meaning in the face of terminal illness, offering a poignant and honest 
    portrayal of the struggles of young people dealing with serious health issues.
    """,

    "David Mitchell": """
    "Cloud Atlas" is a novel by David Mitchell that weaves together six interconnected stories spanning different 
    time periods and genres. The novel explores themes of fate, reincarnation, and the impact of individual actions on 
    the course of history, presenting a complex narrative that challenges conventional storytelling.
    """,

    "Jules Verne": """
    "Twenty Thousand Leagues Under the Sea" is a science fiction novel by Jules Verne that follows the adventures of 
    Professor Aronnax, his servant Ned Land, and a mysterious captain, Nemo, aboard the submarine Nautilus. The story 
    explores themes of exploration, technology, and the natural world as the characters travel through the world's oceans.
    """,

    "C.S. Lewis": """
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe" is a fantasy novel by C.S. Lewis that follows the 
    adventures of four siblings—Peter, Susan, Edmund, and Lucy Pevensie—in the magical land of Narnia. The novel 
    explores themes of good versus evil, bravery, and the power of redemption, set against the backdrop of a land 
    ruled by the White Witch and rescued by the noble lion Aslan.
    """,

    "Roald Dahl": """
    "Charlie and the Chocolate Factory" is a children's novel by Roald Dahl that tells the story of Charlie Bucket, a 
    poor boy who wins a golden ticket to tour Willy Wonka's magical chocolate factory. The novel explores themes of 
    imagination, greed, and the rewards of kindness, offering a whimsical and moralistic tale for young readers.
    """,

    "Philip Roth": """
    "American Pastoral" is a novel by Philip Roth that follows Seymour "Swede" Levov, a successful Jewish-American 
    businessman whose life unravels when his daughter becomes a radical activist. The novel explores themes of 
    identity, family, and the American Dream, examining the impact of societal changes on personal lives.
    """,

    "David Foster Wallace": """
    "Infinite Jest" is a novel by David Foster Wallace that presents a sprawling narrative about a dystopian future 
    dominated by entertainment and addiction. The book explores themes of media saturation, mental health, and the 
    quest for meaning in a hyper-commercialized world, known for its complex structure and deep philosophical insights.
    """,

    "Michael Ende": """
    "The NeverEnding Story" is a fantasy novel by Michael Ende that follows a young boy named Bastian who discovers 
    a magical book that transports him to the world of Fantastica. As Bastian reads, he becomes part of the story, 
    exploring themes of imagination, self-discovery, and the power of storytelling.
    """,

    "Ken Kesey": """
    "One Flew Over the Cuckoo's Nest" is a novel by Ken Kesey that explores life inside a mental institution through 
    the experiences of Randle P. McMurphy, a rebellious patient who challenges the oppressive rules of Nurse Ratched. 
    The novel delves into themes of freedom, conformity, and the nature of sanity and madness.
    """,

    "Hermann Hesse": """
    "Siddhartha" is a novel by Hermann Hesse that tells the story of Siddhartha, a young man in ancient India who 
    embarks on a spiritual journey to find enlightenment. The novel explores themes of self-discovery, the nature 
    of enlightenment, and the quest for personal fulfillment.
    """,

    "Stephen King": """
    "The Shining" is a horror novel by Stephen King that follows Jack Torrance, an aspiring writer who takes a job as 
    the winter caretaker of the isolated Overlook Hotel. As Jack's sanity unravels under the influence of the hotel, 
    the novel explores themes of isolation, madness, and the supernatural, with a focus on the psychological horror 
    of the setting.
    """
}

books_by_authors_3 = {
    "J.R.R. Tolkien": """
    "The Lord of the Rings: The Fellowship of the Ring" is the first volume in J.R.R. Tolkien's epic fantasy trilogy. 
    The story follows Frodo Baggins, a hobbit tasked with destroying the One Ring, a powerful artifact created by 
    the Dark Lord Sauron. Joined by a diverse group of companions, Frodo embarks on a perilous journey to Mordor, 
    encountering various challenges and dark forces. The novel explores themes of friendship, courage, and the 
    struggle between good and evil.
    """,

    "Orson Scott Card": """
    "Ender's Game" is a science fiction novel by Orson Scott Card set in a future where humanity is preparing for an 
    impending alien invasion. The story follows Ender Wiggin, a young boy recruited into a military academy to 
    train as a commander. Through rigorous and often brutal training, Ender must confront complex moral and strategic 
    dilemmas, exploring themes of leadership, ethics, and the nature of war.
    """,

    "Paulo Coelho": """
    "The Alchemist" is a novel by Paulo Coelho that follows Santiago, a young shepherd who dreams of finding a 
    hidden treasure. His journey takes him across the desert and into encounters with various individuals who offer 
    wisdom and guidance. The novel explores themes of destiny, personal legend, and the importance of pursuing one’s 
    dreams.
    """,

    "Khaled Hosseini": """
    "The Kite Runner" is a novel by Khaled Hosseini that tells the story of Amir, a young boy from Kabul who betrays 
    his loyal friend Hassan. As Amir grows up and moves to the United States, he is haunted by his past actions and 
    seeks redemption. The novel explores themes of friendship, guilt, and the impact of personal choices on one's 
    life and relationships.
    """,

    "George R.R. Martin": """
    "A Game of Thrones" is the first book in George R.R. Martin's epic fantasy series, "A Song of Ice and Fire." The 
    novel is set in the fictional continents of Westeros and Essos and follows the complex political and dynastic 
    struggles among several noble families. Themes of power, betrayal, and honor are central as the characters vie 
    for control of the Iron Throne and navigate a world filled with intrigue and danger.
    """,

    "Douglas Adams": """
    "The Hitchhiker's Guide to the Galaxy" is a comedic science fiction novel by Douglas Adams that follows Arthur 
    Dent, an ordinary human who is saved from Earth’s destruction by an alien named Ford Prefect. The novel explores 
    Arthur's adventures across the galaxy, involving eccentric characters and absurd situations, and delves into 
    themes of randomness, bureaucracy, and the meaning of life.
    """,

    "Richard Adams": """
    "Watership Down" is a novel by Richard Adams that follows a group of rabbits as they flee their warren and seek 
    a new home. The story explores themes of leadership, survival, and community as the rabbits face various dangers 
    and challenges on their journey. The novel combines adventure with philosophical insights about nature and society.
    """,

    "E.M. Forster": """
    "A Passage to India" is a novel by E.M. Forster set during British rule in India. It explores the complexities 
    of British-Indian relations through the experiences of Dr. Aziz, an Indian physician, and his interactions with 
    British expatriates. The novel delves into themes of colonialism, cultural misunderstanding, and the search for 
    personal connection.
    """,

    "James Joyce": """
    "Ulysses" is a groundbreaking modernist novel by James Joyce that follows the experiences of Leopold Bloom in 
    Dublin on June 16, 1904. The novel is known for its stream-of-consciousness narrative, intricate structure, 
    and deep exploration of themes such as identity, time, and the human experience. Joyce's work challenges conventional 
    narrative forms and provides a rich, complex reading experience.
    """,

    "Zadie Smith": """
    "White Teeth" is a novel by Zadie Smith that examines the lives of two families of mixed heritage living in London. 
    The novel explores themes of identity, multiculturalism, and family dynamics through interconnected stories and 
    characters spanning different generations. Smith's work offers a vibrant portrayal of contemporary urban life and 
    social issues.
    """,

    "Jean-Paul Sartre": """
    "Nausea" is a novel by Jean-Paul Sartre that follows Antoine Roquentin, a historian who experiences a profound 
    existential crisis and sense of alienation. The novel explores themes of existentialism, freedom, and the absurdity 
    of existence as Antoine grapples with the meaning of his own life and the nature of reality.
    """,

    "Salman Rushdie": """
    "Midnight's Children" is a novel by Salman Rushdie that tells the story of Saleem Sinai, who is born at the exact 
    moment of India's independence. The novel intertwines Saleem's personal life with the historical events of post-colonial 
    India, exploring themes of identity, politics, and magic realism as Saleem navigates the challenges of his extraordinary 
    life.
    """,

    "Ian McEwan": """
    "Atonement" is a novel by Ian McEwan that follows the lives of Briony Tallis and her family, focusing on a 
    misunderstanding that has far-reaching consequences. The novel explores themes of guilt, redemption, and the impact 
    of personal actions on others, spanning several decades and providing a deep, introspective look at the characters' 
    lives and relationships.
    """,

    "Milan Kundera": """
    "The Unbearable Lightness of Being" is a novel by Milan Kundera that explores the lives of four individuals in 
    Czechoslovakia during the 1960s. The novel delves into themes of love, politics, and existential philosophy, examining 
    the tension between personal freedom and political oppression, and the search for meaning in a world marked by 
    uncertainty.
    """
}

books_by_authors_4 = {
    "Stephen King": """
    "It" is a horror novel by Stephen King that follows a group of children who are terrorized by a malevolent entity 
    that appears every 27 years in the town of Derry. The novel repeatedly emphasizes the cycle of fear and the 
    return of the creature, which takes the form of a clown named Pennywise. The story revolves around the themes 
    of childhood trauma, the power of memory, and the recurring nature of evil as the children confront their worst 
    fears and return as adults to face the entity once more.
    """,

    "George R.R. Martin": """
    "A Storm of Swords" is the third book in George R.R. Martin's epic series, "A Song of Ice and Fire." The novel 
    focuses on the ongoing battles for the Iron Throne and the repeated conflicts among the noble families of Westeros. 
    Themes of power, betrayal, and vengeance recur throughout the novel, with characters frequently confronting 
    their rivals and facing repeated cycles of violence and political intrigue.
    """,

    "J.K. Rowling": """
    "Harry Potter and the Prisoner of Azkaban" is the third book in J.K. Rowling's series about Harry Potter. The 
    novel focuses on the recurring threats from the dark wizard Sirius Black and the repeated challenges Harry faces 
    at Hogwarts. Themes of fear, mystery, and the return of past enemies are emphasized as Harry uncovers truths about 
    his past and faces dangers that reappear from previous years.
    """,

    "H.P. Lovecraft": """
    "The Shadow over Innsmouth" is a horror novella by H.P. Lovecraft that centers on a town plagued by recurring 
    supernatural events and dark rituals. The story emphasizes the repeated cycles of strange occurrences and the 
    sinister influence of the Deep Ones, an aquatic, otherworldly race that continuously haunts the town's inhabitants. 
    Themes of dread and cosmic horror pervade the narrative, with the repetition of unsettling events creating an 
    atmosphere of perpetual menace.
    """,

    "Philip K. Dick": """
    "Do Androids Dream of Electric Sheep?" features repeated themes of identity and humanity as Rick Deckard hunts 
    down rogue androids. The novel emphasizes the recurring question of what it means to be human, with Deckard constantly 
    grappling with his own beliefs and the repeated challenges posed by the advanced, indistinguishable androids he 
    encounters.
    """,

    "Ursula K. Le Guin": """
    "The Dispossessed" is a novel by Ursula K. Le Guin that explores the repeated struggles of its protagonist, Shevek, 
    as he seeks to bridge two opposing worlds: an anarchist society and a capitalist one. The novel repeatedly addresses 
    themes of isolation, revolution, and the cyclical nature of societal conflict, reflecting on how these struggles 
    reappear throughout history.
    """,

    "Orson Scott Card": """
    "Ender's Game" features repeated training simulations and battles that emphasize the cyclical nature of conflict 
    and strategy. Ender Wiggin faces recurring tests and challenges as he prepares for an anticipated alien invasion. 
    The novel highlights the recurring themes of leadership, strategy, and the repetition of conflict in a futuristic 
    setting.
    """,

    "Dan Brown": """
    "Angels & Demons" is a thriller by Dan Brown that revolves around the repeated motifs of secret societies and 
    hidden codes. The story repeatedly delves into themes of conspiracy and historical mystery as Robert Langdon uncovers 
    clues and faces repeated dangers related to an ancient secret organization. The novel’s focus on hidden messages 
    and recurring symbols drives the plot forward.
    """,

    "Margaret Atwood": """
    "Oryx and Crake" is a dystopian novel by Margaret Atwood that features repeated references to genetic manipulation 
    and environmental collapse. The story repeatedly emphasizes the consequences of scientific experimentation and 
    the recurring theme of humanity's impact on the world. The novel explores the cyclical nature of ecological and 
    societal decline.
    """,

    "Isaac Asimov": """
    "Foundation and Empire" is the second book in Isaac Asimov's Foundation series. The novel emphasizes the repeated 
    cycles of conflict and political intrigue as the Foundation faces new threats from the remnants of the Galactic Empire. 
    Themes of rebellion, power, and the cyclical nature of history are central as characters repeatedly confront the 
    challenges of preserving their nascent society.
    """,

    "Ray Bradbury": """
    "The Martian Chronicles" is a science fiction novel by Ray Bradbury that repeatedly explores the theme of human 
    colonization of Mars and the consequences of this expansion. The narrative emphasizes the recurring motifs of 
    change, adaptation, and the impact of humanity's actions on an alien world, reflecting on the cyclical nature of 
    human history and its repetition in new contexts.
    """,

    "J.D. Salinger": """
    "The Catcher in the Rye" features repeated themes of alienation and disillusionment as Holden Caulfield navigates 
    his teenage years in New York City. The novel repeatedly addresses Holden's struggle with the phoniness of society 
    and his recurring desire to protect innocence, reflecting his internal conflicts and the repetition of his personal 
    struggles.
    """,

    "Ernest Hemingway": """
    "For Whom the Bell Tolls" is a novel by Ernest Hemingway that emphasizes the recurring themes of war and personal 
    sacrifice. The story repeatedly explores the impact of the Spanish Civil War on the protagonist, Robert Jordan, 
    and his comrades, highlighting the cyclical nature of violence and the recurring sense of duty and loss.
    """,

    "Jane Austen": """
    "Emma" is a novel by Jane Austen that features repeated themes of social status and romantic misunderstandings. 
    The story repeatedly addresses Emma Woodhouse's attempts to matchmake and her evolving perceptions of love and 
    friendship, reflecting the recurring nature of social dynamics and personal growth.
    """,
}

books_by_authors_5 = {
    "Toni Morrison": """
    "Song of Solomon" is a novel by Toni Morrison that repeatedly explores themes of identity and family heritage. 
    The story follows Milkman Dead, whose journey to uncover his family's history involves repeated encounters with 
    the past and the recurring struggles of his ancestors. The novel emphasizes the cyclical nature of personal and 
    cultural history.
    """,

    "Herman Melville": """
    "Moby-Dick" is a classic novel by Herman Melville that emphasizes the repeated obsession of Captain Ahab with 
    hunting the white whale, Moby Dick. The novel's recurring themes of vengeance, fate, and the struggle between 
    man and nature drive the narrative, with Ahab's relentless pursuit being a central motif throughout the story.
    """,

    "F. Scott Fitzgerald": """
    "The Great Gatsby" features repeated motifs of wealth and social status as it explores Jay Gatsby's quest to 
    reclaim his lost love, Daisy Buchanan. The novel repeatedly highlights themes of the American Dream and the 
    illusion of success, with Gatsby's repetitive attempts to recreate the past reflecting the novel's central themes.
    """,

    "J.D. Salinger": """
    "Franny and Zooey" is a novel by J.D. Salinger that repeatedly addresses themes of spiritual and intellectual 
    search. The story focuses on the Glass siblings, who repeatedly grapple with their personal and familial struggles, 
    reflecting their search for meaning and authenticity.
    """,

    "Aldous Huxley": """
    "Brave New World" features repeated themes of technological control and societal conditioning. The novel 
    emphasizes the recurring impact of a dystopian society's obsession with stability and consumerism, with characters 
    repeatedly confronting the consequences of a world stripped of individuality and genuine emotion.
    """,

    "James Joyce": """
    "Ulysses" is known for its repeated narrative techniques and stream-of-consciousness style. The novel explores 
    recurring themes of identity and time as it follows Leopold Bloom through a single day in Dublin, reflecting the 
    cyclical nature of human experience and consciousness.
    """,

    "William Faulkner": """
    "As I Lay Dying" is a novel by William Faulkner that emphasizes the repeated struggles of the Bundren family as 
    they transport their deceased mother to her hometown for burial. The novel features recurring themes of family 
    conflict, perseverance, and the impact of personal burdens on the characters' lives.
    """,

    "John Steinbeck": """
    "Of Mice and Men" is a novel by John Steinbeck that repeatedly explores themes of friendship and the pursuit 
    of dreams in the context of economic hardship. The story follows George and Lennie as they repeatedly face 
    challenges and setbacks while striving for a better future, reflecting the cyclical nature of their struggles.
    """,

    "John Green": """
    "Looking for Alaska" is a novel by John Green that explores the repeated themes of loss and self-discovery. 
    The story follows Miles Halter as he navigates the impact of a tragic event and repeatedly seeks meaning in 
    his relationships and experiences, reflecting themes of growth and the search for identity.
    """,

    "Leo Tolstoy": """
    "Anna Karenina" is a novel by Leo Tolstoy that repeatedly addresses themes of love, infidelity, and social 
    expectations. The story follows Anna's tumultuous relationships and the recurring societal pressures that 
    influence her choices, reflecting the novel's exploration of personal and social conflicts.
    """,

    "H.G. Wells": """
    "The War of the Worlds" is a science fiction novel by H.G. Wells that features repeated themes of alien invasion 
    and human survival. The story emphasizes the recurring threat of extraterrestrial forces and the continuous 
    struggle for survival as humanity faces unprecedented challenges.
    """,

    "Marcel Proust": """
    "In Search of Lost Time" is a novel by Marcel Proust that repeatedly explores themes of memory and time. The 
    narrative emphasizes the cyclical nature of personal recollections and the repetitive nature of the narrator's 
    experiences as he reflects on his past and the passage of time.
    """,
}

books_by_authors_6 = {
    "Gabriel Garcia Marquez": """
    "One Hundred Years of Solitude" is a novel by Gabriel Garcia Marquez that repeatedly explores the theme of 
    solitude across several generations of the Buendia family. The narrative emphasizes the cyclical nature of history 
    and personal struggles, with repeated motifs of magical realism and recurring patterns of behavior influencing 
    the characters' lives.
    """,

    "Ray Bradbury": """
    "Fahrenheit 451" is a dystopian novel by Ray Bradbury that features recurring themes of censorship and the 
    suppression of knowledge. The novel repeatedly explores the consequences of a society that burns books and the 
    characters' ongoing struggles to find and preserve truth in a world of conformity and control.
    """,

    "Jules Verne": """
    "Journey to the Center of the Earth" is a novel by Jules Verne that repeatedly emphasizes themes of exploration 
    and adventure. The story follows a team of explorers who face recurring challenges and discoveries as they delve 
    into the depths of the Earth, highlighting their repeated encounters with the unknown and their perseverance.
    """,

    "Daphne du Maurier": """
    "Rebecca" is a novel by Daphne du Maurier that features recurring themes of memory and identity. The story repeatedly 
    explores the impact of the deceased Rebecca on the lives of the characters, with the novel’s narrative reflecting 
    the ongoing influence of Rebecca’s presence and the repeated uncovering of past secrets.
    """,

    "Oscar Wilde": """
    "The Picture of Dorian Gray" is a novel by Oscar Wilde that repeatedly explores themes of vanity and moral 
    corruption. The story follows Dorian Gray's repeated indulgence in a life of excess and his attempt to escape 
    the consequences of his actions through the supernatural portrait that ages in his place.
    """,

    "Chuck Palahniuk": """
    "Fight Club" is a novel by Chuck Palahniuk that repeatedly addresses themes of identity and consumerism. The 
    story emphasizes the recurring struggles of the narrator as he grapples with his sense of self and his involvement 
    in the underground fight club, reflecting themes of disillusionment and societal critique.
    """,

    "Kurt Vonnegut": """
    "Slaughterhouse-Five" is a novel by Kurt Vonnegut that features repeated themes of time travel and the impact 
    of war. The story follows Billy Pilgrim's recurring experiences of being "unstuck in time," highlighting the 
    cyclical nature of trauma and the ongoing effects of conflict on his life.
    """,

    "Margaret Atwood": """
    "The Handmaid's Tale" is a dystopian novel by Margaret Atwood that repeatedly explores themes of control and 
    resistance. The story emphasizes the recurring struggles of women in a totalitarian society and their attempts 
    to reclaim autonomy and identity amidst oppressive conditions.
    """,

    "Thomas Hardy": """
    "Tess of the d'Urbervilles" is a novel by Thomas Hardy that features recurring themes of social injustice and 
    personal suffering. The story follows Tess as she repeatedly faces societal and personal challenges, reflecting 
    the novel's exploration of fate and the harsh realities of Victorian society.
    """,

    "William Golding": """
    "Lord of the Flies" is a novel by William Golding that emphasizes repeated themes of savagery and civilization. 
    The story explores the recurring breakdown of order among a group of boys stranded on an island, highlighting 
    the repeated descent into chaos and the inherent violence within human nature.
    """,

    "E.M. Forster": """
    "Howards End" is a novel by E.M. Forster that repeatedly addresses themes of class and social change. The story 
    follows the interactions of the Schlegel and Wilcox families, emphasizing the recurring conflicts and evolving 
    relationships as they navigate societal shifts and personal values.
    """,
}
