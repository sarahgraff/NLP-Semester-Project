import re, os
import nltk
import csv
pattern = re.compile(r'START.*?Words > six letters: ?([0-9.]+).*?Numbers: ?([0-9.]+).*?Articles: ?([0-9.]+).*?Prepositions: ?([0-9.]+).*?Feelings: ?([0-9.]+).*?Anxiety: ?([0-9.]+).*?r words: ?([0-9.]+).*?Feeling: ?([0-9.]+).*?l words: ?([0-9.]+).*?Pronouns: ?([0-9.]+).*?1st person singular: ?([0-9.]+).*?1st person plural: ?([0-9.]+).*?3rd person singular: ?([0-9.]+).*?3rd person plural: ?([0-9.]+).*?Home: ?([0-9.]+).*?END',re.DOTALL)
train_results = open("train_results2.txt",encoding="UTF-8").read()
train_matches = re.findall(pattern,train_results)
test_results = open("test_results.txt",encoding="UTF-8").read()
test_matches = re.findall(pattern,test_results)
features = open("features.txt").read()
# print(train_matches)
# print(len(train_matches))
# print(test_matches)
# print(len(test_matches))

genders = []
with open("blog-gender-dataset.csv", "r",encoding="latin-1") as f:
    reader = csv.reader(f)
    for row in reader:
        try: genders.append(row[1])
        except: continue
## csv is off by six, subtract six when indexing genders

train_set = []
counter = 0
for filename in os.listdir("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/train_female"):
    filenum = int(filename[:-4])-6
    liwc = train_matches[counter]
    gender = genders[filenum]
    ftrs = []
    text = open("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/train_female/"+filename,encoding="latin-1").read()
    dist = nltk.FreqDist([word for word in text.split() if word in features])
    tag_text = nltk.pos_tag(nltk.word_tokenize(text))
    pos_dist = nltk.FreqDist(tag_text)
    ftrs.append(dist)
    ftrs.append(liwc)
    ftrs.append(pos_dist)
    train_set.append((ftrs,gender))
    counter+=1
for filename in os.listdir("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/train_male"):
    filenum = int(filename[:-4])-6
    liwc = train_matches[counter]
    gender = genders[filenum]
    ftrs = []
    text = open("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/train_male/"+filename,encoding="latin-1").read()
    dist = nltk.FreqDist([word for word in text.split() if word in features])
    tag_text = nltk.pos_tag(nltk.word_tokenize(text))
    pos_dist = nltk.FreqDist(tag_text)
    ftrs.append(dist)
    ftrs.append(liwc)
    ftrs.append(pos_dist)
    train_set.append((ftrs,gender))
    counter+=1
test_set = []
count = 0
for filename in os.listdir("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/test_female"):
    filenum = int(filename[:-4])-6
    liwc = test_matches[count]
    gender = genders[filenum]
    ftrs = []
    text = open("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/test_female/"+filename,encoding="latin-1").read()
    dist = nltk.FreqDist([word for word in text.split() if word in features])
    tag_text = nltk.pos_tag(nltk.word_tokenize(text))
    pos_dist = nltk.FreqDist(tag_text)
    ftrs.append(dist)
    ftrs.append(liwc)
    ftrs.append(pos_dist)
    test_set.append((ftrs,gender))
    count+=1
for filename in os.listdir("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/test_male"):
    filenum = int(filename[:-4])-6
    liwc = test_matches[count]
    gender = genders[filenum]
    ftrs = []
    text = open("C:/Users/sarah/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/sgraff/api_recipes-master/tests/python/test_male/"+filename,encoding="latin-1").read()
    dist = nltk.FreqDist([word for word in text.split() if word in features])
    tag_text = nltk.pos_tag(nltk.word_tokenize(text))
    pos_dist = nltk.FreqDist(tag_text)
    ftrs.append(dist)
    ftrs.append(liwc)
    ftrs.append(pos_dist)
    test_set.append((ftrs,gender))
    count+=1
