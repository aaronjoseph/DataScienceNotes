SSH is Secure Shell

For SSH to work the remote system needs to have ssh running.

```shell
# Command to check ssh daemon status - if it is running
sudo systemctl status ssh
# Command to start ssh daemon
sudo systemctl enable --now ssh
# Check Firewall status
sudo systemctl status ufw
# Allow ssh
sudo ufw allow ssh
# To get IP Address
ip a # This gives you the IP Address of the ssh server
```