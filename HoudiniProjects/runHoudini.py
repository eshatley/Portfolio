#A wrapper that will run Houdini in a custom environment

import os, subrocess

#Set the path to Houdini's executable file. Note to self, double check Houdini version
#Once we have the path, Python can open it.
houdini = 'C:/Program Files/Side Effects Software/Houdini 16.5.536/bin/houdinifx.exe'

#Setup environment
#Get path to folder where pipeline tools are located
rootPipeline = os.path.dirname(__file__).replace('\\','/')
os.environ['PYTHONPATH'] = '{}/tools;&'.format(rootPipeline)
#Variable pointing at pipeline tools folder
os.environ['ROOT_PIPELINE'] = rootPipeline
#Set project root
os.environ['JOB'] = '{}/3D'.format(os.path.dirname(os.path.dirname(__file__)))

#Open up Houdini
subprocess.Popen(houdini)
