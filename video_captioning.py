import argparse
import os.path
# if os.path.basename(os.getcwd()) != 'web_VideoCaptioning':
#     os.chdir('../web_VideoCaptioning')
import utils


#Parse argument
parser = argparse.ArgumentParser()
parser.add_argument("-p", dest="video_path",
                    help="input video path", default='/Users/chensx/Downloads/VideoCaptioning_att-master/example2.mp4')
parser.add_argument("-n", dest="video_file_name", nargs='+',
                    help="input video file name", default='_O9kWD8nuRU_50_56.avi')
parser.add_argument("-fp", dest="video_full_path",
                    help="input video full path")
args = parser.parse_args()

if args.video_full_path == None:
    video_full_path = os.path.join(args.video_path, args.video_file_name[0])
else:
    video_full_path = args.video_full_path

#extract features and generate sentence
video_feat = utils.extract_video_features(video_full_path)
generated_sentence = utils.get_caption(video_feat)
print type(generated_sentence)
