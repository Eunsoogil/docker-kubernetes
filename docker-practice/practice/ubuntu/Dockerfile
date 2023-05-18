# build시 사용할 platform 지정
FROM --platform=linux/amd64 amd64/ubuntu:20.04

# locale setup
ENV LANG C.UTF-8

# 자주 사용할 linux package download
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y ssh
RUN apt-get install -y wget
RUN apt-get install -y net-tools
RUN apt-get install -y curl
RUN apt-get install -y tree
RUN apt-get install openssh-server sudo -y
RUN apt-get install -y iputils-ping

# ssh 접속을 위한 셋업
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# root 비밀번호 setup
RUN echo 'root:1234' | chpasswd

# allow ssh, http, https
EXPOSE 22 80 443

# multiple command를 위한 shell script
WORKDIR /root
COPY start.sh .
RUN chmod +x start.sh

# CMD가 아닌 ENTRYPOINT를 사용하여 반드시 실행되도록 set up
ENTRYPOINT ["/sbin/init", "sh /root/start.sh"]
