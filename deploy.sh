#!/bin/bash

# TAG can either be a git sha, or a build number from the CI/CD server
# In this case we're using Travis so we get the commit sha

TAG=${TRAVIS_COMMIT::8}

cd charts

sed -iE "s/%TAG%/${TAG}/" test-web-app/values.yaml

helm upgrade test-web-app test-web-app -i -f test-web-app/values.yaml
