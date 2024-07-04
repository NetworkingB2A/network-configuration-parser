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