FROM node:18-alpine as installer
WORKDIR /app

RUN corepack enable
COPY package.json pnpm-lock.yaml ./
RUN pnpm install

COPY public/ public/
COPY index.html .eslintrc.cjs vite.config.ts tsconfig.json tsconfig.node.json ./


FROM installer as development

CMD ["pnpm", "dev", "--host"]


FROM installer as builder

COPY src src/

CMD ["pnpm", "build"]
