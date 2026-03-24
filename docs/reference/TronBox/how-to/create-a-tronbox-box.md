---
title: Create a TronBox Box
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Create a Box

To create a TronBox Box, you need:

* a GitHub repository
* a configuration file\
  The configuration file should be stored in the top-level directory of your repository. With the file and your GitHub repository, the unbox command will be:`tronbox unbox {USER_NAME || ORG_NAME}/{REPO_NAME}`

## Configuration file

Every TronBox Box contains a configuration file tronbox.json, which has three attributes: `ignore`, `commands`, and `hooks`.

### `ignore` (array)

An array of files or relative paths that TronBox ignores when unboxing, usually including `readme.md` or `.gitignore`. These files will not be copied from the Box's repository when you unbox.

```javascript
"ignore": [
  "README.md",
  ".gitignore"
]
```

### `commands` (object)

An object whose key-value pairs are a descriptor and console command respectively. Once your Box is successfully unboxed, the key-value pairs will be shown to users and can be seen as quick instructions.

The following example provides commands not only to compile, migrate, and test smart contracts but also for frontend development.

```javascript
"commands": {
  "Compile": "tronbox compile",
  "Migrate": "tronbox migrate",
  "Test contracts": "tronbox test",
  "Test dapp": "npm test",
  "Run dev server": "npm run start",
  "Build for production": "npm run build"
}
```

### `hooks` (object)

An object that contains console commands to be executed after unboxing. The command is usually `npm install` as we are using Node.js.

```javascript
"hooks": {
  "post-unpack": "npm install"
}
```
