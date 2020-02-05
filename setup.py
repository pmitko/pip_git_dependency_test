from setuptools import setup, find_packages

setup(
    name="pip git dependency",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "db@git+ssh://git@github.com/pmitko/pip_git_dependency.git@master#egg=db"
    ]
)
