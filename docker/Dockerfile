FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN mkdir temp
RUN cd temp
ADD "files/portal" "./temp/portal"
COPY "files/run_connect_yee_hong.py" "./temp/run_connect_yee_hong.py"
COPY "files/google-chrome-stable_current_amd64.deb" "./google-chrome-stable_current_amd64.deb"
COPY "files/chromedriver" "/usr/bin/chromedriver"
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver
RUN apt-get update -y
RUN apt install wget -y
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN apt-get install -f -y
RUN apt-get install python3-pip -y
RUN pip install selenium
RUN rm "./google-chrome-stable_current_amd64.deb"
