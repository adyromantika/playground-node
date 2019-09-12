# Node Playground [![Build Status](https://travis-ci.org/adyromantika/playground-node.svg?branch=master)](https://travis-ci.org/adyromantika/playground-node)

* Docker image
  * Simple Node.js app displaying "Hello World"
* Travis:
  * Build image and push to Docker Hub
  * Test that the container returns the correct string
  * Use helm to render the template
  * Simple bash script to provide tag substition

Obviously, there are more work to be done for a pipeline promotion from lower to higher environments.
