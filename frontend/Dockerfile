#FROM node:16
FROM node:16-alpine

WORKDIR /app

COPY package.json .
COPY yarn.lock .
RUN yarn install

#ENV NODE_PATH=/node_modules
#ENV PATH=$PATH:/node_modules/.bin
RUN npm install

COPY . .

EXPOSE 3000
#EXPOSE 8000
EXPOSE 35729

CMD ['yarn', 'start']
