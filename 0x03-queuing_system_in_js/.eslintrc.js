module.exports = {
  "env": {
      "browser": true,
      "es6": true,
      "node": true,
      "mocha": true
  },
  "extends": "eslint:recommended",
  "globals": {
      "Atomics": "readonly",
      "SharedArrayBuffer": "readonly",
      "expect": "true"
  },
  "parserOptions": {
      "ecmaFeatures": {
          "jsx": true
      },
      "ecmaVersion": 2018,
      "sourceType": "module"
  },
  overrides: [
      {
          files: [
              "**/*.test.js"
          ],
          env: {
              mocha: true
          },
          plugins: ["mocha"],
          rules: {
              "mocha/no-exclusive-tests": "error",
              "mocha/no-pending-tests": "error"
          }
      }
  ]
};
