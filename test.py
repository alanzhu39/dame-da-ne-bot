from moviepy.editor import *
from makevid import makevid

f = open('files/02.png', 'wb')
f.write(open('base.jpg', 'rb').read())
f.close()
makevid()
