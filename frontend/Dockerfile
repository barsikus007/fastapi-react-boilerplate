# pin version to prevent side-effects when new lts version releases
ARG NODE_VERSION=20
# ARG NODE_VERSION=lts
FROM node:${NODE_VERSION}-alpine as installer
ARG USER=node
ARG PNPM_VERSION=latest

RUN corepack enable && \
    corepack prepare pnpm@${PNPM_VERSION} --activate

USER $USER
WORKDIR /app

# docker init's Dockerfile description for pnpm install command
# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.local/share/pnpm/store to speed up subsequent builds.
# Leverage a bind mounts to package.json and pnpm-lock.yaml to avoid having to copy them into
# into this layer.
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=pnpm-lock.yaml,target=pnpm-lock.yaml \
    --mount=type=cache,target=/root/.local/share/pnpm/store \
    # TODO if stmnt below true (seems it could ignored)
    # sharing=private was set intentionally because yarn (pnpm too?) override caches and two parallel yarn (pnpm too?) installs break each other
    # https://stackoverflow.com/a/75428179/12634253
    # --mount=type=cache,target=/root/.local/share/pnpm/store,sharing=private \
    pnpm install --frozen-lockfile

COPY --chown=$USER public/ public/
COPY --chown=$USER package.json pnpm-lock.yaml index.html .eslintrc.yaml vite.config.ts tsconfig.json tsconfig.node.json ./


FROM installer as development

EXPOSE 5173
CMD ["pnpm", "dev", "--host"]


FROM installer as builder

COPY src/ src/
RUN pnpm build


FROM nginx:stable-alpine as serve

COPY --from=builder /app/dist/ /usr/share/nginx/html/
# minimized nginx/nginx.prod.conf
# hadolint ignore=SC2016
RUN echo 'server{listen 80;listen [::]:80;server_name fastapi-react-boilerplate;location /{root /usr/share/nginx/html;try_files $uri /index.html;}}' > /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
