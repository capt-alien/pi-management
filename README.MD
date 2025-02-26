To run the playbook use:


ansible-playbook -i ~/ansible/inventory.yml setup_rsyslog.yml

to ping everyhting:

ansible -i ~/ansible/inventory.yml all -m ping
