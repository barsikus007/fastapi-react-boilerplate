FROM node:18-alpine as installer
WORKDIR /app

RUN corepack enable

# Run the application as a non-root user.
ARG USER=node
# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.local/share/pnpm/store to speed up subsequent builds.
# Leverage a bind mounts to package.json and pnpm-lock.yaml to avoid having to copy them into
# into this layer.
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=pnpm-lock.yaml,target=pnpm-lock.yaml \
    --mount=type=cache,target=/root/.local/share/pnpm/store \
    pnpm install
RUN chown -R $USER /app
USER $USER

COPY public/ public/
COPY package.json pnpm-lock.yaml ./
COPY index.html .eslintrc.cjs vite.config.ts tsconfig.json tsconfig.node.json ./


FROM installer as development

CMD ["pnpm", "dev", "--host"]


FROM installer as builder

COPY src src/

EXPOSE 5173

CMD ["pnpm", "build"]
