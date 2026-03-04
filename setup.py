from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="churn-ml-project",
    version="0.1.0",
    author="gunasekaran_pandiyan",
    description="A churn prediction project using E2E machine learning pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gunasekaranpandiyan/churn-ml-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pandas>=2.3,<3.0",
        "numpy>=1.26,<2.0",
        "scikit-learn>=1.7,<2.0",
        "dill>=0.4,<0.5",
        "xgboost>=3.2,<4.0",
        "Flask>=3.1,<4.0",
        "gunicorn>=25.1,<26.0",
    ],
)
