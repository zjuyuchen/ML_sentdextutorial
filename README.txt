//Open the gitgui and find the SSH for the PC, copy it can paste it to the github SSH key.


GIT
file = readme.txt
git init                                                //initialize
git add file                                            //add a file
git commit -m 'message you want to commit'              //commit
git diff HEAD                                           //show the difference
git checkout -- file                                    //delete file from workaera
git reset HEAD file                                     //unstate from commit
git rm file                                             //remove file from git
git log --pretty=oneline                                //log
git reset --hard HEAD^                                  //return to the last
git reset --hard 3628162                                //return to the number
git reflog                                               //return to the new version
REMOTE
git remote add origin git@github.com:Zjuyuchen/xxx            //XXX/xxx,name of repo.
git push -u origin master                                //1st time
git push origin master                                   //after 1st
git clone git@github.com:Zjuyuchen/xxx                   //clone from remote

git checkout -b dev                                      //new branch dev
git checkout master                                      //return to master branch
git log --graph --pretty=oneline --abbrev-commit         //show the log of branch

git stash                                                //save the branch right now
git stash list                                           //show the saved list
git stash apply ** and git stash drop **
or
git stash pop




