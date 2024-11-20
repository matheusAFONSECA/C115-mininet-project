# Explanation of question 2

## Index

- [A. Creating topology](#a-creating-topology)
- [B. Checking informations of topology](#b-checking-informations-of-topology)
    - [Hosts configurantions](#hosts-configurantions)
    - [Dump of topology](#dump-of-topology)
    - [Net of topology](#net-of-topology)
    - [Nodes of topology](#nodes-of-topology)
- [C. Topology ilustration](#c-topology-ilustration)
- [D. Pings among different nodes using switches in normal mode](#d-pings-among-different-nodes-using-switches-in-normal-flow)
    - [Setting switches to normal flow](#setting-switches-to-normal-flow)
    - [Ping among nodes](#ping-among-nodes)
- [E. Defining new rules](#e-defining-new-rules)
    - [For 1 switch](#for-1-switch)
    - [For 2 switches](#for-2-switches)
    - [For 3 switches](#for-3-switches)
    - [For 4 switches](#for-4-switches)
- [F. Testting rules defined](#f-testting-rules-defined)
    - [For 1 switch](#for-1-switch-1)
    - [For 2 switches](#for-2-switches-1)
    - [For 3 switches](#for-3-switches-1)
    - [For 4 switches](#for-4-switches-1)


### A. Creating topology

The Python code used to create this topology can be found at [main.py](../src/main.py). The code sets the topology proposed.

![Creation of folder and python code 1](../src/images/question_2/folder_python/creating_code_in_project_folder_1.png)
![Creation of folder and python code 2](../src/images/question_2/folder_python/creating_code_in_project_folder_2.png)
![Creation of topology on putty](../src/images/question_2/custom_topology.png)

---

### B. Checking informations of topology

#### Hosts configurantions

![Configuration of H1 and H2](../src/images/question_2/config/config_h1_h2.png)
![Configuration of H3 and H4](../src/images/question_2/config/config_h3_h4.png)
![Configuration of H5 and H6](../src/images/question_2/config/config_h5_h6.png)
![Configuration of H7](../src/images/question_2/config/config_h7.png)

---

#### Dump of topology

![Dump of topology](../src/images/question_2/info/dump.png)

---

#### Net of topology

![Net of topology](../src/images/question_2/info/net.png)

---

#### Nodes of topology

![Nodes of topology](../src/images/question_2/info/nodes.png)

---

### C. Topology ilustration

![Topology ilustration](../src/images/question_2/c115_q2.drawio.png)

---

### D. Pings among different nodes using switches in normal flow

#### Setting switches to normal flow

![Setting normal flow](../src/images/question_2/xterm_switches/action_flow_normal.png)

---

#### Ping among nodes

![Ping among nodes](../src/images/question_2/xterm_switches/pingall.png)

---

### E. Defining new rules 

#### For 1 switch

![Rule for 1 switch](../src/images/question_2/xterm_switches/rules/h2-h3_1_switch.png)

---

#### For 2 switches

![Rule for 2 switches](../src/images/question_2/xterm_switches/rules/h6-h7_2_switches.png)

---

#### For 3 switches

![Rule for 3 switches](../src/images/question_2/xterm_switches/rules/h1-h4_3_switches.png)

---

#### For 4 switches

![Rule for 4 switches](../src/images/question_2/xterm_switches/rules/h1-h2_4_switches.png)

---

### F. Testting rules defined

#### For 1 switch

![Test rule for 1 switch](../src/images/question_2/xterm_switches/test_rules/h2-h3_1_switch.png)

---

#### For 2 switches

![Test rule for 2 switches](../src/images/question_2/xterm_switches/test_rules/h6-h7_2_switches.png)

---

#### For 3 switches

![Test rule for 3 switches](../src/images/question_2/xterm_switches/test_rules/h1-h4_3_switches.png)

---

#### For 4 switches

![Test rule for 4 switches](../src/images/question_2/xterm_switches/test_rules/h1-h2_4_switches.png)

---