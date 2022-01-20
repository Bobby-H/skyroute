from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
def greet():
  print('''\n Hi there and welcome to SkyRoute! \n 
  We'll help you find the shortest route betwen 
  the following Vancouver landmarks: \n''' + landmark_string)

def skyroute():
  greet()

for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)
print(landmark_string)

skyroute()