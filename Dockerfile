# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN wget https://github.com/jgm/pandoc/releases/download/2.14.0.3/pandoc-2.14.0.3-1-amd64.deb \
    && dpkg -i pandoc-2.14.0.3-1-amd64.deb \
    && rm pandoc-2.14.0.3-1-amd64.deb

RUN pip install -r requirements.txt

#RUN apt-get -y update && \
#    apt-get -y install ruby-full

RUN apt-get update && \
    apt-get install -y --no-install-recommends asciidoctor

RUN apt -y install nodejs

#RUN apt-get install -y git-core curl build-essential openssl libssl-dev \
#    && git clone https://github.com/nodejs/node.git \
#    && cd node \
#    && ./configure \
#    && make \
#    && sudo make install

#RUN wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash



#RUN nvm install --lts

RUN apt -y install npm

RUN npm install npm@latest -g

RUN npm i asciidoctor

RUN npm i pagedjs

RUN apt-get install

RUN npm i puppeteer

RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

RUN npm init -y

RUN npm i -g @asciidoctor/core asciidoctor-pdf


#RUN gem install asciidoctor-pdf --pre

#RUN apt-get -qq -y install bison flex libffi-dev libxml2-dev libgdk-pixbuf2.0-dev libcairo2-dev libpango1.0-dev fonts-lyx cmake

#RUN gem install asciidoctor-mathematical

#RUN apt-get install -y graphicsmagick-imagemagick-compat graphicsmagick-libmagick-dev-compat

#RUN gem install prawn-gmagick

ADD main.py .

ADD library.py .

CMD ["python", "./main.py", "asciidoc/index.adoc"]

WORKDIR /data