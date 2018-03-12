# TranslateCSV
This app will take list of sentences in different language in csv file and covert it into English language in another CSV file.

.py to .exe in Python 3.6.1

The thing is, I suffered a lot to do this. Spent many days working on it. Finally, I got the answer. I realized that I got not only the answer but also an ImportError.  Then, I found a solution for that too and I made my python script to an application. Wanna know how? Follow the following steps and so you make people to follow you. Have a nice day 🙂

Steps to convert .py to .exe in Python 3.6
================================================
1.You must be installed Python 3.6 and cx_Freeze.
2.To install cx_Freeze, open your command prompt and type ‘pip install cx_Freeze‘
3.make a .py program of yourself say ‘my first prog.py’ .
4.Create a new python file named ‘setup.py’ on the current directory of your script.
5.On the setup.py, code this and save it.
6.With shift pressed right click on the same directory, so you are able to open a command prompt window.
7.Type in the prompt as >> python setup.py build

If your script is error free, then there is no problem on creating application. Check the newly created folder ‘build‘. It has another folder in it. Within that folder you can able to find your application. Run it. Make yourself happy.
