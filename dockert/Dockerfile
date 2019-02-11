# start from an official image
FROM python:3.7.2-stretch

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
COPY djangoEntrypoint.sh /start.sh
# install our two dependencies
RUN pip install --upgrade pip

# copy our project code

RUN git clone https://github.com/habi3000/salesManagement.git
RUN pip install -r salesManagement/requirements.txt

# expose the port 8000
EXPOSE 8000
# define the default command to run when starting the container
RUN chmod +x /start.sh
CMD ["/start.sh"]
