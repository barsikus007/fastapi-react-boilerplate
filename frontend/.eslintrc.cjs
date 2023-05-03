module.exports = {
  env: { browser: true, es2022: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
    'plugin:react/recommended',
    'airbnb',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module', ecmaFeatures: { jsx: true } },
  plugins: [
    'react-refresh',
    'react',
    '@typescript-eslint',
  ],
  rules: {
    'react-refresh/only-export-components': 'warn',
    'react/jsx-filename-extension': ['warn', { extensions: ['.jsx', '.tsx'] }], // typescript moment
    '@typescript-eslint/ban-ts-comment': 'warn', // typescript moment
    'import/extensions': 'off', // no need to specify extensions for tsx
    'import/no-unresolved': 'off', // doesnt work with vite for no reason (react-dom/client and absolute)
    'import/no-absolute-path': 'off', // absolute import is useful in vite
    'react/prop-types': ['warn', { skipUndeclared: true }], // skip props validation error
    // TODO test 'react/jsx-uses-react': 'off', // plugin:react/jsx-runtime wont work in vscode
    'react/react-in-jsx-scope': 'off', // plugin:react/jsx-runtime wont work in vscode
    'react/jsx-props-no-spreading': 'off', // spreading is useful
    // TODO test 'jsx-a11y/label-has-associated-control': 'off', // turned off due to modern label syntax wont work in vscode
    'arrow-parens': ['error', 'as-needed'], // e => { e.doSmth() }
    'max-len': ['warn', {
      code: 120,
      ignoreComments: true,
      ignoreTrailingComments: true,
      ignoreStrings: true,
      ignoreTemplateLiterals: true,
      ignoreRegExpLiterals: true,
    }],
  },
  settings: {
    'import/resolver': {
      node: {
        extensions: ['.jsx', '.tsx'],
        paths: ['src'],
      },
    },
  },
};
