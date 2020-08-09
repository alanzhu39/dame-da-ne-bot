from moviepy.editor import *

generated = VideoFileClip('generated.mp4')
audioClip = AudioFileClip('damedane.mp3')
generated = VideoFileClip('generated.mp4').fx(vfx.speedx, generated.duration/audioClip.duration)
generated = generated.set_audio(audioClip)
generated.write_videofile('final.mp4')
