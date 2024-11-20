#!/usr/bin/python

from mininet.topo import Topo


class NetworkTopo(Topo):
    # Custom topology for the network - 7 switches and 7 hosts
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)

        # Adding switches
        s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')
        s3 = self.addSwitch('s3', failMode='standalone')
        s4 = self.addSwitch('s4', failMode='standalone')
        s5 = self.addSwitch('s5', failMode='standalone')
        s6 = self.addSwitch('s6', failMode='standalone')
        s7 = self.addSwitch('s7', failMode='standalone')

        # Adding hosts
        h1 = self.addHost('h1', ip='192.168.0.1/28')
        h2 = self.addHost('h2', ip='192.168.0.2/28')
        h3 = self.addHost('h3', ip='192.168.0.3/28')
        h4 = self.addHost('h4', ip='192.168.0.4/28')
        h5 = self.addHost('h5', ip='192.168.0.5/28')
        h6 = self.addHost('h6', ip='192.168.0.6/28')
        h7 = self.addHost('h7', ip='192.168.0.7/28')

        # Connecting hosts to switches
        self.addLink(h1, s2)
        self.addLink(h2, s6)
        self.addLink(h3, s6)
        self.addLink(h4, s5)
        self.addLink(h5, s4)
        self.addLink(h6, s3)
        self.addLink(h7, s7)

        # Connecting switches
        self.addLink(s1, s2)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s6)
        self.addLink(s3, s7)

topos = {'networktopo': (lambda: NetworkTopo())}
