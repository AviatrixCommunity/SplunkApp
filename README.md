# Aviatrix App for Splunk
Copyright &copy; 2014-2020 Aviatrix Systems,Inc. All rights reserved.

* **App Homepage:** https://splunkbase.splunk.com/app/3585/
* **Authors:** Rakesh Ranjan
* **App Version:** 1.6

## Description
Aviatrix App for Splunk is an advanced reporting and analysis tool for Aviatrix cloud networking software. This app leverages Aviatrix controller and gateway logs and Splunk's search and visualization capabilities to provide monitoring and troubleshooting capabilities along with rapid insight and operational visibility for CloudOps and infrastructure engineers.

## Getting Started

### Step1: Install App

This App is available on [Github](https://github.com/AviatrixSystems/SplunkforAviatrix). There are different ways to install splunk app.
#### Install via command line:
You can clone the github repository to install the App.
From ``$SPLUNK_HOME/etc/apps/`` directory, type the following command:

    git clone https://github.com/AviatrixCommunity/SplunkforAviatrix.git SplunkforAviatrix
Restart splunk to start using the app.

#### Install via Splunkbase:
Alternatively you can download tar file of this app from [splunkbase](https://splunkbase.splunk.com/app/3585/), and follow instructions available there to install the app.


### Step 2: Initial Setup
Make sure the latest version of Aviatrix software is installed before you start to configure the controller. You
should see the alert for software upgrade on the menu bar of the controller if a newer version is available.
Click Upgrade and wait for the upgrade to complete.

Follow the steps below to enable the logging for Splunk and Sumo Logic.

1. Launch the web browser and input the URL of your controller.
2. Once logged in, navigate to Settings > Loggings.
3. On the right hand side, enable the logging for Splunk by clicking the status button area. A new panel will appear for you to input Splunk IP Address and Splunk Server Listening Port. Enter Splunk enterprise IP address and port number(Splunk listens on port 9997 by default for forwarders). Click Enable when you are done.
4. To enable AviatrixRule logging, select packet logging when configuring gateway security policies. This is done by clicking the gateway of interests at Gateway panel.
5. To verify if the logs are delivered to the specified Splunk and Sumo Logic servers, make a user VPN connection through any gateway managed by the controller. At the prompt on Search bar of Splunk, type Aviatrix* and you shall see the Aviatrix logs.

## Features
This app comes with few prebuilt dashboards.

### Overview

This dashboard shows an overview of all the traffic logs collected by Splunk from Aviatrix controller.

![Overview](sample/splunk_overview.png)

### Gateway

This dashboard analyses Gatewway related data like network interface, memory, cpu, disk load,etc.
![Gateway](sample/splunk_gateway.png)

### Openvpn

This dashboard analyses data specific to VPN sessions. By default, it shows charts for all VPN sessions, but it can be filtered to show data corresponding to a VPN user in a particular gateway.
![OpenVPN](sample/splunk_openvpn.png)

### Security

This dashboard shows data related to rules violations which can be filtered over gateway.
![Security](sample/splunk_security.png)

### Dependency discovery

This dashboard shows lets you see network flow to/from servers across the network, and can be used for dependency discovery post cloud migration using IPMotion. This dashboard needs ``Sankey Diagram - Custom Visualization`` Splunk app to be preinstalled on Splunk server for visualisation. For more details on this dashboard and setup instructions, click [here](http://docs.aviatrix.com/HowTos/ipmotion_dependency_discovery.html).

![Dependency discovery](sample/splunk_dependency_discovery.png)

## Support
Found a bug or need a feature?
  [Open an issue on github](https://github.com/AviatrixSystems/SplunkforAviatrix/issues)
