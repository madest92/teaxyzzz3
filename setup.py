from setuptools import setup

setup(
    author='Alex-teaxyzzz3',
    author_email='teaxyzzz3@mail.com',
    name='teaxyzzz3',
    version='1.0.33',
    description='A simple package for https://app.tea.xyz/. Example teaxyzzz3',
    url='https://github.com/madest92/teaxyzzz3',
    project_urls={
        'Homepage': 'https://github.com/madest92/teaxyzzz3',
        'Source': 'https://github.com/madest92/teaxyzzz3',
        },
    py_modules=['hello_teaxyzzz3'],
    entry_points={
        'console_scripts': [
            'hello-tea=hello_tea:hello_tea_func'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.20.0',
        'tea-xyz1',
        'tea-xyz2',
    ],
)
