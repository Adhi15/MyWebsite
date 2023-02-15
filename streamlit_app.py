import streamlit as st
from PIL import Image

# https://adhi15-mywebsite-streamlit-app-k54ce4.streamlit.app/

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Adhihariharan AU
''')

image = Image.open('Profile.jpg')
st.image(image, width=150)


st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Hi, my name is Adhi. I am 22 years old. Currently pursuing my master at SMU,Singapore. 
- I am an enthusiastic and high energy driven professional aiming to land a role in data science, data analytics or software development with an organization of high repute offering challenging work profile in the IT industry. Have strong verbal and written communication skills.
- DOB: 15th January 2001
- Gmail: adhi15au@gmail.com
''')

#####################
# Navigation
# 16A2CB

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000000;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/adhihariharan-au-34b167171/" target="_blank">Adhihariharan AU</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
            <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Masters of Science** (Computing, Data Science and Engineering Research track), *Singapore Management University*, Singapore',
'2022-current')

txt('**Bachelors of Engeering** (Computer Science and Engineering), *Sri Venkateswara College of Engineering*, India',
'2018-2022')
st.markdown('''
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**IEEE SSCI 2022**, Student Helper, Singapore Management University, Singapore',
'2022')
st.markdown('''
- The IEEE SSCI 2022 conference was conducted at SMU Singapore. 
- As the student helper I along with a few others helped in conducting the event for 4 days. 
- In this event, I had the opportunity to talk and listen to various researchers and Professors was a very insightful experience.
''')

txt('**Youth Red Cross**, Member, India',
'2020-2022')
st.markdown('''
- Was part of the youth red cross. Participated in various events conducted in our college. 
''')

txt('**FORESE**','')
st.markdown('''
- A club under the placement cell of the college. It is a student run club in which the we conduct various different events to help students become professionally ampt for when they graduate and work in a professional environment. 
- Our flagship event is called Mock Placements. Which is organised for the pre final year students. 
- Over 360+ students participate in the event. 
- In this event we call in actual HRs from various companies like amazon, Zoho, Infosys, IBM, etc.. and they come to our college on a Saturday or a Sunday to conduct mock interviews for the students and if they are interested in the students talent or skil. They can offer them with internship offers. 
- Over 130 HRs from 80+ companies participate in the event ever year. 
- FORESE has helped me improve my communication skills and helped me in various aspects. 
- The biggest one being losing my fear oof speaking in front of a group of people. It has also helped in honing my leadership skills. 
''')

txt('**FORESE**, Executive Director, Sri Venkateswara College of Engeineering, India',
'2020-2021')
st.markdown('''
- As the Executive Director of the club. I along with 4 other executive directors conducted the Mock Placement event in 2021. 
- There were over 60 students that had worked under us. 
- The event was successfully conducted both online and offline. 
''')
txt('**FORESE**, Vice President, Sri Venkateswara College of Engeineering, India',
'2021-2022')
st.markdown('''
- As the Vice President as the club. I had to oversee the juniors work in conducting the event. 
''')

txt('**The Sparks Foundation**, Data Science and Business analytics Intern, Singapore',
'2021')
st.markdown('''
- I was a Data Science and Business analytics intern at The Sparks Foundation. 
- I had to make a data analysis on the Indian Preimer Leauge and provide insights. 
- I was also tasked to update my Linkedin and also the company helped me increase my connections on Linkedin. 
''')

txt('**Glosys Technology Solutions Pvt. Ltd.**, Trainee, India',
'2019')
st.markdown('''
- I was a Data science trainee in this company. I finished a four month course in the Data science using Python course. 
''')


#####################
st.markdown('''
## Projects
''')
txt('**DETECTION OF MALICIOUSLY TAMPERED CT SCANS USING ANOMOLY DETECTION**', '')
txt('**SMART TRAFFIC LIGHT DETECTION**', '')
st.markdown('''
https://github.com/Adhi15/Smart-Traffic-Light-Control-System/tree/main 
''')
st.markdown('''
Sri Sivasubramaniya Nadar College of Engineering conducted a 24 hour hackathon called Hack n Tackle in 2020. 
In which me and a group of three joined. The project we worked on and presented in that hackathon was called Smart Traffic control system. 
In the hackathon there were 3 reviews by mentors who were a mix of students, teachers and people from various industries and there was a final review which was conducted by top industry personalties. 
After the final review they selected 10 teams to go on for the next round to present in front of a panel of judges.
Our team project was selected for the top 10 teams. But unfortunately we were out of the competition after that. 
It was an interesting first experience for me to work as a team on something without any sleep which became a frequent thing nowadays. 
In India the traffic lights are either controlled manually or they have a specific timer that is default in every region or intersection. 
The signals donot account to the traffic and rather give more importance to time. 
- Traffic being a major problem in India. Which is likely to affect the daily livelihood of people. Our project proposes althering the traffic light timer based on traffic in the particular lane rather than keeping a default timer. 
- For example if there is a 4 way junction. Namely a,b,c and d (representing each lane in the four way junction). 
- Lets say there are 10 vehincles in a, 8 vehicles in b, 6 vehicles in c and 15 vehicles in d. 
- Our model will first identify the number of vehicles in each lane and present those numbers to our data structure algorithm which then calculates the greenlight time needed in each lane. 
- I along with a friend worked on the detection on the vehicles in each lane. 
- Our job was to present the number of vehicles in a each lane to the other two group members who further used the numbers to output the green light time.
- We used packages like opencv and PyTorch.
''')
txt('**A DATA ANALYTICS CASE STUDY**', '')
st.markdown('''
https://github.com/Adhi15/A-Data-Analytics-Case-study 
''')
st.markdown('''
During the quarantine in 2020. Coursera and google had launched the google data analytics professional certification. 
And i had taken that course. As part of the course I was tasked to do a capstone project which consisted of a case study. 
The problem statement given to me was, Bellabeat a fictional company has tasked me to focus on one of Bellabeat products and analyze smart device data to gain insight into how consumers are using their smart devices. 
This is my capstone project for the Google Data Analytics Professional Certificate. As a novice who was learning about data visualisation and data cleaning it was a challenge task and an interesting project to spend my time in. 
''')

txt('**ANALYZING NFT INDEXING CAUSED BY A LARGE-SCALE SOCIAL MEDIA PLATFORM**', '')
st.markdown('''
The basic objective of this Project:
- Figure out the relationship between social media platforms and NFTs on OpenSea.
- Create a value prediction model for NFTs based on information gathered from social media and OpenSea.
- We collect information announcing NFTs and follow the linked OpenSea URLs to extract NFT sales information and metadata from OpenSea.
- We crawl NFT images to analyse whether the image in itself exerts an influence on the price. Analysing growth and price trends on OpenSea against popularity metrics from Social Media platform reveals the possible significance of social media features on NFT value. We motivate average selling price as the metric to assign value to an NFT due to limited sales and highly volatile prices of NFT. We further develop and analyse predictive models using Social Media platform, OpenSea and NFT image features to assess their impact on asset value. Basically, 
- To the best of our knowledge, we create a data set for NFTs from OpenSea and their corresponding Social Media Input (can be a tweet, subreddit announcement, discord server announcement).
- We build ordinal classification models to predict NFT asset value using features from both OpenSea and Social Media, as well as the NFT image itself.
- We show that both Social Media Platform and OpenSea features influence the model output. In contrast the predictive power of image features is limited. This shows how branding and metadata (Social Media and OpenSea features) have a stronger effect on the value compared to the NFT product itself.
- We discuss related work on NFTs and asset valuation in the financial domain. 
- We briefly introduce the OpenSea platform and its features, as well as blockchain-specific terms used in our analysis.
- We discuss our data collection pipeline and analyse the impact of Social Media on the OpenSea marketplace from the temporal dimension and value perspective. 
- We discuss multimodal models for NFT asset valuation, present results using various models and feature subsets. At last we conclude with the limitations.
This was my final year project for my bachelor's degree.
''')
txt('**SYN-FLOOD ATTACK SIMULATION AND DETECTION**', '')

st.markdown('''
- The method in which we want to implement our work is by using a Kali Linux virtual machine to attack an Ubuntu virtual machine. 
- The Kali Linux machine uses the hping3 tool which is pre-installed inside the Kali Linux is used to flood the packets into the victim Ubuntu Machine. 
- We also perform IP spoofing which is a part of the tool. 
- The live capturing of packets using the Wireshark tool collects the data from the victim machine while the attack happens and stores it. 
- We use an open-source dataset, clean it and process it.
- Using Python packages and machine learning modules such as SVM, KNN, Gaussian NB, Random Forest, analyzation tree to classify the various DDoS attacks.
- In this project,we explore the various scopes of DDoS and DoS attacks and attempt to detect a DoS Attack with the help of Artificial Intelligence.
- We also give a glimpse of how DoS is executed and analyze DoS attack datasets to present a vivid visualization. 
- Our primary intention for this work is to create awareness about DDoS attacks to the general public and also to allure people's attention towards the importance of Cyber Security in the modern world.
This project was done as a group mini project during my bachelors degree.
''')

txt('**PREDICTING IMAGE SEQUENCING**', '')
st.markdown('''
In this work, 
- We are presented with the task of predicting image sequencing. 
- Image sequencing is a challenging task, but it has significant practical importance as well. 
- In this work, we focus on predicting the unknown order of three images given the order of the other five images of the same sequence. 
- Intuitively, we transfer the image sequencing task into a special video frame prediction problem and propose a model that relies on ResNet18 and ConvLSTM to help predict the order. 
- We conduct experiments on the given dataset and demonstrate that the performance of our model outperforms other baselines.
This project was done as a group project in one of the modules i took at SMU.
''')

txt('**SEMANTIC SEGMENTATION IN A WEAKLY SUPERVISED SETTING WITH ONLY IMAGE-LEVEL LABELS**', '')
st.markdown('''
For this project, 
- We address the problem of semantic seg- mentation in a weakly supervised setting with only image- level labels. 
- We provide a method for semantic segmenta- tion which is trained and evaluated on a given data set with 20 class labels. 
- Class activation maps (CAMs) are com- monly used to identify semantic segmentation problems. Us- ing the popular PuzzleCAM we generate labels on a pixel level. 
- Finally, we use the labels to generate the pseudo mask using inference segmentation. 
- We show the performance of our approach in both public and private leaderboards.
This project was done as a group project in one of the modules i took at SMU.
''')

txt('**FAKE NEWS DETECTION**', '')
st.markdown('''
Using human manual detection to detect fake news is not feasible as millions of articles around the world are being published and removed every minute and even seconds. 
News detection cannot be accountable or feasible manually. 

- To resolve the fake news issue is to create a model that will detect if the article is real or fake news using the  words, phrases, sources and titles from the article. 
- In order to do so, first apply a supervised learning algorithm on a labelled dataset, and train the model using training data followed by testing data before using it on real data. Before performing on real data, first perform a feature selection.
- As a result, we will be creating the model using different classification algorithms to choose the best fit classifier to obtain the highest F1 Score based on the calculated confusion matrix results.
- We also create a telegram bot that will help in fake news detection.
This project was done as a group project in one of the modules i took at SMU.
''')


#####################
st.markdown('''
## Skills
''')
txt3('**Programming**', '`Python`, `R`, `C`, `C++`, `HTML`, `CSS`, `JAVA`')
txt3('**Data processing**', '`SQL`, `pandas`, `numpy`')
txt3('**Data visualization**', '`matplotlib`, `seaborn`, `ggplot2`, `Tableau`')
txt3('**Machine Learning**', '`scikit-learn`')
txt3('**Deep Learning**', '`TensorFlow`, `opencv`, `Pytorch`')
txt3('**Web development**', '`HTML`, `CSS`')
txt3('**Model deployment**', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/adhihariharan-au-34b167171/')
txt2('GitHub', 'https://github.com/Adhi15')

