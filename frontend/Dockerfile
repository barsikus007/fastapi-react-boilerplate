FROM oven/bun:alpine as installer
ARG USER=bun

USER $USER
WORKDIR /app

# docker init's Dockerfile description for pnpm install command, I adapted it to bun
# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.bun/install/cache to speed up subsequent builds.
# Leverage a bind mounts to package.json and bun.lockb to avoid having to copy them into
# into this layer.
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=bun.lockb,target=bun.lockb \
    --mount=type=cache,target=/root/.bun/install/cache \
    # TODO if stmnt below true (seems it could ignored)
    # sharing=private was set intentionally because yarn (bun too?) override caches and two parallel yarn (bun too?) installs break each other
    # https://stackoverflow.com/a/75428179/12634253
    # --mount=type=cache,target=/root/.bun/install/cache,sharing=private \
    bun install --frozen-lockfile

COPY --chown=$USER public/ public/
COPY --chown=$USER package.json bun.lockb index.html .eslintrc.yaml .eslintignore vite.config.ts tsconfig.json tsconfig.node.json ./


FROM installer as development

EXPOSE 5173
CMD ["bun", "dev", "--host"]


FROM installer as builder

ARG VITE_APP_TITLE
COPY src/ src/
RUN bun run build


FROM nginx:stable-alpine as serve

COPY --from=builder /app/dist/ /usr/share/nginx/html/
# minimized nginx/nginx.prod.conf
# hadolint ignore=SC2016
RUN echo 'server{listen 80;listen [::]:80;server_name fastapi-react-boilerplate;location /{root /usr/share/nginx/html;try_files $uri /index.html;}}' > /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
