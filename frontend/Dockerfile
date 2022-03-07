FROM node:16-alpine as installer
WORKDIR /app

COPY package.json yarn.lock .yarnrc.yml ./
COPY .yarn .yarn

RUN yarn set version stable && yarn

COPY public public/


FROM installer as development
ENV NODE_ENV development
ENV WDS_SOCKET_PORT 80

CMD ["yarn", "start"]


FROM installer as builder
ENV NODE_ENV production

COPY src src/

CMD ["yarn", "build"]
