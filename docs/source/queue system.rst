Queue System 
============

Queue is a system that revolutionized the auctions on discord. This system will automatically bring new player after a player is sold. This system requires `Automatic Sold System <https://aucbotdocs.readthedocs.io/en/latest/commands.html#set-automatic-sold-time>` to be enabled as well. 

So let's start with how will we add players to queue.

.. _addtoq:

addtoq
------

This command is used to add players to the queue.

**Example of adding a single player to the queue**

.. code-block:: console

   auc!addtoq Babar Azam

**Example of adding multiple players to the queue**

.. code-block:: console

   auc!addtoq Babar Azam, Muhammad Nawaz, Virat Kohli

**Arguments**

* Player(s)- This can be a player or multiple players, multiple players can be separated by commas as shown up in the example.

**Aliases**: None

**Permissions needed**: Administrator

.. _pausequeue:

pausequeue
----------

This is a toggle command which means if queue system is paused, it will resume it and if the queue system is not paused, it will pause the system.

.. code-block:: console

   auc!pausequeue

**Arguments**: None


**Aliases**

* pq

**Permissions needed**: Administrator

.. _remove_from_queue:

remove_from_queue
-----------------

A very important command in queue system, let's say you have added a player mistakenly in the queue and you want to get him removed, how will you do it? answer is this command.

**Let's remove a player that's on index 4**
.. code-block:: console

   auc!remove_from_queue 4

**Now let's remove all the players from the queue**

.. code-block:: console

   auc!remove_from_queue all

**Arguments**:

* Index- The index of a player in queue, which can be obtained from queue_ command. Or "all" for all the players.

**Aliases**

* rfq

**Permissions needed**: Administrator

.. _queue:

queue
-----

Command to check the queue.

.. code-block:: console

   auc!queue

**Arguments**: None
**Aliases**: None
**Permissions needed**: None


.. _shufflequeue:

shufflequeue
------------

Let's say you want to randomize the players in queue, well this command just allows you to do that. It will randomize the order in queue.

.. code-block:: console

   auc!shufflequeue

**Arguments**: None
**Aliases**: None
**Permissions needed**: Administrator 
.. _shufflequeue:

shufflequeue
------------
