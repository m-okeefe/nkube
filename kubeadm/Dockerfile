#
# Pulled from marun/kubeadm
#
#
# https://github.com/marun/dkr-kubeadm/blob/master/Dockerfile



FROM meganokeefe/systemd-dind:latest 

ADD k8s.repo /etc/yum.repos.d/

RUN dnf -y update && dnf -y install\
 kubeadm\
 kubelet\
 kubectl\
 kubernetes-cni\
 bind-utils\
 bridge-utils\
 ebtables\
 findutils\
 hostname\
 htop\
 iproute\
 iputils\
 less\
 net-tools\
 procps-ng\
 tcpdump\
 traceroute\
 which\
 && dnf clean all

RUN systemctl enable kubelet

# kubeadm requires /etc/kubernetes to be empty
RUN rmdir /etc/kubernetes/manifests

# Docker requires /run have shared propagation in order to start the
# kube-proxy container.
RUN echo 'mount --make-shared /run' >> /usr/local/bin/dind-setup.sh
