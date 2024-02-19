/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string
  // https://vitejs.dev/guide/env-and-mode
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
