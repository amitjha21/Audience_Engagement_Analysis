import os
import shutil

DEBUG = True

# Output Dir Paths
PATH_CAPTURE_DIR = os.path.join("..", "..", "output", "capture")
PATH_CAPTURE_VIDEO = os.path.join("..", "..", "output", "capture_video.avi")
PATH_ENGAGEMENT_CAPTURE_VIDEO = os.path.join("..", "..", "output", "capture_video_engagement.avi")
PATH_ANALYSIS_DIR = os.path.join("..", "..", "output", "analysis")

# Engagement model paths
PATH_ENGAGEMENT_MODEL = os.path.join('..', 'models', 'binary_500pca_008C.pkl')
PATH_PCA_MODEL = os.path.join('..', 'models', 'binary_pca_500.pkl')

#OpenFace path
PATH_OPENFACE_BIN =  "C:\\local\\OpenFace_0.2.3_win_x64\\"     #"/Users/manal/Projects/Tools/OpenFace-master/bin"

INIT_DIR_NAME = "init"
FACS_HAP = "HAPPINESS"
FACS_SAD = "SADNESS"
FACS_SUR = "SURPRISE"
FACS_FER = "FEAR"
FACS_ANG = "ANGER"
FACS_DIS = "DISGUST"
FACS_CON = "CONTEMPT"

def clean_dir(path):
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)