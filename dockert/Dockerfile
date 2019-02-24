FROM python:3.7.2-stretch
RUN mkdir -p /opt/services/djangoapp/src
RUN mkdir -p /var/www/salesmanagement/media
RUN mkdir -p /var/www/salesmanagement/static
RUN chmod -R 777 /var/www/salesmanagement
WORKDIR /opt/services/djangoapp/src
COPY djangoEntrypoint.sh /start.sh
RUN pip install --upgrade pip
RUN git clone https://github.com/habi3000/salesManagement.git
RUN pip install -r salesManagement/requirements.txt
EXPOSE 8000
RUN chmod +x /start.sh
CMD ["/start.sh"]