Sphinx documentation
====================

Documentation template using the Sphinx documentation generator.

* https://www.sphinx-doc.org/

Build the documentation
-----------------------

.. code:: bash

    cd docs/
    pip install -r requirements.txt
    ./gen_documentation.sh html
    firefox build/html/index.html
