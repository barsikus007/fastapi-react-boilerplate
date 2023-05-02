module.exports = {
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module' },
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': 'warn',
  },
}

// package.json
// "eslint-config-airbnb": "^19.0.4",
// "eslint-plugin-import": "^2.25.4",
// "eslint-plugin-jsx-a11y": "^6.5.1"

// eslint.yml
// env:
//   browser: true
//   es2021: true
// extends:
//   - airbnb
//   - plugin:react/recommended
//   - plugin:react/jsx-runtime
// parserOptions:
//   ecmaFeatures:
//     jsx: true
//   ecmaVersion: latest
//   sourceType: module
// plugins:
//   - react
// rules: 
//   react/prop-types:  # skip props validation error in javascript
//     - warn
//     -
//       skipUndeclared: true
//   react/jsx-uses-react: off  # plugin:react/jsx-runtime wont work in vscode
//   react/react-in-jsx-scope: off  # plugin:react/jsx-runtime wont work in vscode
//   react/jsx-props-no-spreading: off  # Spreading is useful
//   jsx-a11y/label-has-associated-control: off  # Turned off due to modern label syntax wont work in vscode
//   arrow-parens:
//     - error
//     - 
//       as-needed
//   max-len:
//     - warn
//     -
//       code: 120
//       ignoreComments: true
//       ignoreTrailingComments: true
//       ignoreStrings: true
//       ignoreTemplateLiterals: true
//       ignoreRegExpLiterals: true
// settings: 
//   import/resolver:
//     node:
//       moduleDirectory:
//         - src
//         - node_modules
