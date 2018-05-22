kubectl exec -it irreverant-dragon-nkube-master-846d76b949-jpwl5 -- /bin/sh

journalctl -u nkube.service | less
