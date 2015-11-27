# Docker Remove Obsolete Image

Docker Remove Obsolete Image


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ docker-rmi --help

Example:

    $ docker-rmi -r nginx -n 3  # Docker remove nginx repo and keep 3 lastest version

    $ docker-rmi # Docker keep 3 lastest version of every repo



