import ffmpeg
import os

if __name__ == '__main__':
    # non silhouette videos
    # directory = '/Users/parthvyas/Documents/SJSU/cs298/datasets/UCF-101/BodyWeightSquats'
    # non silhoutte frames
    # outputpath = '/Users/parthvyas/Documents/SJSU/cs298/datasets/UCF-101-Frames'

    # silhouette videos and frames
    directory = '/Users/parthvyas/Documents/SJSU/cs298/datasets/UCF-101-Silhouette-Videos'
    outputpath = '/Users/parthvyas/Documents/SJSU/cs298/datasets/UCF-101-Silhouette-Frames'

    for filename in os.listdir(directory):
        try:
            os.mkdir(outputpath+'/'+filename.split('.')[0])
            stream = ffmpeg.input(directory+'/'+filename)
            stream = ffmpeg.filter(stream, 'fps', fps=1, round='up')
            stream = ffmpeg.output(stream, outputpath+'/'+filename.split('.')[0]+'/%04d.jpg')
            ffmpeg.run(stream)
        except OSError:
            print("Creation of the directory %s failed" % outputpath)
        else:
            print("Successfully created the directory %s " % outputpath)

