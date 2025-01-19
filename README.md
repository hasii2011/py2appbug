Demonstrate bug

Run from command line:

```bash

python -m py2appbug.py2appbug
```

Works

Create app via py2app

```bash

python setup.py py2app

```

Execute

```bash

/dist/py2appbug.app/Contents/MacOS/py2appbug 
```

fails

```bash
Traceback (most recent call last):
  File "/Users/humberto.a.sanchez.ii/PycharmProjects/py2appbug/dist/py2appbug.app/Contents/Resources/__boot__.py", line 212, in <module>
    _run()
  File "/Users/humberto.a.sanchez.ii/PycharmProjects/py2appbug/dist/py2appbug.app/Contents/Resources/__boot__.py", line 84, in _run
    exec(compile(source, path, "exec"), globals(), globals())
  File "/Users/humberto.a.sanchez.ii/PycharmProjects/py2appbug/dist/py2appbug.app/Contents/Resources/py2appbug.py", line 20, in <module>
    demoBug()
  File "/Users/humberto.a.sanchez.ii/PycharmProjects/py2appbug/dist/py2appbug.app/Contents/Resources/py2appbug.py", line 16, in demoBug
    convertedImage.save('/tmp/CompactImageDump.pdf', format='pdf')
  File "PIL/Image.pyc", line 2590, in save
KeyError: 'PDF'

```