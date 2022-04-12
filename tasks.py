from invoke import task




@task

def start(ctx):
	ctx.run("python3 src/game.py", pty=True)
	
@task
def test(ctx):
	ctx.run("pytest src", pty=True)
	

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src", pty=True)
    
@task
def coverage_report(ctx):
	ctx.run("coverage html", pty=True)
