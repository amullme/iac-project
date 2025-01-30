# iac-project/python/flask-hello/ Objective

Using the existing hello.py, save a requirements.txt file using a Python virtual environment

# Steps
- If not done, use the README.md file in the `components/vagrant` folder in this repo to launch `testvm` and `prodvm`
- SSH to the testvm using the command below:
```
vagrant ssh testvm
```
- Navigate the to shared vagrant folder containing hello.py:
```
cd /vagrant/python/flask-hello
```
- Create a Python virtual environment:
```
python -m venv ~/venv
```
- Activate the virtual environment:
```
source ~/venv/bin/activate
```
- Run `hello.py` using the command below [^1].
```
python3 hello.py
```
- Use `pip3` [^2] to install missing packages until `hello.py` works: https://docs.python.org/3/installing/index.html
- Once everything is working, run the command below to generate a requirments.txt file [^3].
```
pip3 freeze > requirements.txt
```
[^1]: You may need to use `python`
[^2]: You may need to use `pip`.
[^3]: Alternative commands to create a `requirements.txt` file can be found here: https://www.geeksforgeeks.org/how-to-create-requirements-txt-file-in-python/
