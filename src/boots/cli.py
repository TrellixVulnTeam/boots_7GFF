import click

import boots._core


@click.group()
def main():
    pass


@main.command()
@click.option(
    '--personal-access-token',
    '--pat',
    'personal_access_token',
    prompt='Personal Access Token',
    hide_input=True,
)
def remotelock(personal_access_token):
    archive_bytes = boots._core.make_remote_lock_archive()
    archive_url = boots._core.post_file(data=archive_bytes)
    print(archive_url)
    build = boots._core.request_remote_lock_build(
        archive_url=archive_url,
        username='altendky',
        personal_access_token=personal_access_token,
    )

    build.wait_for_lock_build()

    build.get_lock_build_artifact()
