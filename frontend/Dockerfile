FROM node:16-alpine as base
WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn

ENV PATH $PATH:/node_modules/.bin

COPY public public/
# COPY src src/
# COPY config config/
# COPY scripts scripts/
COPY tsconfig.json .

FROM base as development
ENV NODE_ENV development

CMD ["yarn", "start"]


FROM base as production
ENV NODE_ENV production

RUN yarn build

RUN yarn global add serve

CMD ["serve", "-s", "build", "-l", "3000"]
