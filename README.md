# Exercise 1

## Introduction
#### Overall Goal
In exercise 1, you implement a module called `lyrics_processor`. The module offers functionalities to transform lyrics into a structure that is easier to analyze.
You use Test Driven Development (TDD) to develop your code and you control its versioning via GitLab. 

Therefore, start by forking this project which means creating a personal copy of the exercise repository. Have a look at the `how_to_exercises.pdf` on `OLAT > Material > Tutorial` to familiarise yourself on how to get and hand in the exercises.

Look at the tutorial videos on the [Tutorial Stream Channel](https://web.microsoftstream.com/channel/6d8c8dd6-c5ab-489e-b268-de97a017c142) (also accessible via MS Teams Channel “Tutorial” > Tab “Tutorial Videos”), the [git exercise](https://gitlab.uzh.ch/pcl2-2021-assignments/git-exercise) and the tutorial slides on `OLAT > Material > Tutorial` to get to know the most important git commands and how to work with git in different environments.

Use modules from python’s standard library only, unless it is stated otherwise in the exercise description.

#### Unit Tests
For each task, you first define unit tests so that you can verify the correctness of your implementation. The file `sample_lyrics.txt` contains some example lyrics that you can use for testing. 
In `lyrics_processor.py` and `lyrics_processor_test.py` there is already a code skeleton. Extend the latter by adding at least two additional calls of an assertion method for every function to be tested. The completed `lyrics_processor_test` module should be handed in besides the `lyrics_processor` module.

#### Functionalities
Implement the functionalities according to their specification in the tests. To verify the basic technical requirements (e.g. does the function exist, is the interface correct?), we provide you with some non-functional tests. They can be found in `lyrics_processor_test.py` and check if your function's output returns the type that is specified in the task. They do not check specific behaviours of the function, so if they pass, it does not mean automatically that the whole function is implemented correctly.

#### Deliverables
* `lyrics_processor` module containing the required functions
* `lyrics_processor_test` module with your own assertions added
* text file with written answers for task 5

Please solve and hand in the exercise in groups of two. Add the names of the authors and their immatriculation number to every file you hand in. To hand in the exercise, you need to make sure that you add all tutors as 'Reporters' to your project and create a release. **Only projects with a release created before the deadline will be considered.**

usernames of tutors:
* bernailke.ersoy
* veralara.bernhard
* florina.vogel

The deadline for handing in your solution is **16th March 2021, 23:59**.


## Task 1
Write a function `split_up_lines(lyrics_str: str) -> List[str]` to split the lyrics of a song into its lines. The dataset contains one song per line, and the individual lines of a song are separated by a dot.


#### Example 
```
split_up_lines('It was you,. That showed me who I am..') -> ['It was you,', 'That showed me who I am.']
```

#### Outcome

* 2 test assertions in addition to the one provided

* Implementation of function `split_up_lines(lyrics_str: str) -> List[str]`



## Task 2
Write a function `tokenize_lines(split_lyrics: List[str]) -> List[List[str]]` to transform the lines into tokens. Usually, whitespace and punctuation are an indicator of token separators. You should also remove double quotation marks (") in this step, as they don't provide substantial semantic information for our purpose and might get in our way when we process lyrics, as the corpus we will be working with in the upcoming exercises has an irregular usage of those.

#### Example 
```
tokenize_lines(['It was you,', 'That showed me who I am.']) -> [['It', 'was', 'you', ','], ['That', 'showed', 'me', 'who', 'I', 'am', '.']]
tokenize_lines(['""Sometimes it lasts in love, but sometimes it hurts instead""']) -> [['Sometimes', 'it', 'lasts', 'in', 'love', ',', 'but', 'sometimes', 'it', 'hurts', 'instead']]
```

#### Outcome

* 2 test assertions in addition to the one provided

* Implementation of function `tokenize_lines(split_lyrics: List[str]) -> List[List[str]]`



## Task 3
Write a function `filter_profanity(tokenized_lyrics: List[List[str]], filename: str) -> Tuple[List[List[str]], int]` that finds profane words according to the list given in `profane_words.txt` and replaces them with the equivalent number of '#' (i.e. number of characters = number of '#'). Furthermore, the function should count how many words have been replaced (profanity score). 


#### Example 
```
filter_profanity([['Huh', ',', 'it's', 'pissing', 'me', 'off', '.'], ['Rock', 'me', 'baby']]) -> ([['Huh', ',', 'it's', '#######', 'me', 'off', '.'], ['Rock', 'me', 'baby']], 1)
```

#### Outcome

* 2 test assertions in addition to the one provided

* Implementation of function `filter_profanity(tokenized_lyrics: List[List[str]], filename: str) -> Tuple[List[List[str]], int]`



## Task 4
Write a function `print_lyrics(processed_lyrics: List[List[str]]) -> None`
that prints the tokenized and processed lyrics in a readable way, line by line. No tests needed for this one. 


## Task 5
a) List three advantages or disadvantages of Test Driven Development. In addition, describe an example where TDD has affected the way you have implemented a function. 

b) What did you test in your unit tests? Please list at least three different test criteria.

c) Please give us a short feedback about the exercise. How long did it take you to solve the tasks? Where did you have difficulties? What was easy to handle? Did you gain any new knowledge by solving the exercise?

#### Outcome

* Answers to questions a-c in a separate text file `task_5.txt`.

## Data Sources

`sample_lyrics.txt`: https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres?select=lyrics-data.csv

`profane_words.txt`: https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
