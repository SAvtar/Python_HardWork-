heads = []
descs = []
keywords = []
for filename in range(13):
    with open('/mnt/745AA3875AA34528/SOFTWARES/How_to_make_a_text_summarizer-master/test.txt','r') as fp:
        text = fp.read()
        temp = text
        heads.append(temp.split("\n")[0])
        descs.append(text) 
        keywords.append(None)
import pickle       
with open('data.pickle', 'wb') as f:
     pickle.dump((heads,descs,keywords),f)
