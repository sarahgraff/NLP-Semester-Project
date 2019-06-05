import pytumblr
import re
#get blogs followers add to set and get their posts
#I CREATED A TUMBLR APPLICATION AND ACCOUNT FOR THIS SO THAT WE CAN ALL ACCESS IT
client = pytumblr.TumblrRestClient(
    'kh9xQ0Z1N4U84B4tpIyjnfvsq2uGIoat23eiq8D4VzvO4RwuCz',
    'uBYCSdpLUZ0SELb08lL68qOL7zDXz4KcGkQcNLQJwPlYR7oIzN',
    'dPze4r22S9340cTUX7J6vgMEkW5ZPU0RUd9KfJGnFhyMHtA3vk',
    'neMMN9Gp4oU7fwqxCkQNHyTNm9rvWIFyWN7fhSE5D9uSYD4Aa7'
)

# I know this is ugly but I have ideas to streamline when there is more time
def getGender(desc):
    d = desc.lower()
    gender = ""
    if d.find("trans") > -1 and d[d.find("trans"):d.find("trans")+9] != "transcend": #note that this doesn't catch \
        # if the first usage is transcend but the second is just "trans"
        gender += "t"
    if d.find("cis") > -1 and d[d.find("cis")-5:d.find("cis")+4] != "criticism" and d[d.find("cis")-2:d.find("cis")] \
            != "ra" and d[d.find("cis")-2:d.find("cis")] != "fa": #same issue here
        gender += "c"
    if ("nb" in d and d[d.find("nb") - 1:d.find("nb") + 8] != "inbetween") or "enby" in d or "nonbinary" in d or \
            "non binary" in d or "non-binary" in d or "they/them" in d or "genderqueer" in d or "gender queer" in d \
            or "gender-queer" in d or "genderfluid" in d or "gender fluid" in d or "gender-fluid" in d:
        gender = "nb" #this is intentional bc many but not all nb say they're trans, we consider it implied
    elif "female" in d or "woman" in d or ("girl" in d and d[d.find("girl")+4:d.find("girl")+10] != "friend") \
            or "lady" in d or "womyn" in d or "she/her" in d or "lesbian" in d:
        gender += "f"
    elif ("man" in d and d[d.find("man")-2:d.find("man")] != "hu" and d[d.find("man")-2:d.find("man")+4] != "romant") \
            or "male" in d or "boy" in d or "guy" in d or "he/him" in d:
        gender += "m"
    if "intersex" in d or "intersexed" in d or "inter sex" in d or "inter-sex" in d:
        gender = "i" #intentional
    return gender


blogs = {}

#I FOLLOWED 200 BLOGS TO GET US STARTED
cInfo = client.info()
totFollowing = cInfo['user']['following']
for i in range(0,totFollowing,20):
    f = client.following(offset=i)
    for j in f['blogs']:
        u = j['url']
        if "http" in u and "//" in u:
            h = re.compile(r'^http.*\/\/')
            u = re.sub(h,"",u)
        gender = getGender(j['description'])
        if gender in ("cm","cf","nb","tm","tf", "i"):
            blogs[u[:-1]] = gender
            #print("added")
        #print (j['description'])
        #print (gender)
        #print("********")

print(blogs)

count = 0
g = ""
op = ""
fout = open("allPosts.txt", "w")
for blog in blogs:
    #THIS IS GIVING US HTML SO THERE IS A LOT OF 'JUNK' IN THE POST, PROBABLY EASY TO WEED OUT
    k = client.posts(blog, type='text', filter="html") #only gets up to 20 posts but i think thats ok
    posts = k[u'posts']
    for post in posts:
        try:
            d = post['date']
            p = post[u'trail'][0]
            if u'is_current_item' in p:
                origPost = p[u'content_raw']
                wordsEstimate = origPost.count(" ")
                if wordsEstimate >= 150:
                    g = blogs[blog] + "\n"
                    print(g)
                    op = str(origPost)
                    #fout.write(blog + ":\n")
                    #fout.write()
                    #fout.write(origPost + "\n")

        except:
            pass
            #fout.write("THERE WAS AN ERROR")
            #fout.write("\n**********\n")
        if g and op:
            fout.write(str(op.encode(encoding='UTF-8',errors='strict')))
            fout.write("\n**********\n")
            count += 1
        g = ""
        op = ""

fout.close()
print(count)

