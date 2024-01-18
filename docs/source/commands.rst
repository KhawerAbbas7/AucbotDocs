Commands
========

.. _Prefix:

Prefix
-------

The default prefix for Aucbot is ``auc!`` and it will be the permanent prefix along with whatever you set as a prefix. To set or change a prefix you can run the ``prefix`` command. 

.. code-block:: console

   auc!prefix .

**Arguments**

#. Prefix: char

**Aliases**
None

**Permissions needed**

#. Administrator 


.. _setlogchannel:

setlogchannel
--------------

A logging channel is a channel where auction logs are sent, such as who bought what and what was unsold. This is an essential step to start the auction. To set or change a logging channel, you can use the ``setlogchannel`` command, here's an example:

.. code-block:: console

   auc!setlogchannel #logs

**Arguments**

#. channel: channel id| channel mention| channel name

**Aliases**

#. slc

**Permissions needed**

#. Administrator

.. _setpurse:

setpurse
-------

It's a command used for setting a member's purse, You can set purse of multiple players using this command by giving it a role id or role mention.
Example of setting a member's purse:

.. code-block:: console

   auc!setpurse @zuhairasif 50m

Example of setting a Role's purse:

.. code-block:: console

   auc!setpurse @players 50m
