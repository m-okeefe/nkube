### bug 1: serviceaccount inside the pod doesn't have permissions to get pods

on minikube start...

kubectl apply -f fabric8-rbac.yaml

helm init


### how to debug once deployed

kubectl exec -it unhinged-chinchilla-nkub-master-66ddbbfc59-5cb2m -- /bin/sh

journalctl -u nkube.service -f



### bug 2: kubeadm init did not accept capital A-Z letters in the token.

E5TB": token ["<token>"] was not of form ["^([a-z0-9]{6})\\.([a-


**  token1 and token1  can't have capitals!!!


had to add a "lower" in the go template in the chart secret.


### bug 3: the kubelet systemd service fails to start due to Swap being on

https://github.com/kubernetes/kubeadm/issues/610

fixed by updating the kubelet config to disable swap, in the part of nkube.sh that does a daemon-reload on the kubelet systemd service.



### bug 4: the master node won't start up

`172.17.0.6:6443: getsockopt: connection refused` and `container runtime is down`
