from gettext import install
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='investimentos-package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Aqui você pode adicionar dependências, se necessário
        # Exemplo: 'numpy', 'pandas'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    description='Descricao da sua lib investimentos',
    author='seu nome',
    author_email='seu.email@example.com',
    url='https://github.com/tadrianonet/investimentos',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
