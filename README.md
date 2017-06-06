# Aviatrix App for Splunk
Copyright &copy; 2014-2017 Aviatrix Systems,Inc. All rights reserved.

* **App Homepage:** https://splunkbase.splunk.com/app/3585/
* **Authors:** Rakesh Ranjan
* **App Version:** 1.1

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

##### 1. Aviatrix Gateway locations by number of connections
![Aviatrix_Gateway_locations_by_number_of_connections](sample/1_Aviatrix_Gateway_locations_by_number_of_connections.png)

##### 2. Top 10 VPN users
![Top_10_VPN_users](sample/2_Top_10_VPN_users.png)

##### 3. VPN users (hh:mm:sec)
![VPN_users (hh:mm:sec)](sample/3_VPN_users(hh:mm:sec).png)

##### 4. Gateway utilization time
![Gateway_utilization_time](sample/4_Gateway_utilization_time.png)

##### 5. Active VPN Sessions
![Active_VPN_Sessions](sample/5_Active_VPN_Sessions.png)

##### 6. Top 10 services
![Top_10_services](sample/6_Top_10_services.png)

##### 7. Top 10 Destination IPs
![Top_10_Destination_IPs](sample/7_Top_10_Destination_IPs.png)


### Gateway

This dashboard analyses Gatewway related data like network interface, memory, cpu, disk load,etc.
![Gateway_Statistics_fitering](sample/8_Gateway_Statistics_fitering.png)

##### 1. Average Rx rate(Kb/s)
![Average_Rx_rate_Kbps](sample/9_Average_Rx_rate_Kbps.png)

##### 2. Peak Rx rate(Kb/s)
![Peak_Rx_rate_Kbps](sample/10_Peak_Rx_rate_Kbps.png)

##### 3. Average Tx rate(Kb/s)
![Average_Tx_rate_Kbps](sample/11_Average_Tx_rate_Kbps.png)

##### 4. Peak Tx rate(Kb/s)
![Peak_Tx_rate_Kbps](sample/12_Peak_Tx_rate_Kbps.png)

##### 5. Average CPU utilization
![Average_CPU_utilization_time](sample/13_Average_CPU_utilization_time.png)

##### 6. Peak CPU utilization
![Peak_CPU_utilization_time](sample/14_Peak_CPU_utilization_time.png)

##### 7. Disk usage
![Disk_usage](sample/15_Disk_usage.png)


### VPN

This dashboard analyses data specific to VPN sessions. By default, it shows charts for all VPN sessions, but it can be filtered to show data corresponding to a VPN user in a particular gateway.
![Vpn_Filtering](sample/VPN_Session_fitering.png)

##### 1. Cumulative VPN session time
![Cumulative_VPN_session_time](sample/16_Cumulative_VPN_session_time.png)

##### 2. VPN connections by SRC and DST IP
![VPN_connections_by_SRC_and_DST_IP](sample/17_VPN_connections_by_SRC_and_DST_IP.png)

##### 3. Rx Bytes
![Rx_Bytes](sample/18_Rx_Bytes.png)

##### 4. Tx Bytes
![Tx_Bytes](sample/19_Tx_Bytes.png)

##### 5. Accessed services
![Accessed_services](sample/20_Accessed_services.png)

##### 6. Destination IP connections
![Destination_IP_connections](sample/21_Destination_IP_connections.png)

### Security

This dashboard shows data related to rules violations which can be filtered over gateway.
![Security_statistics_filtering](sample/22_Security_statistics_filtering.png)

##### 1. Accepted domain names
![Accepted_domain_names](sample/23_Accepted_domain_names.png)

##### 2. Blocked domain names
![Blocked_domain_names](sample/24_Blocked_domain_names.png)

## Support
Found a bug or need a feature?
  [Open an issue on github](https://github.com/AviatrixSystems/SplunkforAviatrix/issues)
