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
- Create a Python virtual environment [^1]:
```
python3 -m venv ~/venv
```
- Activate the virtual environment:
```
source ~/venv/bin/activate
```
- Run `hello.py` using the command below.
```
python3 hello.py
```
- Use `pip3` [^2] to install missing packages until `hello.py` works: https://docs.python.org/3/installing/index.html
```
pip3 install flask
pip3 install faker
```
- Open a new terminal and SSH to `prodvm`:
```
vagrant ssh prodvm
```
- Test to make sure the Flask server is issuing the page. You should see `Hello Random Name` [^4]:
```
curl 10.0.0.10:5000
```
- Once everything is working, run the command below from test VM to generate a requirments.txt file which will be used in the next step to create a Docker image [^3].
```
pip3 freeze > requirements.txt
```
- You can now move on the the next step `components/docker/README.md`


### Footnotes
[^1]: You may need to use `python` rather than `python3`
[^2]: You may need to use `pip` rather than `pip3`
[^3]: Alternative commands to create a `requirements.txt` file can be found here: https://www.geeksforgeeks.org/how-to-create-requirements-txt-file-in-python/
[^4]: You can probably also access http://10.0.0.10:5000 from a browser on your host machine 
