# Aviatrix App for Splunk
Copyright &copy; 2014-2017 Aviatrix Systems,Inc. All rights reserved.

* **App Homepage:** https://splunkbase.splunk.com/app/3585/
* **Authors:** Rakesh Ranjan
* **App Version:** 1.0

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

##### 1. VPN Gateway locations by number of connections
![VPN_Gateway_locations_by_number_of_connections](sample/1_VPN_Gateway_locations_by_number_of_connections.png)

##### 2. Top 10 VPN connection duration by users
![Top_10_VPN_connection_duration_by_users](sample/2_Top_10_VPN_connection_duration_by_users.png)

##### 3. Top 10 VPN connection duration by users (hh:mm:sec)
![Top_10_VPN_connection_duration_by_users (hh:mm:sec)](sample/3_Top_10_VPN_connection_duration_by_users(hh:mm:sec).png)

##### 4. Total User connection time by gateway
![Total_User_connection_time_by_gateway](sample/4_Total_User_connection_time_by_gateway.png)

##### 5. Active VPN Sessions
![Active_VPN_Sessions](sample/5_Active_VPN_Sessions.png)

##### 6. Destination services by number of connections
![Destination_services_by_number_of_connections](sample/6_Destination_services_by_number_of_connections.png)

##### 7. Destination IP
![Destination_IP](sample/7_Destination_IP.png)


### Gateway statistics

This dashboard analyses Gatewway related data like network interface, memory, cpu, disk load,etc.
![Gateway_Statistics_fitering](sample/8_Gateway_Statistics_fitering.png)

##### 1. Average Rx rate(Kb/s)
![Average_Rx_rate_Kbps](sample/9_Average_Rx_rate_Kbps.png)

##### 2. Average Tx rate(Kb/s)
![Average_Tx_rate_Kbps](sample/10_Average_Tx_rate_Kbps.png)

##### 3. Average CPU Idle time
![Average_CPU_Idle_time](sample/11_Average_CPU_Idle_time.png)

##### 4. Average disk usage
![Average_disk_usage](sample/12_Average_disk_usage.png)


### VPN Session

This dashboard analyses data specific to VPN sessions. By default, it shows charts for all VPN sessions, but it can be filtered to show data corresponding to a VPN user in a particular gateway.
![Vpn_Filtering](sample/13_VPN_Session_fitering.png)

##### 1. VPN connection duration by Gateway and User
![VPN_connection_duration_by_Gateway_and_User](sample/14_VPN_connection_duration_by_Gateway_and_User.png)

##### 2. VPN number of connections by SRC and DST IP
![VPN_number_of_connections_by_SRC_and_DST_IP](sample/15_VPN_number_of_connections_by_SRC_and_DST_IP.png)

##### 3. Rx Bytes
![Rx_Bytes](sample/16_Rx_Bytes.png)

##### 4. Tx Bytes
![Tx_Bytes](sample/17_Tx_Bytes.png)

### Security statistics

This dashboard shows data related to rules violations which can be filtered over gateway.
![Security_statistics_filtering](sample/18_Security_statistics_filtering.png)

##### 1. Accepted domain names
![Accepted_domain_names](sample/19_Accepted_domain_names.png)

##### 2. Blocked domain names
![Blocked_domain_names](sample/20_Blocked_domain_names.png)

## Support
Found a bug or need a feature?
  [Open an issue on github](https://github.com/AviatrixSystems/SplunkforAviatrix/issues)
