# Linux Installation Guide
Hello! This guide will help you set up everything you need for the Python workshop.
Just follow the instructions step by step.

## Step 1: Installing VSCode
First, we start by installing Visual Studio Code (VSCode),
VSCode will be our integrated development environment (IDE) where we write and run code.

1. Go to this website https://code.visualstudio.com/download and download and install VSCode using the method of your choice
3. Once the installation is finished, open VSCode from your applications menu or type `code` in the terminal

## Step 2: Installing Git
Next, we install Git which we will use to download and continuously update the course materials

1. Open Terminal in VSCode (Terminal -> New Terminal from the top menu)
2. Type: `sudo apt-get install git`
3. To verify the installation worked, type: `git --version`
4. You should see a version number

## Step 3: Installing Miniforge
Finally, we have to install Miniforge, which is the software we use to manage our Python environment and install packages such as PsychoPy.
If you already have an installation of Anaconda on your computer, you can use it instead of Miniforge, the steps in the following sections will be identical.
However, some institutes removed access to the Anaconda servers which may prevent you from installing new packages.
Check if you are affected by this and consider uninstalling Anaconda and replacing it with Miniforge.

1. Download the Miniforge installer from the website https://conda-forge.org/download/
1. Open Terminal in VSCode (Terminal -> New Terminal from the top menu)
2. Install Miniforge by typing `bash ~/Downloads/Miniforge3-Linux-x86_64.sh` (the file location may differ)
3. Proceed through the installer, selecting yes for every option
4. Close VSCode and open it again
5. Open a new terminal and type: `conda --version`
6. You should see a version number

## Step 4: Setting up Python
Now we can create a new Python environment where we can install all the packages that we will need in this course.

1. In the VSCode terminal, create a new environment by typing: `conda create -n psychopy python=3.10` and type 'y' (yes) to confirm
2. After it finishes, type: `conda activate psychopy` to activate the new environment --- You should see (psychopy) at the start of your terminal line
3. Go to this webiste https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ and download the wxPython wheel for your distribution and Python version (for examplen ubuntu-24.04/wxPython-4.2.2-cp310-cp310-linux_x86_64.whl for the latest Ubuntu and Python version 3.10)
4. Install wxPython by typing `pip install ~/downloads/wxPython-4.2.1-cp39-cp39-linux_x86_64.whl` (the file location may differ)
4. Then, finally install the required packages by typing `pip install psychopy psychtoolbox pytest ipytest ipykernel`

## Step 5: Testing the Installation
Now the installation is finished, let's test that everything works!

1. In VSCode, open the file `test_psychopy.ipynb`
2. Click yes for any extension VSCode suggests installing
3. In the top right corner, click on "Select Kernel" and choose the previously created psychopy environment
4. If the environment is not detected, restart VSCode
5. Run the cell in the notebook by clicking the arrow to the left of the cell or pressing `Ctrl+Enter` while the cell is focused
6. If this opens a gray window and displays some text, everything worked out!
```