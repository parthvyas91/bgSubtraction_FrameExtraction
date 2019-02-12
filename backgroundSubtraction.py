import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os


if __name__ == '__main__':

    # bg subtract ucf-101 squat videos

    inputpath = '/Users/parthvyas/Documents/SJSU/cs298/datasets/UCF-101/BodyWeightSquats'
    outputpath = '/Users/parthvyas/Documents/SJSU/cs298/datasets/UCF-101-Silhouette-Videos'

    for filename in os.listdir(inputpath):
        try:
            cap = cv.VideoCapture(inputpath + '/' + filename)
            fgbg = cv.createBackgroundSubtractorMOG2()
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            out = cv.VideoWriter(outputpath+'/'+filename.split('.')[0]+'.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                                 (frame_width, frame_height), isColor=False)
            while (1):
                ret, frame = cap.read()
                if ret == True:
                    fgmask = fgbg.apply(frame)
                    # frame = cv.cvtColor(fgmask, cv.COLOR_GRAY2RGB)
                    out.write(fgmask)
                    # cv.imshow('frame', fgmask)

                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv.destroyAllWindows()

        except Exception:
            print("Error")


    # test on single video

    # cap = cv.VideoCapture('/Users/parthvyas/Documents/SJSU/cs298/frameExtractor/v_BodyWeightSquats_g01_c01.avi')
    # fgbg = cv.createBackgroundSubtractorMOG2()
    # frame_width = int(cap.get(3))
    # frame_height = int(cap.get(4))
    # out = cv.VideoWriter('outpy5.avi',cv.VideoWriter_fourcc('M','J','P','G'), 5, (frame_width,frame_height),isColor=False)
    #
    # while (1):
    #     ret, frame = cap.read()
    #     if ret == True:
    #         fgmask = fgbg.apply(frame)
    #         # frame = cv.cvtColor(fgmask, cv.COLOR_GRAY2RGB)
    #         out.write(fgmask)
    #         cv.imshow('frame', fgmask)
    #
    #         if cv.waitKey(1) & 0xFF == ord('q'):
    #             break
    #
    #     else:
    #         break
    # cap.release()
    # out.release()
    # cv.destroyAllWindows()