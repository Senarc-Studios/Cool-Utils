from setuptools import setup

requirements = []
README = ""
# Please don't change the indentation.
with open("requirements.txt") as f:# I gave you access!
	requirements = f.read().splitlines()

with open("README.rst") as f:
	README = f.read()

packages = [
	"cool_utils"
]

setup(
	name="cool-utils",
	author="Benitz Original",
	author_email="benitzcoding@yahoo.com",
	url="https://github.com/Senarc-Studios/Cool-Utils",
	project_urls={
		"Documentation": "https://cool-utils.senarc.org",
		"Issue tracker": "https://github.com/Senarc-Studios/Cool-Utils/issues",
		"Github": "https://github.com/Senarc-Studios/Cool-Utils/tree/Development"
	},
	version="1.2.0.1",
	packages=packages,
	license="BSD",
	description="This is Cool Utility tools that you can use in python.",
	long_description=README,
	long_description_content_type="text/x-rst",
	include_package_data=True,
	install_requires=requirements,
	python_requires=">=3.7.0",
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: BSD License",
		"Intended Audience :: Developers",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Topic :: Internet",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Utilities",
	]
)