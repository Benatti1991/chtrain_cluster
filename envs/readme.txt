Example of an inverted pendulum created with Chrono.
http://api.projectchrono.org/
Environment and syntax were made to be as close as possible to those provided by OpenAI
PPO algorithm based on the work by Patrick Coady
https://github.com/pat-coady/trpo

Command line options:
An env_name must be given through the command line options (even if for the moment there's only one environment) 
in order to create a directory for the log files. 

An example of command line can be the following

./ train.py chrono_pend -n 800 -b 20