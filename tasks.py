from invoke import task
import subprocess

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
def coverage(ctx):
    """Suorittaa testit coverage-raportilla."""
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    """Generoi coverage-raportin HTML-muodossa."""
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    """Suorittaa pylintin tarkistuksen src-hakemistolle."""
    result = subprocess.run(['pylint', 'src'], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
