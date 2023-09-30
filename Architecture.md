SPACE TIME
    - Handle the state of time of an obj in the program.
    - Present returns true if an obj is within 100ms +/- datetime.now
    - Past returns True if the obj is less (<) 100ms - datetime.now
    - Future returns True if the obj is greater (>) 100ms + datetime.now

STORAGE
    - Handles data in the program
    - Will contain multiple storage files like json
    - Main.json: this is the main storage of the program
        - It stores a reference to the different storages in the programs
    - create a storage file as it discovers more
    - Maps to images using pillow python3 library
    - Load into the memory when the program is up and running using multiprocessing library

Web scrapping
    - Using the request, and other scrapping library to scrap information from the internet when it is idle
 
Cache
    - Stores a number of most used files in the program and load them first hand when the program starts running.

Background operations
    - which means the programs runs some calculations in the background to arrive at its own conclusion
    - This can be equivalent the human taught

Pattern Recognition
    - Recognize patterns in text so as to be able to generates its own meaningful text
