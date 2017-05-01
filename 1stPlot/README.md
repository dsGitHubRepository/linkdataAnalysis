
# Contents
1. [Project Overview](README.md#project-overview)
2. [Input Data](README.md#input-data)
3. [Analysis 1stplot](README.md#Analysis-plot1)
4. [Insight](README.md#Insight-and-matrices)
5. [Summary](README.md#Summary)

# Project Overview

Today's world is in the middle of extreme wave innovation. As the consumers data is incraesing exponentially, not only the business growth, but also the productivity of a company is significantly dependent on the modes of competition and value capture of the consumers' data.

# Input Data

The input data is a NASA server log file of 4.4 millions login activity that provides user's ip address, timestamp for login, HTTP reply code, byte transferred during resource usages, etc. 

# Analysis 1stplot

First part of the project analyzed the ips that accessed the site over a certain time period for which the log is collected. It sort out the top IPs that visited the site most frequently. The code can analyzed N number of top IPs and their corresponding login count over 4.4 million login activity.  

# Insight

The plot of the login count of various IPs shows an exponential decay which is expected since users' access to a popular site  through various IPs is a random event. When the users' login activity is logged over a very large number of IPs (ideally infinity); it is expected to show a Normal distribution.

# Summary

The distribution of login activity count shows an exponential decraese that predicts users log acvity will exibit Normal distribution.


