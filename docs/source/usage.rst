Setup
=====

.. _Setting up the bot:

Setting up prefix
------------------

The default prefix for Aucbot is ``auc!``. If you want to change it, you can do that by:

.. code-block:: console

   auc!prefix .
.. NOTE:: In the case above new prefix will be ``.`` You can change it to anything.

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

