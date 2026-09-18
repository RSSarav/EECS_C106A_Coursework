from pathlib import Path
import xml.etree.ElementTree as ET

from setuptools import find_packages, setup

package_name = 'my_chatter'
metadata = ET.parse(Path(__file__).parent / 'package.xml').getroot()
maintainer = metadata.find('maintainer')

setup(
    name=package_name,
    version=metadata.findtext('version'),
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer=maintainer.text,
    maintainer_email=maintainer.attrib['email'],
    description=metadata.findtext('description'),
    license=metadata.findtext('license'),
    entry_points={
        'console_scripts': [
            'my_talker = my_chatter.Publisher:main',
            'my_listener = my_chatter.Subscriber:main',
        ],
    },
)
