import requests
import bs4

def downloadPage(url):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text,"html.parser")

    title=soup.find("h2",class_="chapter-title").get_text()
    # print(title) #检测是否能够获取标题内容
    page=title+".txt" #拟定每章小说以文本文件类型保存

    knowledges=soup.find_all("div",class_="article")
#     print(knowledges) #检测是否能够获取小说内容
# downloadPage("https://www.qimao.com/reader/index/149774/")
    for knowledge in knowledges:
        with open(page,"w+") as f:
            print(f"[+]当前正在下载{page}")
            f.write(str(knowledge.text))


pageNum=int(input("[+]请输入你要下载多少页："))
for i in range(70,71+pageNum-1):
    if i==70:
        downloadPage("https://www.qimao.com/reader/index/149774/")
    else:
        url="https://www.qimao.com/shuku/149774-3172"+str(i)+"/"
        downloadPage(url)