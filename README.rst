Cool Utils
==========


`Documentation <https://github.com/Senarc-Studios/Cool-Utils/wiki/Documentation>`_

This is Cool Utility tools that you can use in python. There are a few
tools that you might find very useful, you can use this on pretty much
any project and some utils might help you a lot and save so much time
since it’s a simple function. We hope you like our utils. Have a nice
day!

Badges
------

|Discord| |PyPi| |Python Version| |License| |Issues| |Forks| |Stars|

Installation
------------

   **PyPi Installation**

**Windows:**

.. code:: sh

   $ pip install -U cool-utils

**Linux/MacOS:**

.. code:: sh

   $ python3 -m pip install -U cool-utils

..

   **Development Installation**

**Windows:**

.. code:: sh

   $ pip install git+https://github.com/Senarc-Studios/Cool-Utils

**Linux/MacOS:**

.. code:: sh

   $ python3 -m pip install -U git+https://github.com/Senarc-Studios/Cool-Utils

Examples
--------

**Compile:**

.. code:: python

   from cool_utils import Compile

   strings = ["This", "Is", "A", "String"]
   num_list = [9, 4, 2]
   print(Compile.string(strings, startwith="Hey, ", endwith=".", joints=" "))
   print(Compile.numbers(num_list, startwith=6, endwith=0))
   >> Hey, This Is A String.
   >> 69420

**JSON:**

.. code:: python

   import cool_utils

   cool_utils.JSON.open("sample")
   cool_utils.JSON.register_value(variable="foo", value="bar") # This creates a JSON file.
   data = utils.JSON.get_data(variable="foo")
   invalid_data = utils.JSON.get_data("non-existant value") # You can do this instead of doing the variable's name.
   print(data)
   print(invalid_data)
   >> bar
   >> None

Collaborators
-------------

This wouldn’t be made possible without these people

1. `BenitzCoding <https://github.com/BenitzCoding>`__
2. `JDJG Inc. Official <https://github.com/JDJGInc>`__
3. `P3ter <https://github.com/darkp3ter>`__

.. |Discord| image:: https://discord.com/api/guilds/886543799843688498/embed.png
   :target: https://discord.gg/5YY3W83YWg
.. |PyPi| image:: https://img.shields.io/pypi/v/cool-utils.svg
   :target: https://pypi.python.org/pypi/cool-utils
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/cool-utils.svg
   :target: https://pypi.python.org/pypi/cool-utils
.. |License| image:: https://img.shields.io/github/license/Senarc-Studios/Cool-Utils?style=plastic
   :target: https://github.com/Senarc-Studios/Cool-Utils/blob/master/LICENSE
.. |Issues| image:: https://img.shields.io/github/issues/Senarc-Studios/Cool-Utils?style=plastic
   :target: https://github.com/Senarc-Studios/Cool-Utils/issues
.. |Forks| image:: https://img.shields.io/github/forks/Senarc-Studios/Cool-Utils?style=plastic
   :target: https://github.com/Senarc-Studios/Cool-Utils/network
.. |Stars| image:: https://img.shields.io/github/stars/Senarc-Studios/Cool-Utils?style=plastic
   :target: https://github.com/Senarc-Studios/Cool-Utils/stargazers
