# -*- coding:utf8 -*-
import os
# 安装kubernetes
os.system('mv -f /config/kubernetes/kubernetes.repo /etc/yum.repos.d/')
os.system('yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes')
os.system('systemctl enable kubelet && systemctl start kubelet')