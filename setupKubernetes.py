# -*- coding:utf8 -*-
import os
# 安装kubernetes
os.system('yum -y install git')
os.system('cd /usr/local/ && git clone https://github.com/Tower-7/kubernetes.git')
os.system('cd /usr/local/kubernetes && tar -zxvf kubernetes.tar.gz')