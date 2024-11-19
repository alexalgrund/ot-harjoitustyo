from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    """Käynnistää ohjelman."""
    ctx.run("python src/main.py")

@task
def test(ctx):
    """Suorittaa testit pytestin avulla."""
    ctx.run("pytest")

@task
def coverage_report(ctx):
    """Luo testikattavuusraportin."""
    ctx.run("pytest --cov=src --cov-report html")
