# Data Processing in Python (JEM207)

The course site for Data Processing in Python (JEM207) at IES FSV CUNI. See information on [SIS](https://is.cuni.cz/studium/predmety/index.php?do=predmet&kod=JEM207).

The course is taught by [Josef Kurka](mailto:josef.kurka@fsv.cuni.cz). 

## Upcoming project work

0) Matching document: [link](https://docs.google.com/spreadsheets/d/1i35pSZcNPoxzA7_RwpYkGdjvlNV8YXt2SdojpBzLV-w/edit?usp=sharing)
1) Approval of project proposals - 27/4/2025
2) Work-in-progress consultations - 05/2026
3) Project submissions - 14/6/2026

Final project **deadline**: June 14, 2026 before midnight. Late submissions will be awarded **0 points**.

- **Submit link to your project github repository** via Google forms [link TBD]

## Information for the summer semester of 2025/2026

## FAQ - pre semester

* If you are on **waiting list** there is *nothing* we can do to enroll you. We managed to master somehow `python`, but SIS is something else. We follow the rules. Students usually drop from the course during the first week of the semester so **there is a good chance** you will be able to register.

## Schedule (updated February 14)

Here's your schedule with the semester beginning on February 16:  

| WEEK | DATE | L/S | TOPIC | DEADLINE |
| --- | --- | --- | --- | --- |
| 1 | 16/2 | S | Setup (Jupyter, VScode, Git, OS basics) | |
| 1 | 18/2 | L | Python basics | |
| 2 | 23/2 | L | Python basics II | |
| 2 | 25/2 | S | Basics | |
| 3 | 2/3 | L | Numpy | HW 1 |
| 3 | 4/3 | S | Numpy | |
| 4 | 9/3 | L | Pandas I | |
| 5 | 16/3 | L | Pandas II + Matplotlib | |
| 6 | 23/3 | S | Pandas | |
| 7 | 30/3 | L | Data formats, APIs | HW 2  |
| 7 | 1/4 | S | Data formats, APIs |  |
| 8 | 6/4 | - | Easter - **no lecture** | |
| 8 | 8/4 | L | Algorithmic problem solving | HW 3 |
| 9 | 13/4 | - | **MIDTERM** | |
| 9 | 15/4 | S | Midterm solution | |
| 10 | 20/4 | L | Data science | |
| 10 | 22/4 | S | Data science case-study | |
| 11 | 27/4 | L | How to code (avoiding spaghetti code) | Project proposal approval |
| 12 | 29/4 | L | Mixed topics: pkg, tests, docs, sql |  |
| 12 | 4/5 | L | Guest Lecture: TBA | |
| 13 | 11/5 | - | Project work | |
| 15 | 18/5 - 22/5 | - | **WiP:** Project consultations | |
| 16 | 25/5 - 29/5 | - | **WiP:** Project consultations | |
| 17 | 14/6 | - | **Deadline Final Project** - submit | Project submission |

Topics of the last weeks of the semester might be changed.

Let me know if you need any other adjustments! 😊
  
## Course requirements

The requirements for passing the course are homeworks (**5pts**), the midterm (**25pts**), work in-progress presentation (**10pts**), and the final project (**60pts**).

At least 50% from the **work-in-progress** presentation  and **final project** is required for passing the course.

Credit load 5 ECTS equivalent to 125+ hours of student work:

* participation lecture time - 16 hours
* participation seminar time - 9 hours
* homework assignments - 5 hours
* midterm preparation - 20 hours
* project work - 50 hours
* additional home study - 25 hours

### Final project (60%)

* Students in teams by 2
* Submit your proposal [TBD]()
* Deadline for topic submission (week to consult): April 20, 2026
* Deadline to attend the WiP consultation: May 29, 2026, [link here]
* Deadline for completed project: June 14, 2026 

#### Projects' Evaluation criteria

* Use of git by both students - 5 pts
  * meaningful commit messages
* Runnable code - 10 pts
  * by far the most important one! The project needs to run from scratch after installing versioned requirements.
* Pythonic code principles and structure - 20 pts
  * Provide requirements.txt file of the dependencies with versions (can use pip freeze) so that we can install with `pip install -r requirements.txt`
  * code is more often read than written, EAFP (Easier to Ask for Forgiveness than Permission)
  * functions (classes), properly named variables
  * following Python style guidelines
  * README
  * documentation
  * proper repository structure
* Analysis, visualization - 10 pts
  * highlight key points of your project, give it some narrative
* Originality, difficulty - 15 pts
  * insightful application on a topic you are passionate about
  * project is sufficiently elaborate
  * analysis is interactive
  * difficulty to download the data and the scope of the dataset
  * the goal is to challenge yourselves and learn something new, regardless if you're a Python novice or you write python code every week

## Project work - presentation (10%)

* Brief presentation of work-in-progress related to the final project.
* You should have 50% of your project completed at this stage.
* Prepare questions, understand the goals of your project

## Midterm exam (25%)

* Live coding (80 minutes), "open browser", no collaboration between the students.
* No artificial intelligence
* More details during the lecture the week before

## Homework Assignments (5%)

* Create [leetcode.com](https://leetcode.com) account
* You are expected to submit in the following [Google Form](https://forms.gle/ic5Hd19mFpsSr9nV6) (please make sure to use your Charles University email address, xxxxxxxx@fsv.cuni.cz):
  * Link to the problem
  * Print page showing your solution and submission statistics
    * Like this: [Path Sum III - Submission Detail - LeetCode.pdf](/files/PathSumIII-SubmissionDetail-LeetCode.pdf)
    * **EDIT:** You can access the **statistics** of your **solution** (even it is not accepted by *leetcode*) via the top right button to your `profile`. You go to your `submissions`, then column `status` and you obtain the `solution details`. These details you save/print to `.PDF` and upload. **Your `name` or `e-mail` must be legible in the PDF of your submission**
  * Plain text of your script (in python 3!)

* Rules:
  * Do not use **AI tools**. The purpose of the homeworks is to get hands on experience with coding in Python, not to get cheap points by cheating. We will make an effort to find out, and you will be penalized as per academic integrity guidelines. 
    * Have fun and try to beat the world!
    * Your submission will ideally be accepted by leetcode, but send us your best attempt regardless, you can still get the points. If anything, try to optimize run time, do not worry about memory.
    * You will struggle, but if you solve many of those, your next stop is Google cafeteria as an employee!
    * If you cannot decide, there is a shuffle button which will pick something for you.

* HW 1 (1 pts):
  * Choose one of the easy problems. Have fun and send us how far you have got!
    * Example: [Two Sum](https://leetcode.com/problems/two-sum/)
* HW 2 (2 pts):
  * One Medium problem
    * Must be from [Pandas set of problems](https://leetcode.com/problemset/pandas/)
* HW 3 (2 pts):
  * TBD