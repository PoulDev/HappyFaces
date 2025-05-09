# HappyFaces
A python script to generate SVG profile pictures of simple happy faces

![](./examples/1.svg)
![](./examples/2.svg)
![](./examples/3.svg)
![](./examples/4.svg)
![](./examples/5.svg)

## Simple usage
Generate from CLI:
```
python3 avatars.py
```

## API Server
Setup the virtual environment
```bash
python3 -m venv .venv
# on linux
source .venv/bin/activate
# on windows
.\.venv\Scripts\Activate.ps1
```

Install the libraries
```
pip install -r requirements.txt
```


Start the Server
```
python3 avatarServer.py
```
You can now access your random avatars at http://127.0.0.1:8000 or if you are too lazy to run it check it out on https://0xwassoky.pythonanywhere.com/ 

