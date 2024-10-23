# Data Processing in Python (JEM207)

The course site for Data Processing in Python (JEM207) at IES FSV CUNI. See information on [SIS](https://is.cuni.cz/studium/predmety/index.php?do=predmet&kod=JEM207). The course is taught by [Luboš Hanus](mailto:lubos.hanus@fsv.cuni.cz) and [Vilém Krejcar](mailto:vilem.krejcar@fsv.cuni.cz).

<!-- ## Communication
Please direct all questions to Vílem Krejcar preferably.
-->

## Final project (quick info, more info below)

### Project - paring

* If you are looking for a partner [use this google sheet](https://docs.google.com/spreadsheets/d/1QYylYxtln3RWoOszFfswOXG7KQw69cGdIozcO12K7E8/edit?usp=sharing) with your CUNI account logged in. If you have a partner, delete your info, please, to make it easier for others.

### WiP consultations

Please reserve your date and time of the consultation [Link](https://docs.google.com/spreadsheets/d/1vv13AmQ1eQNxM5v2V0e5vEUc2ibgbjH9wdj-_gyamYc/edit?usp=sharing) - the first two weeks of Jan 2025.

* See full instructions below schedule.

## FAQ - pre semester

* If you are on **waiting list** there is *nothing* we can do to enroll you. We managed to master somehow `python`, but SIS is something else. We follow the rules. Students usually drop from the course during the first week of the semester so **there is a good chance** you will be able to register.

* The course is held **in-person** and there is by default **no online** option.

## Schedule (updated Oct 23)

| WEEK | DATE | L/S | TOPIC | LECTURER | DEADLINE |
| --- | --- | --- | --- | --- | --- |
| 1 | 30/9 | S | Seminar 0: Setup (Jupyter, VScode, Git, OS basics) | Luboš | |
| 1 | 1/10 | L | Python basics | Luboš | |
| 2 | 8/10 | L | Python basics II | Luboš | |
| 3 | 14/10 | S | Seminar 1: Basics | Luboš | |
| 3 | 15/10 | L | Numpy | Luboš | HW 1 |
| 4 | 22/10 | L | Pandas I | Luboš | |
| 5 | 29/10 | L | Pandas II + Matplotlib  | Luboš | HW 2 |
| 6 | 4/11 | S | Seminar 2: Numpy & pandas | Luboš | |
| 6 | 5/11 | L | Data formats, APIs | Luboš | |
| 7 | 11/11-12/11 | S, L | *(almost sure)* A class on Nov 12 | - | - |
| 8 | ~~18/11~~ | ~~S~~ | ~~Seminar 3: Data formats & APIs~~| Luboš | |
| 8 | 19/11 | L | Algorithmic problem solving | Luboš | HW 3 |
| 9 | 25/11 | - | MIDTERM | Luboš & Vilém | |
| 9 | 26/11 | L | Data science | Luboš | |
| 10 | 2/12 | S | Seminar 4: Midterm solution | Vilém | |
| 10 | 3/12 | L | Mixed topics: probably polars, beautifulsoup, SQL, etc. | Luboš | |
| 11 | 9/12 | S | Seminar 5: Data science case-study | Vilém | |
| 11 | 10/12 | L | How to code (avoiding spaghetti code) | Luboš | Project proposal |
| 12 | 17/12 | L | Guest Lecture @ TBA | Luboš & Vilém | |
| 13 | 6/1-8/1 | - | WiP: Project consultations | Luboš & Vilém | |
| 14 | 13/1-15/1 | - | WiP: Project consultations | Luboš & Vilém | |

## Course requirements

The requirements for passing the course are homeworks (5pts), the midterm (25pts), work in-progress-presentation (10pts), and the final project - including the final delivery presentation (60pts).
At least 50% from the homeworks assignments and work-in-progress presentation is required for passing the course.

### Final project (60%)

* Students in teams by 2
* [Submit you proposal here](https://forms.gle/ApDvW7zEToCNjh1SA)
* Deadline for topic approval: 3rd of December 2024
* Deadline: 6rd of February 2025

#### Projects' Evaluation criteria

* Use of git by both - 5pts
  * meaningful commit messages
* Pythonic code principles - 5 pts
  * Provide requirements.txt file of the dependencies with versions (can use pip freeze) so that we can install with `pip install -r requirements.txt`
  * code is more often read than written, EAFP (Easier to Ask for Forgiveness than Permission)
* Runnable code - 15 pts
  * by far the most important one! The project needs to run from scratch after installing versioned requirements.
    * provide requirements.txt file with specific versions of packages (use pip freeze to get it), and specify your precise Python version. 
* Code structure - 15 pts
  * functions (classes), properly named variables
* README, documentation - 5 pts
* Analysis, visualization - 15 pts
  * highlight key points of your project, give it some narrative

## Project work - presentation (10%)

* Presentation of work-in-progress related to the final project.
* Prepare questions, understand the goals of your project

## Midterm exam (25%)

* Live coding (80 minutes), "open browser", no collaboration between the students.
* More details during the lecture the week before

## Homework Assignments (5%)

* Create [leetcode.com](https://leetcode.com) account
* You are expected to submit in a specified [Google form](https://forms.gle/QbjFFcmJwgabbSyA7):
  * Link to the problem
  * Print page showing your solution and submission statistics
    * Like this: [Path Sum III - Submission Detail - LeetCode.pdf](/99_files/PathSumIII-SubmissionDetail-LeetCode.pdf)
    * **EDIT:** You can access the **statistics** of your **solution** (even it is not accepted by *leetcode*) via the top right button to your `profile`. You go to your `submissions`, then column `status` and you obtain the `solution details`. These details you save/print to `.PDF` and upload. **Your `name` or `e-mail` must be legible in the PDF of your submission**
  * Plain text of your script (in python 3!)

* Rules:
  * Do not just copy the public solutions or what ChatGPT tells you. We will make an effort to find out and you will be penalized as per academic integrity guidelines. Do not try to get easy points by cheating, it is not the purpose of the HW tasks.
    * Have fun and try to beat the world!
    * Your submission will ideally be accepted by leetcode, but send us your best attempt regardless, you can still get the points. If anything, try to optimize run time, do not worry about memory.
    * You will struggle, but if you solve many of those, your next stop is Google cafeteria as an employee!
    * If you cannot decide, there is a shuffle button which will pick something for you.

* HW 1 (1 pts):
  * Choose one of the easy problems. Have fun and send us how far you have got!
    * Example: [Two Sum](https://leetcode.com/problems/two-sum/)
* HW 2 (2 pts):
  * One easy or one Medium problem
    * Example: Medium: [Parentheses](https://leetcode.com/problems/generate-parentheses/)
* HW 3 (2 pts):
  * One easy or one Medium problem
  * Must be from [Pandas set of problems](https://leetcode.com/problemset/pandas/)
