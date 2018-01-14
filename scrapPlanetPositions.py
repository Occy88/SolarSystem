
class Planet:
    """
    Class to keep track of a planet's location and vector.
    """
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.velocityX=0.0
        self.velocityY=-0.0
        self.radius=1
        self.MASS=1

    def __repr__(self):
        return "Planet at: ("+str(round(self.x, 2))+', '+\
               str(round(self.y, 2))+'); radius: '+\
               str(round(self.radius, 2))+' & velocity: ('+\
               str(round(self.velocityX, 7))+', '+\
               str(round(self.velocityY, 7))+')'



import requests
from bs4 import BeautifulSoup
import re
import planets
from selenium import webdriver


def create_planet_list(download=True):
    planet_list=[]

    if download:
        url = 'http://www.theplanetstoday.com/#'
        browser = webdriver.Firefox()
        browser.get(url)
        app = browser.find_element_by_id("JavaApp") 
        html_doc=browser.page_source
        browser.close()
    else:
        f=open('page.txt', 'r')
        html_doc=f.read()
        f.close()
    soup = BeautifulSoup(html_doc, 'html.parser')
    shema=soup.find(id="JavaApp")
    test_str=str(shema)



    regex = r"<img .{70,150}left.{70,150}>"
    matches = re.findall(regex, test_str)

    match=matches[0]

    sun=planets.Planet()
    sun.x=float(re.findall(r"[0-9.]+", re.findall(r"left: [0-9.]*px", match)[0])[0])
    sun.y=float(re.findall(r"[0-9.]+", re.findall(r"top: [0-9.]*px", match)[0])[0])
    a="http://www.theplanetstoday.com/" + \
       re.findall(r"\"images.{15,50}\" ", match)[0][1:-2]
    file='img'+re.findall(r"/[^/]*$", a)[0]
    download_photo(a, file)
    sun.file=file
    sun.MASS=10**35

    planet_list.append(sun)

    for match in matches[1:-1]:
        #print(match)
        a="http://www.theplanetstoday.com/" + \
           re.findall(r"\"images.{15,50}\" ", match)[0][1:-2]
        file='img'+re.findall(r"/[^/]*$", a)[0]
        #print(a, file)
        download_photo(a, file)

        y=re.findall(r"[0-9.]+", re.findall(r"top: [0-9.]*px", match)[0])[0]
        x=re.findall(r"[0-9.]+", re.findall(r"left: [0-9.]*px", match)[0])[0]
        r=re.findall(r"[0-9.]+", re.findall(r"width: [0-9.]*px", match)[0])[0]

        planet_list.append(createPlanet(x, y, r, file, sun))

    return planet_list













def download_photo(img_url, filename):
    r_img = requests.get(img_url) 
    f = open(filename,'wb') 
    f.write(r_img.content) 
    f.close()


def createPlanet(x, y, radius, file, sun):
    a=planets.Planet()
    a.x=float(x)*3+100
    a.y=float(x)*2.25+75
    a.file=file
    a.radius=float(radius)
    a.MASS=float(radius)*10**12
    #create inital velocity that make sense
    x=(a.x-sun.x)
    y=(a.y-sun.y)
    r2=x**2+y**2
    a.velocityX=-(y/r2)*sun.MASS*planets.G_CONST*10**-27
    a.velocityY=(x/r2)*sun.MASS*planets.G_CONST*10**-27
    return a



if __name__=='__main__':
    l=create_planet_list(False)
    for i in l:
        print(i)









