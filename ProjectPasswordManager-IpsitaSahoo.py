#!/usr/bin/env python
# coding: utf-8

# # Kalia Sante

# ## Submitted by : Ipsita Sahoo

# ## Password Manager

# DESCRIPTION
# 
# Zara is developing a new version of password manager. Earlier, she was using some third-party password manager but she figured out that it can't keep track of all the passwords which have been set for the respective account. As she is very concerned about the security, she decided to develop her own version of the password manager
# 
# 
# Objective: To develop a custom password manager using Python
# 
# Domain:  Security
# Steps to perform:
# 
# 1.	Implement the following design
# 
# class BasePasswordManager
#     
# members
#         
#     old_passwords: is a list that holds all of the user's past passwords.The last item of the list is the user's current password.
#     
# methods
#         
#     get_password method that returns the current password as a string.
#  
#         
#         is_correct method that receives a string and returns a boolean
#              True or False depending on whether the string is equal to
#              the current password or not.
#  
# 
# class PasswordManager
#     
# This class inherits from BasePasswordManager
#  
#         
#     methods
#         
#         set_password method that sets the user's password.
#              
#         Password change is successful only if: 
#                     
#              - Security level of the new password is greater.
#                     
#              - Length of new password is minimum 6
#  
#              
#                     However, if the old password already has the highest security level,
#                       a new password must be of the highest security level for a successful password change.
#  
#         
#         get_level method that returns the security level of the current password.
#              
#             It can also check and return the security level of a new password passed as a string.
# 
#                  Security levels:
# 
#                   level 0 - password consists of alphabets or numbers only.
# 
#                   level 1 - Alphanumeric passwords.
# 
#                   level 2 - Alphanumeric passwords with special characters.
# 

# In[1]:


class BasePasswordManager:
    old_passwords = []
    old_passwords = ['jagannatha']
    
    def __init__(self):
        pass
    
    def get_password(self):
        try:
            return self.old_passwords[-1]
        except IndexError as e:
            print('No passwords are set, please register your first password')
            print('Error found as: '+repr(e))
            return -1
        
    def is_correct(self,entered_password):
            return entered_password == self.get_password()
#         print('You must create a password first then match')
        


# In[2]:


import regex as re
import string
special = string.punctuation


# In[3]:


class PasswordManager(BasePasswordManager):
    
    security_level =[0,1,2]
    
    def __init__(self):
        pass
    
    def set_password(self,new_password_option):
        if len(new_password_option) >= 6:
            if (not len(self.old_passwords)):
                self.old_passwords.append(new_password_option)
                print('\npassword set successfully')
            elif (self.get_level() == self.security_level[-1]):
                if (self.get_level(new_password_option) == self.security_level[-1]):
                    self.old_passwords.append(new_password_option)
                    print('\npassword set successfully')
                else:
                    print('''\nNote:
                    As the older password has the highest security level 
                    the password you want to set also needs to be of the highest level''')
            elif (self.get_level() < self.get_level(new_password_option)):
                self.old_passwords.append(new_password_option)
                print('password set successfully')
            else:
                print('''\nNote:
                As the pssword you re suggesting does not have 
                higher security level than the previous password
                the password cannot be updated! The newer password must be 
                of greater security level than older. If the older password
                is at highest security the new one must also be of highest
                security level''')
        else:
            print('\nNote:The password should be of atleast 6 characters')
        
       
    def get_level(self,str = ''):  # I want to make a call here
        
        if str == '':
            str = self.get_password()
            
        if re.search(' ',str):
            print('Password can only contain Alphabets, Numeric Digits and Special Characters.')
            return -1;
        
        flag = True             # flag for all special
        flag1 = False;          # flag for atleast 1 special but not all special
        flaga = False           # flag for all alphabets
        flagn = False;          # flag for all numeric
        
        for i in str:
            if i not in special:
                flag = False
                break;
                
        if not flag:
            for i in str:
                if i in special:
                    flag1 = True
                    break;
                    
        if (len(re.findall('[a-zA-Z]',str))):
            flaga = True
            
        if (len(re.findall('[0-9]',str))):
            flagn = True
            
        if str.isdecimal() or str.isalpha() or flag:
            print('level is 0')
            return 0
        elif(flag1 and flaga and flagn):
            print('level is 2 highest')
            return 2
        elif (str.isalnum()) or (flaga and flag1) or (flagn and flag1):
            print('level is 1')
            return 1
        else:
            print('Something is worng with your password suggestion level is -1')
            return -1


# In[4]:


'jagannatha8'.isdecimal(),'jagannatha8'.isalpha(),'jagannatha8'.isalnum()


# #### implementation of get_level  (Self Note)
# def get_level(self,str = (super().get_password())):
# RuntimeError: super(): no arguments
# 
# def get_level(self,str = self.get_password()):
# NameError: name 'self' is not defined
# 

# In[5]:


pw = PasswordManager()


# In[6]:


pw.old_passwords


# In[7]:


pw.get_password()


# In[8]:


pw.is_correct('kalia')


# In[9]:


pw.set_password('kalia')


# In[10]:


pw.set_password('jagannatha')


# In[11]:


pw.set_password('9090707061')


# In[12]:


pw.get_password()


# In[13]:


pw.is_correct('kalia')


# In[14]:


pw.is_correct('jagannatha')


# In[15]:


pw.set_password('mahaprabhu')


# In[16]:


pw.set_password('jagannath@')


# In[17]:


pw.set_password('jagannatha8')


# In[18]:


pw.set_password('jagannath@8')


# In[19]:


pw.set_password('      ')


# In[20]:


pw.set_password('@8___________')


# In[21]:


pw.set_password('jagannath@')


# In[22]:


pw.is_correct('jagannath@8')


# In[ ]:




