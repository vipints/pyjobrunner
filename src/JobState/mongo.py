from pymongo.connection import Connection


class MongoTable(object):
    """
    simple wrapper for mongo db table
    """
    
    
    def __init__(self, address, db_name, table_name, port=27017):
        """
        set up connection
        """

        self.address = address
        self.db_name = db_name
        self.table_name = table_name
        self.connection = Connection(address, port)
        self.database = self.connection[db_name] 
        self.table = self.database[table_name]    
        
        
    def save(self, item):
        """
        save item
        """
        
        self.table.save(item)
        
        
    def load_all(self, where_dict=None):
        """
        load all elements, where key=value
        """
        
        return self.table.find(where_dict)
        
        
    def load_one(self, where_dict={}):
        """
        loads item, where key=value according to where_dict 
        """
        
        return self.table.find_one(where_dict)


    def count(self, where_dict={}):
        """
        check if we have at least one entry with key
        """
    
        num_entries = self.table.find(where_dict).collection.count()
       
        return num_entries
    
    
    def load_distinct(self, key):
        """
        check if we have at least one entry with key
        """
    
        return self.table.find().collection.distinct(key)
        
    
    def remove(self, where_dict={}):
        """
        removes entries defined by where_dict
        """
    
        self.table.remove(where_dict)
        
            
