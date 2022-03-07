FROM node:16-alpine as builder
WORKDIR /app

COPY package.json yarn.lock .yarnrc.yml ./
COPY .yarn .yarn

RUN yarn set version stable
RUN yarn

COPY public public/


FROM builder as development
ENV NODE_ENV development

CMD ["yarn", "start"]


FROM builder as production
ENV NODE_ENV production

RUN yarn build

RUN yarn global add serve

CMD ["serve", "-s", "build", "-l", "3000"]
