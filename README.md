# Voyce
## How to run the app
* Fork this repo
* cd to the directory you want to save your file and run 
```
git clone https://github.com/khuyentran1401/voyce
```
* Create the branch on your local machine 
```
git branch <name_of_your_new_branch>
```

* Switch in this branch :
```
 git checkout -b [name_of_your_new_branch]
```
* cd to voyce repo
```
cd voyce
```
* Create the virtual env
* Run
```
python manage.py runserver
```
You should be able to see the website

## Note:
In settings.py, I use PostgreSQL, you could fix this in the settings (DATABASE) for the settings for MySQL

## How to commit
Since we want to agree on the change before changing the master, create a branch is a great way to do that
Check out [this tutorial](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches) on how to commit.

Push the branch on github :
```
git push origin [name_of_your_new_branch]
```
When you want to commit something in your branch, be sure to be in your branch. Add -u parameter to set-upstream.

Update your branch when the original branch from official repository has been updated :
```
git fetch [name_of_your_remote]
```
As we review on the change, we can merge the other branch:
```
git merge [name_of_your_remote]
```
Delete a branch on your local filesystem
```
git branch -d [name_of_your_new_branch]
```
Delete the branch on github :
```
git push origin :[name_of_your_new_branch]
```
