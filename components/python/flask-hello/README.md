
# this section is a work in progress
# iac-project/python/flask-hello/ Objective

Build a small Python file using Flask as a web server which can be built into a docker image with requirments.txt

# Steps
## Edit hello.py if desired
Use the hello.py file as is or as a template to build a better app

## Generate a requirements.txt file
1. Create a Python virtual environment: https://docs.python.org/3/library/venv.html
1. Navigate the to folder containing your hello.py with the file and run it using the command below [^1].
```
python hello.py
```
3. Use pip3 to install missing packages: https://docs.python.org/3/installing/index.html
3. Once everything is working, run the command below to generate a requirments.txt file [^2]. This will be used later by a Dockerfile
```
pip freeze > requirements.txt
```
[^1]: You may need to use `python3`
[^2]: You may need to use `pip3`. Alternative commands can be found here: https://www.geeksforgeeks.org/how-to-create-requirements-txt-file-in-python/
