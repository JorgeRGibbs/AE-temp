transportc2path="/opt/transportc2"
sudo systemctl stop transportc2.service; sudo rm -f $transportc2path/transportdb.sqlite; sudo systemctl start transportc2.service
sudo systemctl status transportc2.service --no-pager