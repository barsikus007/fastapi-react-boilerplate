FROM node:16

WORKDIR /app

COPY package.json ./
#ADD package.json /package.json

#ENV NODE_PATH=/node_modules
#ENV PATH=$PATH:/node_modules/.bin
RUN npm install

COPY . /app

#EXPOSE 8000
#EXPOSE 35729

#ENTRYPOINT ["/bin/bash", "/app/run.sh"]
CMD ["start"]
