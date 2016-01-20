# Notes on using github

### References:
* https://www.atlassian.com/git/tutorials/using-branches
* https://git-scm.com/docs
* https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf

### Install and configure github 
* sudo apt-get install git
* git config --list
* git config --global user.email jeffnju@gmail.com
* git config --global user.name dreamingbird88
* sudo git config --system core.editor vim

### Clone a repository
* git clone kaggle **or** git clone https://github.com/dreamingbird88/kaggle
* git remote add name https://github.com/dreamingbird88/kaggle/

### Create a repository
1. First create a repository with browser;
2. Then clone it with command line.

### Edit/add files and push to the repository
* git add somefile.ext # *add* can refer to **modified**.
* git commit -m "a test." # **g4 change**
* git commit --amend
* git push -u origin master # **g4 submit**

### Others
* check the commit (change list): *git status* # **g4 pending**
* list remote names: *git remote -v* # **g4 list**
* move a file: *git mv MarkDown.md notes/*

vim .gitignore
git log
git checkout
git add to_be_deleted.txt 
git checkout
git commit -m "First message"
git add another_test.txt 
git checkout
git status
git commit -m "second message"
git log --oneline
git reset HEAD~2
git add .gitignore 
vim .gitignore
git add .gitignore 
git commit -m "add .gitignore"
git log
git clean -df
git checkout master
git fetch origin master
git rebase -i origin/master
git status
git log
git push origin master
git remote add name https://github.com/dreamingbird88/kaggle/
git push --repo=name origin master
git rm another_test.txt 
git commit -m "Delete another_test.txt"
git log
git status
git push --repo=name origin master
git rm to_be_deleted.txt 
git status
git commit -m "delete to_be_deleted.txt"
git status
git log --oneline
git revert 17a722c
git log --oneline
git reset f0f78c4
git log --oneline
git reset b6cdb5c
git log --oneline
git status
git push --repo=name origin master
git push programming master 
git checkout bcbef3e configs/.bashrc
git checkout bcbef3e 
git revert bcbef3e
git reset bcbef3e

