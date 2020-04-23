from django.shortcuts import render

from .models import Projects,Portfolio,Blogs

def index(request):

    myself = '''Hi! I’m Kishan, a student born and raised in Madurai, India. I have been pursuing my B.Tech degree (Information Technology) since 2017. I try to grab any opportunity I can in developing myself and enhancing my abilities. 
    I am an interesting, fun-loving guy with a good sense of humor. One thing about me that is important to know though is that at first I come off as a very shy individualistic guy but once I get to know people and are comfortable with my environment, I am great. 
    It is hard for me to make friends but once I make them, it’s great and I am all different. I joke, laugh and humor people and I also get as much as I give. I am a very kind, compassionate, sensitive guy as my close friends will tell you. 
    I have a tough shell but on the inside I am soft. I am also a very principled person and stand strong on what is right and wrong. I am also a very straight and honest person.'''

    mrs = Projects()
    mrs.img = 'movies.png'
    mrs.name = 'MOVIE RECOMMENDER SYSTEM'
    mrs.desc = 'Makes a prediction of which Movie a user may like based on his activity on the system.'
    mrs.liveDemo = 'https://movierecommendersystem.herokuapp.com/'
    mrs.codeLink = 'https://github.com/kishan0725/Content-Based-Movie-Recommender-System'

    sf = Projects()
    sf.img = 'mails.png'
    sf.name = 'SPAM FILTER'
    sf.desc = "A spam filter is a program that is used to detect unsolicited and unwanted email and prevent those messages from getting to a user's inbox."
    sf.liveDemo = 'https://spam-check.herokuapp.com/'
    sf.codeLink = 'https://github.com/kishan0725/End-to-End-Spam-Filter'

    hms = Projects()
    hms.img = 'hospitals.png'
    hms.name = 'HOSPITAL MANAGEMENT SYSTEM'
    hms.desc = "The software that covers all the aspects of management and operation of hospital."
    hms.liveDemo = 'https://kishan0725.000webhostapp.com/'
    hms.codeLink = 'https://github.com/kishan0725/Hospital-Management-System'

    dl = Projects()
    dl.img = 'dl.png'
    dl.name = 'IMAGE CLASSIFICATION USING VGG16 AND RESNET50'
    dl.desc = "Classifying images of cats and dogs using Transfer Learning models such as Visual Geometry Group 16 (VGG16) and Residual Networks 50 (ResNet50)."
    dl.liveDemo = ''
    dl.codeLink = 'https://github.com/kishan0725/Breast-Cancer-Wisconsin-Diagnostic'

    bmi = Projects()
    bmi.img = 'bmix.png'
    bmi.name = 'BMI PREDICTION'
    bmi.desc = "Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women and find out if you are healthy."
    bmi.liveDemo = 'https://bmi-prediction.herokuapp.com/'
    bmi.codeLink = 'https://github.com/kishan0725/BMI_Prediction'

    ga = Projects()
    ga.img = 'education.png'
    ga.name = 'GRADUATE ADMISSION'
    ga.desc = "To estimate chances of graduate admission from an Indian perspective based on the features like GRE Scores, TOEFL Scores, UG CGPA, etc."
    ga.liveDemo = 'https://graduateadmission.herokuapp.com/'
    ga.codeLink = 'https://github.com/kishan0725/Graduate-Admission'

    bcp = Projects()
    bcp.img = 'cancerx.png'
    bcp.name = 'BREAST CANCER PREDICTION'
    bcp.desc = "Predict whether the given patient is having Malignant or Benign tumor based on the attributes in the given dataset."
    bcp.liveDemo = ''
    bcp.codeLink = 'https://github.com/kishan0725/Breast-Cancer-Wisconsin-Diagnostic'

    ad = Projects()
    ad.img = 'ad.png'
    ad.name = "PREDICTION OF AD’S SUCCESS"
    ad.desc = "A binary classification problem where the task is to predict whether an ad buy will lead to netgain."
    ad.liveDemo = ''
    ad.codeLink = 'https://github.com/kishan0725/Predict-the-Ad-success'

    gsp = Projects()
    gsp.img = 'graph.png'
    gsp.name = "GOOGLE STOCK PRICE PREDICTION"
    gsp.desc = "Predicting the open stock price of Google using a type of recurrent neural network known as Long Short-Term Memory (LSTM)."
    gsp.liveDemo = ''
    gsp.codeLink = 'https://github.com/kishan0725/Google-Stock-Price-Prediction'

    psc = Projects()
    psc.img = 'security.png'
    psc.name = "PASSWORD STRENGTH CLASSIFIER"
    psc.desc = "The software that analyzes the strength of the password to facilitate organizations launch a multi-faceted defense against password breach."
    psc.liveDemo = 'https://checkpasswordstrength.herokuapp.com/'
    psc.codeLink = 'https://github.com/kishan0725/Checking-the-Password-Strength-using-ML'

    food = Projects()
    food.img = 'food.png'
    food.name = "FOODIE"
    food.desc = "A food delivery app developed using ReactJS that brings delicious food from your favourite local restaurant right to your door."
    food.liveDemo = ''
    food.codeLink = 'https://github.com/kishan0725/Foodie'

    phn = Projects()
    phn.img = 'phone.png'
    phn.name = "SIMPLE PHONE CALL APP"
    phn.desc = "A mobile app that can make a phone call and send SMS. The app is developed using Android Studio. Speech Recognizer can also be used for converting speech to text in order to send long messages instead of typing."
    phn.liveDemo = ''
    phn.codeLink = 'https://github.com/kishan0725/My-Phone-App'

    css = Portfolio()
    css.img = "sslc.jpg"
    css.name = "CENTUM IN SCIENCE & SOCIAL SCIENCE"
    css.ctg = "Award"

    tip = Portfolio()
    tip.img = "tip.jpg"
    tip.name = "TENSORFLOW IN PRACTICE"
    tip.ctg = "Certification"

    lt = Portfolio()
    lt.img = "lt.jpg"
    lt.name = "LOONEY TUNES"
    lt.ctg = "Art"

    ml = Portfolio()
    ml.img = "ml.jpg"
    ml.name = "MACHINE LEARING"
    ml.ctg = "Certification"

    s2 = Portfolio()
    s2.img = "schl2.jpeg"
    s2.name = "SCHOOL SECOND (12TH GRADE)"
    s2.ctg = "Award"

    sql = Portfolio()
    sql.img = "sqlc.jpg"
    sql.name = "SQL FUNDAMENTALS"
    sql.ctg = "Certification"

    cpl = Portfolio()
    cpl.img = "couple.jpg"
    cpl.name = "COUPLE"
    cpl.ctg = "Art"

    md = Portfolio()
    md.img = "msv1.jpeg"
    md.name = "How to handle missing values with Python?"
    md.ctg = "Article"
    md.link = "https://medium.com/@kishansmart0/how-to-handle-missing-values-with-python-7560bd7be7a2?source=friends_link&sk=4c8c80907bd6e43650476ca82e1fa80f"

    time = Blogs()
    time.img = "time.jpg"
    time.name = "THE VALUE OF TIME"
    time.desc = "Imagine there is a bank that credits your account each morning with $86,400. It carries over no balance from day to day. Every evening deletes whatever......"
    time.link = "https://kishan0725.wordpress.com/2018/08/18/the-value-of-time/"

    rel = Blogs()
    rel.img = "cpl.jpg"
    rel.name = "THE KEYS TO A SUCCESSFUL RELATIONSHIP"
    rel.desc = "Being in a loving long-term romantic relationship is one of the surest routes to long term happiness. But it ....."
    rel.link = "https://kishan0725.wordpress.com/2018/08/22/the-keys-to-a-successful-relationship/"

    dtr = Blogs()
    dtr.img = "destiny1.jpg"
    dtr.name = "YOUR DETERMINATION DETERMINES YOUR DESTINY"
    dtr.desc = "What is your dream life? What kind of destiny you want to create for yourself? At one point, we have a clue what......"
    dtr.link = "https://kishan0725.wordpress.com/2018/08/24/your-determination-determines-your-destiny/"

    gl = Blogs()
    gl.img = "goal.jpg"
    gl.name = "7 P'S OF GOAL SETTING"
    gl.desc = "When you are inspired by the generosity of philanthropists, you aspire to be one of them. However, you have to be rich. In order to be rich....."
    gl.link = "https://kishan0725.wordpress.com/2018/12/09/7-ps-of-goal-setting/"

    psy = Blogs()
    psy.img = "hope.jpg"
    psy.name = "THE PSYCHOLOGY OF HOPEFULNESS"
    psy.desc = "Hopefulness refers to an optimistic attitude and mindset that allows you to see the bright side of things and plan for a better future. This concept represents.... ."
    psy.link = "https://kishan0725.wordpress.com/2019/05/28/the-psychology-of-hopefulness/"

    itm = Blogs()
    itm.img = "time.jpeg"
    itm.name = "IMPORTANCE OF TIME MANAGEMENT"
    itm.desc = "What is time management? It is a set of principles, practices, skills, tools and systems that help you use your time to accomplish what you want....."
    itm.link = "https://kishan0725.wordpress.com/2018/12/07/importance-of-time-management/"


    


    projects = [mrs,sf,hms,dl,bmi,ga,bcp,ad,gsp,psc,food,phn]
    portfolio = [css,tip,lt,ml,s2,sql,cpl,md]
    blogs = [time,rel,dtr,psy,gl,itm]
    return render(request, 'index.html',{'myself':myself,'projects':projects,'portfolio':portfolio,'blogs':blogs})
