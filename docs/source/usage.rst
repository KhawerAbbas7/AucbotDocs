Setup
=====

.. _Setting up the bot:

Setting up prefix
------------------

The default prefix for Aucbot is ``auc!``. If you want to change it, you can do that by:

.. code-block:: console

   auc!prefix .
.. NOTE:: In the case above new prefix will be ``.`` You can change it to anything.

Setting up the Logging Channel
------------------------------

A logging channel is a channel where auction logs are sent, such as who bought what and what was unsold. This is an essential step to start the auction. To set or change a logging channel, you can use the ``setlogchannel`` command, here's an example:

.. code-block:: console

   auc!setlogchannel #logs

.. NOTE:: The bot requires the send_message permission in both channels, the one from which the command is being run and the one where the log channel is being set.
