# Seminar 0

September 29, 2025

**Contents**:

0. Preliminary info
1. Installations (Python, Git, Github, VScode, Jupyter)
2. IDE
3. Bash basics
4. Git basics

## Installations

Check you have installed **python** and **git + git bash** and **VScode**
- [Python](https://www.python.org/downloads/)
  - or via [(ana)conda](https://docs.anaconda.com/anaconda/install/index.html) - **preferably** for Win users
    - Anaconda asks you if you want to install python with it (register with it) ⟹ check yes.
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [[dowload page](https://git-scm.com/downloads)]
- [GitHub](https://github.com/)
  - register with your school e-mail, you should be eligible for [GitHub Student Developer Pack](https://education.github.com/pack)
- [VScode](https://code.visualstudio.com/download)

------

### Let us repeat the installation instructions from the e-mail

**Git**
Install Git on your machines and register for GitHub (https://github.com/join), ideally using the school e-mail since you can apply for the GitHub Student Developer Pack. (https://education.github.com/pack).
Go through the GitHub handbook, 10-minutes only. (https://guides.github.com/introduction/git-handbook/)

**Jupyter & (Ana)conda:**
Based on your OS (here *Windows* links), download (Ana)conda from here:
https://www.anaconda.com/distribution/#windows
and install it following these instructions:
https://docs.anaconda.com/anaconda/install/windows/
Jupyter should be installed automatically. If you encounter problems, that basic google-search cannot solve, we are happy to help you when you write us an email.
On *macOS* you can use brew installer or anaconda as well.

**VScode**
Finally, also install Visual Studio Code (VScode): https://code.visualstudio.com/

*Thank you!*

#### Additionally, you could consult these resources:

Installing python3 on Windows if not using Anaconda:
https://www.digitalocean.com/community/tutorials/install-python-windows-10

Installing python3 on macOS if not using Anaconda but homebrew:
https://www.geeksforgeeks.org/how-to-install-python-on-mac/

------

*Seminar 0 continues here:*

## IDEs

- integrated development environment
- use some!
- standard features:
  - text editor
  - _code completion_
  - linting
  - debugger
- lot of options, but the best (IMHO) is hands down [Visual Studio Code](https://code.visualstudio.com)

## Shell basics

- shell is simply a programming environment (just like Python)
- what happens when you run commands in your shell?

  - you are really writing a small bit of code that your shell interprets
  - if the shell is asked to execute a command that doesn’t match one of its programming keywords, it consults an environment variable called $PATH that lists which directories the shell should search for programs when it is given a command

- for Linux and macOS, the path '/' is the “root” of the file system, under which all directories and files lie, whereas on Windows there is one root for each disk partition (e.g., C:\).
- a path that starts with '/' is called an absolute path

  - relative paths are relative to the current working directory
  - in a path, `.` refers to the current directory, and `..` to its parent directory

- you need to be using a Unix shell like Bash or ZSH.

  - if you are on Linux or macOS, you are set out-of-the-box
  - if you are on Windows, don't run cmd.exe or PowerShell!
    - use [Window Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/) or at least [git Bash](https://gitforwindows.org/) to emulate Unix shell

- `echo` returns whatever you type at the shell prompt

- `pwd` prints the current working directory
  - the current working directory is the default place where the shell commands will look for data files
- the UNIX file hierarchy has a tree structure

  - to reach a particular folder or file, we need to traverse certain paths within this tree structure
  - paths separate every node of the above structure with the help of a slash character - `/`
  - `\` on Windows

- `ls <directory>` to list contents of a directory
  - `ls <directory> -a` to list all hidden files
- `cd <directory>` changes the active directory to the path specified

  - `cd ..` changes to the parent directory
  - `cd` changes to the HOME directory

- `mkdir` creates a folder
- `touch` creates an empty file
- `rm` delete a file

  - `rm -r *` deletes a folder with all its contents

- the redirection operator `>` will redirect the normal output initially intended to be on stdout and print it directly into the file.

  - `echo "Git is awesome." > file.txt`

- `cat` reads a file and outputs its content

## Git and GitHub

### Git

*Git was created for use in the development of the Linux kernel by Linus Torvalds and others developing the kernel. (wiki)*

- version control system
- short course at IES, [martinhronec.github.io/JEM224](http://martinhronec.github.io/JEM224)

### Github

- place with repositories where you can collaborate on your projects
- repositories with packages
- repositories for websites (github.io)
- alternatives: gitlab, bitbucket
