import hashlib
import getpass

from models.founder import *
from models.mentor import *
from models.investor import *



def login_user(username, user_password, connection):
    """
        Login a user by username and password.
        Returns the appropriate User object (Founder/Mentor/Investor) or None
        """
    cursor = connection.cursor(dictionary=True) #to return a dictionary

    #hashing the password because that is how it is stored in the database
    user_password = hashlib.sha256(user_password.encode()).hexdigest() 
    cursor.execute('''
            SELECT * FROM users 
            WHERE username = %s AND password = %s
        ''', (username, user_password))
        
    user_data = cursor.fetchone()
    cursor.close()
        
    if not user_data:
        return None
        
    # Create appropriate user object based on role
    role = user_data['role']
    user_id = user_data['user_id']
        
    if role == 'Founder':
        from models.founder import Founder
        return Founder.get_from_db(user_id, connection)
    
    elif role == 'Mentor':
        from models.mentor import Mentor
        return Mentor.get_from_db(user_id, connection)
    
    elif role == 'Investor':
        from models.investor import Investor
        return Investor.get_from_db(user_id, connection)
    
    connection.close()   
    return None


