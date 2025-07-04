from setuptools import setup, find_packages

setup(
    name='pentago',
    version='0.1.3',
    packages=find_packages(),
    python_requires='>=3.6',
    author='Klypse',
    description='Unofficial Papago API using reverse-engineered web endpoints',
    long_description=open('README.md', encoding='utf-8').read() if __name__ == '__main__' else '',
    long_description_content_type='text/markdown',
    url='https://github.com/Klypse/PentaGo',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

