To set the time in same zone, use below terminal command.

```
localhost@shell:~$sudo dpkg-reconfigure tzdata

```

To synchronize the time on both machines follow below commands

Commands on Local Machine
```
localhost@shell:~$ sudo systemctl restart chrony
localhost@shell:~$ sudo systemctl status chrony
localhost@shell:~$ sudo systemctl enable chrony

```

Commands on Robot
```
ButtlerBot_docker@shell:~# sudo /etc/init.d/chrony restart
ButtlerBot_docker@shell:~# sudo initctl restart chrony
ButtlerBot_docker@shell:~# sudo initctl enable chrony
```

