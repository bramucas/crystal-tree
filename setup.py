import setuptools
from crystal_tree import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crystal-tree",
    version=__version__,
    author="Brais Muñiz",
    author_email="mc.brais@gmail.com",
    description="From decision trees to explainable logic programs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bramucas/crystal-tree",    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        'artificial intelligence',
        'explainable artificial intelligence'
        'logic programming',
        'answer set programming',
    ],
    python_requires='>=3.6.0',
    install_requires=[
        'sklearn'
    ],
    packages=[
        'crystal_tree',
    ]
)
