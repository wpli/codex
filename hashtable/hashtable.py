class HashTable():
    def __init__( self, memory=1000, hash_type = "naive", collision_handling = "linear" ):
        self.array = [None]*memory
        self.hash_type = hash_type
        self.collision_handling = collision_handling

    def hash( self, key ):
        if self.hash_type == "naive":
            pos = self.naive_hash( key )

        # add other hashing methods here
        else:
            print "%s not found as a hash type" 
            pos = self.naive_hash( key )

        return pos

    def naive_hash( self, key ):
        pos = key % len( self.array )
        if self.array[ pos ] == None:
            return pos
        else:
            # collision handling
            if self.collision_handling == 'linear':
                
                while ( self.array[pos] != None ):
                    if self.array[pos][0] == key:
                        break

                    pos += 1
                    if pos == len( self.array ):
                        pos = 0


        return pos

    def add_key( self, key, value ):
        pos = self.hash( key )
        self.array[ pos ] = ( key, value )

        
    def lookup( self, key ):
        pos = self.hash( key )

        if self.array[ pos ] == None:
            print "%s not in hash table!" % key 
            return None
        else:
            if self.array[ pos ][0] == key:
                return key, self.array[ pos ][1]
            else:
                raise Error("there is a bug.")
                

if __name__ == '__main__':
    memory = 10
    hashTable = HashTable( memory )
    hashTable.add_key( 293, 294 )
    hashTable.add_key( 342, 343 )
    hashTable.add_key( 524, 525 )
    print hashTable.lookup( 342 )
    print hashTable.lookup( 293 )
    print hashTable.lookup( 5342 )
    print hashTable.lookup( 524 )
    hashTable.lookup( 537 )
    hashTable.add_key( 537, 5234 )
    print hashTable.lookup( 537 )

    print hashTable.array
    

