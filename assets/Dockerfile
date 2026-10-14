FROM ubuntu:24.04

ENV LC_ALL="C.UTF-8"

RUN apt update

# User and ssh section
RUN apt install -y \
    software-properties-common \
    sudo \
    openssh-server \
    ca-certificates curl \
    apt-transport-https \
    git \
    zip \
    mariadb-client

RUN mkdir -p /run/sshd
RUN chmod 755 /run/sshd

RUN ssh-keygen -A

RUN useradd -ms /bin/bash phpe
RUN echo "phpe:stpassword" | chpasswd
RUN usermod -aG sudo phpe
RUN echo "phpe ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN chown -R phpe:phpe /home/phpe
EXPOSE 22

RUN add-apt-repository ppa:ondrej/php
RUN apt update

RUN apt install php8.5-cli php8.5-curl php8.5-dom php8.5-mysql -y
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

RUN rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D"]

