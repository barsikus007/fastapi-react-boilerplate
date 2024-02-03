module.exports = {
  env: { browser: true, es2022: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
    'plugin:react/recommended',
    'airbnb',
    'prettier',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    ecmaFeatures: { jsx: true },
  },
  plugins: ['react-refresh', 'react', '@typescript-eslint'],
  rules: {
    // tsx import fixes
    '@typescript-eslint/ban-ts-comment': 'warn', // typescript moment
    'react/jsx-filename-extension': ['warn', { extensions: ['.tsx'] }], // JSX fix
    'import/extensions': [
      'off',
      'ignorePackages',
      { ts: 'never', tsx: 'never' },
    ], // .tsx extension fix

    // fix vite /public to / mapping cause eslint can't resolve vite.resolve.alias
    'import/no-unresolved': ['error', { ignore: ['^/.*'] }],
    'import/no-absolute-path': 'off',

    // allow imports autosort
    'import/order': [
      'error',
      {
        groups: [
          'builtin',
          'external',
          'internal',
          'parent',
          'sibling',
          'index',
          'object',
          'type',
        ],
        'newlines-between': 'always',
      },
    ],

    // other fixes
    'import/no-extraneous-dependencies': ['off'], // @tanstack/react-virtual wont resolve
    'react-refresh/only-export-components': 'warn', // vite initial rule
    'react/prop-types': ['warn', { skipUndeclared: true }], // skip props validation error
    // TODO test 'react/jsx-uses-react': 'off', // plugin:react/jsx-runtime wont work in vscode
    'react/react-in-jsx-scope': 'off', // plugin:react/jsx-runtime wont work in vscode
    'react/jsx-props-no-spreading': 'off', // spreading is useful
    'jsx-a11y/label-has-associated-control': 'off', // turned off due to modern label syntax wont work
    // TODO prettier
    // 'max-len': ['warn', {
    //   code: 120,
    //   ignoreComments: true,
    //   ignoreTrailingComments: true,
    //   ignoreStrings: true,
    //   ignoreTemplateLiterals: true,
    //   ignoreRegExpLiterals: true,
    // }],
  },
  settings: {
    'import/resolver': {
      typescript: {},
    },
  },
};
