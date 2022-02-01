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

def set_start_and_end(start_point, end_point):
  if start_point is not None:
    print('''
    What would you like to change? \n
    You can enter 'o' for 'origin',\n
    'd' for 'destination',\n
    or 'b' for 'both':
    ''')
    change_point = input()
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()
    elif change_point == 'o':
      start_point = get_start()
    elif change_point == 'd':
      start_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b' ... ")
      set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()
    return start_point, end_point

def get_start():
  print("Where are you coming from?\n Type in the corresponding letter:")
  start_point_letter = input()
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. let's try this again...")
    get_start()

def get_end():
  print("Where are you headed?\n Type in the corresponding letter:")
  end_point_letter = input()
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. let's try this again...")
    get_end()

for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)
print(landmark_string)