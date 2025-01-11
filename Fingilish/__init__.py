class Fn:
    def __init__(self):
        self.data = {}
    
    def bn(self, content):
        print(content)
    
    def zk(self, key, value):
        self.data[key] = value
    
    def zb(self, key):
        return self.data[key]
    
    def ag(condition, action):
        if condition:
            if callable(action):
                return action()
            return action

    def rk(content):
        return str(content)
    
    def ak(content):
        return int(content)

    def bk(content):
        return bool(content)
    
    def sk(content):
        return float(content)

class Finglish:
    def __init__(self):
        self.data = {}
    
    def benevis(self, content):
        print(content)
    
    def zakhire_kon(self, key, value):
        self.data[key] = value
    
    def zakhire_bede(self, key):
        return self.data[key]
    
    def agar(condition, action):
        if condition:
            if callable(action):
                return action()
            return action
        
    def reshte_kon(content):
        return str(content)
    
    def adad_kon(content):
        return int(content)
    
    def boolean_kon(content):
        return bool(content)
    
    def shenavar_kon(content):
        return float(content)
