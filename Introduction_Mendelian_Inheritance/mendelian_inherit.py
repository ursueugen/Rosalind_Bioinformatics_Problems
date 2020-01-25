"""
.
"""

k = 18
m = 30
n = 24


class ProbabilityTree(object):

    def __init__(self, k, m, n):
        self.pop_size = float(k+m+n)
        self.AA = k
        self.Aa = m
        self.aa = n
        self.p_AA = k/self.pop_size
        self.p_Aa = m/self.pop_size
        self.p_aa = n/self.pop_size

        self.genotypes = ['AA', 'Aa', 'aa']
        self.genotypes_pop_prob = {"AA": self.p_AA, 
                                  "Aa": self.p_Aa,
                                  "aa": self.p_aa}
        self.genotypes_counts = {"AA": k, 
                                 "Aa": m,
                                 "aa": n}


    def probs(self, g1, g2, g3):
        """ Return prob of offspring having at least one dominant allele."""
        
        if g1 == "AA" or g2 == "AA":
            if g3 == 'AA':
                return 1.0
            else:
                return 0

        elif g1 == "aa" and g2 == "aa":
            if g3 == 'AA' or g3 == 'Aa':
                return 0
            else:
                return 1.0

        elif (g1 == 'aa' and g2 == 'Aa') or (g1 == 'Aa' and g2 == 'aa'):
            if g3 == 'AA':
                return 0
            elif g3 == 'Aa':
                return 0.5
            elif g3 == 'aa':
                return 0.5
        
        elif (g1 == 'Aa' and g2 == 'Aa'):
            if g3 == 'AA':
                return 0.25
            elif g3 == 'Aa':
                return 0.5
            elif g3 == 'aa':
                return 0.25
        else:
            raise EnvironmentError 


    def compute_probability(self):
        '''Computes probability by traversing the probability tree.'''
        pr = 0
        for g1 in self.genotypes:
            
            p1 = self.genotypes_pop_prob[g1]
            
            for g2 in self.genotypes:
                
                if g2 == g1:
                    p2 = (self.genotypes_counts[g1] - 1.0)/(self.pop_size - 1)  # reestimate prob
                else:
                    p2 = self.genotypes_counts[g2] / (self.pop_size - 1)

                for g3 in self.genotypes:

                    p = self.probs(g1, g2, g3)
                    
                    if g3 in ['AA', 'Aa']:
                        pr += p1*p2*p
        
        return pr

tr = ProbabilityTree(k, m, n)
p = tr.compute_probability()

print(p)