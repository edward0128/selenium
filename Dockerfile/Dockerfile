FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get install git -y

COPY requirements.txt requirements.txt
COPY test test
RUN  pip3 install -r ./requirements.txt
# setting the ssh client
#ENV DEBIAN_FRONTEND=noninteractive
#RUN sed -i 's/archive.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list
#RUN apt update && apt install wget -y
#RUN echo deb http://deb.obspy.org xenial main >> /etc/apt/sources.list
#RUN wget --quiet -O - https://raw.github.com/obspy/obspy/master/misc/debian/public.key | apt-key add -
#RUN apt update
#RUN apt install -y openssh-server
#RUN mkdir /var/run/sshd
#RUN echo 'root:password' | chpasswd
#RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
#ENV NOTVISIBLE "in users profile"
#RUN echo "export VISIBLE=now" >> /etc/profile

# install the library by pip 
#RUN pip install --upgrade pip
#RUN pip install keras==2.2.4
#RUN pip install matplotlib
#RUN pip install pandas

## expose port 8888,22
#EXPOSE 8888
#EXPOSE 22

# Setting jupyter notebook
#COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

# install Anaconda3
#RUN wget --quiet https://repo.continuum.io/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
#    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
#    rm ~/anaconda.sh && \
#    echo "export PATH=/opt/conda/bin:$PATH" >> ~/.bashrc

###
#RUN mkdir /data-share
#RUN mkdir /lab

#COPY run_jupyter.sh run_jupyter.sh
#USER root
#CMD ./run_jupyter.sh
