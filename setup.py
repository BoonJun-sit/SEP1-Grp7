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
            "smartphone = test_py_pkg.smartphone:main",
            "number_publisher = test_py_pkg.number_publisher:main",
            "number_counter = test_py_pkg.number_counter:main",
            "add_two_ints_server = test_py_pkg.add_two_ints_server:main",
            "add_two_ints_client_no_oop = test_py_pkg.add_two_ints_client_no_oop:main",
            "add_two_ints_client = test_py_pkg.add_two_ints_client:main",
            "hw_status_publisher = test_py_pkg.hardware_status_publisher:main",
            "led_panel = test_py_pkg.led_panel:main",
            "battery = test_py_pkg.battery:main"
            
        ],
    },
)
