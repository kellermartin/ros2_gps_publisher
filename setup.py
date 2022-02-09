from setuptools import setup

package_name = 'gps_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Martin Keller',
    maintainer_email='martinkellers@outlook.com',
    description='GPS publisher node using NavSatFix sensor msg format',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_publisher = gps_publisher.gps_publisher:main'
        ],
    },
)
