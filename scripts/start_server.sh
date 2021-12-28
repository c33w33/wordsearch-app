#!/bin/bash
cd /home/ec2-user/wordsearch-app
source environment/bin/activate
supervisord -c supervisord.conf