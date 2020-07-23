#################
#
# Author:      Des Jones (dejones@alertlogic.com)
# Project:     defender automation
# Date:        Fri 14 Feb 17:39:51 GMT 2020
# Version:     1.0
# Git:         git@github.com:alertlogic/al-nodejs12-el7.git
# Notes:       rpmbuild -ba al-nodejs12-el7
#              please manage versioning automagically with git tags
# 
###################################################

Name:       al-nodejs12-el7
Version:    %{version}
Release:    %{release}
Summary:    AlertLogic al-nodejs12-el7
License:    AlertLogic (c). All rights reserved.
BuildArch:  noarch
Requires:   al-s3repo

%description
Install and configure al-nodejs12-el7

%prep
# add sources
cp -R %{_sourcedir}/%{name}/* .

%build
cat > %{name}.sh <<'EOF'
#!/bin/bash

# rpm macro variables
NAME=%{name}
VERSION=%{version}

# environment override variables
BOOTSTRAP=${BOOTSTRAP:-"false"}
BOOTSTRAPCFN=${BOOTSTRAPCFN:-"false"}
BOOTSTRAPLATE=${BOOTSTRAPLATE:-"false"}
MY_SECRET=${MY_SECRET:-""}

# install/update logic
if [ "${1}" == 1 ]; then # if install
  # save a secret from the environment
  if [ ! -z "${MY_SECRET}" ]; then
    sed -i "s/^MY_SECRET=.*$/MY_SECRET=${MY_SECRET}/" /etc/default/al-nodejs12-el7
  fi
  
  # if bootstrap, run on next boot, else run now
  if [ $BOOTSTRAPLATE == "true" ]; then
    echo "running config 3 minutes after next boot" 1>&2
    ln -s /usr/local/sbin/al-nodejs12-el7-config.sh /etc/rc.runoncelate/
  elif [ $BOOTSTRAPCFN == "true" ]; then
    echo "running config when called by cfn init" 1>&2
    ln -s /usr/local/sbin/al-nodejs12-el7-config.sh /etc/rc.runoncecfn/
  elif [ $BOOTSTRAP == "true" ]; then
    echo "running config after next boot" 1>&2
    ln -s /usr/local/sbin/al-nodejs12-el7-config.sh /etc/rc.runonce/
  else
    echo "running config now" 1>&2
    /usr/local/sbin/al-nodejs12-el7-config.sh
  fi

  echo "script installed and ran sucessfully" 1>&2
elif [ "${1}" == 2 ]; then # if update
  echo "script updated and ran sucessfully" 1>&2
fi

# if update or install
echo "install or update ran succesfully" 1>&2
EOF

%install
cp -R {usr,etc}/ %{buildroot}/
install -m 755 %{name}.sh %{buildroot}/usr/local/sbin/%{name}.sh

%files
/usr/local/sbin/*
/usr/local/share/%{name}/*
%config(noreplace) /etc/default/*

%pre
if [ "${1}" == 1 ]; then # if install
  echo "i run before rpm is installed" 1>&2
elif [ "${1}" == 2 ]; then # if update
  echo "i run before rpm is updated" 1>&2
fi

%post
/usr/local/sbin/%{name}.sh $1

%preun
# turn things off before uninstalling
echo "i run before rpm is uninstalled" 1>&2

%clean
if [ -d %{buildroot} ] ; then
  rm -rf %{buildroot}/*
fi

%changelog
# date "+%a %b %d %Y"
* Thu Mar 26 2020 desmond jones <dejones@alertlogic.com> %{version}-%{release}
- initial release

