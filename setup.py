import setuptools

version = {}
with open('./crystal_tree/_version.py') as fp:
    exec(fp.read(), version)

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='crystal-tree',
    version=version['__version__'],
    author='Brais Muñiz',
    author_email='mc.brais@gmail.com',
    description='From large, deep trees to short, clear explanations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bramucas/crystal-tree',    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'artificial intelligence',
        'explainable artificial intelligence'
        'logic programming',
        'answer set programming',
    ],
    include_package_data=True,
    python_requires='>=3.6.0',
    install_requires=[
        'importlib_resources',
        'setuptools-git',
        'numpy',
        'sklearn',
        'dafact',
        'xclingo',
    ],
    packages=[
        'crystal_tree',
        'crystal_tree.logic_tree',
        'crystal_tree.logic_tree.defaults_lp',
    ]
)
