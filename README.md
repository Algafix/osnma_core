

osnma_core
========

Working in an oficial implementation and complete refactor of the receiver that will be published in July. Until then, don't expect any update.
========

osnma_core is a helpfull package that will provide a bunch of methods and atributes to
implement an OSNMA Galileo receiver.

To instanciate an OSNMACore object and start performing OSNMA functions:

    import osnma_core
    
    osnma = osnma_core.OSNMACore()
    osnma.process_pkr(raw_data)

Features
--------

- Can process and verify complete OSNMA messages
- The verification of different messages also can be done manually
- Stores the value and size of OSNMA fields
- Contains auxiliar data for the OSNMA receiver such as the structure of messages, bitmasks and field meanings.

Installation
------------

Install osnma_core by running:

    python3 pip install osnma_core

Contribute
----------
- Documentation: https://osnma-core.readthedocs.io
- Source Code: https://github.com/Algafix/osnma_core
- PyPI: https://pypi.org/project/osnma-core/

Support
-------

If you are having issues, please let me know.

License
-------

The project is licensed under the GPLv3 license.
