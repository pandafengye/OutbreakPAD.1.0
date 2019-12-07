#!/usr/bin/env python
# coding=utf-8

from setuptools import  find_packages,setup
setup(
    name="OutbreakPAD",  #pypi中的名称，pip或者easy_install安装时使用的名称
    version="1.0",
    author="Zou",
    author_email="21818662@zju.edu.cn",
    description=("This is a script of outbreak prediction"),
    license="GPLv3",
    keywords="Outbreak Prediction subscripe",
    url="https://github.com/FengYe-Lab/OutbreakPAD",
    packages=find_packages(),  # 需要打包的目录列表
    package_dir={ "OutbreakPAD": "OutbreakPAD" },
    package_data={"OutbreakPAD": ["exampledata/*.csv"]},
    test_suite="tests",

    # 需要安装的依赖
    install_requires=[
        'numpy>=1.7.0',
        'scipy',
        'pandas',
     #   'json',
        'statsmodels',
        'tensorflow',
        'neupy',
 #       'sklearn',
        'scikit-learn>=0.16.1',
        'matplotlib>=1.3.0'
    ],
    classifiers=[
    'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX :: Linux',
      'Operating System :: MacOS',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Topic :: Software Development :: Libraries :: Python Modules'],
    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
 #   entry_points={'console_scripts': [
 #       'redis_run = DrQueue.RedisRun.redis_run:main',
 #   ]},
    zip_safe=False
)
