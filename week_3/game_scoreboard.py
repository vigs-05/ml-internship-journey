class GameScoreboard:
    
    _instance = None
    
    def __new__(cls):
        
        if cls._instance is None :
            cls._instance = super().__new__(cls)
        return cls._instance
    
s1 = GameScoreboard()
s2 = GameScoreboard()

print(id(s1))
print(id(s2))

print(s1 is s2)