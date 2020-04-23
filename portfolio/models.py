from django.db import models

class Projects:
    id:int
    img: str
    name: str
    desc: str
    liveDemo: str
    codeLink: str

class Portfolio:
    id:int
    img: str
    name: str
    ctg: str
    link: str

class Blogs:
    id:int
    img:str
    name:str
    desc:str
    link:str
    
