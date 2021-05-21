import requests;
from bs4 import BeautifulSoup
from datetime import date,time,datetime
import csv
columns=["name","website","problem","language","result","score","sub_time"]

submissions=[]
def get_website(url):
    if url.find("codechef") != -1:
        return "codechef"
    if url.find("hackerrank") != -1:
        return "hackerrank"
    if url.find("codeforces") != -1:
        return "codeforces"
    if url.find("hackerearth") != -1:
        return "hackerearth"
    if url.find("leetcode") != -1:
        return "leetcode"
    else:
        return url

def stalk_user(handle):

    today=date.today()

    hit_url=f"https://www.stopstalk.com/user/submissions/{handle}";
    print(f"stalking {handle}")
    req=requests.get(hit_url)
    soup=BeautifulSoup(req.text,'html.parser')
    _table=soup.find('table',{"class":"submissions-table"})
    if not _table:
        print("Aajtak koi submission nai h ...")
        return
    tbody=_table.find('tbody')
    rows=tbody.findChildren('tr')
    for row in rows:
        allHeadings=row.findAll("td")
        name=allHeadings[0].div.a.text
        website=allHeadings[1].a['href']
        website=get_website(website)
        problem=allHeadings[3].div.a['href']
        problem=f"https://www.stopstalk.com{problem}"
        language=allHeadings[4].text
        result=allHeadings[5].img['title']
        score=allHeadings[6].text
        sub_time=row.find("td",{"class":"stopstalk-timestamp"})
        sub_date=date.fromisoformat(sub_time.text.split(" ")[0])
        sub_object={"name":name,"website":website,"problem":problem,"language":language,"result":result,"score":score,"sub_time":sub_date}
        if today<=sub_date:
            print(sub_object)
            submissions.append(sub_object)


if __name__ == '__main__':
    members=["abskbnsl","ananyapunia28","ananya23101","danshika42","anuragshukla07","acrolyte","avi_11","gauravkm59829","gauri_dargar","hrshb05","kanishka_nagar","kritika_m22",
    "kunnu1371",
    "bolt",
    "mridulcr7cr7",
    "nancyksd10",
    "nishantjawla",
    "pjra99",
    "prashant182002",
    "preksha002",
    "ritikasingh02",
    "shivaag04",
    "shvmsh20",
    "shivendu_mishra",
    "shreya_porwal19",
    "s_infinity21",
    "smriti2411",
    "sumeetkvd",
    "itsutkarsh2711",
    "vansri24",
    "rey_yuvraj","lakshaykumar0510"]
    for member in members:
        stalk_user(member)
    
    submissions_file_name="test.csv"
    try:
        with open(submissions_file_name,"w") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=columns)
            writer.writeheader()
            for submission in submissions:
                writer.writerow(submission)
    except IOError:
        print("I/O error")