# C115-mininet-project
A repository dedicated to storing the final project of the C115 mininet - connected devices course at INATEL (Instituto Nacional de Telecomunicações).

---

## Index

1. [Proposal](#proposal)
2. [Documentation](#documentation)
3. [Author](#author)

## Proposal

```text
Question 1: Linear Topology with Eight Hosts

A. Topology Setup
- Using the standard Mininet command line, create a linear topology with eight hosts.
- Ensure the topology uses standardized MAC addresses.
- Configure bandwidth (`bw`) to 30 Mbps.
- Use the default Mininet controller (no need to specify).

B. Inspection
- Inspect interface information, MAC addresses, IP addresses, and ports using command-line inspection.

C. Illustrative Diagram
- Create an illustrative diagram of the topology, including all inspected details from the previous step.

D. Ping Tests
- Run ping tests between different nodes.
- Use the `tcpdump` command to display packet arrival at the nodes.

E. Iperf Tests
- Specify that Host 1 on port 5555 will act as a TCP server and Host 2 as a client.
- Conduct `iperf` tests with a 15-second duration, reporting every second.
- Perform tests for bandwidths of 1, 5, 10, 15, 20, and 25 Mbps.
- Reconstruct the topology for each bandwidth value.

Question 2: Custom Topology with Python

A. Topology Setup
- Use Python to create the following custom topology:
```

![Proposal topology for question 2](/src/images/question_2/proposal_topology.png)

```text
B. Inspection
- Inspect interface information, MAC addresses, IP addresses, and ports using command-line inspection.

C. Illustrative Diagram
- Create an illustrative diagram of the topology with all the inspected details.

D. Ping Tests with Standard Switches
- Run ping tests considering the standard switches.

E. MAC-Based Rules
- Remove previous rules and implement MAC address-based rules for specific nodes.
- Ensure communication between hosts on different switches.

F. Ping Tests for Rule Validation
- Conduct ping tests to demonstrate successful implementation of the MAC-based rules
```

---

## Documentation

The documentation files for the project are located in the ``docs`` folder.

### [Explanation of Question 1](docs/Explanation_question_1.md)  
This document provides a detailed explanation of **Question 1**, including commands, results, and observations.  

### [Explanation of Question 2](docs/Explanation_question_2.md)  
This document outlines the solution for **Question 2**, detailing the Python script, configurations, and testing outcomes.  

---

## Author

### [Matheus Fonseca](https://github.com/matheusAFONSECA)

Undergraduate student in the eighth (8th) semester of Computer Engineering at the National Institute of Telecommunications (Inatel). I participated in a Scientific Initiation at the Cybersecurity and Internet of Things Laboratory (CS&ILAB), where, in the Park Here project, I developed skills in computer vision applied to parking systems, focusing on license plate recognition and vehicle identification. Additionally, I served as a teaching assistant for Physics 1, 2, and 3, helping with practical classes, report writing, and answering theoretical questions. Currently, I am an intern at the Inatel Competence Center (ICC) in the PDI SW department.