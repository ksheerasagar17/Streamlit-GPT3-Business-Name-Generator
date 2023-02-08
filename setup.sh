# Download Miniconda or Python
# For Miniconda you can go to below URL.
https://docs.conda.io/en/latest/miniconda.html

# Runs the Miniconda3 installation script for MacOS, which installs Miniconda3 on the user's machine.
bash Miniconda3-latest-MacOSX-x86_64.sh

# Download Code
git clone https://github.com/ksheerasagar17/Streamlit-GPT3-Business-Name-Generator.git
cd Streamlit-GPT3-Business-Name-Generator

# Creates a new virtual environment named "streamlit" and sets the python version to 3.10.8. 
# The "-y" option means it will run without confirming and "-n" option is used to specify the name of the environment.
conda create -y -n streamlit python=3.10.8
or
python -m venv streamlit

# Activates the "streamlit" environment, so all packages installed after this point will be installed within the "streamlit" environment.
conda activate streamlit
or
source streamlit/Scripts/activate

# Installs the streamlit package, which is a web framework for building data apps in python.
pip install streamlit

# Exports the OPENAPI_KEY environment variable, which is used in the python script to access the OpenAI API. This is fake key. Don't use it.
# GO to the OpenAI website and SignUp for a Key in the Below Link.
# https://platform.openai.com/account/api-keys
export OPENAPI_KEY=sk-9wvblVeu2fMYmgo7t1gqjkcjAvW0uOaTNQ3lG6HKt37PjSUa

# run_ui.py script using the streamlit run command. 
# The script will run within the "streamlit" environment and have access to the streamlit package and OPENAPI_KEY environment variable.
streamlit run run_ui.py
