from setuptools import setup, find_packages

setup(
    name='official-doc',
    version='1.0.0',
    description='公文格式转换 - 将 Markdown 转为党政机关公文格式',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/official-doc',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-docx>=1.1.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Government',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'official-doc=src.md2docx:main',
        ],
    },
)