# Scenario
# Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
# the system was created by a group of volunteers who worked with no clear “clean coding” rules;
# the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;
# your task is to prepare a metaclass that is responsible for:
# equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
# equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.
# * The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).

# Your metaclass should be used to create a few distinct legacy classes;
# create objects based on the classes;
# list the class names that are instantiated by your metaclass.

######################################################################################################################


from time import time
class meta (type):
    timestamp = time()
    instClasses = []
    def __new__(msc,name,bases,dic):
        
        obj = super().__new__(msc,name,bases,dic)
        obj.__instantiation_time__ = time()-meta.timestamp
        def getinst(): return obj.__instantiation_time__
        obj.get_instantiation_time = getinst
        meta.instClasses.append(name)
        return obj
        
        
class class1 (metaclass = meta):
    pass
class class1_1 (metaclass = meta):
    pass
class class2_1 (metaclass = meta):
    pass
class class1_2 (metaclass = meta):
    pass
class class3_1 (metaclass = meta):
    pass
class class4_1 (metaclass = meta):
    pass
class class2_2 (metaclass = meta):
    pass

for i in meta.instClasses:
    print(i)