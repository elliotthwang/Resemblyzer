from setuptools import setup, find_packages

with open("/content/Resemblyzer/README.md", "r") as f:
    long_description = f.read()

with open("/content/Resemblyzer/requirements_package.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="Resemblyzer",
    version="0.1.1-dev",
    packages=find_packages(),
    package_data={
        "resemblyzer": ["/content/drive/My Drive/TTS/中文 Pretrained/Encoder/ge2e_pretrained.pt"]
    },
    python_requires=">=3.5",
    install_requires=requirements,
    author="Corentin Jemine",
    #author_email="corentin@resemble.ai",
    description="Analyze and compare voices with deep learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/resemble-ai/Resemblyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
