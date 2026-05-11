from setuptools import find_packages, setup

package_name = 'test_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bj',
    maintainer_email='bj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [

            "py_node = test_py_pkg.test:main",
            "robot_news_station = test_py_pkg.robot_news_station:main",
            "smartphone = test_py_pkg.smartphone:main"
            
        ],
    },
)
