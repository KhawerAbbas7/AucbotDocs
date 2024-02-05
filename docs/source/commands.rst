Commands
========

.. _Prefix:

Prefix
-------

The default prefix for Aucbot is ``auc!`` and it will be the permanent prefix along with whatever you set as a prefix. To set or change a prefix you can run the ``prefix`` command. 

.. code-block:: console

   auc!prefix .

**Arguments**

* Prefix (char)

**Aliases**
None

**Permissions needed**

* Administrator 


.. _setlogchannel:

setlogchannel
--------------

A logging channel is a channel where auction logs are sent, such as who bought what and what was unsold. This is an essential step to start the auction. To set or change a logging channel, you can use the ``setlogchannel`` command, here's an example:

.. code-block:: console

   auc!setlogchannel #logs

**Arguments**

* channel- channel id| channel mention| channel name

**Aliases**

* slc

**Permissions needed**

* Administrator

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

.. NOTE:: It is not recommended to assign a purse to a role that has more than 20 members.



**Arguments**

* Member or Role.
* Purse 

.. NOTE:: Purse can be done in millions, billions, trillions and thousands by shortcuts. For example, for 20 millions we will write ``20M`` and for 20 thousands we will write ``20K``. B for billions, T for trillions. There's no system for crores as of now.

**Aliases**

#. sp

**Permissions needed**

#. Administrator 


.. _sell:

sell
----

Sell is a command to initiate an Auction, to sell a player/member/item you need to use this command. This command can be used by slash and text however it's better to use this with slash command.

Example of using it with text command:

.. code-block:: console

   auc!sell @zuhairasif 1m 1m

Example of using it with sell command:

.. code-block:: console

   /sell playerbeingsold: Zuhair Asif baseprice:1m increment:1m

**Arguments**

- playerbeingsold (string)-Player or Item that want to be sold.

.. NOTE:: While using text command this can't have space in between for example ``auc!sell Khawer Abbas 1m 1m`` will throw an error that's why it's better to use slash command.

* Baseprice- The first price from which the auction will get started.

.. NOTE:: Baseprice can be done in millions, billions, trillions and thousands by shortcuts. For example, for 20 millions we will write ``20M`` and for 20 thousands we will write ``20K``. B for billions, T for trillions. There's no system for crores as of now.

* Increment- It's the amount that will get added to the previous bid, for example if bid number 1 is 50 and increment is 5 now on next bid, bid amount will be ``50+5=55``

* Message (string(optional))-It's a fun thing if you want to give a message to the bidders then you can use this argument.

**Aliases**

None

**Permissions needed**

* Administrator 

.. _bid:

bid
---

Bid is a command through which you can bid on an item/player.

.. NOTE:: You cannot bid manually i.e ``auc!bid 3m`` It will go with the increment.

**Example:**


.. code-block:: console

   auc!bid


**Arguments**
None

**Aliases**
None

**Permissions needed**
None

.. _leaderboard:

leaderboard
------------

The leaderboard command displays the current purses and the number of players each member has.

**Example:**


.. code-block:: console

   auc!leaderboard

**Arguments**

#. Order: You can use ``roster`` as an argument to view the leaderboard sorted by roster size.

**Example to view the leaderboard ordered by roster size:**


.. code-block:: console

   auc!leaderboard roster

**Aliases**
* lb

**Permissions needed**
None

.. _setdifference:

setdifference 
--------------

To change the increment you can use this command. Increment was explained here sell_

**Example:**


.. code-block:: console

   auc!setdifference 1M

.. NOTE:: Increment can be done in millions, billions, trillions and thousands by shortcuts. For example, for 20 millions we will write ``20M`` and for 20 thousands we will write ``20K``. B for billions, T for trillions. There's no system for crores as of now.

**Arguments**

* Increment

**Aliases**

* sd

**Permissions needed**

* Administrator


.. _balance:

balance
-------

To check the amount you currently have or anyone else's amount you can use ``balance`` command.

**Example of using it to check your own balance:**


.. code-block:: console

   auc!balance

**Example of using it to check anyone else's balance:**


.. code-block:: console

   auc!balance @zuhairasif

**Arguments**

* User(discord Member(optional))- To check anyone else's balance.

**Aliases**

* bal
* b
* purse
* wallet

**Permissions needed** : None

.. _squad:

squad
------

You can use the ``Squad`` command to check out the players you've bought or those of others.

**Example of using it to check your own squad:**


.. code-block:: console

   auc!squad

**Example of using it to check anyone else's squad:**


.. code-block:: console

   auc!squad @zuhairasif

**Arguments**

* User(discord Member(optional))- To check anyone else's squad.

**Aliases**: None
**Permissions needed**: None

.. _delete:

delete
-------

The command ``Delete`` is used by admins to remove a player from a member's squad or clear all the players from a member's squad.

**Example of using it for deleting a player**

.. code-block:: console

   auc!delete @zuhairasif 1

**Example of using it for deleting all the players**

.. code-block:: console

   auc!delete @zuhairasif all

**Arguments**

* User(discord Member)- The member from whose squad we are going to remove the player/players

* Index- It can be: Index of a player which is basically a number of a player which can be seen through the squad_ command or it can ``all`` for removing all the players.

**Aliases**: None
**Permissions needed**: Administrator

.. _add_player:

add_player
----------

Quite opposite of delete_ command, through this command add **a** player to a member's squad or multiple players. This command can be used both via text command and slash.

**Example of using it for adding a single player.**

.. code-block:: console

   auc!add_player @zuhairasif Liam Livingstone

**Example of using it for adding Multiplayer players.**

.. code-block:: console

   auc!add_player @zuhairasif Liam Livingstone, Babar Azam, Virat Kohli

**Arguments**

* Member (Discord Member)- The member to whom we are going to add a player to his/her squad.

* Player(s)- This can be single and multiple, for multiple you have to separate players by ``,``.

**Aliases**:

* ap

**Permissions needed**: Administrator 

.. _swap:

swap
----

This is a command to swap the position of players you have bought in your squad. For example you have "Virat Kohli" at number 7 in your squad and you want to move him to number 1, you can this command.

.. code-block:: console

   auc!swap 7 1

**Arguments**

* Index1 (int)- The first index, index of a player can checked through squad_ command.
* Index2 (int)- The second index.

**Aliases**: None

**Permissions needed**: None
