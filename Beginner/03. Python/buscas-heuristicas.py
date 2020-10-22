#'Importa pacote Numpy e renomeia com NP'
import numpy as np
#'Importa módulo base.funcoes e renomeia para FN'
import base.funcoes as fn

from base.grafo import Aresta

#'De Pillow importar Image, ImageDraw'
from PIL import Image, ImageDraw
#'De queue=fila importar Queue, LifoQueue'
from queue import Queue, LifoQueue, PriorityQueue
from base.queues import ReversePriorityQueue
#'De base.funcoes importar addQueue'
from base.funcoes import addQueue

#'Criando classe chamada Buscas(parâmetro{object}):'


class Buscas(object):
    #'Definindo função de inicialização para a classe buscas=self'
    def __init__(self):
        #'buscas=self aponta para visitado que é um array vazio'
        self.visitado = []
        #'self aponta para marcado que é um array vazio'
        self.marcado = []
        #'self aponta para resultado que é um arrayvazio'
        self.resultado = []

    def drawPoint(self, data, aresta, color):
        if color == 'branco':
            data[aresta.line][aresta.column] = [255, 255, 255, 255]
        elif color == 'cinza':
            data[aresta.line][aresta.column] = [0, 0, 135, 255]
        else:
            data[aresta.line][aresta.column] = [255, 69, 0, 255]


class BuscaLargura(Buscas):
    # Variaveis que serão utilizadas durante a busca
    def __init__(self):
        super().__init__()
        self.cor = {}
        self.pred = {}
        self.d = {}
        # Nome da busca
        self.name = "Busca Largura"

    def search(self, data, estado_pai):
        for v in fn.list_state(estado_pai, []):             
            self.d[v] = np.inf
            self.cor[v] = 'branco'  # branco cinza e preto
            # Marca os estados como none, para saber quais os estados que se deve passar novamente
            self.pred[v] = None
            self.drawPoint(data, v, self.cor[v])

        # Marca o estado pai como cinza
        self.cor[estado_pai] = 'cinza'
        self.d[estado_pai] = 0
        self.drawPoint(data, estado_pai, self.cor[estado_pai])

        Q = Queue()
        Q.put(estado_pai)

        # Verifica se tem algum estado pai na minha lista, caso tenha ele entra no while
        while not Q.empty():
            u = Q.get_nowait()

        # Caso o atual "u" que é minha lista de estados pai, contenha o estado pai objetivo, então sai do while
            if u.goal:
                break

        # para cada filho na lista de filhos do pai a ser analisado
            for v in u.children:
                # se sua cor for branca, eu troco ela pra cinza
                if self.cor[v] == 'branco':
                    self.cor[v] = 'cinza'
                    self.d[v] = self.d[u] + 1
                    self.pred[v] = u
                    self.drawPoint(data, v, self.cor[v])

                    self.visitado.append((u, v))

                    Q.put(v)
            self.cor[u] = 'preto'
            self.drawPoint(data, u, self.cor[u])

        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']

        # Salva uma imagem com os dados coletados nos passos anteriores e com os estados visitados pintados
        fn.save_image(data, "Resolucao-Largura.png")


class BuscaProfundidade(Buscas):
    # Variaveis que serão utilizadas durante a busca
    def __init__(self):
        super().__init__()
        self.cor = {}
        self.pred = {}
        self.d = {}
        # Nome da busca
        self.name = "Busca Profundidade"

    def search(self, data, estado_pai):
        for v in fn.list_state(estado_pai, []):             
            self.d[v] = np.inf
            self.cor[v] = 'branco'  # branco cinza e preto
            # Marca os estados como none, para saber quais os estados que se deve passar novamente
            self.pred[v] = None
            self.drawPoint(data, v, self.cor[v])

        # Marca o estado pai como cinza
        self.cor[estado_pai] = 'cinza'
        self.d[estado_pai] = 0
        self.drawPoint(data, estado_pai, self.cor[estado_pai])

        Q = LifoQueue()
        Q.put(estado_pai)

        # Verifica se tem algum estado pai na minha lista, caso tenha ele entra no while
        while not Q.empty():
            u = Q.get_nowait()

        # Caso o atual "u" que é minha lista de estados pai, contenha o estado pai objetivo, então sai do while
            if u.goal:
                break

        # para cada filho na lista de filhos do pai a ser analisado
            for v in u.children:
                # se sua cor for branca, eu troco ela pra cinza
                if self.cor[v] == 'branco':
                    self.cor[v] = 'cinza'
                    self.d[v] = self.d[u] + 1
                    self.pred[v] = u
                    self.drawPoint(data, v, self.cor[v])

                    self.visitado.append((u, v))

                    Q.put(v)
            self.cor[u] = 'preto'
            self.drawPoint(data, u, self.cor[u])

        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']

        # Salva uma imagem com os dados coletados nos passos anteriores e com os estados visitados pintados
        fn.save_image(data, "Resolucao-Largura.png")

# NÃO UTILIZADO.
# class BuscaProfundidade(Buscas):
#     # Variaveis que serão utilizadas durante a busca
#     def __init__(self):
#         super().__init__()
#         self.cor = {}
#         self.pred = {}
#         self.d = {}
#         self.f = {}
#         # Nome da busca
#         self.name = "Busca Profundidade"

#     def search(self, data, estado_pai):
#         # tempo inicial
#         tempo = 0

#         # Para cada estado possivel a partir do estado pai, ele armazena estes estados em uma lista e os coloca todos como cor branca
#         for v in fn.list_state(estado_pai, []):
#             # cores possíveis: branco, cinza e preto
#             self.cor[v] = 'branco'
#             self.pred[v] = None

#         for v in fn.list_state(estado_pai, []):
#             # para cada filho na lista, verifica-se se ele é branco
#             if self.cor[v] == 'branco':
#                 tempo = self.visit(estado_pai, v, tempo)

#         self.resultado = [key for key in self.cor if self.cor[key] == 'preto']



#     def visit(self, G, s, tempo):
#         tempo = tempo + 1
#         self.d[s] = tempo
#         self.cor[s] = 'cinza'

#         for v in G.children:
#             if self.cor[v] == 'branco':
#                 self.pred[v] = s
#                 self.visitado.append((s, v))
#                 tempo = self.visit(G, v, tempo)

#         self.cor[s] = 'preto'
#         self.tempo = tempo + 1
#         self.f[s] = tempo

#         return tempo


class BuscaCustoUniforme(Buscas):
    """
    Algoritmo Busca - Uniforme
    1. Definir um conjunto L de nós iniciais

    2. Ordene L em ordem crescente de custo

    3. Se L é vazio
        Então Busca não foi bem sucedida
        Senão seja n o primeiro nó de L;

    4. Se n é um nó objetivo
        Então
            Retornar caminho do nó inicial até N;
            Parar
        Senão
            Remover n de L;
            Adicionar em L todos os nós filhos de n, rotulando cada nó com o seu caminho até o nó inicial;
            Ordene L em ordem crescente de custo;
            Volte ao passo 3.
    """

    def __init__(self):
    # Variaveis que serão utilizadas durante a busca
        super().__init__()
        self.cor = {}
        # Nome da busca
        self.name = "Busca Custo Uniforme"

    def geraResultado(self):
        self.resultado = [key for key in self.cor if self.cor[key] == 'preto']


    def search(self, data, estado_pai):
        frontier = PriorityQueue()
        frontier.put((0, estado_pai))
        # se a fila dos estados pai não estiver vazia, entra no while
        while not frontier.empty():
            ucs_w, current_node = frontier.get()
            #Pega o estado atual da minha lista "frontier", ao andar pega o estaddo atual e o coloca na lista de estados visitados
            self.visitado.append(current_node)

            # Se o estado atual for o objetivo, finaliza a busca
            if current_node.goal:
                # print("Cheguei no final! ", current_node)
                return

            # para cada estado filho
            for node in current_node.children:
                custo = current_node.arestas[node].custo
                filho = current_node.arestas[node].g_fim

                if not filho in self.visitado:
                    self.resultado.append((current_node, filho))
                    frontier.put(
                        (custo, filho)
                    )

class BuscaGreedy(Buscas):
    """
    Algoritmo Busca - Uniforme
    1. Definir um conjunto L de nós iniciais

    2. Ordene L em ordem crescente de custo

    3. Se L é vazio
        Então Busca não foi bem sucedida
        Senão seja n o primeiro nó de L;

    4. Se n é um nó objetivo
        Então
            Retornar caminho do nó inicial até N;
            Parar
        Senão
            Remover n de L;
            Adicionar em L todos os nós filhos de n, rotulando cada nó com o seu caminho até o nó inicial;
            Ordene L em ordem crescente de custo;
            Volte ao passo 3.
    """

    def __init__(self):
        # Variaveis que serão utilizadas durante a busca
        super().__init__()
        self.cor = {}
        self.H = {}
        # Nome da busca
        self.name = "Busca Greedy (Gulosa)"

    def search(self, data, estado_pai):
        frontier = PriorityQueue()
        frontier.put((0, estado_pai))

        # Se a minha lista de estados pai não estiver vazia, entra no while
        while not frontier.empty():
            ucs_w, current_node = frontier.get_nowait()
            # O estado atual a ser analizado é adcionado na lista de visitados
            self.visitado.append(current_node)

            # Se o estado atual for o fim, finaliza o while
            if current_node.goal:
                # print("Cheguei no final! ", current_node)
                return
            
            # Para cada estado filho
            for node in current_node.children:
                # Adiciona seu custo com uma busca heuristica
                custo = current_node.arestas[node].custoH
                filho = current_node.arestas[node].g_fim
                if not filho in self.visitado:
                    self.resultado.append((current_node, filho))
                    frontier.put(
                        (custo, filho)
                    )


class BuscaAEstrela(Buscas):
    # Variaveis que serão utilizadas durante a busca
    def __init__(self):
        super().__init__()
        # Nome da busca
        self.name = "Busca A* (A Estrela)"
        self.came_from = {}
        self.cost_so_far = {}


    def search(self, data, estado_pai):
        frontier = PriorityQueue()
        frontier.put((0, estado_pai))
        
        self.cost_so_far[estado_pai] = 0

        # Se minha lista de pais não for vazia, entra no while
        while not frontier.empty():
            ucs_w, current = frontier.get_nowait()
            # adiciona o atual estado a ser analizado na lista de visitados
            self.visitado.append(current)
            
            # Se o estado atual for o estado final, sai do while
            if current.goal:
                # print("Cheguei no final! ", current_node)
                return

            # Para o proximo estado na lista de filhos
            for next in current.children:
                # Ele recebera um novo custo sendo este custo a soma da distancia ja andada para chegar até ele, 
                # Mais a heuristica dele mesmo até o final
                new_cost = ucs_w + current.arestas[next].custo
                filho = current.arestas[next].g_fim
                
                # se o custo do proximo filho a ser comparado não for maior que o do filho analizado anteriormente, 
                # ou o novo custo for menor que a distancia que ele ja percorreu ele entra no if
                if next not in self.cost_so_far or new_cost < ucs_w:
                    priority = new_cost + current.arestas[next].custoH
                    self.resultado.append((current, filho))
                    frontier.put((priority, filho))
