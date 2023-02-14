from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
d = generate_distutils_setup(
    packages=['simple_program'],
    package_dir={'': 'src'},
    requires=['rospy']
)

setup(**d)
