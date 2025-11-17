from setuptools import setup, find_packages

setup(
    name="reddit-gaming-bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "praw>=7.7.0",
        "aiohttp>=3.8.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.8",
)
