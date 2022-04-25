from invoke import task




@task

def start(ctx):
	ctx.run("python3 src/menu.py", pty=True)
	
@task
def test(ctx):
	ctx.run("pytest src --ignore src/test_main_game.py", pty=True)
	
@task
def lint(ctx):
	ctx.run("pylint src", pty=True)
@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src --ignore src/test_main_game.py", pty=True)
    
@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html", pty=True)
