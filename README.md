# Voyce
## How to run the app
* Fork this repo
* cd to the directory you want to save your file and run 
```
git clone https://github.com/khuyentran1401/voyce.git
```
* Create the new branch on your local machine (To make sure we don't change the master file before reviewing the change)
```
git branch <name_of_your_new_branch>
```
* See the exising branch:
```
git branch
```
* Switch in your branch :
```
 git checkout [name_of_your_new_branch]
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
Add the files to commit
```
git add .
```
Commit the fields
```
git commit -m "Some message"
```
Push the branch on github :
```
git push origin [name_of_your_new_branch]
```
Update your branch when the original branch from official repository has been updated :
```
git fetch
```
As we review on the change, we can merge the other branch:
```
git merge 
```
Delete a branch on your local filesystem
```
git branch -d [name_of_your_new_branch]
```
Delete the branch on github :
```
git push origin :[name_of_your_new_branch]
```
