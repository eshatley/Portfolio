#A wrapper that will run Houdini in a custom environment

import subrocess

#Set the path to Houdini's executable file. Note to self, double check Houdini version
#Once we have the path, Python can open it.
houdini = 'C:/Program Files/Side Effects Software/Houdini 16.5.536/bin/houdinifx.exe'

#Open up Houdini
subprocess.Popen(houdini)
