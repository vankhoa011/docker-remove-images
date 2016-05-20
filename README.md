# Docker Remove Obsolete Image

Docker Remove Obsolete Image


# Installation

sudo pip install docker-rmi

# Usage

To use it:

    $ docker-rmi --help

Example:

    $ docker-rmi -r nginx -n 3  # Docker remove nginx repo and keep 3 latest version

    $ docker-rmi # Docker keep 3 latest version of every repo
