# -*- coding: utf-8 -*-
from graph_class import Graph

class WCNF_Clauses:
    """
        Transfer graph problems to wcnf, here is just clique problem
    """
    def __init__(self, fname = "test.wcnf"):
        self.cnf_clauses = []
        self.iterals_num=0
        self.clasues_num=0
        self.wcnf_fname=fname
        
    def _clique_to_cnf(self, graph:Graph):
        ##get the iteraks num, it will equal to the vertices
        self.iterals_num = len(graph.vertices)
        
        ## soft clasue
        unconnected_vertices =  [((i, j)) for i in graph.vertices for j in graph.vertices if i != j and i not in j.neighbors]
        
        ## find the all unconnect nodes
        for v in graph.vertices:
            self.cnf_clauses.append("1 "+str(int(graph.vertices.index(v) + 1)) + " 0\n")
            
        ## Hard clauses, denotes the connectivty of graph
        for i in unconnected_vertices:
            self.cnf_clauses.append("100000 -"+str(int(graph.vertices.index(i[0]) + 1))+" "+"-"+str(int(graph.vertices.index(i[1]) + 1)) +" 0\n")
        self.clasues_num = len(self.cnf_clauses)
            
    def _build_wcnf_file(self):
        """
            write everying to a wcnf file
        """
        wcnf_file=open( self.wcnf_fname, "w")
        wcnf_file.write("p wcnf "+str(self.iterals_num)+ " " + str(self.clasues_num)+"\n")
        wcnf_file.writelines(self.cnf_clauses)
        wcnf_file.flush()
        wcnf_file.close()
        
    def build_clique_wcnf(self, graph):
        self._clique_to_cnf(graph)
        self._build_wcnf_file()