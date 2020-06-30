import os
import sys
import webvtt
import srt
from datetime import timedelta


    

def convert(file_path):

    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)

    if not '.vtt' in file_name:
        return
    
    file_path = file_dir + '/' + file_name

    content = []
    i = 1
    for caption in webvtt.read(file_path):
        content.append(srt.Subtitle(index=i, start=srt.srt_timestamp_to_timedelta(caption.start), end=srt.srt_timestamp_to_timedelta(caption.end), content=caption.text, proprietary=''))

        i+=1

    file_create(file_path.replace(".vtt", ".srt"), srt.compose(content))




def file_create(str_name_file, str_data):
    """Create a file with some data

       Keyword arguments:
       str_name_file -- filename pat
       str_data -- dat to write
       """
    # --------------------------------
    # file_create(str_name_file, str_data)
    # create a text file

    try:
        f = open(str_name_file, "w")
        f.writelines(str(str_data))
        f.close()
    except IOError:
        str_name_file = str_name_file.split(os.sep)[-1]
        f = open(str_name_file, "w")
        f.writelines(str(str_data))
        f.close()



def detect(path):

    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            convert(item_path)
        
        elif os.path.isdir(item_path):
            detect(item_path)



arg_size = len(sys.argv)

if arg_size == 1:
    print('set word file address')

elif arg_size > 1:
    if os.path.isfile(sys.argv[1]):
        convert(sys.argv[1])
    
    elif os.path.isdir(sys.argv[1]):
        detect(sys.argv[1])

