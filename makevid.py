import imageio
import importlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from skimage import img_as_ubyte
import warnings
warnings.filterwarnings("ignore")

def makevid():
    source_image = imageio.imread('files/02.png')
    driving_video = imageio.mimread('files/04.mp4')

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    demo = importlib.import_module('first-order-model.demo')
    generator, kp_detector = demo.load_checkpoints(config_path='first-order-model/vox-256.yaml', \
                                checkpoint_path='files/vox-cpk.pth.tar')

    predictions = demo.make_animation(source_image, driving_video, generator, kp_detector, relative=True)

    imageio.mimsave('generaged.mp4', [img_as_ubyte(frame) for frame in predictions])

makevid()
