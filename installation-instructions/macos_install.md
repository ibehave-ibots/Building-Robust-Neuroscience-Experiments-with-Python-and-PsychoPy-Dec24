# macOS Installation Guide
Hello! This guide will help you set up everything you need for the Python workshop.
Just follow the instructions step by step.

## Step 1: Installing VSCode
First, we start by installing Visual Studio Code (VSCode),
VSCode will be our integrated development environment (IDE) where we write and run code.
1. Go to https://code.visualstudio.com/download and download the macOS version
2. Open the downloaded file (should end in .dmg)
3. Drag Visual Studio Code.app to Applications folder
4. Open VSCode from your Applications folder

## Step 2: Installing Git
Next, we install Git which we will use to download and continuously update the course materials
1. Install Apple's Command Line Tools which includes Git:
   - Open Terminal (you can use Spotlight search with Cmd+Space and type "Terminal")
   - Type: `xcode-select --install`
   - Click "Install" in the popup window that appears
2. To verify the installation worked, go to VSCode and, in the top menu select Terminal -> New Terminal
3. In the terminal that opened, type `git --version`
4. You should see a version number

## Step 3: Installing Miniforge
Finally, we have to install Miniforge, which is the software we use to manage our Python environment and install packages such as PsychoPy.
If you already have an installation of Anaconda on your computer, you can use it instead of Miniforge, the steps in the following sections will be identical.
However, some institutes removed access to the Anaconda servers which may prevent you from installing new packages.
Check if you are affected by this and consider uninstalling Anaconda and replacing it with Miniforge.
1. Download the Miniforge installer for macOS from https://conda-forge.org/download/
   - If you have an Intel Mac, download Miniforge3-MacOSX-x86_64.sh
   - If you have Apple Silicon (M1/M2), download Miniforge3-MacOSX-arm64.sh
2. Open Terminal in VSCode (Terminal -> New Terminal)
3. Type: `bash ~/Downloads/Miniforge3-MacOSX-*.sh`
4. Accept the license agreement by typing "yes"
5. Press Enter to confirm the default location
6. Type "yes" when asked about initialization
7. Close VSCode and open it again
8. Open a new terminal and type: `conda --version`
9. You should see a version number

## Step 4: Setting up Python
Now we can create a new Python environment where we can install all the packages that we will need in this course.
1. In the VSCode terminal, create a new environment by typing: `conda create -n psychopy python=3.8` and type 'y' (yes) to confirm
2. After it finishes, type: `conda activate psychopy` to activate the new environment --- You should see (psychopy) at the start of your terminal line
3. Then, finally install the required packages by typing `pip install psychopy psychtoolbox pytest ipytest ipykernel`

## Step 5: Testing the Installation
Now the installation is finished, let's test that everything works!
1. In VSCode, open the file `test_psychopy.ipynb`
2. Click yes for any extension VSCode suggests installing
3. In the top right corner, click on "Select Kernel" and choose the previously created psychopy environment
4. If the environment is not detected, restart VSCode
5. Run the cell in the notebook by clicking the arrow to the left of the cell or pressing `Cmd+Enter` while the cell is focused.
6. If this opens a gray window and displays some text, everything worked out!