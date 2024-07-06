# network-configuration-parser
This package is to help network engineers have a easy interface to parse device config.
Currently the goal is to say a function(device stats, configuration, bgp neighbors(although that kinda fits into device stats hhhhmmmm..... ), ping up down(maybe))

goal for project
- Allow users to run commands or run services on their devices.
- Make adding to repo easy.
- User inputs device and services they want to run they get command and parsed output back to them.

Important for me
- Create tests for code

Why am I doing this?
- To help me learn programming better.
- Because creating a pyats parsers are hard to develop for and hard to add features
- Selfishly I want to have a repo that is known out in the community but one that also benefits me
- Not all data parsing is cli sometimes its controller based. and I want to be able to get data back from both controller based network devices and cli devices


Components 
- Nornir
  - Needed to help create my workflow
  - also help with creating inventory
- TextFSM
  - This is to take a TextFSM template and a CLI command and give back structured data
- ntc-templates
  - This is a library of textfsm templates
- nornir_netmiko
  - Used as a connection plugin for nornir to use netmiko
  - I decided to use this plugin because many many tools that are used in network automation uses netmiko under the hood.
  - Netmiko was developed based off paramiko and designed for network devices.
- Poetry
  - I wanted to try it out and help maintain my environment

Standards
- .yaml is my yaml file extension

Steps I follow
- Set up environment
  - set up github repo
  - install poetry
  - poetry init new-python-package-name
  - poetry add python-packages
- Create nornir config file
- Create nornir inventory for first testing
- play around with nornir a bit and see if my config file works and my inventory works.
- create script file to play around with.
- figure out how to run script with poetry
  - poetry shell to get into venv
  - poetry run python network-config-parser/init_script.py 
  - I did have to fix my folder structure in order to make sure I grabbed the correct files. 
- found out that my poetry is running python 3.8 but i want to use 3.12. now i need to figure out how to update my python in my poetry
- run poetry config --list to find what your poetry is configured to use.
- took me a while but here is what worked
  - update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1
  - This set python3.12 as my system default
  - I had a lot A LOT of issues here.
  - What worked for me was to uninstall python 3.8
  - run these commands
    - update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1
    - update-alternatives --install /usr/bin/python python3 /usr/bin/python3.12 1
    - curl -O https://bootstrap.pypa.io/get-pip.py
    - python get-pip.py
    - finally after all that poety was working with python 3.12
- also forgot to enable autocompletion in bash to i added that.
  - poetry completions bash >> ~/.bash_completion
- as I am trying to figure out how to use nornir_netmiko, I look at the nornir_netmiko github repo a lot to see how the project is laid out. one example is figuring out how to import the task I want to use quickly. I see that the task I want to use i in nornir_netmiko then in tasks finally I see the module I care about.
- I took a look at the multicommand task, but that appears to be more for configuration where you might get prompted to  run a command, type y on your keyboard then you need to hit enter on your keyboard for confirm. another example would be configuring a interface. and first you say the interface, then you enter the interface command mode and update the ip address or the description.
- Long story short that command doesnt work for what I want to do.
- instead of printing out a bunch of statements trying to get the data you need its better to use the vscode debug. that gives you a nice gui to look through the data and find what you need.
- Next I decided to test out how ntc and textfsm work together.
- started by creating a new module.
- I found a example on the ntc-template docs I was able to use that. 
- Init commit of project inbound. This is more or less a working solution basic solution for what I want.