from moviepy.editor import *

generated = VideoFileClip('final.mp4')
audioClip = AudioFileClip('damedane.mp3')
generated = generated.set_audio(audioClip)
generated.write_videofile('final.mp4', bitrate='256k')
