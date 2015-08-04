#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    virtualchain
    ~~~~~
    :copyright: (c) 2015 by Openname.org
    :license: MIT, see LICENSE for more details.
"""

# example plugin to a virtual chain that defines its behavior.

def get_virtual_chain_name():
   """
   Get the name of the virtual chain we're building.
   """
   print "\nreference implementation of get_virtual_chain_name\n"
   return "virtualchain-test"


def get_virtual_chain_version():
   """
   Get the version string for this virtual chain.
   """
   print "\nreference implementation of get_virtual_chain_version\n"
   return "v0.01-beta"


def get_first_block_id():
   """
   Get the id of the first block to start indexing.
   """ 
   print "\nreference implementation of get_first_block_id\n"
   return 50000


def get_db_state():
   """
   Return an opaque 'state' object that will be preserved across calls
   to the blockchain indexing callbacks.
   """
   print "\nreference implementation of get_db_state\n"
   return None 


def get_opcodes():
   """
   Return the set of opcodes we're looking for.
   """
   print "\nreference implementation of get_opcodes\n"
   return ["a", "b", "c", "d", "e"]


def get_magic_bytes():
   """
   Return the magic byte sequence we're scanning OP_RETURNs for.
   """
   print "\nreference implementation of get_magic_bytes\n"
   return "vv"

def get_op_processing_order():
   """
   Return a sequence of opcodes as a hint to the order in which 
   the indexer should process opcodes.
   """
   print "\nreference implementation of get_op_processing_order\n"
   return None 


def db_parse( block_id, opcode, op_payload, senders, outputs, fee, db_state=None ):
   """
   Given the block ID, and information from what looks like 
   an OP_RETURN transaction that is part of the virtual chain, parse the 
   transaction's OP_RETURN nulldata into a dict.
   
   Return the dict if this is a valid op.
   Return None if not.
   
   NOTE: the virtual chain indexer reserves all keys that start with 'virtualchain_'
   """
   print "\nreference implementation of db_parse\n"
   return None


def db_check( block_id, checked_ops, opcode, op, db_state=None ):
   """
   Given the block ID and a parsed operation, check to see if this is a *valid* operation
   for the purposes of this virtual chain's database.
   
   checked_ops is a dict that maps opcodes to operations already checked by
   this method for this block.
   
   Return True if so; False if not.
   """
   print "\nreference implementation of db_check\n"
   return False
   
   
def db_commit( block_id, opcode, op, db_state=None ):
   """
   Given a block ID and checked opcode, record it as 
   part of the database.  This does *not* need to write 
   the data to persistent storage, since save() will be 
   called once per block processed.
   """
   print "\nreference implementation of db_commit\n"
   return False


def db_save( block_id, filename, db_state=None ):
   """
   Save all persistent state to stable storage.
   
   Return True on success
   Return False on failure.
   """
   print "\nreference implementation of db_save\n"
   return True


def db_iterable( block_id, db_state=None ):
   """
   Return an iterable object that represents 
   a stable ordering of all serialized records in the database.
   That is, each entity yielded by the returned iterable must be 
   a string that represents a record, and the strings yielded 
   back by the iterable must be subject to a stable total ordering.
   For example, sorting the serialized set of records and returning 
   an array of them would work, provided that the set of records 
   is small enough to fit into RAM.
   
   This is used to generate the data that will be fed into 
   the consensus hash for the current block.
   """
   print "\nreference implementation of db_iterable\n"
   return []
