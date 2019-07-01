# Starting-with-Python
A little repository which is catching up my way to a beautiful ide and getting started with coding python

# IDE := integrated development environment
My favorite ide , which i am using for all my private projects, is:
##### ATOM
At work i am using pycharm!

So lets get started :)
Go to http://www.atom.io or to you ubuntu store and download atom.
Next we need to install python.
Open your terminal and follow this section:

# Install Python

At first update your apt:
'''sudo apt update'
'sudo apt upgrade'''

With sudo you get the full wrights - so please be careful by using it

In the next step we check the python version:
'python -V' (you although can use 'python --version')
Probably it shows something like "python 2.4.x"
Now we need to update:

'sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1'
the code means the following:
update-alternatives --install is taking a <link> than the <name> , the <path> and at least the priority.

check again what python version you get now with:
'python -V'

If you want to configure the version you can take a closer look at:
'update-alternatives --config python'

# Install pip

With installing pip there are very often a lot of problems ... don't ask me why!
If you just installed pip you need to start with this lines of code:

'python -m pip uninstall pip'
'apt remove python-pip'
'whereis pip' should should you something like this: "pip:  "

Now we are installing pip:

'sudo wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py'
'sudo python3 /tmp/get-pip.py'
'sudo pip install --user pipenv'
'sudo pip3 install --user pipenv'
'echo "PATH=$HOME/.local/bin:$PATH" >> ~/.profile'
'source ~/.profile'
'whereis pip'

# Installing a kernel to be able to execute python code inside Atom

If pip is installed correct then the following two lines should not be a big problem:
'sudo python -m pip install ipykernel'
'sudo python -m ipykernel install --user'

And that's it!!
Only two little steps before we can start coding in Atom!

# Changes in Atom

Now open Atom and start closing all the unnecessary "welcome" tabs.
Go to "Edit" and than "Preferences"
Click the tab "Install"
We are installing two packages now to be able to run our code WITHOUT calling it over the terminal!
Search for "Hydrogen" (The version today is 2.10.2 with 1.104.180 downloads) and install it.
That takes a little time ...
Next search for "script" (The version today is 3.18.1 with 1.871.706 downloads) and install it.
When bot packages are installed - close Atom and restart it!

Create a new file and let's try our achievements

For example, type:

'print("Hello World")'

Save it as name.py file (name stands for any name for the file you want to ;) )

# Run the Code
There are two ways to run our code:

### First Way: Hydrogen
Hydrogen is a beautiful way to run code AND keep all the output, because you can run cell after cell
How to do it:
Mark the lines of code you want to run -> go to Packages -> Hydrogen -> run cell (Alt + Ctrl + Enter)

### Second Way: Script
A very simple and puristic way to run our code!
Go to Packages -> Script -> Run Script (Ctrl + Shift + B)

That's it!!
Type your Python Code and enjoy


