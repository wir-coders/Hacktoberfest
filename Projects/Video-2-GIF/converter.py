from moviepy.editor import *


logo = r'''
          V҉i҉d҉e҉o҉2҉G҉I҉F҉
	  https://github.com/SandyUndefined/Video-2-GIF
'''

features = r'''
       FEATURES
        1.Simple Gif
'''


def simplegif():
    path = input("Enter file path: ")
    video = VideoFileClip(path)
    video.write_gif("output.gif")


if __name__ == '__main__':
    print(logo)
    print(features)
    n = int(input("Select the feature: "))
    if n == 1:
        simplegif()
    else:
        print("Please select")


