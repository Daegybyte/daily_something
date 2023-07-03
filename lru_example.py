class LRU_Example:
    from functools import lru_cache
    
    def non_caching_increment(num):
        print("Doing some resource intensive code")
        return num + 1
    
    @lru_cache
    def caching_increment(num):
        print("Doing some resource intensive code")
        return num + 1

if __name__ == "__main__":
    print(LRU_Example.non_caching_increment(1))
    print(LRU_Example.non_caching_increment(2))
    print(LRU_Example.non_caching_increment(3))
    print(LRU_Example.non_caching_increment(1))
    """
    Doing some resource intensive code
    2
    Doing some resource intensive code
    3
    Doing some resource intensive code
    4
    Doing some resource intensive code
    2
    
    2 is recomputed
    """ 
    
    print(LRU_Example.caching_increment(1))
    print(LRU_Example.caching_increment(2))
    print(LRU_Example.caching_increment(3))
    print(LRU_Example.caching_increment(1))
    """
    Doing some resource intensive code
    2
    Doing some resource intensive code
    3
    Doing some resource intensive code
    4
    2
    
    By utilising LRU (Least Recently Used) Caching, the last function call recognises
    that the argument (1) has been passed before and does not have to recompute the output.
    """
