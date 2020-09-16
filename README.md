# py4web-gae-example
Gae example deployment of a py4web app

Follow this instructions:

https://github.com/web2py/py4web/tree/master/deployment_tools/gae

```
cd deployment_tools/gae
make setup
mkdir apps
touch apps/__init__.py
# symlink the apps that you want to deploy to GAE, for example:
cd apps
ln -s ../../../apps/_default .
cd ..
```
But I make the symlink this way:

https://groups.google.com/g/py4web/c/mtQSHVHODrc/m/oB4vBdTJEwAJ 

### The way I did

```
[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example(master) $ ls
apps  LICENSE  myappforgae  README.md

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example(master) $ cd myappforgae

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ ls
app.yaml  index.yaml  main.py  Makefile  requirements.txt

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ py4web setup apps
Create missing folder apps? [y/N]: y
Create app _minimal? [y/N]: N
Create app _dashboard? [y/N]: N
Create app _documentation? [y/N]: N
Create app _default? [y/N]: Y
[X] Unzipping app py4web.app._default.zip
Create app _scaffold? [y/N]: N

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ cd apps

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae/apps(master) $ ls
_default  __init__.py

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae/apps(master) $ cd ..

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ mkdir -p lib

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ python3 -m pip install -U --no-deps py4web -t lib/
Processing /home/jacinto/.cache/pip/wheels/35/6f/7e/ca95c1d82f805a7da036a2dff344b42f46c456037aa82ba1bc/py4web-1.20200905.1-py3-none-any.whl
Installing collected packages: py4web
Successfully installed py4web-1.20200905.1

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ ls
apps  app.yaml  index.yaml  lib  main.py  Makefile  requirements.txt

```

#### Deploy in gae

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ gcloud app deploy app.yaml -v=3 --no-promote


### Access from py4web local _dashboard

```
[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ ln -sf /home/jac/PROGRAMACION/TESTS/py4web-gae-example/myappforgae/apps/_default /home/jac/PROGRAMACION/TESTS/py4web-gae-example/apps/myappforgae
```

This way you can access the application from py4web _dashboard

```
[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/myappforgae(master) $ cd ../apps

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/apps(master) $ ls
_dashboard  _default  _documentation  __init__.py  _minimal  myappforgae  _scaffold

[py4web382] jac@PCXX:~/PROGRAMACION/TESTS/py4web-gae-example/apps(master) $ 
``` 

