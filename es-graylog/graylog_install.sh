apt-get install apt-transport-https openjdk-8-jre-headless uuid-runtime pwgen
wget https://packages.graylog2.org/repo/packages/graylog-2.0-repository_latest.deb
sudo dpkg -i graylog-2.0-repository_latest.deb
sudo apt-get update && sudo apt-get install graylog-server
