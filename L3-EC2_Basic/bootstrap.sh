#!/bin/sh
yum -y install httpd php php-mysql \n
chkconfig httpd on \n
/etc/init.d/httpd start
