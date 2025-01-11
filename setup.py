from setuptools import setup, find_packages

setup(
    name="Fingilish",  # Replace with your actual library name
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,  # Includes files listed in MANIFEST.in
    install_requires=[],  # List dependencies here if any
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # If README is markdown
    description="A python library for iranian people to code better and easier.",
    author="soodi592",
    author_email="soodi.592.ali@gmail.com",
    license="MIT",  # Make sure this matches the contents of your LICENSE file
    url="https://github.com/soodi592/Finglish",  # Link to your repository or homepage
)