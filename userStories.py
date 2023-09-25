from database import *
import time

story1 = '''As a college student, I want to join inCollege, a specialized social networking app for students, so I can easily connect with my peers, discover career opportunities, and access academic resources. I want to create a profile highlighting my skills, interests, and education, and I'd like to connect with classmates and professionals in my field. Additionally, I want to stay updated on campus events, job postings, and relevant news to enhance my college experience and prepare for my future career. By using inCollege, I aim to build a strong network, gain valuable insights, and make the most of my college years.'''

story2 = '''As a college student, I want to use inCollege to explore internship opportunities relevant to my major and career goals. I plan to create a detailed profile showcasing my skills and experiences and connect with professionals and alumni in my field. I also want to receive personalized internship recommendations and access resources to help me succeed in my applications. By utilizing inCollege, I hope to secure valuable hands-on experiences that will boost my resume and prepare me for a successful career after graduation.'''

story3 = '''As a college student, I want to use inCollege to find study groups and collaborate with classmates on projects and assignments. I aim to create a profile highlighting my academic interests and connect with fellow students in my courses. I also want to access a feature that helps me schedule study sessions and track our progress. This will help me excel academically, build strong relationships with my peers, and make the most of my college education.'''

def userStories():
  cursor = conn.cursor()  # Create a cursor object to execute SQL commands
  
  cursor.execute("INSERT INTO stories (story) VALUES (?)", (story1,))
  cursor.execute("INSERT INTO stories (story) VALUES (?)", (story2,))
  cursor.execute("INSERT INTO stories (story) VALUES (?)", (story3,))
  
  conn.commit() 

def videoPlay():
  from landing import startupLanding
  print("Video is now playing")
  time.sleep(3)
  startupLanding()