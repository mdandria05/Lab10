from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

        self._dizionario_hub = {} #[id] = Hub()
        self._dizionario_spedizioni = {} #[{H_O,H_D}] = media

    def getAllHub(self):
        hubs = DAO.readHub()
        for hub in hubs:
            self._dizionario_hub[hub.id] = hub

    def getAllSpedizioni(self):
        spedizioni = DAO.readMySpedizione()
        for spedizione in spedizioni:
            chiave_corrente = frozenset({spedizione.id_hub_origine, spedizione.id_hub_destinazione})
            if chiave_corrente in self._dizionario_spedizioni.keys():
                self._dizionario_spedizioni[frozenset({spedizione.id_hub_origine, spedizione.id_hub_destinazione})][0] += spedizione.conteggio
                self._dizionario_spedizioni[frozenset({spedizione.id_hub_origine, spedizione.id_hub_destinazione})][1] += spedizione.somma
            else:
                self._dizionario_spedizioni[frozenset({spedizione.id_hub_origine, spedizione.id_hub_destinazione})] = [spedizione.conteggio,spedizione.somma]

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        for hub in self._dizionario_hub.values():
            self.G.add_node(hub)
        for (h_o,h_d) in self._dizionario_spedizioni.keys():
            media = self._dizionario_spedizioni[frozenset({h_o,h_d})][1]/self._dizionario_spedizioni[frozenset({h_o,h_d})][0]
            if media >= threshold:
                h1_nodo = self._dizionario_hub[h_o]
                h2_nodo = self._dizionario_hub[h_d]
                self.G.add_edge(h1_nodo, h2_nodo, Tratta_Commerciale=media)
    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return f"Numero di Tratte: {self.G.number_of_edges()}"
    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return f"Numero di Hubs: {self.G.number_of_nodes()}"
    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        lista_grafo = []
        for u, v, peso in self.G.edges(data=True):
           lista_grafo.append(f"[{u} -> {v}] -- Guadagno Medio Per Spedizione: € {peso['Tratta_Commerciale']:.2f}")
        return lista_grafo