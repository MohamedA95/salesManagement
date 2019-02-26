FROM ubuntu:latest
RUN mkdir -p /opt/services/djangoapp/src
RUN mkdir -p /var/www/salesmanagement/media
RUN mkdir -p /var/www/salesmanagement/static
RUN chmod -R 777 /var/www/salesmanagement
RUN apt-get update -y  && apt-get upgrade -y && apt-get  install  -y  python3 python3-pip postgresql-client-common postgresql-client-10 git
WORKDIR /opt/services/djangoapp/src
COPY djangoEntrypoint.sh /start.sh
RUN pip3 install --upgrade pip
RUN git clone https://github.com/habi3000/salesManagement.git
RUN pip3 install -r salesManagement/requirements.txt
EXPOSE 8000
RUN chmod +x /start.sh
CMD ["/start.sh"]
