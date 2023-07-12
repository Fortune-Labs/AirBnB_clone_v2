from fabric import task

@task
def deploy(c):
    c.run("echo Deploying your application")

@task
def restart(c):
    c.run("echo Restarting the server")
