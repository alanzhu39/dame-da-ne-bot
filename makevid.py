import imageio
import importlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from skimage import img_as_ubyte
import warnings
from moviepy.editor import *
warnings.filterwarnings("ignore")

def makevid():
    source_image = imageio.imread('files/02.png')
    driving_video = imageio.mimread('files/04.mp4', memtest=False)

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    demo = importlib.import_module('first-order-model.demo')
    generator, kp_detector = demo.load_checkpoints(config_path='first-order-model/config/vox-256.yaml', \
                                checkpoint_path='files/vox-cpk.pth.tar', cpu=True)

    predictions = demo.make_animation(source_image, driving_video, generator, kp_detector, relative=True, cpu=True)

    imageio.mimsave('generated.mp4', [img_as_ubyte(frame) for frame in predictions])

    generated = VideoFileClip('generated.mp4')
    audioClip = AudioFileClip('damedane.mp3')
    generated = VideoFileClip('generated.mp4').fx(vfx.speedx, generated.duration/audioClip.duration)
    generated = generated.set_audio(audioClip)
    generated.write_videofile('final.mp4', audio_codec='aac')

if __name__ == "__main__":
    makevid()
