# install dependancies
set -ex
yum install -y http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm || true
yum install -y xfsprogs s3fs-fuse fuse-utils jq nmap-ncat telnet htop iotop iftop python2-pip
yum install -y redhat-lsb-core sudo wget bash curl gpg2 which git source vim
yum groupinstall -y 'Development Tools'
yum install -y rpmdevtools rpmlint createrepo yum-utils
# add dependancy repos here
