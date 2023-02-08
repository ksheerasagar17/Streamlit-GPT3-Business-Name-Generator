bash Miniconda3-latest-MacOSX-x86_64.sh
conda create -y -n streamlit python=3.10.8
conda activate streamlit
pip install streamlit
export OPENAPI_KEY=sk-9wvblVeu2fMYmgo7t1gqjkcjAvW0uOaTNQ3lG6HKt37PjSUa
streamlit run generate_smart_business_names.py