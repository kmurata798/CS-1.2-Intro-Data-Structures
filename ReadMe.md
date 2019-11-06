# CS 1.2: How Data Structures Work

## Course Description

A project based course that looks under the hood at data structures and algorithms to see how they work. In addition to implementing these structures in an application; students will build them from scratch, analyze their complexity, and benchmark their performance to gain an understanding of their tradeoffs and when to use them in practice. Students will write scripts, functions, and library modules to use text processing tools like regular expressions, construct and sample probability distributions to create a Markov language model and gain insight into how grammar works and natural language processing techniques.


## Repository Setup

:warning: **Important:** Please follow [these instructions](Setup.md) exactly to set up your clone of this course repository.


## Schedule

**Course Dates:** Monday, October 21 – Wednesday, December 11, 2019 (7.5 weeks)

**Class Times:** Monday & Wednesday at 1:30-3:20pm (section A) or 3:30–5:20pm (section B)


| Class |    Date     |              Topics               |
|:-----:|:-----------:|:---------------------------------:|
|   1   | Mon, Oct 21 | [Strings & Random Numbers][]      |
|   2   | Wed, Oct 23 | [Histogram Data Structures][]     |
|   3   | Mon, Oct 28 | [Probability & Sampling][]        |
|   4   | Wed, Oct 30 | [Flask Web App Development][]     |
|   5   | Mon, Nov  4 | [Application Architecture][]      |
|   6   | Wed, Nov  6 | [Generating Sentences][]          |
|   7   | Mon, Nov 11 | [Arrays & Linked Lists][]         |
|   8   | Wed, Nov 13 | Linked List [Algorithm Analysis][] |
|   9   | Mon, Nov 18 | [Hash Tables][]                   |
|  10   | Wed, Nov 20 | Hash Table [Algorithm Analysis][] |
|  11   | Mon, Nov 25 | Project Lab Day                   |
|   –   | Wed, Nov 27 | *No Class (Thanksgiving Break)*   |
|  12   | Mon, Dec  2 | [Higher Order Markov Chains][]    |
|  13   | Wed, Dec  4 | [Regular Expressions][]           |
|  14   | Mon, Dec  9 | Time to Tweet & Launch Day!       |
|  15   | Wed, Dec 16 | *Final Exam (Tentative)*          |

[Strings & Random Numbers]: Lessons/RandomStrings.md
[Histogram Data Structures]: Lessons/Histograms.md
[Probability & Sampling]: Lessons/Probability.md
[Flask Web App Development]: Lessons/FlaskWebApp.md
[Application Architecture]: Lessons/Architecture.md
[Generating Sentences]: Lessons/Sentences.md
[Arrays & Linked Lists]: Lessons/ArraysLinkedLists.md
[Hash Tables]: Lessons/HashTables.md
[Algorithm Analysis]: Lessons/AlgorithmAnalysis.md
[Higher Order Markov Chains]: Lessons/MarkovChains.md
[Regular Expressions]: Lessons/RegularExpressions.md


## Prerequisites

Students must pass the following course and demonstrate mastery of its competencies:
-   [CS 1.1: Programming Fundamentals](https://make.sc/cs11)


## Learning Objectives

By the end of this course, students will be able to:
1.   Create Python programs that read and write text files and manipulate strings
1.   Build web apps with the Flask framework and deploy to the web
1.   Construct and sample probability distributions based on observed word frequencies
1.   Create Markov language models and use them to generate new sentences
1.   Use unit tests that assert correct behavior of functions and classes
1.   Implement core data structures including singly linked lists and hash tables
1.   Analyze the complexity of iterative algorithms and data structures with visual loop counting


## Project Tutorial

Students will complete the following guided project tutorial in this course:
-   [Tweet Generator: Data Structures & Probability with Python](http://make.sc/oa-tweet-generator)


## Evaluation

To pass this course, students must meet the following requirements:
-   Actively participate in class and abide by the attendance policy
-   Make up all classwork from all absences
-   Complete the required project tutorial
-   Pass the project according to the [associated project rubric](https://make.sc/cs11-rubric)
-   Pass the summative assessment (final exam)


## Attendance

Just like any job, attendance at Make School is required and a key component of your success. Attendance is being onsite from 9:30am to 5:30pm each day, attending all scheduled sessions including classes, huddles, coaching and school meetings, and working in the study labs when not in a scheduled session. Working onsite allows you to learn with your peers, have access to support from TAs, instructors and others, and is vital to your learning.

Attendance requirements for scheduled sessions are:
-   No more than two unexcused absences ("no-call-no-shows") per term in any scheduled session.
-   No more than four excused absences (communicated in advance) per term in any scheduled session.

Failure to meet these requirements will result in a Participation Improvement Plan (PIP).
Failure to improve after the PIP is cause for not being allowed to continue at Make School.


## Make School Policies

-   [Academic Honesty](https://make.sc/academic-honesty)
-   [Accomodation Policy](https://make.sc/accommodations-for-students)
-   [Attendance Policy](https://make.sc/attendance-policy)
-   [Diversity Statement](https://make.sc/diversity-and-inclusion-policy)
-   [Grading System](https://make.sc/grading-system)
-   [Program Learning Outcomes](https://make.sc/program-learning-outcomes)
-   [Title IX Disclaimer](https://make.sc/title-ix-policy)

## Step 6 QUESTIONS:
1. What are the key feature of the app? Are these clearly separated into their own files, classes, and/or modules?

A:  
    Key features are: —> ``Reading from a file to create a histogram; Pick a specific histogram word; Output the histogram word; Arranging the histogram word in a specific order to form a sentence; and Randomizing the output based on the ratio of the histogram word values.

    Yes these key features are separated into different files/modules.
———————=======================================================================---------------------------
2. Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?

A:  
    The names are appropriate but may be more accurate if I were to change some of the names. I could make the names more descriptive possibly, or combine some together that would have relations with each other.
———————=======================================================================---------------------------
3. What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?

A:  
    Scopes of variables are the ways to restrict the access of certain variables to be used in a functions or classes.
    
    Scope of variables are needed to have the ability to use specific functions for certain tasks throughout the project.
———————=======================================================================---------------------------
4.  Are the functions small and clearly specified, with as few side effects as possible?

A:  
    Yes, the functions are small and clearly specified with small numbers of parameters to keep the project more organized.
———————=======================================================================---------------------------
5. Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?

A:  
    Yes there could be, the dictionary, list, and tuple data structures can be combined into a class and vary different methods based on the data structure requested.
———————=======================================================================---------------------------
6. Can files be used as both modules and as scripts?

A:  
    Yes, files can be used as both modules and scripts. 

    The difference is that scripts are usually relatively short and not meant to be linked with other files.

    Modules on the other hand are code files that are more suited for being imported to other files.
———————=======================================================================---------------------------
7. Do modules all depend on each other or can they be used independently?

A:  Both answers are viable. Modules can either be imported into other modules, or they can be used to run as scripts which aren’t meant to be imported into other files. Modules that share code don’t execute any code, but rather share its functions, variables, and parameters with the other files it is imported into.
