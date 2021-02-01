import unittest
import hiddenpower.commands.caesar

# TODO test argument parsing

# TODO test encrypt rotation uppercase -> k=13
#   "ZEKROM, USE BOLT STRIKE!"
#   "MRXEBZ, HFR OBYG FGEVXR!" 

# TODO test encrypt rotation lowercase -> k=13
#   "zekrom, use bolt strike!"
#   "mrxebz, hfr obyg fgevxr!"

# TODO test decrypt rotation uppercase -> k=13
#   "MRXEBZ, HFR OBYG FGEVXR!"
#   "ZEKROM, USE BOLT STRIKE!" 

# TODO test decrypt rotation lowercase -> k=13
#   "mrxebz, hfr obyg fgevxr!"
#   "zekrom, use bolt strike!"

# TODO test encrypt/decrypt special chars like é, à, õ, ã, ç, etc... -> k=13
#   "Pegá-los eu tentarei! Vai ser grande a emoção! Pokémon!"
#   "Crtá-ybf rh gragnerv! Inv fre tenaqr n rzbçãb! Cbxézba!"

# TODO test key > 25

# TODO test key < 0