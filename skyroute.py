from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
stations_under_construction = []
def greet():
  print('''\n Hi there and welcome to SkyRoute! \n 
  We'll help you find the shortest route betwen 
  the following Vancouver landmarks: \n''' + landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()
  
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

def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      metro_system = get_active_stations() if stations_under_construction else vc_metro
      if len(stations_under_construction) > 0:
        possible_route = dfs(metro_system, start_station, end_station)
      else:
        if not possible_route:
          return None
      route = bfs(metro_system, start_station, end_station)
      routes.append(route)
  shortest_route = min(routes, key=len)
  return shortest_route

def new_route(start_point = None, end_point = None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  if shortest_route is not None:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print(f"Unfortunately, there is currently no path between {start_point} and {end_point} due to maintenance.")
  print('Would you like to see another route? Enter y/n: ')
  show_landmarks()
  again = input()
  if again == 'y':
    new_route(start_point, end_point)
  
def show_landmarks():
  print('Would you like to see the list of landmarks again?\n enter y/n')
  see_landmarks = input()
  if see_landmarks == 'y':
    print(landmark_string)

def goodbye():
  print('Thanks for using SkyRoute!')

for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)
print(landmark_string)