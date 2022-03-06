FROM node:16-alpine as base
WORKDIR /app

COPY package.json yarn.lock .yarnrc.yml ./
COPY .yarn .yarn

RUN yarn set version stable
RUN yarn

# TODO is needed?
ENV PATH $PATH:/node_modules/.bin

COPY public public/
# COPY config config/
# COPY scripts scripts/


FROM base as development
ENV NODE_ENV development

CMD ["yarn", "start"]


FROM base as production
ENV NODE_ENV production

RUN yarn build

RUN yarn global add serve

CMD ["serve", "-s", "build", "-l", "3000"]
