# bnas-project
Work assignments for Building Network Automation Solution training @ipspace

## Folder E01
Hands-on exercise for week1. Create a Github repository, including readme file and commit and push a file with lab description.

## Folder E02
Hands-on exercise for week2. Create a report. Consists basically of 2 files:
  * Python script: *build_map.py*
  * Ansible's Playbook: *latency_report.yml*
- **build_map.py**
Takes a list of hosts (IP or hostnames) and returns a dictionary as JSON formatted string with the optimized list of pairs. i.e., if the host list is "H1, H2, H3, H4 and H5", the returned dict is:
```
H1: [H2, H3, H4, H5]
H2: [H3, H4, H5]
H3: [H4, H5]
H4: [H5]
```
- **latency_report.yml**
  - The Playbook, takes a list of hosts and get the minimum pair sets to test RTT latency (ping).
  - Send the list to the *build_map.py* script and get the dictionary to iterate through
  - Launch the ping job on all specified hosts
  - Capture the results for each host and save them in individual files

It is assumed that there is the target Ansible's hosts file includes an alias named "ansible_host"

So far only supported for Cisco IOS devices

## Folder E03
Hands-on exercise for week3. Build data model and generate de ice configurations. Is based on "MPLS-infrastructure" example from ipspace. Starting from a fabric definition for a WAN cloud (that consists on few Leaf sites connected via point-to-point links to a Hub site) the playbooks extract per-nodes data and creates both generic and BGP configs.
- **fabric.yml**
WAN cloud data model
- **create-data-model.yml**
Playbook that extracts per-node data to "nodes.yml"
- **models/nodes.j2**
Nodes' data template
- **generic/gen_config.j2**
Generic configuration's template
- **generic/config_gen.yml**
Playbook that generates per node's generic configuration file
- **generic/deploy.yml**
Playbook that calls the configuration templates generations and in future will also call configuration push and test
- **bgp/bgp_config.j2**
BGP configuration's template 
- **bgp/config_bgp.yml**
Playbook that generates per node's BGP configuration file
- **bgp/deploy.yml**
Playbook that calls the configuration templates generations and in future will also call configuration push and test

## Folder E04
Hands-on exercise for week4. Generate and push device configurations. It continues the exercise E03. It builds the configuration in XML format (according to differnet Yang modules) that is passed on to the Ansible's Netconf module. Tested with Cisco IOS XE 16.7.1. Some differences compared to E03:
- **generic/gen_config_nc.j2**
Generic configuration's template in XML format. Uses "ietf-interfaces" Yang module for generic features and "Cisco-IOS-XE-native" Yang module for BFD config.
- **bgp/bgp_config.j2**
BGP configuration's template in XML format. Use "Cisco-IOS-XE-native" Yang module for BGP and route-map configurations

