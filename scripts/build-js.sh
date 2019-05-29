#! /usr/bin/env bash

## Move the global navigaiton module
cp node_modules/@canonical/global-nav/dist/index.js static/js/global-nav.js

## Move the cookie-policy module
cp node_modules/@canonical/cookie-policy/build/js/cookie-policy.js static/js/cookie-policy.js

