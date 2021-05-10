import random

# util para calcular o ponto medio, dividir o comprimento do vetor sobre o cumprimento
def scalar_multiply(escalar, vetor):
    return[escalar * i for i in vetor]

#lista = [1,2,3]
#escalar = 2

#for item in scalar_multiply(escalar, lista):
#    print(item)

def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result



def vector_mean(vetores):
    return scalar_multiply(1/ len(vetores), vector_sum(vetores))


def dot(v,w):
    return  sum([v_1 * w_i for v_1,w_i  in  zip(v,w)])


def sum_of_squares(v):
    return dot(v,v)

def vector_subtract(v,w):
    return [v_i - w_i  for v_i,w_i in zip(v,w)  ]


def square_distance(v,w):
    return sum_of_squares (vector_subtract(v,w))



class KMeans:
    def __init__(self, k, means = None):
        self.k = k   # número de argupamento
        self.means = means # ponto médio de agrupamentos
        self.pontos = [] # pontos 
    def classify(self, ponto):
        return min(range(self.k ), key= lambda i : square_distance(ponto,self.means[i]))


    def train(self, pontos):
       #escolha pontos l aleatorios como media inicial
       self.means = random.sample(pontos,self.k)
       assignments = None
       while True:

           #encontre associações
           new_assignments = list(map(self.classify,pontos))

           #se nenhuma associaao mudou, terminamos
           if assignments == new_assignments:
               return

           # se nao mantenha as associações
           assignments = new_assignments

           # e compute as novas medias, baseados nas n ovas associações

           for i in range(self.k):
    
               # encontre todos os pontos associados ao agrupamento
               i_points = [p for p, a in zip(pontos,assignments) if a == i]
               # adicione os pontos para cada protótipo / centroide
               self.pontos.append(i_points)
               # certifique que  i_points nao está vazio para nao dividir por 0
               if i_points:
                   self.means[i] = vector_mean(i_points)

    def __str__(self): 
        [print(f'Centroide {self.means[i]} : {self.pontos[i]}')    for i in range(self.k)]

def test_kmeans():
    dados = [[1] ,[2] , [3] , [6] , [10] ,[11] ]
    kmeans = KMeans(3,[[1],[3],[11]])
    kmeans.train(dados)
    print(kmeans.means)
    kmeans.__str__()

test_kmeans()





