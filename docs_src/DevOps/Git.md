---
title: Git Cheatsheet
category: sourcecontrol
tags: SCM DevOps
---

# Git Cheatsheets

* [Graphical git cheatsheet](http://byte.kde.org/~zrusin/git/git-cheat-sheet-medium.png)
* [Git basic commands](https://www.atlassian.com/git/tutorials/svn-to-git-prepping-your-team-migration/basic-git-commands)
* [Git cheatsheet (visual)](https://www.maxoberberger.net/media/cheatsheet/git-cheatsheet-visual.pdf)
* [Git cheatsheet (interactive)](http://ndpsoftware.com/git-cheatsheet.html#loc=workspace)
* [Git full documentation](https://git-scm.com/doc)

*Repo hosting:*
* [BitBucket](https://bitbucket.org/)
* [GitHub](https://github.com/)	


## Common Commands

- Create a new Git repository in current directory:

```bash
git init
```

- Or create an empty Git repository in the specified directory:

```bash
git init <directory>
```

- Or copy an existing Git repository:

```bash
git clone <repo URL>
```

- Clone the repository located at <repo> into the folder called <directory> on the local machine:

```bash
git clone <repo> <directory>
git clone username@host:/path/to/repository
```

- Global Configuration:

```bash
$ git config --global user.name "Firstname Lastname"
$ git config --global user.email "your_email@youremail.com"
```

- Stage all changes in `<file>` for the next commit:

```bash
git add <file>
```

- Or stage all changes in `<directory>` for the next commit:

```bash
git add <directory>  # usually '.' for current directory
```

- Commit the staged snapshot to the project history:

```bash
git commit  # interactive   
git commit -m "<message>"
```

- Or add and commit all in one:

```bash
git commit -am "message"
```

- Fix up the most recent commit (don't do that if shared history):

```bash
git commit --amend
```

- List which files are staged, unstaged, and untracked:

```bash
git status
git status -s  # short format
```

- Show file diff:

```bash
git diff           #  git diff by itself doesn’t show all changes made since your last commit – only changes that are still unstaged.
git diff --staged  #  Shows file differences between staging and the last file version
```

- Open GUI:

```bash
git gui
```

- Displays committed snapshots:

```bash
git log -n <limit>
git log --graph --decorate --oneline
```

- Checking out commits, and checking out branches:

```bash
git checkout <commit>       #  Return to commit
git checkout master         #  Return to the master branch (or whatever branch we choose)
```

- Check out a previous version of a file:

```bash
git checkout <commit> <file>    #  Check out the version of the file from the selected commit
git checkout HEAD hello.py      #  Check out the most recent version
```

## Branches

Branches are just pointers to commits.

- List all of the branches in your repository.  Also tell you what branch you're currently in ('*' branch):

```bash
git branch
```

- Create a new branch called ``<branch>``. 

```bash
git branch <branch>
```

This does not check out the new branch. You need:

```bash
git checkout <existing-branch>
```

Or direcly create-and-check out ``<new-branch>``.

```bash
git checkout -b <new-branch>
```

- Safe delete the branch:

```
git branch -d <branch>
```

- Merge the specified branch into the current branch:

```bash
git merge <branch>
```

- Undo any undesired changes

Generate a new commit that undoes all of the changes introduced in ``<commit>``, then apply it to the current branch

```bash
git revert <commit>
```

``git revert`` undoes a single commit — it does not “revert” back to the previous state of a project by removing all subsequent commits.

- Reset (dangerous method - erases history):

```bash
git reset
```

- List the remote connections you have to other repositories.

```bash
git remote -v
```

- Create a new connection / delete a connection to a remote repository.

```bash
git remote add <name> <url>  # often "origin"
git remote rm <name>         # delete
```

- Fetch the specified remote’s copy of the current branch and immediately merge it into the local copy. This is the same as ``git fetch <remote>`` followed by ``git merge origin/<current-branch>``.

```bash
git pull <remote>
```

- Put my changes on top of what everybody else has done. Ensure a linear history by preventing unnecessary merge commits.

```bash
git pull --rebase <remote>
```

- Transfer commits from your local repository to a remote repo.

```bash
git push <remote> <branch>
```

- Pushes the current branch to the remote server and links the local branch to the remote so next time you can do ``git pull`` or ``git push``.

```bash
git push -u origin <branch>
```

## Typical Workflows

### Clone a Repo

```bash
$ mkdir repos
$ cd ~/repos
$ git clone https://<url>
$ ls -al  <repo dir>
```

### Add a change in the working directory to the staging area

```bash
$ git status
$ git add README
```

``-A``, ``--all`` finds new files as well as staging modified content and removing files that are no longer in the working tree.

```bash
$ git add -A
$ git commit -m "Add repo instructions"
$ git push -u origin master
$ git pull
$ ssh -p 2222 user@domain.com
```

###  Short-lived topic branches

* Start a new feature: 

```bash
git checkout -b new-feature master
```

* Edit some files:

```bash
git add <file>
git commit -m "Start a feature"
```

* Edit some files

```bash
git add <file>
git commit -m "Finish a feature"
```

* Merge in the ``new-feature`` branch

```bash
git checkout master
git merge new-feature
git branch -d new-feature
```

### Push and pull from a centralized repo

* To push the master branch to the central repo:

```bash
git push origin master
```

If local history has diverged from the central repository, Git will refuse the request.

```bash
git pull --rebase origin master
```

### Sync my local repo with the remote repo

```bash
git pull origin master
git add filename.xyz
git commit . -m “comment”
git push origin master
```

### Create a central Repo

The ``--bare`` flag creates a repository that doesn’t have a working directory, making it impossible to edit files and commit changes in that repository. Central repositories should always be created as bare repositories because pushing branches to a non-bare repository has the potential to overwrite changes.

```bash
$ git init --bare foobar.git  
$ git rev-parse --show-toplevel     # print top-level directory
$ git rev-parse --git-dir           # print .git directory name
```
