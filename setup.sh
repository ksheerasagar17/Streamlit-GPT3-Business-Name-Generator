# this line runs the Miniconda3 installation script for MacOS, which installs Miniconda3 on the user's machine.
bash Miniconda3-latest-MacOSX-x86_64.sh
# this line creates a new virtual environment named "streamlit" and sets the python version to 3.10.8. 
# The "-y" option means it will run without confirming and "-n" option is used to specify the name of the environment.
conda create -y -n streamlit python=3.10.8
# this line activates the "streamlit" environment, so all packages installed after this point will be installed within the "streamlit" environment.
conda activate streamlit
# this line installs the streamlit package, which is a web framework for building data apps in python.
pip install streamlit
# this line exports the OPENAPI_KEY environment variable, which is used in the python script to access the OpenAI API.
export OPENAPI_KEY=sk-9wvblVeu2fMYmgo7t1gqjkcjAvW0uOaTNQ3lG6HKt37PjSUa
# this line runs the generate_smart_business_names.py script using the streamlit run command. 
# The script will run within the "streamlit" environment and have access to the streamlit package and OPENAPI_KEY environment variable.
streamlit run generate_smart_business_names.py
