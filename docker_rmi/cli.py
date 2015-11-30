#!/usr/bin/env python
import click
HAS_DOCKER_PY = False
try:
    import docker
    from docker import Client
    from docker.utils import kwargs_from_env
    c = Client(version='auto', **kwargs_from_env(assert_hostname=False))
    HAS_DOCKER_PY = True
except ImportError:
    HAS_DOCKER_PY = False


def remove_image(repo, number_version):
    """ Remove image """
    if repo == '<none>':
        images = c.images(filters={"dangling": "true"}, quiet="true")
        if images:
            for image in images:
                try:
                    c.remove_image(image=image)
                except docker.errors.APIError as de:
                    print de
                except Exception as ex:
                    print ex

    images = c.images(name=repo)

    if len(images) >= number_version:
        for i in range(number_version, len(images)):
            try:
                c.remove_image(image=images[i]['Id'])
            except docker.errors.APIError as de:
                print de
            except Exception as ex:
                print ex


def get_list_repo(repo, number_version):
    """ Get list repo """

    if repo == 'all':
        images = c.images()
        repos = []
        for image in images:
            repos.append(image['RepoTags'][0].split(":")[0])
        repos = set(repos)
        for r in repos:
            remove_image(r, number_version)
    else:
        remove_image(repo, number_version)


@click.command()
@click.option('--repo', '-r', default='all', help='Specific one image repo or all repo')
@click.option('--number-version', '-n', default=3, help='Number version want to keep')
def main(repo, number_version):
    """Docker Remove Obsolete Image"""
    if HAS_DOCKER_PY is not True:
        print "docker-py is required"
    get_list_repo(repo, number_version)

if __name__ == '__main__':
    main()
