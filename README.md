# crontabs

files were autmated by launching a vm on Azure
then by using the terminal ssh into the vm
updated the vm using sudo apt-get update, installed necessary requirements
used git clone to bring the repo into machine
commands such as crontab -e was used to run the cron expressions



0 0 1 */3 *  python 3 /crontab/test.py
0 0 * * * python3 /crontab/test.py once a day
0 22 * * SUN python3 /crontab/test.py ## every sunday at 10pm