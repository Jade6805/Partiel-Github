Microsoft Windows [version 10.0.19042.1466]
(c) Microsoft Corporation. Tous droits réservés.

C:\Users\fathj>git init
Reinitialized existing Git repository in C:/Users/fathj/.git/

C:\Users\fathj>cd C:\Users\fathj\Desktop\Partiel-Github

C:\Users\fathj\Desktop\Partiel-Github>git init
Reinitialized existing Git repository in C:/Users/fathj/Desktop/Partiel-Github/.git/

C:\Users\fathj\Desktop\Partiel-Github>git add .
warning: LF will be replaced by CRLF in fath_jade_création_de_fonction_comportant_des_modules_de_gestions_des_exceptions_.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in fath_jade_fonction_factorielle.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in fath_jade_fonction_polynomiale.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in fath_jade_suite_de_fibonnaci.py.
The file will have its original line endings in your working directory

C:\Users\fathj\Desktop\Partiel-Github>git commit -m "les 4 fichiers pour le partiel"
[master (root-commit) e593733] les 4 fichiers pour le partiel
 4 files changed, 218 insertions(+)
 create mode 100644 "fath_jade_cre\314\201ation_de_fonction_comportant_des_modules_de_gestions_des_exceptions_.py"
 create mode 100644 fath_jade_fonction_factorielle.py
 create mode 100644 fath_jade_fonction_polynomiale.py
 create mode 100644 fath_jade_suite_de_fibonnaci.py


C:\Users\fathj\Desktop\Partiel-Github>git remote add https://github.com/Jade6805/Partiel-Github.git
usage: git remote add [<options>] <name> <url>

    -f, --fetch           fetch the remote branches
    --tags                import all tags and associated objects when fetching
                          or do not fetch any tag at all (--no-tags)
    -t, --track <branch>  branch(es) to track
    -m, --master <branch>
                          master branch
    --mirror[=(push|fetch)]
                          set up remote as a mirror to push to or fetch from


C:\Users\fathj\Desktop\Partiel-Github>git remote add Github https://github.com/Jade6805/Partiel-Github.git

C:\Users\fathj\Desktop\Partiel-Github>git remote -v
Github  https://github.com/Jade6805/Partiel-Github.git (fetch)
Github  https://github.com/Jade6805/Partiel-Github.git (push)

C:\Users\fathj\Desktop\Partiel-Github>git push -u Github master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.21 KiB | 1.10 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/Jade6805/Partiel-Github/pull/new/master
remote:
To https://github.com/Jade6805/Partiel-Github.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'Github'.

C:\Users\fathj\Desktop\Partiel-Github>
