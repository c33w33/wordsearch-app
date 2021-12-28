#!/bin/bash
cd /home/ec2-user/wordsearch-app
source wordsearch-app/environment/bin/activate
sudo pkill -f "supervisord.conf"
supervisord -c supervisord.conf