from random import choice, randint
from time import sleep
import datetime
from aya_functions import *

global dict_floor_queues #waiting queues to enter the runways
dict_floor_queues = {'queue_1':{}, 'queue_2':{}, 'queue_3':{}}

global dict_sky_queues #waiting queues to enter the runways
dict_sky_queues = {'queue_1':{}, 'queue_2':{}}

global dict_runways #airplane runways
dict_runways = {'runway_1':{}, 'runway_2':{}, 'runway_3':{}}

global dict_available_spaces
dict_available_spaces = {0:3,1:2,2:1,3:0} #parameterizing queues availability 

global dict_runway_to_queue #relating queues to runways
dict_runway_to_queue = {'runway_1':'queue_1','runway_2':'queue_2','runway_3':'queue_3'}

global dict_queue_to_runway #relating runways to queues
dict_queue_to_runway = {'queue_1':'runway_1','queue_2':'runway_2','queue_3':'runway_3'}

global global_dict_crashed_airplanes
global_dict_crashed_airplanes = {}
global_dict_crashed_airplanes['CURRENT TIME'] = {}

global airplane_crash #number of airplanes crashing
airplane_crash = 0

global emergency_landings #number of emergency landings
emergency_landings = 0


print('Welcome to AYA Airport!\n')

all_dicts_names = ['FLOOR QUEUES', 'RUNWAYS','TAKING OFF', 'SKY QUEUES','CRASHED AIRPLANES', 'EMERGENCY LANDINGS', 'LANDINGS']
moment_of_execution = str(datetime.datetime.now())
final_output_json = {'CURRENT TIME': {}}
all_df = []
SLEEP_TIME = 2
show_image = False
NUMBER_OF_ROUNDS = 4

while True:
  for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


  screen.fill((0, 0, 0))
  #pygame.draw.rect(screen, (152,152,152), pygame.Rect(30, 30, 60, 60), 2)
  pygame.display.flip()

#saving DataFrame on .xlsx
final_df = pd.concat(all_df)
final_df = final_df.reset_index()
final_df.drop(["index"], axis=1, inplace=True)
exec_moment = moment_of_execution.replace(':','-').replace(' ','-')
final_df.to_excel(f'AYA_Airport_Output_{exec_moment}.xlsx')

#saving the data on .json
with open(f'AYA_Airport_Output_{exec_moment}.json','a') as file:
  file.write(str(final_output_json))

#saving the data on .json
with open(f'AYA_Airport_Output_{exec_moment}.txt','a') as file:
  file.write(f'Number of rounds: {NUMBER_OF_ROUNDS}')
  file.write(f'\nTotal of airplane crashed: {airplane_crash}')