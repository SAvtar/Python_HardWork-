import os
def second_img():
    rootDir = 'files'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            continue
    # Remove the first entry in the list of sub-directories
    # if there are any sub-directories present
            if len(subdirList) > 0:
                del subdirList[0]


second_img()